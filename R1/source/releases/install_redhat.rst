.. _install_redhat:

Installation on Red Hat Linux
=============================

Varnish Cache is packaged in RPMs for easy installation and upgrade on Red Hat
systems. The Varnish Cache project maintains official packages for the current
Enterprise Linux versions. Varnish Cache 4.1 and 5.x are supported on EL6 and EL7.

Official packages of 6
----------------------

Starting from Varnish Cache 5.0, we've simplified our packaging down to two:
the main package and a development package.

The official Varnish Cache repository is now hosted at Packagecloud.io.
Note that while Packagecloud.io provides Bash Script installs, we recommend
using the manual installation procedures.

Instructions for installing the official repository which contains the newest 
Varnish Cache 6 release are available at:

* https://packagecloud.io/varnishcache/varnish5/install#manual-rpm

Official packages of 4.1
------------------------

To use Varnish Cache 4.1 packages from the official varnish-cache.org repos,
follow the instructions available at:

* https://packagecloud.io/varnishcache/varnish41/install#manual-rpm

External packaging
------------------

Varnish Cache is also distributed in third party package repositories.

.. _`Fedora EPEL`: https://fedoraproject.org/wiki/EPEL

* `Fedora EPEL`_ does community packaging of Varnish Cache.

* RedHat has packaged versions of Varnish Cache available since Software Collections 2.1. Announcement on <http://developers.redhat.com/blog/2015/11/17/software-collections-2-1-generally-available/>.


Cloud images
------------

Varnish Cache is also made available by Varnish Software in the following 
clouds providers:


Amazon Web Services (AWS EC2)
.............................

Here is a list of the currently available images for RHEL7 on 
Amazon Web Services (AWS) Elastic Compute Cloud (EC2):

* `Varnish Cache 4 on Red Hat Enterprise Linux 7 on AWS`_
* `Varnish Cache 5 on Red Hat Enterprise Linux 7 on AWS`_

.. _`Varnish Cache 4 on Red Hat Enterprise Linux 7 on AWS`: https://aws.amazon.com/marketplace/pp/B01H2061O4
.. _`Varnish Cache 5 on Red Hat Enterprise Linux 7 on AWS`: https://aws.amazon.com/marketplace/pp/B01MR09UKM


Microsoft Azure
...............

Here is a list of the currently available images for RHEL7 on 
Microsoft's Azure cloud:

* `Varnish Cache 4 and 5 on Red Hat Enterprise Linux 7 on Azure`_

.. _`Varnish Cache 4 and 5 on Red Hat Enterprise Linux 7 on Azure`: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/varnish.varnish-cache_


Google Cloud Platform (GCP)
...........................

Here is a list of the currently available images for RHEL7 on 
Google Cloud Platform (GCP):

* `Varnish Cache 4 on Red Hat Enterprise Linux 7 on GCP`_
* `Varnish Cache 5 on Red Hat Enterprise Linux 7 on GCP`_

.. _`Varnish Cache 4 on Red Hat Enterprise Linux 7 on GCP`: https://console.cloud.google.com/launcher/details/varnish-public/varnish-cache-4-payg-red-hat
.. _`Varnish Cache 5 on Red Hat Enterprise Linux 7 on GCP`: https://console.cloud.google.com/launcher/details/varnish-public/varnish-cache-5-payg-red-hat
