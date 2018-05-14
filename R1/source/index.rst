Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

:ref:`Questions and Answers<faq>`

What is happening
-----------------

2018-04-26 - Maintenance release: Varnish Cache 4.1.10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This maintenance release is recommended for all users of 4.0 and 4.1 versions,
and contains several bug fixes. More information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/4.1/doc/changes.rst>`_

2018-03-15 - Varnish 6.0.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel6.0.0`

Now with support for Unix Domain Sockets, better HTTP/2 support,
many bugfixes and ... Well read more about it all
`here </docs/6.0/whats-new/changes-6.0.html>`_

2017-11-15 - Security Advisory: (Unlikely) data leak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Certain uncommon configurations of Varnish may leak data in
synthetic responses from `vcl_backend_error{}`

Please see :ref:`vsv00002`

We have released Varnish :ref:`rel4.1.9` and :ref:`rel5.2.1` to fix this issue.

2017-09-15 - Varnish 5.2.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel5.2.0`


2017-08-02 - Security Advisory: Denial of Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All varnish versions from 4.0.1 are vulnerable to a Denial of Service
attack, please see :ref:`vsv00001`

2017-08-02 - Security releases: 4.0.5, 4.1.8 and 5.1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions 4.0.5, 4.1.8 and 5.1.3 are now available. See
:ref:`vsv00001` for details.

Package repository status
-------------------------

The official Linux (apt/yum) package repositories are now located
at Packagecloud.io.
A list of all available repositories can be found at:
https://packagecloud.io/varnishcache

The old http://repo.varnish-cache.org/ is going to be removed on the 31st of August.

For more details on packages, see :ref:`Releases & Downloads <releases>`

Privacy
-------

You can access the varnish-cache homepages with HTTP or HTTPS as you
like.

We save the logfiles from our Varnish instance for a limited period,
in order to be able to debug problems.

The old homepage ran Google Analytics, but this has now been discontinued.


.. toctree::
   :hidden:

   intro/index
   security/index
   business/index
   faq/index
   releases/index
   docs/index
   support/index
   extras/index
   vmods/index
   tips/index
