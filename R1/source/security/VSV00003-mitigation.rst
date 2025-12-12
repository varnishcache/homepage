.. _VSV00003-mitigation:

VSV00003 DoS attack vector VCL mitigation
=========================================

Date: 2019-09-03

The issue documented in :ref:`VSV00003 <VSV00003>` can be mitigated from
VCL where deployment of binary fixes is not possible immediately.

We provide two methods of mitigation, one simple with a performance
impact, and one more complex method which can avoid the performance
impact, but may also need to the fall back to it.

Simple mitigation
-----------------

The simple mitigation method is to not use HTTP/1 keepalive connections by
setting the `Connection: close` header of the client response, which is
respected by varnish in that it closes the connection after all of the
response body has been sent.

HTTP/1 keepalive connections avoid overhead by re-using TCP
connections and, where used, TLS connections for multiple requests. By
not using keepalive connections, an increase in response times and
server load is to be expected.

To apply this mitigation method, add this snippet near the top of your
VCL after the `vcl 4.0` or `vcl 4.1` statement::

 # https://vinyl-cache.org/security/VSV00003-mitigation.html
 sub return_deliver_mitigate_vsv00003 {
    if (req.esi_level == 0 && req.proto != "HTTP/2.0") {
	set resp.http.Connection = "close";
    }
    return (deliver);
 }

and replace any `return (deliver);` statements in `sub vcl_deliver {}`
and `sub vcl_synth {}` with `call return_deliver_mitigate_vsv00003;`

For example, given you have::

 sub vcl_deliver {
     # ... your code
     return (deliver);
 }

 sub vcl_synth {
     # ... your code
     return (deliver);
 }

replace with::

 sub vcl_deliver {
     # ... your code
     call return_deliver_mitigate_vsv00003;
 }

 sub vcl_synth {
     # ... your code
     call return_deliver_mitigate_vsv00003;
 }


If there is no explicit `return (deliver)`, add the call statement at
the end of `vcl_deliver {}` and/or `vcl_synth {}`.

If there is no `vcl_deliver {}`, add one with just the call statement.

If there is no `vcl_synth {}`, copy it from the `builtin.vcl` and replace
the `return (deliver);`.

Complex mitigation avoiding the performance impact
--------------------------------------------------

The complex mitigation has the potential to avoid the performance
impact by `Connection: close`, but has the drawback of requiring
inline-C.

It can avoid the `Connection: close` for many cases, but needs to fall
back to it if newline characters are found on the workspace. For
simple VCL code, these should not exist.

Notice that this method should be applied with extra care. Though it
has been tested thoroughly, it is provided for use at your own
risk. In particular, this method may not work if the Varnish-Cache
source code has been patched.

The code has been tested with:

* varnish-6.2.0 and git master as of 2019-08-22
* varnish-6.1.1
* varnish-6.0.3

To apply this method:

* download :download:`vsv00003-mitigation.vcl`

  * SHA256=03b923357c02b83110bbef065690df9f0f4a0af3e155331922b83cb7d35f6729

* and put it into a directory contained in your `vcl_path` (usually
  `/usr/share/varnish/vcl` or `/etc/varnish`)

* ensure the varnish `vcc_allow_inline_c` parameter is set to `true`:

  * add `-p vcc_allow_inline_c=true` to the varnishd start parameters,
    unless already present

  * use the following command to change the current setting::

        varnishadm param.set vcc_allow_inline_c true

* at the top of your VCL, but after the `vcl 4.0` or `vcl 4.1`
  statement, add::

	include "vsv00003-mitigation.vcl"

* do _not_ include the `sub return_deliver_mitigate_vsv00003` from
  above

* but follow the steps to *replace any `return (deliver);`
  statements* as described above.

In other words, the include file is a replacement for the subroutine
from the simple mitigation method.

Monitoring the mitigation
-------------------------

The simple mitigation method should not require any monitoring.

For the complex mitigation method, an increase of the rate of the
`MAIN.sc_req_close` statistic is to be expected. If that rate increase
accounts for a relevant portion of the request rate, an attempt can be
made to avoid the additional `Connection: close` conditions by
checking if newline characters are produced by the client side VCL
code.

If `synthetic()` / `set resp.body` is used, this increase is expected.
