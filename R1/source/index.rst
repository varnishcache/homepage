Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

:ref:`Questions and Answers<faq>`

What is happening
-----------------

2016-11-21 - New Tool in Town
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I finally sat down and wrote a Varnish specific "Continuous
Integration" tool, and people are busy starting it on the various
machines we use for testing in the project.

You can `see the result(s) here. </vtest/index.html>`_

If you want to run a "sandbox" for us, you just need to run
`a small simple shell-script
<https://github.com/varnishcache/varnish-cache/blob/master/tools/vtest.sh>`_
`no need for a Java Runtime or anything else.
</docs/trunk/phk/trialerror.html>`_

/phk


2016-09-27 - Send us (more) money!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If we want to keep up the same activity level as the last couple
of years, we need €2000/month to buy more of Poul-Hennings time.

So if Varnish improves your company's profit, please invest in a
one-time or recurring `Varnish Moral License <http://phk.freebsd.dk/VML>`_
to help fund the projects future.

Thanks in advance!

And a big thanks to the companies already sponsoring Varnish:

* Fastly
* Varnish-Software
* UPLEX
* [your companys name could have been here...]


2016-09-15 - Varnish 5.0
~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache 5.0.0 has been released!  /Lasse /phk

See:

* :ref:`Releases` 
* `Release Note </docs/5.0/whats-new/relnote-5.0.html>`_
* `Upgrading </docs/5.0/whats-new/upgrading-5.0.html>`_
* `Changes </docs/5.0/whats-new/changes-5.0.html>`_

(And yes, we're dog-food running it on the varnish-cache.org site)


2016-08-16 - Separate VCL files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In varnish 5.0 it will be possible to use separate VCL files
for different kinds of requests, for instance one VCL file
per ``Host: domain``.

You can test it already now in the trunk version.

`Read more about separate VCL files here
</docs/trunk/users-guide/vcl-separate.html>`_

2016-07-18 - HTTPOXY workaround
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are running Varnish, protecting against the
`HTTPOXY <https://httpoxy.org/>`_ CGI vulnerability is a simple
as::

	sub vcl_recv {
		unset req.http.proxy;
	}

2016-07-06 - Varnish 4.1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~
:ref:`rel4.1.3` has been released! /Lasse


Privacy
-------

You can access the varnish-cache homepages with HTTP or HTTPS as you
like.

We save the logfiles from our Varnish instance for a limited period,
in order to be able to debug problems.

The old homepage ran Google Analytics, and we have continued that here
for now, but unless we actually learn something useful from the data
they collect, it will be discontinued.


.. toctree::
   :hidden:

   intro/index
   security/index
   news/index
   business/index
   faq/index
   releases/index
   docs/index
   support/index
   extras/index
   vmods/index
   tips/index
