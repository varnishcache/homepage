.. _rel4.0.3:

Varnish Cache 4.0.3
===================

* Source download :download:`varnish-4.0.3.tar.gz <varnish-4.0.3.tar.gz>`

* SHA256=94b9a174097f47db2286acd2c35f235e49a2b7a9ddfdbd6eb7aa4da9ae8f8206

* `SHA256 evidence <https://svnweb.freebsd.org/ports/head/www/varnish4/distinfo?view=markup&pathrev=380358>`_

* `Change log <https://github.com/varnishcache/varnish-cache/blob/4.0/doc/changes.rst>`_

* 2015-02-19 /scn


By Operating System 
-------------------

* :ref:`install_ubuntu`
* :ref:`install_debian`
* :ref:`install_redhat`
* :ref:`install_freebsd`



Summary of changes
------------------

* 26 reported bugs fixed.
* Replaced objects are now expired immediately,
  instead of kept around until expiry.
* Memory usage on chunked backend responses is lower.
