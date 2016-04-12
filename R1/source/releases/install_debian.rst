.. _install_debian:

Installation on Debian
======================

Varnish is distributed in the Debian package repositories but the
version there might be out of date and we generally recommend using
the packages provided by varnish-cache.org or packages from
backports.debian.org.

To use the varnish-cache.org repository and install Varnish under
Debian 8 ("jessie") do the following as root::

    apt-get install apt-transport-https
    curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add -
    echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1"\
	>> /etc/apt/sources.list.d/varnish-cache.list
    apt-get update
    apt-get install varnish

Packages are built for wheezy and jessie on amd64. Varnish 4.0
packages are available in the "varnish-4.0" component.

Ubuntu LTS users please follow :ref:`these instructions <install_ubuntu>`.
