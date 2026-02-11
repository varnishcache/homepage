Vinyl HTTP Cache
================

(The FOSS software formerly known as "Varnish HTTP Cache")

:ref:`I'm new here, please explain this Varnish thing <intro>`

What is happening
-----------------

Name-change in progress
~~~~~~~~~~~~~~~~~~~~~~~

We are in the process changing the project name now, so dont
be confused if you see Vinyl/Varnish being mixed up for a
while.

Vinyl Cache is moving - please prepare
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To prepare for the upcoming move of Vinyl Cache to a self hosted code forge,
please register an account if you are interested in continued collaboration with
the project by following `this link <https://code.vinyl-cache.org/user/sign_up?jwt=eyJhbGciOiJSUzI1NiIsImtpZCI6IkRWZFVKUFU5QlJVVUNRdHl5Uk1xcS00TmdIVXZJVmtSbE5BUE5jeDgyMmciLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiIvdXNlci9zaWduX3VwIiwiZXhwIjoxNzcxNDQwNjkyLCJpYXQiOjE3NzA4MzU4OTIsImlzcyI6Ii91c2VyL3NldHRpbmdzL2ludml0YXRpb25zIiwibmJmIjoxNzcwODM1ODkyLCJzdWIiOiJzbGluayJ9.LFDvydBh_cxhyvP1sOdobInlEr4OtqISQtwoDiYE6AvvI6q4A2PxqikFOrwpg5NP5dqSU84ctwxMmiDI61-ypk2nRGya6RW5xAu4PskcaDO8_41gob9SQ-MUtbJCBeldHpDJIrYi1GS_tmdjh4x2jEXne9vSoTXBAmFmh8k7c1gyJvtRJx_HJApPTbcreZ-ug2RjLGvK8zLf-llnPA1AeaeF1SRLZIGD6i8-wvT25u6Taaz64gPICl-I5k8mvwODCt1aZy3R9sUB9jY1YKxvKiBEhCpLn51Nr2cmSc9MzCOonqwsnIZ3Ql-aJo5BwAdvDl82fBiKOoZV6La7GOoW5Q>`_.

It expires 2026-02-18T19:51:32+01:00.

After this date, anyone who already has an account should be able to help out,
unless we still get abused by spammers and need to close registrations again.

If you have registered and do not receive the email confirmation, please check
your SPAM folder.

Announcing VCOT: OpenTelemetry Instrumentation for Vinyl-Cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We're happy to announce to have opened the repository of `VCOT
(VinylCacheOpenTelemetry)
<https://gitlab.com/uplex/varnish/VinylCacheOpenTelemetry>`_, a brand new
open-source (GPL) Go utility designed to enhance observability in Vinyl-Cache
(and, for the time being, Varnish-Cache) environments through an integration
with OpenTelemetry.

Up until now Vinyl-Cache was able to produce highly-detailed logs and provide
precise insight into the cache behavior, but it was not able to integrate with
modern observability standards.

VCOT addresses the need for modern monitoring in high-performance systems by
parsing Varnish Shared Logs (VSL) in real-time and exporting telemetry data -
traces, metrics, and logs - to OpenTelemetry-compatible backends.

This is just the beginning, VCOT is destined to evolve based on users' feedback.
Please open issue and/or PRs if you wish to see this tool improve.

.. _logo_contest:

Vinyl Cache - Logo and Mascot Contest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Edits:** We made changes since the first publication of this call for
participation. See :ref:`logo_contest_edits`.

After nearly 20 years, we decided to rename the FOSS Varnish Cache project to
Vinyl Cache as explained in `20 years old and it is time to get serious(er)`_.

To make this rebranding happen, we need a new logo and a mascot. This is why we
open a contest for the best design. The top 3 to 6 winners will be rewarded
monetary prizes and eternal fame among Vinyl Cache users (not guaranteed but
likely).

*How can you enter this contest?*

The contest consists of two categories. We encourage you to make combined
submissions for both, and we suspect that selecting matching submissions will be
a good choice, but we can not know this upfront.

