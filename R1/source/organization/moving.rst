.. _moving:

Vinyl Cache is moving
=====================

As of 2026-02-12, we are about to move all our collaboration activities off
github. First and foremost, here is

... what you need to do
~~~~~~~~~~~~~~~~~~~~~~~

To prepare for the upcoming move of Vinyl Cache to a self hosted code forge,
please register an account if you are interested in continued collaboration with
the project by following `this link <https://code.vinyl-cache.org/user/sign_up?jwt=eyJhbGciOiJSUzI1NiIsImtpZCI6IkRWZFVKUFU5QlJVVUNRdHl5Uk1xcS00TmdIVXZJVmtSbE5BUE5jeDgyMmciLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiIvdXNlci9zaWduX3VwIiwiZXhwIjoxNzcxNDQwNjkyLCJpYXQiOjE3NzA4MzU4OTIsImlzcyI6Ii91c2VyL3NldHRpbmdzL2ludml0YXRpb25zIiwibmJmIjoxNzcwODM1ODkyLCJzdWIiOiJzbGluayJ9.LFDvydBh_cxhyvP1sOdobInlEr4OtqISQtwoDiYE6AvvI6q4A2PxqikFOrwpg5NP5dqSU84ctwxMmiDI61-ypk2nRGya6RW5xAu4PskcaDO8_41gob9SQ-MUtbJCBeldHpDJIrYi1GS_tmdjh4x2jEXne9vSoTXBAmFmh8k7c1gyJvtRJx_HJApPTbcreZ-ug2RjLGvK8zLf-llnPA1AeaeF1SRLZIGD6i8-wvT25u6Taaz64gPICl-I5k8mvwODCt1aZy3R9sUB9jY1YKxvKiBEhCpLn51Nr2cmSc9MzCOonqwsnIZ3Ql-aJo5BwAdvDl82fBiKOoZV6La7GOoW5Q>`_.

It expires 2026-02-18T19:51:32+01:00.

After this date, anyone who already has an account should be able to help out,
unless we still get abused by spammers and need to close registrations again.

If you have registered and do not receive the email confirmation, please check
your SPAM folder.

... an overview of what is going to happen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At some point in time, probably at around 2026-02-13 (no, we are absolutely not
superstitious), we are going to start the migration from github to
https://code.vinyl-cache.org.

After this point, the following will happen for each of our github repositories
in turn:

* A ``last`` tag will be pushed.

* A note will be added to the README to inform about the migration, new
  repository location and ``last`` tag.

* The central script/tool called for code builds will be changed to fail and
  point to the README. This will usually be ``configure`` or a primary ``make``
  target.

* The repository will be set to *archived*. This will mean that no changes to
  the code, pull requests, issues, the wiki or whatever will be possible.

* The repository will be migrated to the new location. Migration should include
  all date.

* Once the migration is complete and manual sanity checks look OK, the
  repository will be opened at the new location.

Location mapping old/new
~~~~~~~~~~~~~~~~~~~~~~~~

This process will be repeated for all our repositories, given here with old and
new location. The translation rules are:

* the prefix changes from ``https://github.com/varnishcache/`` to
  ``https://code.vinyl-cache.org/vinyl-cache/``.

* in the project name, ``varnish`` is replaced with ``vinyl``.

Or expressed as a ``sed`` command::

        sed -e 's:github.com/varnish:code.vinyl-cache.org/vinyl-:; s:varnish:vinyl:'

==================================================== ==========================================================
old                                                  new
==================================================== ==========================================================
https://github.com/varnishcache/varnish-cache        https://code.vinyl-cache.org/vinyl-cache/vinyl-cache
https://github.com/varnishcache/homepage             https://code.vinyl-cache.org/vinyl-cache/homepage
https://github.com/varnishcache/pkg-varnish-cache    https://code.vinyl-cache.org/vinyl-cache/pkg-vinyl-cache
https://github.com/varnishcache/varnish-devicedetect https://code.vinyl-cache.org/vinyl-cache/vinyl-devicedetect
https://github.com/varnishcache/libvmod-example      https://code.vinyl-cache.org/vinyl-cache/libvmod-example
https://github.com/varnishcache/fuzzdata             https://code.vinyl-cache.org/vinyl-cache/fuzzdata
https://github.com/varnishcache/vc-commit-event      https://code.vinyl-cache.org/vinyl-cache/vc-commit-event
https://github.com/varnishcache/pkg-debian           https://code.vinyl-cache.org/vinyl-cache/pkg-debian
https://github.com/varnishcache/varnish-release-rpm  https://code.vinyl-cache.org/vinyl-cache/vinyl-release-rpm
==================================================== ==========================================================


These are the web frontend URLs. The git clone URLs change accordingly with
``.git`` appended, ssh access changes from ``git@github.com:___.git`` to
``git@code.vinyl-cache.org/___.git`` with paths substituted as per the table
above.

Note that some repositories have not been in use for some time. We will still
migrate them and possibly decide to then also archive them on our own forge.


What we will do after the migration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the migration is done, we will be very busy getting our tooling back, which
is mainly vtest and other CI as well as the automatic website update.

When the dust has settled, we will add mirrors, which will provide read only
access to *code only*. They will get announced on https://vinyl-cache.org

