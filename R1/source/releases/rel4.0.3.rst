.. _rel4.0.3:

Varnish Cache 4.0.3
===================

* 2015-02-19 /scn

By Operating System 
-------------------

* :ref:`install_ubuntu`
* :ref:`install_debian`
* :ref:`install_redhat`
* :ref:`install_freebsd`

`Source download <https://repo.varnish-cache.org/source/varnish-4.0.3.tar.gz>`_

`Change log <https://github.com/varnishcache/varnish-cache/blob/4.0/doc/changes.rst>`_

Summary of changes
------------------

* 26 reported bugs fixed.
* Replaced objects are now expired immediately,
  instead of kept around until expiry.
* Memory usage on chunked backend responses is lower.
