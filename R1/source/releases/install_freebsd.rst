.. _install_freebsd:

Installation on FreeBSD
=======================

Varnish is distributed in the FreeBSD ports collection as 'www/varnish6'.

You can either install it as binary package::

	pkg install varnish6

Or build it from source::

	cd /usr/ports/www/varnish6
	make all install clean
