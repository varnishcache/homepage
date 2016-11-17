.. _install_debian:

Installation on Debian and Ubuntu
=================================

Varnish Cache is distributed in the Debian and Ubuntu package repositories.

The versions there might be out of date, but they provide a simple and elegant
way of getting started with Varnish Cache.

::

    $ sudo apt-get update
    $ sudo apt-get install varnish


Official packages of 5.0
------------------------

Starting from Varnish Cache 5.0, we've simplified our packaging down to two:
the main package and a development package.

In due time, we may add these to some repository software. Currently
they're available on:

    https://repo.varnish-cache.org/pkg/


Packages from repo.varnish-cache.org (<5.0)
-------------------------------------------

To use the varnish-cache.org repository and install Varnish on
Debian jessie do the following as root::

    $ sudo apt-get install apt-transport-https
    $ curl https://repo.varnish-cache.org/GPG-key.txt | sudo apt-key add -
    $ echo "deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" \
    	| sudo tee -a /etc/apt/sources.list.d/varnish-cache.list
    $ sudo apt-get update
    $ sudo apt-get install varnish


There are Ubuntu builds available under ``/ubuntu/``.

Some earlier/legacy builds are also available under the "varnish-3.0" and
"varnish-4.0" components.

On the Cloud
------------

Varnish Cache is also made available by Varnish Software for Ubuntu LTS on 
Amazon Web Services (AWS) Elastic Compute Cloud (EC2). Here is a list of the 
current instances available:

.. _`Varnish Cache 4 on Ubuntu LTS 14.04`: https://aws.amazon.com/marketplace/pp/B01H2063F6

* `Varnish Cache 4 on Ubuntu LTS 14.04`_

Fresh releases, such as Varnish Cache 5, will be made available soon.