*(A1) Logotype and logomark*

Design a logo. The logo should consist of two elements:

- the text "Vinyl Cache" (logotype)

- and a graphical logo / symbol (logomark) for Vinyl Cache.

It should be possible to use the logotype and logomark both in combination with
each other and separately, so provide both visual representations.

*(A2) Mascot*

The mascot should be a friendly character which users and contributors to Vinyl
Cache can positively identify with. Please do not suggest characters relating to
vinyl turntable records.

Some of the properties of Vinyl Cache which we think would be great to associate
with the mascot are it being

- fast and efficient,

- versatile,

- resilient, working reliably under tough conditions

- clean, secure, well tested

It should be possible to use the mascot character as a standalone visual and
also in combination with the logotype and logomark, so please provide both
visual representations if you make submissions to both categories.

*What to submit*

Please regard the competition as a pitch: Our intention is to see your ideas -
we do not need polished, finalized work, but rather drafts or sketches and
some idea of how your finished designs usually looks like. This can be in the
form of some examples or a portfolio.

To be clear, please submit:

* (A) your drafts/sketches of

  * (A1) Logotype and logomark *and/or*

  * (A2) Mascot

  and

* (B) your portfolio or other examples of your finished designs.

The competition entries can be in any accessible digital format like SVG, PNG or
PDF.

Please do not submit entries in proprietary formats.

*Winner selection*

The selection process will be guided not by how finished your entries are, but
rather by originality and how well your ideas represent our project, given that
you showed that you are able to finalize your work.

You get bonus points if you provide a good approximation of the logotype and
logomark in 7 bit ASCII (sorry, no UTF-8, we live in HTTP land).

See also `other rules <logo-other-rules>`_ below.

We promise to be as fair and objective as possible to mere mortals and the
judges will not get to see any creator identifying information (unless you put
it into your submission). But other than giving our word, the selection process
is entirely up to the founding members of the Vinyl Cache project and we accept
no jurisdiction of a court regarding the procedure of this competition.

*Monetary prizes*

We will award prizes to the three best designs either in both categories
combined or individually.

- top 1 winner: 1000€ or 500€ + 500€ in total

- top 2 winner: 250€ or 125€ + 125€

- top 3 winner: 250€ or 125€ + 125€

The Vinyl Cache project does not handle any money. These prizes are donated by
our long-term contributor https://uplex.de/

To make clear that we want to reward the tedious work of finalizing drafts, we
will first grant the same price of 250€ (for logo and mascot) or 125€ + 125€
(for logo or mascot) to all 3-6 best entries as submitted.

We will then work with the first winner for logo and/or mascot, respectively, to
finalize their work and pay out the remaining 750€ (for logo and mascot) or 375€
+ 375€ (for logo or mascot) for the final design.

*Timeline*

- Submit your designs until the end of November via email to:
  `logo@vinyl-cache.org <mailto:logo@vinyl-cache.org>`_.

- The winners will be announced in December 2025 on https://vinyl-cache.org/ and Mastodon.

.. _logo-other-rules:

*Other Rules*

.. _`CC BY`: https://creativecommons.org/licenses/by/4.0/

- You can submit as many design proposals as you wish.

- You may not use any AI tools for the creation of your submissions.

- You may only use fonts and other elements compatible with licensing under `CC
  BY`_. You may not use any elements incurring additional license fees.

- You get bonus karma points if you work with FOSS tools only (but we do not
  want to discriminate against any artist who chooses otherwise).

- By entering designs into the contest, you promise to make a finalized version
  of your entry available under the `CC BY`_ license if selected as a winner.
  Note that the Vinyl Cache project will have the same rights as everyone else.

- You are free to re-use non-winning entries for any other purpose, but we ask
  you to avoid a public conflict with the chosen Vinyl Cache project branding.

- In particular, we reserve the right not to name any winners if too few
  submissions meet our quality expectations.

- To redeem a price, you will need to issue a formal invoice.

