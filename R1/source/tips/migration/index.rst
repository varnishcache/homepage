.. _migration:

Migrating Varnish versions
==========================

This page is a continuous work in progress, and contributions to this
is very much welcomed. Do not hesitate to open a "pull request" on
`our GitHub repository <https://github.com/varnishcache/homepage/>`.

The following resources documents upgrades from unsupported versions:

* `Migrating from 3.0.x to 4.0.x
  </docs/4.1/whats-new/upgrade-4.0.html>`_
* `Migrating to 4.1.x </docs/4.1/whats-new/upgrading.html>`_
* `Upgrading to 5.0 </docs/6.0/whats-new/upgrading-5.0.html>`_
* `Upgrading to 5.1 </docs/6.0/whats-new/upgrading-5.1.html>`_
* `Upgrading to 5.2 </docs/6.0/whats-new/upgrading-5.2.html>`_
* `Upgrading to 6.0 </docs/6.0/whats-new/upgrading-6.0.html>`_

Releases after 6.0 do not come with Long Time Support, but are
released as "fresh". A "fresh" release will get security updates for a
while, but not general bug fixes. A release can be promoted to LTS in
a separate announcement, and it will then receive general bug fixes
and some new features from newer releases and development.

Updating to the latest releases are documented here:

* `Upgrading to 6.1 </docs/trunk/whats-new/upgrading-6.1.html>`_
* `Upgrading to 6.2 </docs/trunk/whats-new/upgrading-6.2.html>`_
* `Upgrading to 6.3 </docs/trunk/whats-new/upgrading-6.3.html>`_

Upgrading from 4.x to the latest LTS should be very straightforward,
and require much less effort than going to 3.x to 4.x.

Versions of the VCL language
============================

Currently there are two official versions of the VCL language, 4.0 and
4.1, and they are only slightly different.

This table shows which versions of the VCL language are supported in
different versions of Varnish:

=============== ======================
Varnish version Supported VCL versions
=============== ======================
4.0*            4.0
4.1*            4.0
5.0*            4.0
5.1*            4.0
5.2*            4.0
6.0 LTS         4.0, 4.1
6.1*            4.0, 4.1
6.2*            4.0, 4.1
6.3             4.0, 4.1
=============== ======================

The versions marked with a star (*) are End Of Life.
