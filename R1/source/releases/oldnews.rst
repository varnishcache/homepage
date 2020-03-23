.. _oldnews:

Older Varnish HTTP Cache news
=============================


2018-10-26 - Bug fix release: Varnish 6.1.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are proud to release :ref:`rel6.1.1` to the world.

This release is recommended for everyone running 6.1, and packages are
available from the official repositories. There are no new features in
the release, and no reconfiguration is necessary.

Read more about Varnish Cache 6.1 `here </docs/6.1/whats-new/changes-6.1.html>`_

2018-09-17 - Varnish 6.1.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel6.1.0`

This release brings many improvements under the hood with no
need for reconfiguration for practically all users.

Read more about it `here </docs/6.1/whats-new/changes-6.1.html>`_

2018-08-29 - Maintenance release: Varnish Cache 6.0.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Today we made :ref:`rel6.0.1` available on the download page and the official package repositories.

This maintenance release is recommended for all users of 6.0.0,
and contains many bug fixes. More information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_

2018-06-08 - Publically available packages from UPLEX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The varnish-cache contributors from `UPLEX`_ are happy to announce an
alternative source for varnish binary packages for Debian, Ubuntu and
RHEL/CentOS (work in progress).

Debian/Ubuntu packages are based on fairly recent varnish-cache master
snapshots and are expected to be updated on a bi-weekly basis,
synchronized with the official varnish-cache weekly builds.

The main purpose of the `UPLEX Packages`_ is to provide simple and
efficient access to up-to-date varnish builds and a matching range of
additional vmods which are not commonly found in package repositories
like `blobdigest`_, `re`_, `re2`_, `geoip2`_ and `dcs`_ in addition to
the `varnish-modules`_ vmod bundle. Other will be added over time.

This packaging effort is still in its early stages and will grow over time.

.. _`UPLEX Packages`: https://pkg.uplex.de/
.. _`UPLEX`: https://uplex.de/#anchorvarnish
.. _`blobdigest`: https://code.uplex.de/uplex-varnish/libvmod-blobdigest/
.. _`re`: https://code.uplex.de/uplex-varnish/libvmod-re/
.. _`re2`: https://code.uplex.de/uplex-varnish/libvmod-re2/
.. _`geoip2`: https://github.com/fgsch/libvmod-geoip2
.. _`dcs`: https://code.uplex.de/uplex-varnish/dcs_classifier
.. _`varnish-modules`: https://github.com/varnish/varnish-modules

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