2025-09-15 - New release: 8.0.0 with bonus project news
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have a new major release today: :ref:`8.0.0 <rel8.0.0>`,
and some major project news for you.

20 years old and it is time to get serious(er)
----------------------------------------------

Slagelse, 2025-09-15

This coming february 22nd, The Varnish Cache Project will officially
be 20 years old.  We consider the first surviving commit from the
subversion-to-git conversion the official birthday of the Project.

This is as good as any excuse to take stock and make some changes
so we are ready for the next 20 years.

Open Source is not what it used to be:  The EU has launched a
broadside of directives against software related industries, and
while they have gone to great lengths to carve out a niche for Free
and Open Source Software, they have wisely not chosen to make it a
"Get out of jail for free" card to slap "FOSS" sticker on something.

Concepts like "Maintainers", "Stewards" and "Contributors" of FOSS
have formal legal definitions now, and we need to find out how we
can and want to fit in.

Which again means we have to find out who makes that kind of decisions
for the project, both now and in the future.

Many successful FOSS projects have spawned "Foundations" which are
typically tax-exempt benefical/charity corporations in some country
or other, but we have decided to not go there.  For one thing, none
of us want to take on such a task, but more importantly:  We're are
less than impressed by how well that model seems to work in practice.

We will instead form a voluntary association, a "Forening", under
the laws of Denmark, with bylaws that set out what the goal is
(develop, maintain and distribute the software), who gets to make
the decisions (a governing board appointed by the members), who can
become members (anybody but subject to approval by the members) and
that the association cannot ever hold or handle any money.

The commented bylaws of the association will be ratified by the
founders and made public this autumn, and the first general assembly
will be on Monday February 23rd 2026 - hopefully with many membership
applications to approve - more about that when we publish the bylaws.

We will also, at the same time, reluctantly change the name of the project.

The Varnish Cache FOSS software was initiated and sponsored by the
Norvegian newspaper Verdens Gang.  They hired a company called
"Linpro" to handle the logistics and me to write the code.

From Linpro grew the company Varnish Software, and if anybody had,
they had earned the right to use "Varnish" in their name commercially. 

I was deeply worried about the potential for confusion and line
drawing issues between the commercial entity and the FOSS project,
and as Varnish Software have grown to become a huge international
company, those worries materialized.

I thought I had an verbal agreement with them, that "Varnish Cache"
was the FOSS project and "Varnish Software" was the commercial
entity, but the current position of Varnish Software's IP-lawyers
is that nobody can use "Varnish Cache" in any context, without their
explicit permission.

The need to get permission from Varnish Software to use our own
name has already caused some potential contributors and supporters
from engaging with the FOSS project.

We have tried to negotiatiate with Varnish Software for many months
about this issue, but their IP-Lawyers still insist that Varnish
Software owns the Varnish Cache name, and at most we have being
offered a strictly limited, subject to their veto, permission
for the FOSS project to use the "Varnish Cache" name.

We cannot live with that:  We are independent FOSS project with our own name.

So we will change the name of the project.

The new association and the new project will be named "The Vinyl
Cache Project", and this release 8.0.0, will be the last under the
"Varnish Cache" name.  The next release, in March will be under the
new name, and will include compatibility scripts, to make the
transition as smooth as possible for everybody.

I want to make it absolutely clear that this is 100% a mess of my
making:  I should have insisted on a firm written agreement about
the name sharing, but I did not.

I will also state for the record, that there are no hard feelings
between Varnish Software and the FOSS project.

Varnish Software has always been, and still is, an important and
valued contributor to the FOSS project, but sometimes even friends
can make a mess of a situation.

On behalf of the Varnish Cache Project,

Poul-Henning Kamp


2025-08-20 - New releases: 7.7.3, 7.6.5 and 6.0.16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are new releases available, :ref:`7.7.3 <rel7.7.3>`, :ref:`7.6.5
<rel7.6.5>` and :ref:`6.0.16 <rel6.0.16>`. These address a regression from
the handling of :ref:`VSV00017 <VSV00017>`.

