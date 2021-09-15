Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

What is happening
-----------------

2021-09-15 - Varnish 7.0.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.0.0`

The 6.5 series is no longer supported in any capacity.

(The 2022-03-15 release is likely to be 8.0.0)

2021-08-17 - Open Source parallel ESI for varnish-cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On

  * https://code.uplex.de/uplex-varnish/libvdp-pesi
  * https://gitlab.com/uplex/varnish/libvdp-pesi (mirror)

we have released a Varnish Delivery Processor (VDP) for parallel ESI processing,
which can deliver relevant speedups where portions of ESI-processed objects are
not served from cache.

.. _`The pESI Announcement`: https://varnish-cache.org/lists/pipermail/varnish-announce/2021-August/000746.html

Read `The pESI Announcement`_ for more details.

2021-07-13 - HTTP/2 Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request smuggling
vulnerability when the HTTP/2 support is enabled. Please see
:ref:`VSV00007` for more information.

2021-07-13 - Security releases: 6.0.8, 6.6.1 and 6.5.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.8 <rel6.0.8>`, :ref:`6.6.1 <rel6.6.1>` and
:ref:`6.5.2 <rel6.5.2>` are now available. These releases fix the
vulnerability described in :ref:`VSV00007 <VSV00007>`.

2021-07-13 - Varnish 6.0.8 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.8`.

This combined maintenance and security release is recommended for all
users of the 6.0 LTS and contains several bug fixes, improvements and new
features. More information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_

2021-03-16 - Denial of Service in varnish-modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some versions of the separate `varnish-modules` bundle allow for a
potential denial of service attack when the ``header.append()`` or
``header.copy()`` functions are used.

Please see :ref:`VSV00006`.

2021-03-15 - Varnish 6.6.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel6.6.0`

(The 2021-09-15 release is likely to be 7.0.0)

2020-11-06 - Varnish 6.0.7 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.7`.

This maintenance release is recommended for all users of the 6.0 LTS
and contains several bug fixes, improvements and new features. More
information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_


2020-09-25 - Varnish 6.5.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When preparing the 6.5.0 release, it was forgotten to bump the
VRT_MAJOR_VERSION number defined in the `vrt.h` include file. This major
version bump is needed due to the API and ABI changes as part of the
release, to make sure that VMODs are not allowed used if they were
compiled for the wrong Varnish version.

This has been fixed in the :ref:`rel6.5.1` release.


2020-09-15 - Varnish 6.5.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel6.5.0`


2020-03-16 - Varnish 6.4.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release :ref:`rel6.4.0`

2020-02-04 - Security Advisory: Denial of Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a denial of service attack
when using the Proxy Protocol version 2. Please see :ref:`VSV00005
<VSV00005>`.

2020-02-04 - Security releases: 6.0.6, 6.2.3 and 6.3.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions 6.0.6, 6.2.3 and 6.3.2 are now available. See
:ref:`VSV00005 <VSV00005>` for details.

:ref:`Older news <oldnews>`

Package repository status
-------------------------

The official Linux (apt/yum) package repositories are now located
at Packagecloud.io.
A list of all available repositories can be found at:
https://packagecloud.io/varnishcache

For more details on packages, see :ref:`Releases & Downloads <releases>`

Privacy
-------

You can access the varnish-cache homepages with HTTP or HTTPS as you
like.

We save the logfiles from our Varnish instance for a limited period,
in order to be able to debug problems.

We do not use any external trackers and do not analyze traffic.

.. toctree::
   :hidden:

   intro/index
   security/index
   business/index
   releases/index
   docs/index
   support/index
   extras/index
   vmods/index
   tips/index
