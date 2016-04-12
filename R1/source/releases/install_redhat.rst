.. _install_redhat:

Installation on RedHat
======================

Installing Varnish Cache is as simple as enabling our package
repository and installing the packages. Varnish Cache 4.0 and 4.1
are supported on EL6 and EL7.

Varnish 4.1
-----------

If you are on a compatible Linux distribution, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el7.rpm
    (or: rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el6.rpm for RHEL6)
    yum install varnish

Varnish 4.0
-----------

If you are on RHEL 6 or a compatible distribution, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.0.el6.rpm
    yum install varnish

For RHEL 7 and compatible distributions, use::

    yum install epel-release
    rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.0.el7.rpm
    yum install varnish

The --no-signature is only needed on initial installation, since
the Varnish GPG key is not yet in the yum keyring.

Varnish Cache is also distributed in the EPEL (Extra Packages for
Enterprise Linux) package repositories. However, while EPEL allows
new versions to be distributed, it does not allow for
backwards-incompatible changes. Therefore, new major versions will
not hit EPEL and it is not necessarily up to date.