2025-08-13 - Varnish HTTP/2 Made You Reset Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00017`

2025-08-13 - Security release 7.7.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish version :ref:`7.7.2 <rel7.7.2>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00017 <VSV00017>`.

2025-08-13 - Security release 7.6.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish version :ref:`7.6.4 <rel7.6.4>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00017 <VSV00017>`.

2025-08-13 - Security release 6.0.15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish version :ref:`6.0.15 <rel6.0.15>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00017 <VSV00017>`.

2025-05-12 - Security release 7.7.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.7.1 <rel7.7.1>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-05-12 - Request Smuggling Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00016`.

2025-05-12 - Security release 7.6.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.6.3 <rel7.6.3>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-05-12 - Security release 6.0.14
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.14 <rel6.0.14>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00016 <VSV00016>`.

2025-03-17  - Varnish 7.7.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.7.0`

The 7.5 series is no longer supported in any capacity.


2025-03-17 - Varnish HTTP/1 client-side desync vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00015`.

2025-03-17 - Security release 7.6.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.6.2 <rel7.6.2>` is now available.
This release addresses the vulnerability described in
:ref:`VSV00015 <VSV00015>`.

2024-11-08 - Varnish 7.6.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.6.1 has been released and can be found here: :ref:`rel7.6.1`

This maintenance release fixes a few bugs introduced in 7.6.0.

2024-09-13 - Varnish 7.6.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.6.0`

The 7.4 series is no longer supported in any capacity.

2024-03-18 - Varnish 7.5.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.5.0`

The 7.3 series is no longer supported in any capacity.

2024-03-18 - Varnish HTTP/2 Broke Window Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Varnish Cache releases with HTTP/2 support suffer a vulnerability in
the HTTP/2 protocol. Please see :ref:`VSV00014` for more information.

2024-03-18 - Security releases: 6.0.13, 7.3.2 and 7.4.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.13 <rel6.0.13>`, :ref:`7.3.2 <rel7.3.2>` and
:ref:`7.4.3 <rel7.4.3>` are now available. These releases are published to
address the vulnerability described in :ref:`VSV00014 <VSV00014>`.

2024-02-06 - `SLASH/`_ 1.0.0-rc1
--------------------------------

.. _`SLASH/`: https://gitlab.com/uplex/varnish/slash/-/blob/master/README.rst

Celebrating the 18th anniversary of Varnish-Cache and the first
anniversary of the `SLASH/`_ storage engines today, your Open-Source
Varnish-Cache friends from `UPLEX`_ have just tagged the first version
1.0.0 candidate of our extension with storage engines (stevedores) and
storage routers (loadmasters).

Over the past year, we have received a lot of helpful input from our
users and have implemented substantial improvements. THANK YOU to
everyone who has contributed by reporting issues, providing feedback
and, just recently, adding documentation. SLASH/fellow has also helped
improve Varnish-Cache itself.

After rigorous testing in particular over the past weeks, we now
boldly claim that SLASH/ deserves a 1.0 version tag.

HAPPY BIRTHDAY Varnish-Cache!

HAPPY BIRTHDAY SLASH/buddy and SLASH/fellow!

.. _`Mastodon post`: https://fosstodon.org/@slink/111886397903235142

.. _`Changelog`: https://gitlab.com/uplex/varnish/slash/-/blob/master/CHANGES.rst?ref_type=heads

Continue reading:

* `Mastodon post`_
* `Changelog`_


2023-11-13 - Varnish HTTP/2 Rapid Reset Attack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Varnish Cache releases with HTTP/2 support suffer a vulnerability in
the HTTP/2 protocol. Please see :ref:`VSV00013` for more information.

2023-11-13 - Security releases: 6.0.12, 7.3.1 and 7.4.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.12 <rel6.0.12>`, :ref:`7.3.1 <rel7.3.1>` and
:ref:`7.4.2 <rel7.4.2>` are now available. These releases are published to
address the vulnerability described in :ref:`VSV00013 <VSV00013>`.

