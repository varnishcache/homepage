Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

What is happening
-----------------

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

2019-10-21 - Security Advisory: Information leak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish can potentially leak some
information when certain conditions are met. Please see :ref:`VSV00004
<VSV00004>`.

2019-10-21 - Security releases: 6.0.5, 6.2.2 and 6.3.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions 6.0.5, 6.2.2 and 6.3.1 are now available. See
:ref:`VSV00004 <VSV00004>` for details.

2019-09-17 - Varnish 6.3.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release :ref:`rel6.3.0`

2019-09-03 - Security Advisory: Denial of Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish are vulnerable to a Denial of
Service attack, please see :ref:`VSV00003 <VSV00003>`.

2019-09-03 - Security releases: 6.0.4 and 6.2.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions 6.0.4 and 6.2.1 are now available. See
:ref:`VSV00003 <VSV00003>` for details.


2019-03-15 - Varnish 6.2.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel6.2.0`

This release brings many improvements under the hood and also some changes that VCL writers need to be aware of.

Read more about it `here </docs/6.2/whats-new/changes-6.2.html>`_


2019-02-20 - Maintenance release: Varnish Cache 6.0.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.3`.

This maintenance release is recommended for all users of the 6.0 LTS
and contains several bug fixes, improvements and new features. More
information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_

2019-02-11 - Maintenance release: Varnish Cache 4.1.11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel4.1.11`.

This maintenance release is recommended for all users of 4.0 and 4.1 versions,
and contains several bug fixes. More information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/4.1/doc/changes.rst>`_

2018-11-12 - Varnish 6.0.2 released, official Long Term Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.2`.

This release is recommended for everyone running 6.0, and it contains
many bug fixes and some new features.

At the same time we bring you the news that that 6.0 will maintained
much longer than other Varnish Cache Releases, and that new
repositories, Varnish 6.0 LTS, are introduced.

If you are currently using official packages, you need to change to
the new LTS repositories to get 6.0.2. Please follow the instructions
on the release page to set up the new repository for your platform.

The packaging of this release differs slightly from previous Varnish
versons. This is described in the
`upgrading notes <docs/6.0/whats-new/upgrading-6.0.html#packaging-changes>`_
for 6.0. These changes were originally intended for the initial 6.0
release, but unfortunately they did not make it into the 6.0.0 or
6.0.1 packages.

At some point the previous LTS, Varnish 4.1, will reach its End of
Life. It was first released in September 2015, and now is the time
for users to start upgrading to Varnish 6.0 LTS.

If you are still using Varnish 4.1, you should be able to migrate to
6.0 without touching your VCL.  In our experience so far, upgrading is
very straightforward.

Read more about `upgrading <docs/6.1/whats-new/upgrading-6.0.html>`_
and `what's new </docs/6.0/whats-new/changes-6.0.html>`_ in Varnish
Cache 6.0.

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
