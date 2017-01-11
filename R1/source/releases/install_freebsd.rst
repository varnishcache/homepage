.. _install_freebsd:

Installation on FreeBSD
=======================

Varnish is distributed in the FreeBSD ports collection as 'www/varnish'.

You can either install it as binary package::

	pkg install varnish5

Or build it from source::

	cd /usr/ports/www/varnish5
	make all install clean
