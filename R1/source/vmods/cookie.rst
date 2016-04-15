.. _vmods_cookie:

Cookie
======

Functions to handle the content of the Cookie header without complex use of regular expressions.

Parses a cookie header into an internal data store, where per-cookie get/set/delete functions are available. A `filter_except()` method removes all but a set comma-separated list of cookies.

A convenience function for formatting the Set-Cookie Expires date field is also included. It might be needed to use libvmod-header if there might be multiple Set-Cookie response headers.

+----------------------------+-------------------------------------------------------------+
| Status:                    | Used in production                                          |
+----------------------------+-------------------------------------------------------------+
| Dependencies:              | None. Might need https://github.com/varnish/libvmod-header  |
+----------------------------+-------------------------------------------------------------+
| Licence:                   | FreeBSD                                                     |
+----------------------------+-------------------------------------------------------------+
| Varnish version supported: | Varnish 3.0                                                 |
+----------------------------+-------------------------------------------------------------+
| Commercial support:        | Varnish Software                                            |
+----------------------------+-------------------------------------------------------------+
| Surce repository URL:      | https://github.com/lkarsten/libvmod-cookie                  |
+----------------------------+-------------------------------------------------------------+