2023-09-20 - Varnish 7.4.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.4.1 has been released and can be found here: :ref:`rel7.4.1`

This maintenance release fixes a bug preventing protected headers
to be read from several subroutines.

2023-09-15 - Varnish 7.4.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.4.0`

The 7.2 series is no longer supported in any capacity.


2023-08-17 - VSV00012: Vulnerability in vmod_digest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see :ref:`vsv00012`

2023-03-15 - Varnish 7.3.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.3.0`

The 7.1 series is no longer supported in any capacity.

2023-02-06 - Two new Storage Engines for Varnish-Cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _`UPLEX`: https://uplex.de/

Celebrating the 17th anniversary of Varnish-Cache today, your
Open-Source Varnish-Cache friends from `UPLEX`_ have just released an
extension with two new storage engines (stevedores) and two basic
storage routers (loadmasters). One of the storage engines, `fellow`,
offers persistent storage on disks (or SSDs, rather).

The preferred public repository with support for issues,
merge-requests and other activities is at
https://gitlab.com/uplex/varnish/slash

.. _`The SLASH/ Announcement`: https://vinyl-cache.org/lists/pipermail/varnish-announce/2023-February/000757.html

.. _`The SLASH/ README`: https://gitlab.com/uplex/varnish/slash/-/blob/master/README.rst

.. _`The SLASH/ module documentation`: https://gitlab.com/uplex/varnish/slash/-/blob/master/src/vmod_slash.man.rst

To read more:

* `The SLASH/ Announcement`_
* `The SLASH/ README`_
* `The SLASH/ module documentation`_

2022-11-08 - Request Forgery Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request forgery
vulnerability on HTTP/2 connections. Please see :ref:`VSV00011` for more
information.

2022-11-08 - Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache releases 7.1 and 7.2 suffer from a Request Smuggling
vulnerability. Please see :ref:`VSV00010` for more information.

2022-11-08 - Security releases: 6.0.11, 7.2.1 and 7.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.11 <rel6.0.11>`, :ref:`7.2.1 <rel7.2.1>` and
:ref:`7.1.2 <rel7.1.2>` are now available. These releases are published to
address the vulnerabilities described in :ref:`VSV00010 <VSV00010>` and
:ref:`VSV00011 <VSV00011>`.

2022-09-15 - Varnish 7.2.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.2.0`

The 7.0 series is no longer supported in any capacity.

2022-08-09 - Denial of Service Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache releases 7.0 and 7.1 suffer from a Denial of Service
vulnerability. Please see :ref:`VSV00009` for more information.

2022-08-09 - Security releases: 7.1.1 and 7.0.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`7.1.1 <rel7.1.1>` and :ref:`7.0.3 <rel7.0.3>` are
now available. These releases fix the vulnerability described in
:ref:`VSV00009 <VSV00009>`.

2022-03-15 - Varnish 7.1.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.1.0`

The 6.6 series is no longer supported in any capacity.

2022-01-25 - HTTP/1 Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request smuggling
vulnerability on HTTP/1 connections. Please see :ref:`VSV00008` for more
information.

2022-01-25 - Security releases: 6.0.10, 7.0.2 and 6.6.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.10 <rel6.0.10>`, :ref:`7.0.2 <rel7.0.2>` and
:ref:`6.6.2 <rel6.6.2>` are now available. These releases fix the
vulnerability described in :ref:`VSV00008 <VSV00008>`.

2021-11-24 - Varnish 6.0.9 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 6.0.9 has been released and can be found here: :ref:`rel6.0.9`

This maintenance release is recommended for all users of the 6.0 LTS
and contains several bug fixes.

2021-11-23 - Varnish 7.0.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish 7.0.1 has been released and can be found here: :ref:`rel7.0.1`

This is a maintenance release to correct some bugs that got into the 7.0.0
release.

