.. _rel4.1.7:

Varnish Cache 4.1.7
===================

* Source download :download:`varnish-4.1.7.tar.gz <varnish-4.1.7.tar.gz>`

* SHA=c52ee2f5d052a496f3700d8ac8eb4da45144779c863f09f7be70daec3cfed105

* `SHA evidence <https://gitweb.gentoo.org/repo/gentoo.git/tree/www-servers/varnish/Manifest?id=ba4ad6bba2c8574369965f9725346b45aeb2dd5e>`_

* `Change log <https://github.com/varnishcache/varnish-cache/blob/4.1/doc/changes.rst>`_

* 2017-06-28 /Pål Hermunn

Varnish Cache 4.1.7 is a maintenance release of the 4.1 branch with
several bug fixes. See the change log for a complete list of changes,
and pay special attention to `#1764 - Correctly honor nuke_limit
parameter
<https://github.com/varnishcache/varnish-cache/issues/1764>`_ if your
varnish instance does a considerable amount of LRU nuking.

All users on 4.1 and 4.0 are recommended to upgrade to this version.


Operating System Specific Installation Guides
---------------------------------------------

* :ref:`install_ubuntu`
* :ref:`install_debian`
* :ref:`install_redhat`
* :ref:`install_freebsd`
