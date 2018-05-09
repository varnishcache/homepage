.. _install_openbsd:

Installation on OpenBSD
=======================

Varnish is distributed in the OpenBSD ports collection as 'www/varnish'.

You can either install it as binary package::

	pkg_add varnish

Or build it from source::

	cd /usr/ports/www/varnish
	make install
