.. _security:

Security, bugs & vulnerabilities
================================

* Rev. 2021-03-16 *slink*

List of all Varnish CVEs
------------------------

============= =============== ============================================
Versions      CVE             What
============= =============== ============================================
6.x, 7.x      <TBD>           :ref:`vsv00011`
7.1, 7.2      <TBD>           :ref:`vsv00010`
7.0, 7.1      CVE-2022-38150_ :ref:`vsv00009`
< 7.0.2       CVE-2022-23959_ :ref:`vsv00008`
6.0, 6.5, 6.6 CVE-2021-36740_ :ref:`vsv00007`
(6.5)         CVE-2021-28543_ :ref:`vsv00006`
6.0, 6.2, 6.3 CVE-2020-11653_ :ref:`vsv00005`
6.0, 6.2, 6.3 CVE-2019-20637_ :ref:`vsv00004`
6.0, 6.2      CVE-2019-15892_ :ref:`vsv00003`
4.1, 5.2      CVE-2017-8807_  :ref:`vsv00002`
4.x, 5.x      CVE-2017-12425_ :ref:`vsv00001`
< 3.0.5       CVE-2013-4484_  DoS
<= 3.0.3      CVE-2013-0345_  Local information leak
2.0.6         CVE-2009-4488_  Trophy hunting
< 2.1.0       CVE-2009-2936_  Trophy hunting
============= =============== ============================================

.. _CVE-2020-11653:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11653
.. _CVE-2019-20637:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-20637
.. _CVE-2019-15892:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-15892
.. _CVE-2017-8807:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8807
.. _CVE-2017-12425:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-12425
.. _CVE-2013-4484:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-4484
.. _CVE-2013-0345:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0345
.. _CVE-2009-4488:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-4488
.. _CVE-2009-2936:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-2936
.. _CVE-2021-28543:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28543
.. _CVE-2021-36740:     https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36740
.. _CVE-2022-23959:     https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23959
.. _CVE-2022-38150:	https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38150

.. toctree::
	:hidden:
	:maxdepth: 1

	VSV00011.rst
	VSV00010.rst
	VSV00009.rst
	VSV00008.rst
	VSV00007.rst
	VSV00006.rst
	VSV00005.rst
	VSV00004.rst
	VSV00003.rst
	VSV00002.rst
	VSV00001.rst
	gpg.rst

We take security and quality *very* seriously in the Varnish project,
and we are more than a little proud that it took eleven years before
we had a major security issue.

I have found a security hole
----------------------------

Send email to Poul-Henning, Nils and Martin: :ref:`gpg_keys`

I want to hear about security vulnerabilities
---------------------------------------------

Subscribe to the `Varnish Announce mailing list </lists/mailman/listinfo/varnish-announce>`_

Vulnerabilities are and will also be listed further at the top of this page when they are new
and further down when they get older.

I'm a VIVU goddammit!
---------------------

Varnish users come in all sizes and importance, some are private
homepages, some are global CDNs, national governments or major
news outlets.

We want to provide some way to for Varnish users to get early warning about
future security incidents, but we do not want to pass judgement on
who are "Very Important Varnish Users" and much less to we want to
try to keep a list of up to date contact information for a list
that long.

We also don't want to make this information free, because if we
did, every criminal and his brother would sign up, to get a head
start against the Varnish users.

The rule going forward is therefore that if you contributed at least
EUR240 towards a `Varnish Moral License <http://phk.freebsd.dk/VML/>`_
in the 12 months previous to the disclosure-date, you will get early
warning about security issues.

On a case-by-case basis and purely at our discretion, we will also
extend this privilege to people who have contributed significantly
to the project in other ways.

Security Politics
-----------------

To be totally honest, this is section is quite speculative, we have
very little experience in this area, but this is how I expect we
would react to a major security issue:

* Assign a VSV number
* Try to get a CVE assigned.
* Create a VCL workaround, if at all possible.
* Fix the problem.
* If it makes sense (ie: no VCL workaround), roll a point-release.
* Announce on announce@varnish-cache.org and homepage.
* Kick ourselves, for *months*, for missing the bug.

Define "Major"
--------------

As you will notice if you peruse the CVEs listed above, we are not
kindly inclined to trophy-hunting and shrill alarmism.

If security advisories are to have any utility, they should be both
rare and relevant.

In particularly we do not consider it a security vulnerability that
somebody has a different taste in program architecture, or that
aliens might be able to DoS varnish servers if they have invented
quantum computers we cannot even comprehend.

On the other hand, if we find anything, on our own or thanks to
external contributors, which imperil Varnish users, we will not
hesitate to issue a CVE to get peoples attention.

11 years, really?
-----------------

Yes, indeed.  Luck probably has a lot to do with it, but luck tends
to favour the well-prepared, and we have had a big focus on quality
since the very start.

`Here is a piece I wrote about it last year </docs/trunk/phk/thatslow.html>`_