2021-09-15 - Varnish 7.0.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel7.0.0`

The 6.5 series is no longer supported in any capacity.

(The 2022-03-15 release is likely to be 8.0.0)

2021-08-17 - Open Source parallel ESI for varnish-cache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On

  * https://code.uplex.de/uplex-varnish/libvdp-pesi
  * https://gitlab.com/uplex/varnish/libvdp-pesi (mirror)

we have released a Varnish Delivery Processor (VDP) for parallel ESI processing,
which can deliver relevant speedups where portions of ESI-processed objects are
not served from cache.

.. _`The pESI Announcement`: https://vinyl-cache.org/lists/pipermail/varnish-announce/2021-August/000746.html

Read `The pESI Announcement`_ for more details.

2021-07-13 - HTTP/2 Request Smuggling Vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a request smuggling
vulnerability when the HTTP/2 support is enabled. Please see
:ref:`VSV00007` for more information.

2021-07-13 - Security releases: 6.0.8, 6.6.1 and 6.5.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions :ref:`6.0.8 <rel6.0.8>`, :ref:`6.6.1 <rel6.6.1>` and
:ref:`6.5.2 <rel6.5.2>` are now available. These releases fix the
vulnerability described in :ref:`VSV00007 <VSV00007>`.

2021-07-13 - Varnish 6.0.8 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.8`.

This combined maintenance and security release is recommended for all
users of the 6.0 LTS and contains several bug fixes, improvements and new
features. More information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_

2021-03-16 - Denial of Service in varnish-modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some versions of the separate `varnish-modules` bundle allow for a
potential denial of service attack when the ``header.append()`` or
``header.copy()`` functions are used.

Please see :ref:`VSV00006`.

2021-03-15 - Varnish 6.6.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release is here:  :ref:`rel6.6.0`

(The 2021-09-15 release is likely to be 7.0.0)

2020-11-06 - Varnish 6.0.7 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are happy to announce the release of :ref:`rel6.0.7`.

This maintenance release is recommended for all users of the 6.0 LTS
and contains several bug fixes, improvements and new features. More
information is available in the
`Change log <https://github.com/varnishcache/varnish-cache/blob/6.0/doc/changes.rst>`_


2020-09-25 - Varnish 6.5.1 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When preparing the 6.5.0 release, it was forgotten to bump the
VRT_MAJOR_VERSION number defined in the `vrt.h` include file. This major
version bump is needed due to the API and ABI changes as part of the
release, to make sure that VMODs are not allowed used if they were
compiled for the wrong Varnish version.

This has been fixed in the :ref:`rel6.5.1` release.


2020-09-15 - Varnish 6.5.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Come and get it... :ref:`rel6.5.0`


2020-03-16 - Varnish 6.4.0 is released
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our bi-annual "fresh" release :ref:`rel6.4.0`

2020-02-04 - Security Advisory: Denial of Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All supported versions of Varnish suffer from a denial of service attack
when using the Proxy Protocol version 2. Please see :ref:`VSV00005
<VSV00005>`.

2020-02-04 - Security releases: 6.0.6, 6.2.3 and 6.3.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish versions 6.0.6, 6.2.3 and 6.3.2 are now available. See
:ref:`VSV00005 <VSV00005>` for details.

:ref:`Older news <oldnews>`

Package repository status
-------------------------

The official Linux (apt/yum) package repositories are now located
at Packagecloud.io.
A list of all available repositories can be found at:
https://packagecloud.io/varnishcache

For more details on packages, see :ref:`Releases & Downloads <releases>`

Privacy
-------

You can access the varnish-cache homepages with HTTP or HTTPS as you
like.

We save the logfiles from our Varnish instance for a limited period,
in order to be able to debug problems.

We do not use any external trackers and do not analyze traffic.

.. toctree::
   :hidden:

   intro/index
   security/index
   business/index
   releases/index
   docs/index
   support/index
   extras/index
   vmods/index
   tips/index
   tutorials/index
   organization/index
   misc/gdpr-redacted
