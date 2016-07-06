.. _install_redhat:

Installation on Red Hat Linux
=============================

Varnish Cache is packaged in RPMs for easy installation and upgrade on Red Hat
systems.


Official packages
-----------------

The Varnish Cache project maintains official packages for the current Enterprise Linux versions.
Varnish Cache 4.0 and 4.1 are supported on EL6 and EL7.

Varnish 4.1
~~~~~~~~~~~

If you are on a compatible Linux distribution, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el7.rpm
    (or: rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el6.rpm for RHEL6)
    yum install varnish

Varnish 4.0
~~~~~~~~~~~

If you are on RHEL 6 or a compatible distribution, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.0.el6.rpm
    yum install varnish

For RHEL 7 and compatible distributions, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.0.el7.rpm
    yum install varnish

The `--no-signature` argument is only needed on initial installation, since
the Varnish GPG key is not yet in the yum keyring.


External packaging
------------------

Varnish Cache is also distributed in third party package repositories.

.. _`Fedora EPEL`: https://fedoraproject.org/wiki/EPEL

* `Fedora EPEL`_ does community packaging of Varnish Cache.

* RedHat has packaged versions of Varnish Cache available since Software Collections 2.1. Announcement on <http://developers.redhat.com/blog/2015/11/17/software-collections-2-1-generally-available/>.

