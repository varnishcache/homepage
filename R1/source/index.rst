Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

What is happening
-----------------

2025-05-12 - Security release 7.7.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.7.1 <rel7.7.1>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-05-12 - Request Smuggling Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00016`.

2025-05-12 - Security release 7.6.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.6.3 <rel7.6.3>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-05-12 - Security release 6.0.14
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.14 <rel6.0.14>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-03-17  - Varnish 7.7.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.7.0`

The 7.5 series is no longer supported in any capacity.


2025-03-17 - Varnish HTTP/1 client-side desync vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00015`.

2025-03-17 - Security release 7.6.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.6.2 <rel7.6.2>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00015 <VSV00015>`.

2024-11-08 - Varnish 7.6.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.6.1 has been released and can be found here: :ref:`rel7.6.1`

This maintenance release fixes a few bugs introduced in 7.6.0.

2024-09-13 - Varnish 7.6.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.6.0`

The 7.4 series is no longer supported in any capacity.

2024-03-18 - Varnish 7.5.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.5.0`

The 7.3 series is no longer supported in any capacity.

2024-03-18 - Varnish HTTP/2 Broke Window Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Varnish Cache releases with HTTP/2 support suffer a vulnerability in
the HTTP/2 protocol. Please see :ref:`VSV00014` for more information.

2024-03-18 - Security releases: 6.0.13, 7.3.2 and 7.4.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.13 <rel6.0.13>`, :ref:`7.3.2 <rel7.3.2>` and
:ref:`7.4.3 <rel7.4.3>` are now available. These releases are published to
address the vulnerability described in :ref:`VSV00014 <VSV00014>`.

2024-02-06 - `SLASH/`_ 1.0.0-rc1
--------------------------------

.. _`SLASH/`: https://gitlab.com/uplex/varnish/slash/-/blob/master/README.rst

Celebrating the 18th anniversary of Varnish-Cache and the first
anniversary of the `SLASH/`_ storage engines today, your Open-Source
Varnish-Cache friends from `UPLEX`_ have just tagged the first version
1.0.0 candidate of our extension with storage engines (stevedores) and
storage routers (loadmasters).

Over the past year, we have received a lot of helpful input from our
users and have implemented substantial improvements. THANK YOU to
everyone who has contributed by reporting issues, providing feedback
and, just recently, adding documentation. SLASH/fellow has also helped
improve Varnish-Cache itself.

After rigorous testing in particular over the past weeks, we now
boldly claim that SLASH/ deserves a 1.0 version tag.

HAPPY BIRTHDAY Varnish-Cache!

HAPPY BIRTHDAY SLASH/buddy and SLASH/fellow!

.. _`Mastodon post`: https://fosstodon.org/@slink/111886397903235142

.. _`Changelog`: https://gitlab.com/uplex/varnish/slash/-/blob/master/CHANGES.rst?ref_type=heads

Continue reading:

* `Mastodon post`_
* `Changelog`_


2023-11-13 - Varnish HTTP/2 Rapid Reset Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Varnish Cache releases with HTTP/2 support suffer a vulnerability in
the HTTP/2 protocol. Please see :ref:`VSV00013` for more information.

2023-11-13 - Security releases: 6.0.12, 7.3.1 and 7.4.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.12 <rel6.0.12>`, :ref:`7.3.1 <rel7.3.1>` and
:ref:`7.4.2 <rel7.4.2>` are now available. These releases are published to
address the vulnerability described in :ref:`VSV00013 <VSV00013>`.

2023-09-20 - Varnish 7.4.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.4.1 has been released and can be found here: :ref:`rel7.4.1`

This maintenance release fixes a bug preventing protected headers
to be read from several subroutines.

2023-09-15 - Varnish 7.4.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.4.0`

The 7.2 series is no longer supported in any capacity.


2023-08-17 - VSV00012: Vulnerability in vmod_digest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00012`

2023-03-15 - Varnish 7.3.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.3.0`

The 7.1 series is no longer supported in any capacity.

2023-02-06 - Two new Storage Engines for Varnish-Cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _`UPLEX`: https://uplex.de/

Celebrating the 17th anniversary of Varnish-Cache today, your
Open-Source Varnish-Cache friends from `UPLEX`_ have just released an
extension with two new storage engines (stevedores) and two basic
storage routers (loadmasters). One of the storage engines, `fellow`,
offers persistent storage on disks (or SSDs, rather).

The preferred public repository with support for issues,
merge-requests and other activities is at
https://gitlab.com/uplex/varnish/slash

.. _`The SLASH/ Announcement`: https://varnish-cache.org/lists/pipermail/varnish-announce/2023-February/000757.html

.. _`The SLASH/ README`: https://gitlab.com/uplex/varnish/slash/-/blob/master/README.rst

.. _`The SLASH/ module documentation`: https://gitlab.com/uplex/varnish/slash/-/blob/master/src/vmod_slash.man.rst

To read more:

* `The SLASH/ Announcement`_
* `The SLASH/ README`_
* `The SLASH/ module documentation`_

2022-11-08 - Request Forgery Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request forgery
vulnerability on HTTP/2 connections. Please see :ref:`VSV00011` for more
information.

2022-11-08 - Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache releases 7.1 and 7.2 suffer from a Request Smuggling
vulnerability. Please see :ref:`VSV00010` for more information.

2022-11-08 - Security releases: 6.0.11, 7.2.1 and 7.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.11 <rel6.0.11>`, :ref:`7.2.1 <rel7.2.1>` and
:ref:`7.1.2 <rel7.1.2>` are now available. These releases are published to
address the vulnerabilities described in :ref:`VSV00010 <VSV00010>` and
:ref:`VSV00011 <VSV00011>`.

2022-09-15 - Varnish 7.2.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.2.0`

The 7.0 series is no longer supported in any capacity.

2022-08-09 - Denial of Service Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache releases 7.0 and 7.1 suffer from a Denial of Service
vulnerability. Please see :ref:`VSV00009` for more information.

2022-08-09 - Security releases: 7.1.1 and 7.0.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.1.1 <rel7.1.1>` and :ref:`7.0.3 <rel7.0.3>` are
now available. These releases fix the vulnerability described in
:ref:`VSV00009 <VSV00009>`.

2022-03-15 - Varnish 7.1.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.1.0`

The 6.6 series is no longer supported in any capacity.

2022-01-25 - HTTP/1 Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request smuggling
vulnerability on HTTP/1 connections. Please see :ref:`VSV00008` for more
information.

2022-01-25 - Security releases: 6.0.10, 7.0.2 and 6.6.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.10 <rel6.0.10>`, :ref:`7.0.2 <rel7.0.2>` and
:ref:`6.6.2 <rel6.6.2>` are now available. These releases fix the
vulnerability described in :ref:`VSV00008 <VSV00008>`.

2021-11-24 - Varnish 6.0.9 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 6.0.9 has been released and can be found here: :ref:`rel6.0.9`

This maintenance release is recommended for all users of the 6.0 LTS
and contains several bug fixes.

2021-11-23 - Varnish 7.0.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.0.1 has been released and can be found here: :ref:`rel7.0.1`

This is a maintenance release to correct some bugs that got into the 7.0.0
release.

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
   tutorials/index
   organization/index
   misc/gdpr-redacted
