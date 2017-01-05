Varnish HTTP Cache
==================

:ref:`I'm new here, please explain this Varnish thing <intro>`

:ref:`Questions and Answers<faq>`

What is happening
-----------------

2017-01-05 - Source Code Coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I usually brag that we have 90%+ automatic test coverage in Varnish,
and that comes with a couple of footnotes.

The main one is that we don't automatically test the curses(3) based
tools (varnish{hist|top|stat|...}) - only because I havn't found a
way to do so.

For 2017 I've raised the bar: from now our goal is 90%+ on *all* our
source code.

At the same time, I have retooled our code coverage test scripts
so the `GCOV results can be seen online </gcov>`_ .

Presently at 81.8%, but we'll get there...

/phk

2016-12-21 - Project server upgraded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now running FreeBSD 11-RELEASE /phk

2016-12-02 - Maintenance release of 4.1.4, 4.0 is End Of Life
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache 4.1.4 has been released and is ready for download. This
is a maintenance release with bug fixes and performance enhancements.

In other news, Varnish Cache 4.0 has reached End Of Life, and with
this we have released Varnish Cache 4.0.4. This contains all the last
fixes from git, and there will be no 4.0.5. Please upgrade to 4.1 or 5.0
as soon as you can.

Pål Hermunn Johansen, Varnish Software Group

2016-11-21 - New Tool in Town
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I finally sat down and wrote a Varnish specific "Continuous
Integration" tool, and people are busy starting it on the various
machines we use for testing in the project.

You can `see the result(s) here. </vtest/index.html>`_

If you want to run a "sandbox" for us, you just need to run
`a small simple shell-script
<https://github.com/varnishcache/varnish-cache/blob/master/tools/vtest.sh>`_
- there is `no need for a Java Runtime or anything else.
</docs/trunk/phk/trialerror.html>`_

/phk


2016-09-27 - Send us (more) money!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If we want to keep up the same activity level as the last couple
of years, we need €2000/month to buy more of Poul-Hennings time.

So if Varnish improves your company's profit, please invest in a
one-time or recurring `Varnish Moral License <http://phk.freebsd.dk/VML>`_
to help fund the projects future.

Thanks in advance!

And a big thanks to the companies already sponsoring Varnish:

* Fastly
* Varnish-Software
* UPLEX
* [your companys name could have been here...]


2016-09-15 - Varnish 5.0
~~~~~~~~~~~~~~~~~~~~~~~~

Varnish Cache 5.0.0 has been released!  /Lasse /phk

See:

* :ref:`Releases` 
* `Release Note </docs/5.0/whats-new/relnote-5.0.html>`_
* `Upgrading </docs/5.0/whats-new/upgrading-5.0.html>`_
* `Changes </docs/5.0/whats-new/changes-5.0.html>`_

(And yes, we're dog-food running it on the varnish-cache.org site)


Privacy
-------

You can access the varnish-cache homepages with HTTP or HTTPS as you
like.

We save the logfiles from our Varnish instance for a limited period,
in order to be able to debug problems.

The old homepage ran Google Analytics, and we have continued that here
for now, but unless we actually learn something useful from the data
they collect, it will be discontinued.


.. toctree::
   :hidden:

   intro/index
   security/index
   news/index
   business/index
   faq/index
   releases/index
   docs/index
   support/index
   extras/index
   vmods/index
   tips/index
