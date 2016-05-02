.. _intro:

Introduction to Varnish
=======================

The basics
~~~~~~~~~~

Varnish Cache is a web application accelerator also known as a caching
HTTP reverse proxy. You install it in front of any server that speaks
HTTP and configure it to cache the contents. Varnish Cache is really,
really fast. It typically speeds up delivery with a factor of 300 -
1000x, depending on your architecture. A high level overview of what
Varnish does can be seen in the video attached to this web page.

Performance
~~~~~~~~~~~

Varnish performs really, really well. It is usually bound by the speed
of the network, effectively turning performance into a non-issue. We've
seen Varnish delivering 20 Gbps on regular off-the-shelf hardware.

Flexibility
~~~~~~~~~~~

One of the key features of Varnish Cache, in addition to its
performance, is the flexibility of its configuration language, VCL. VCL
enables you to write policies on how incoming requests should be
handled. In such a policy you can decide what content you want to serve,
from where you want to get the content and how the request or response
should be altered. And, you can `extend Varnish with modules
(VMODs) <https://www.varnish-cache.org/vmods>`__. You can read more
about this in our
`tutorial <https://www.varnish-cache.org/docs/trunk/tutorial/>`__.

Further reading
~~~~~~~~~~~~~~~

There is a good article describing `Varnish Cache on
Wikipedia <http://en.wikipedia.org/wiki/Varnish_(software)>`__.

Licence and origin
~~~~~~~~~~~~~~~~~~

Varnish is free software licensed under a two-clause BSD licence, also
known as the FreeBSD licence. The project was initiated in 2005. Varnish
Cache 1.0 was released in september 2006.

The name "Varnish"
~~~~~~~~~~~~~~~~~~

The name Varnish comes from when the instigator of Varnish spent a long
time staring at an art-poster with the word “Vernisage” and ended up
checking it in a dictionary, which gives the following three meanings of
the word:

*r.v. var·nished, var·nish·ing, var·nish·es*

    #. *To cover with varnish.*
    #. To give a smooth and glossy finish to.
    #. **To give a deceptively attractive appearance to; gloss over.**

To get in touch with the people operating this website please send an
email to phk@ or `ruben@varni.sh <mailto:ruben@varni.sh>`__.


Logo
----

A high resolution version of the Varnish Cache logo can be found
`here <https://old.varnish-cache.org/sites/default/files/pictures/varnishcache_rgb-gimp2-alpha.png>`__.

About this website
------------------

This site is statically generated. Powered by Sphinx running on Apache 
httpd on top of FreeBSD. It flies thanks to Varnish Cache. :-) 


.. toctree::
	:hidden:
