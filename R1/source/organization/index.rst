.. _organization:


Varnish Cache organization and day-to-day operation
===================================================

The Varnish cache project is going through a transition on how it is
organized. This page describes the current state of affairs, and the
direction we are moving in.

.. _organization_behavior:

Behavior / Code of conduct
--------------------------

General rules about how contributors should behave within the Varnish
Cache project:

* Show respect for others.

* Be sensible.

* If in doubt, think.

* If still in doubt, ask.

* Admit your mistakes, it's faster that way.

* Thou SHALL not paint `bikesheds. <http://bikeshed.org/>`_

* We will toss you out of the project rather than add another rule.

.. _organization_current_governance:

Current governance of the project
---------------------------------

We recognize that the Truck Factor of the Varnish Cache project is low.

As mitigation we have created a Varnish Governance Board (VGB)
and implemented procedures so no project asset have a Truck Factor
less than 3.

The Varnish Governance Board is the ultimate authority in the
project, but does little to nothing on a daily basis.

The important thing is that there is agreement beforehand about who
has the authority to step in, if need be.

Appointment to the VGB is by acclamation, and we prefer the members
to have enough distance and neutrality to be able to resolve
conflicts, should it ever become necessary.

Current members of the VGB:

* Rogier Mulhuijzen
* Lasse Karstensen
* Poul-Henning Kamp

.. _organization_near_future:

Governance of the Varnish Cache Project in the near future
----------------------------------------------------------

The Varnish Governance Board (VGB) was originally nominated to
formally govern the project in order to mitigate a low Truck Factor
and resolve conflicts, but has been inactive for several years.

As of September 2019, Martin Blix Grydeland (Varnish Software) and
Nils Goroll (UPLEX) have been tasked by the participants of the
Varnish Developer Day (VDD) with working out a suggestion for
bootstrapping the process to transfer the Varnish Cache project to an
independent legal entity in the form of a Verein / Forening /
Foundation. This entity would then elect a new VGB, which should have
enough distance and neutrality to be able to resolve conflicts, should
it ever become necessary.

.. _organization_maintainers:

Maintainer Roles
----------------

Regarding the day-to-day development of Varnish-Cache, decisions are
made by project maintainers on:

* disputed pull requests
* VIPs
* which contributors should be granted the commit bit
* and all other relevant decisions regarding the design of Varnish Cache

When a change is proposed, maintainers must get ample time to review
the proposition. Then, if the maintainers who are *for* the change
outnumber the ones *against* by at least two, the pull request can be
merged or the change implemented.

Maintainers are nominated by VDD participants by majority decision,
and will in the future be ratified by the VGB.

As of September 2019, three maintainer "hats" have been nominated,
held by

* Firma den Andensidste Viking (Poul-Henning Kamp)
* Varnish Software
* UPLEX

The companies will nominate a developer as their maintainer, and this
can vary throughout the year (to allow for vacations etc.).

.. _organization_vdd:

The Varnish Developer Day
-------------------------

The Varnish Developer Day (VDD) has, in recent years, been by
invitation only, and traditionally, core developers and relevant
supporters of the project participated. The exact rules for future
Developer Days are still to be worked out, but the project will
continue to invite all developers who have made meaningful
contributions. The purpose of the VDD will remain to provide a
platform for discussion of technical aspects of Varnish and its
implementation.

We are also looking to bring back Varnish User Group (VUG) meetings
before or after VDDs so that Varnish users can take a bigger part in,
and have a bigger influence on the direction of Varnish Cache.

.. _organization_issues:

Bugs, pull requests, feature requests
-------------------------------------

Bugs start out as GitHub issues or, if they already have a patch, Pull
Requests.

Security issues should be reported responsibly, by sending a PGP
encrypted email to one or more of the maintainers. See
:ref:`security` for more information on this.

Feature requests should be sent to the `varnish-misc mailing list
<https://varnish-cache.org/lists/mailman/listinfo/varnish-misc>`_. A
feature request which is considered important and where a developer is
assigned to implement it, *can* be made into an issue. The list is
meant to be a place where developers can bring up ideas of features and
their implementation, before the actual code is written.

If a feature request make sense, but is not picked up by a developer,
it gets moved to a wiki/VIP page until somebody implements it.

Monday at 15:00-15:30 (EU time) we "bug-wash" on IRC to decide who
handles which issue and how. See the :ref:`support` for details on how
to reach us on IRC. Maintainers are present during the bug-wash, and
external contributors are encouraged to attend to discuss any Pull
Requests or bug reports they have submitted.

Pull requests are obligatory for all contributions, unless they
qualify for the exceptions laid out below.

Everybody are encouraged to review pull requests.

Maintainers can approve pull requests, as described in
:ref:`organization_maintainers` above.

The exception to the pull request process are trivial, *risk free*
changes, which can be committed and pushed (by a developer with the
*commit bit*) without a review. These include in particular, but are
not limited to,

* Documentation changes, unless they concern policies or governance of
  the project

* Simple bug fixes tested by a varnishtest case (VTC).

The commit bit
--------------

The commit bit is handed out to contributors who have proven their
knowledge of Varnish internals, and must be approved unanimously by
the maintainers.

Committers who have not made contributions in 18 months will have
their commit bit suspended, but can ask the maintainers to hand it
back.

Commit bits expire after 36 months with no contribution.

.. toctree::
   :hidden:
