.. _install_freebsd:

Installation on FreeBSD
=======================

Varnish is distributed in the FreeBSD ports collection as 'www/varnish'.

You can either install it as binary package::

	pkg install varnish

Or build it from source::

	cd /usr/ports/www/varnish
	make all install clean
