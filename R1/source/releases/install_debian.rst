.. _install_debian:

Installation on Debian and Ubuntu
=================================

Varnish Cache is distributed in the Debian and Ubuntu package repositories.

The versions there might be out of date, but they provide a simple and elegant
way of getting started with Varnish Cache.

::
    apt update
    apt install varnish

Official packages of 5.0
------------------------

Starting from Varnish Cache 5.0, we've simplified our packaging down to two,
the main package and a development package.

In due time, we may add these to some repository software. Currently
they're available on:

    https://repo.varnish-cache.org/pkg/



Packages from repo.varnish-cache.org (<5.0)
------------------------------------

To use the varnish-cache.org repository and install Varnish on
Debian jessie do the following as root::

    apt-get install apt-transport-https
    curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -
    echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1"\
	>> /etc/apt/sources.list.d/varnish-cache.list
    apt-get update
    apt-get install varnish

There are Ubuntu builds available under /ubuntu/.

Some earlier/legacy builds are also available under the "varnish-3.0" and
"varnish-4.0" components.

List of supported platforms varies.


