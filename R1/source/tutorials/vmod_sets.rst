Sets in VMODs re2 and selector
==============================

.. contents:: Table of Contents
   :local:

Eliminate the elsifs
--------------------

Here's a common sight in many VCL deployments::

  sub vcl_backend_fetch {
	if (bereq.url ~ "^/foo/") {
		set bereq.backend = foo_backend;
	}
	elsif (bereq.url ~ "^/bar/") {
		set bereq.backend = bar_backend;
	}
	elsif (bereq.url ~ "^/baz/") {
		set bereq.backend = baz_backend;
	}
	elsif (bereq.url ~ "^/quux/") {
		set bereq.backend = quux_backend;
	}

	# ... and more elsifs to follow ...
  }

This snippet shows a common way to route requests to backends --
according to the prefix of the URL path. In this tutorial we will
focus not so much on a subject such as backend routing, but rather on
the pattern in VCL. Sequences such as this, string matches in a series
of ``if-elsif-elsif`` comparisons, are ubiquitous in VCL, deployed for
numerous purposes:

* Routing to backends based on URL path (as above) or the Host header
* URL rewrites
* Generating redirect responses for selected Hosts or URL paths
* Choosing to return ``pass`` or ``hash`` in ``vcl_recv`` for selected
  URL paths
* Setting the cache TTL of backend responses for selected URL paths
* Dispatching subroutine calls based on the URL path on Host header

These functions and many others are often implemented in VCL by
similar means -- sequences of string comparisons in an
``if-elsif-elsif`` series.

Of course there's no problem with that if only a handful of
comparisons are necessary. But the ``if-elsif-elsif`` solution doesn't
scale. What if your site is a large deployment with dozens of
backends? What if there are hundreds of URLs that need to be
rewritten? What if you need to recognize requests with many different
URL paths as having uncachaeble responses, so that you can return
``pass`` for those but not for others?

VCL with several screenfuls of ``if-elsif-elsif`` sequences are not
unusual for many Varnish deployments, and the longer your ``elsif``
train becomes, the longer it takes to process them all. One way to get
a handle on that is to put the most frequently matched strings first
in the series. But that requires knowledge of the frequency of
requests at your site, which may be changing all the time. Getting the
order right between, say, the 20th and 30th ``elsif`` is a chore that
will hardly be kept up to date on a regular basis. And even then,
requests with the misfortune of being matched by the last ``elsif``,
or not matching any of them, will always take the longest path.

But what if you could just do this::

  sub vcl_backend_fetch {
	if (backend_dispatch.match(bereq.url)) {
		set bereq.backend = backend_dispatch.backend();
	}
  }

This snippet makes use of a VMOD object ``backend_dispatch`` and a
method ``.match()`` to do all of the string matching in a single
operation. When the match succeeds, the backend assignment is done
with the method ``.backend()`` -- a kind of associative array that
maps URL path patterns to backends. The match operation scales well
for large sets of strings, and the result is short and easily
maintainable VCL code. No ``elsif`` is necessary.

.. _vmod_re2: https://gitlab.com/uplex/varnish/libvmod-re2
.. _vmod_selector: https://gitlab.com/uplex/varnish/libvmod-selector/

In the following we take a look at two VMODs, `re2 <vmod_re2_>`_ and
`selector <vmod_selector_>`_, that make this possible. Both VMODs
provide objects called *sets* -- collections of patterns and strings
with scalable match operations, associations to other objects such as
backends, and a few other useful features.

Sets in VMOD re2
----------------

For VMOD re2, we declare the set object ``backend_dispatch`` from the
previous example like this::

  import re2;

  sub vcl_init {
	new backend_dispatch = re2.set(anchor=start);
        backend_dispatch.add("/foo/", backend=foo_backend);
        backend_dispatch.add("/bar/", backend=bar_backend);
        backend_dispatch.add("/baz/", backend=baz_backend);
        backend_dispatch.add("/quux/", backend=quux_backend);
  }

The constructor in ``vcl_init`` defines ``backend_dispatch`` as a
``set`` object of VMOD re2. Its parameter ``anchor=start`` means that
each pattern in the set is matched as if it begins with the regular
expression symbol ``^`` for start-of-text -- meaning that any match
can only be at the beginning of a string.

The invocations of the ``.add()`` method specify the data of the
``set`` -- the patterns to be matched, and in this case the backends
to be associated with each pattern, specified with the ``backend``
argument.

.. _libre2: https://github.com/google/re2/
.. _re2_set: https://github.com/google/re2/blob/main/re2/set.h

VMOD re2 is a wrapper for the
`Google re2 regular expression library <libre2_>`_, which has a
`set class <re2_set_>`_. An re2 set can be understood as the regular
expression formed from the alternation of all of the patterns added to
it -- all of them joined with the `|`  operator for "or"::

  ^/foo/|^/bar/|^/baz/|^/quux/

But an re2 set differs from this regex in two ways:

#. If a string matches successfully against the set (i.e. against the
   alternation of patterns), we know afterward *which* pattern matched.

#. The match operation does not attempt to match against each pattern
   individually, one after the other. Instead, it scans the string to
   be matched from left to right, following the paths that may lead to
   a match.

The first property makes it possible to associate the matched string
with a backend, or with other kinds of objects as we shall see.

The second property makes set matches scalable. To get an idea of how
it works, consider matching the path ``/bar/index.html`` against the
set shown in the example above:

* The first character must be ``/``, followed by an ``f``, ``b`` or
  ``q``.
* We match ``/b`` in the URL path, so the next character must be ``a``
  followed by ``r`` or ``z``.
* We match the ``a`` and ``r``, as well as the ``/`` that must follow.

Thus we have shown that ``/bar/index.html`` matches the pattern
``/bar/``, without having to evaluate each pattern in order, as an
``if-elsif-elsif`` sequence would have done.

The re2 library's pattern matching execution may be more involved than
that, because it supports regular expressions in each element of the
set. In this example, static assets are identified by the URL path,
either with the prefix ``/assets/``, or by file extensions that are
typical for static resources::

  import re2;

  sub vcl_init {
	new static = re2.set();
        static.add("^/assets/");
        static.add("\.html$");
        static.add("\.png$");
        static.add("\.jpg$");
        static.add("\.jpeg$");
        static.add("\.css$");
        static.add("\.js$");
  }

In this case we don't declare the set with an ``anchor`` parameter,
because the individual patterns use ``^`` or ``$`` to set anchors at
the start or end of the string to be matched.

The ``static`` set can then be used to set a long cache TTL for
responses whose request URL matches a pattern in the set::

  sub vcl_backend_response {
	if (static.match(bereq.url)) {
		set beresp.ttl = 1d;
	}
  }

But even with more complex patterns in the set, the principle is the
same -- the string to be matched is scanned from left to right, and
the matcher follows paths that may lead to a potential match, or
stopping at the first character that cannot lead to any match. That
way, the re2 library and VMOD can match a large number of patterns
simultaneously, in a single line.

Sets in VMOD selector
---------------------

Regular expressions, as supported by VMOD re2, are powerful tools for
pattern matching, and many use cases for Varnish call for their full
capabilities. But string matching in VCL can also be quite simple. In
the examples of prefix matches that we have seen so far, fixed strings
are constrained to match at the beginning of a string; but other than
that, the patterns have not used any other regex syntax::

  # Prefixes match at the start-of-text with '^', but are otherwise
  # all fixed strings.
  if (req.url ~ "^/foo/") {
	# ... code for prefix /foo/ ...
  }
  elsif (req.url ~ "^/bar/") {
	# ... code for prefix /bar/ ...
  }
  elsif (req.url ~ "^/baz/") {
	# ... code for prefix /baz/ ...
  }

  # ... more elsifs ...
  
For some purposes, we don't do any pattern matching at all, but only
compare strings for equality::

  # Matching host names for string equality only.
  if (req.http.Host == "www.foo.com") {
	# ... code for host www.foo.com ...
  }
  elsif (req.http.Host == "www.bar.com") {
	# ... code for host www.bar.com ...
  }
  elsif (req.http.Host == "www.baz.com") {
	# ... code for host www.baz.com ...
  }

  # ... and so on ...

This is not unusual for string matching requirements in VCL --
sometimes, all we need are fixed strings, matched either as prefixes
or for equality. If that's the problem we need to solve, the full
power of a regular expression engine seems to be a bit of overkill.

That's where VMOD selector comes in. Like VMOD re2, VMOD selector
provides objects called sets that are used in very similar ways::

  import selector;

  sub vcl_init {
	new backend_dispatch = selector.set();
        backend_dispatch.add("/foo/", backend=foo_backend);
        backend_dispatch.add("/bar/", backend=bar_backend);
        backend_dispatch.add("/baz/", backend=baz_backend);
        backend_dispatch.add("/quux/", backend=quux_backend);

	new host_matcher = selector.set();
        host_matcher.add("www.foo.com", backend=foo_backend);
        host_matcher.add("www.bar.com", backend=bar_backend);
        host_matcher.add("www.baz.com", backend=baz_backend);
  }

But the strings added with VMOD selector's ``.add()`` method are just
plain strings. Regex metacharacters have no significance, nor does any
other pattern matching syntax.

Sets in VMOD selector have two match methods: ``.match()`` is true of
a string if it is equal to any string in the set, and ``.hasprefix()``
is true if the string has a prefix that equals a string in the set::

  sub vcl_backend_fetch {
	# Choose the backend based on the Host header, if it matches,
	# otherwise based on the URL path prefix.
	if (host_matcher.match(bereq.http.Host)) {
		set bereq.backend = host_matcher.backend();
	}
	elsif (backend_dispatch.hasprefix(bereq.url)) {
		set bereq.backend = backend_dispatch.backend();
	}
  }

But why bother with another VMOD? A regular expression library such as
re2 can certainly express simple matches such as these. But VMOD
selector has a couple of advantages, if the use case allows the
limitation to fixed strings.

* The implementation of VMOD selector is self-contained and does not
  require an external library (whereas VMOD re2 requires the re2
  library).

* The two match operations in VMOD selector are considerably faster
  than the corresponding operations with re2.

.. _perfect_hash: https://en.wikipedia.org/wiki/Perfect_hash_function
.. _trie: https://en.wikipedia.org/wiki/Trie

The performance advantage of VMOD selector exemplifies a common result
of tradeoffs in software. Fixed strings are limited in expressiveness
compared to regular expressions, but that makes faster algorithms
possible.

* VMOD selector's ``.match()`` operation is implemented as lookup for
  a `perfect hash <perfect_hash_>`_, since the set of strings to be
  matched is fixed at VCL initialization time, and is never changed
  for the lifetime of the VCL instance. Hence a ``.match()``
  invocation requires constant time, regardless of the size of the
  set.

* The ``.prefix()`` operation is an efficient `trie <trie_>`_ search.
  Similar to matches for re2 sets, the prefix match scans the string
  to be matched from left to right until the prefix is found, or the
  first non-matching character is encountered.

For use cases that require equality or prefix matches against sets of
fixed strings, VMOD selector is the preferred choice.

Sets as arrays
--------------

In the examples above, we have seen that backends can be assigned to
the strings in a set, making it possible to choose a backend for fetch
based on the URL path or Host header; a common use case for VCL. Used
this way, a set from either of the two VMODs functions as an
*associative array*, mapping the matched string or pattern to other
data.

The VMODs support mappings to other data types as well, including
strings and integers. In the next example, string mappings are used
for URL rewrites in addition to the backend assignment::

  import selector;

  sub vcl_init {
  	# The associated string with version number must be
        # prefixed to the client URL for the backend apps.
	new host_matcher = selector.set();
        host_matcher.add("www.foo.com", backend=foo_backend,
                         string="/v1/foo");
        host_matcher.add("www.bar.com", backend=bar_backend,
                         string="/v2/bar");
        host_matcher.add("www.baz.com", backend=baz_backend,
                         string="/v1/baz");
        host_matcher.add("www.quux.com", backend=quux_backend,
                         string="/v2/quux");
  }

  sub vcl_backend_fetch {
	if (host_matcher.match(bereq.http.Host)) {
        	# Set the backend and rewrite the URL.
		set bereq.backend = host_matcher.backend();
		set bereq.url = host_matcher.string() + bereq.url;
	}
  }

In the example, when the Host header is ``www.foo.com``, the code in
``vcl_backend_fetch`` assigns the backend and prepends the string
``/v1/foo`` to the URL path before the fetch.

In the next example, integers are associated with elements of a set,
which are used to set caching TTLs, for both the Varnish cache and for
downstream caching by means of the ``Cache-Control`` header::

  import re2;
  import std;

  sub vcl_init {
  	# The integers are TTLs in seconds.
        # 604800s = 1 week
  	new cacheable = re2.set();
        cacheable.add("^/assets/",  integer=604800);
        cacheable.add("\.html$",    integer=604800);
        cacheable.add("\.png$",     integer=604800);
        cacheable.add("\.jpe?g$",   integer=604800);
        cacheable.add("\.css$",     integer=604800);
        cacheable.add("\.js$",      integer=604800);
        cacheable.add("^/product/", integer=3600);
        cacheable.add("^/news/",    integer=86400);
  }
  
  sub vcl_backend_response {
  	if (cacheable.match(bereq.url) {
        	# Use VMOD std to convert the integer to a duration.
        	set beresp.ttl = std.duration(cacheable.integer());
                set beresp.http.Cache-Control =
                	"public, max-age=" + cacheable.integer();
        }
  }

Data that are retrieved with methods such as ``.string()`` or
``.integer()`` are associated with the string that was matched by the
most recent ``.match()`` or ``.prefix()`` operation in the same client
or backend context. The backend side of VCL processing is executed in
subroutines with the ``vcl_backend_*`` prefix, while the client side
is executed in all other subroutines. The match does not need to have
been invoked in the same subroutine. For example, data may be
retrieved in ``vcl_deliver`` for set object after a match in
``vcl_recv``, since delivery always comes last on the client side. But
matching contexts do not propagate across the client/backend boundary.

Sets in the two VMODs can also be accessed as *indexed arrays*, using
a numeric index to retrieve data associated with strings in the set.
The indexing corresponds to the order in which strings were added to
the set with the ``.add()`` method in ``vcl_init``, counting from 1::

  sub vcl_init {
	new strings = selector.set();
        strings.add("/foo/", string="first");	# 1
        strings.add("/bar/", string="second");	# 2
        strings.add("/baz/", string="third");	# 3
        strings.add("/quux/", string="fourth");	# 4
  }

  sub vcl_recv {
	set req.http.X-First = strings.string(n=1);
  }

The optional ``n`` parameter in the ``.string()`` method specifies the
index; in this case, ``n=1`` indicates the string added with the first
``.add()`` invocation, in this case ``"first"``. Note that a prior
matching operation is not required when data is retrieved by index, it
can be done in any context.

Rewriting strings
-----------------

A common use case for the ``if-elsif-elsif`` pattern in VCL is to
rewrite strings, such as headers or the URL path. In the following
example, the initial component of the URL path is removed and the
``Host`` header is set to distinguish the endpoints::

  sub vcl_recv {
  	if (req.url ~ "^/foo/") {
        	set req.http.Host = "www.foo.com";
        	set req.url = regsub(req.url, "^/foo(/.*)$", "\1");
        }
  	elsif (req.url ~ "^/bar/") {
        	set req.http.Host = "www.bar.com";
        	set req.url = regsub(req.url, "^/bar(/.*)$", "\1");
        }
  	elsif (req.url ~ "^/baz/") {
        	set req.http.Host = "www.baz.com";
        	set req.url = regsub(req.url, "^/baz(/.*)$", "\1");
        }
  	elsif (req.url ~ "^/quux/") {
        	set req.http.Host = "www.quux.com";
        	set req.url = regsub(req.url, "^/quux(/.*)$", "\1");
        }
        # ... and so on
  }

The string rewrites are accomplished with the standard VCL function
``regsub()``, which uses capturing groups from a regular expression
match to replace the URL path. ``regsub()`` the first maching portion
of the target string (``req.url`` in the example) with the string in
the third argument. Here we have used a backreference ``\1`` to
extract the string in the captured group. ``regsub()`` only replaces
one string, whereas the function ``regsuball()`` replaces each
non-overlapping portion of the target string that matches.

With set objects from VMOD re2, rewrites can be accomplished by taking
advantage of the fact that the set elements themselves are regular
expressions. To achieve this, include the capturing subexpressions in
the elements of the set. After a successful match, the ``.sub()``
method executes the rewrite, using the individual regular expression
that matched::

  import re2;

  sub vcl_init {
  	# With the optional parameter save=true, each individual regex
        # is compiled and stored, and hence can be used for rewrites
        # with the .sub() method.
  	new path_rewrite = re2.set(anchor=both);
        path_rewrite.add("^/foo(/.*)$", save=true, string="www.foo.com");
        path_rewrite.add("^/bar(/.*)$", save=true, string="www.bar.com");
        path_rewrite.add("^/baz(/.*)$", save=true, string="www.baz.com");
        path_rewrite.add("^/quux(/.*)$", save=true, string="www.quux.com");
  }

  sub vcl_recv {
  	if (path_rewrite.match(req.url)) {
        	set req.http.Host = path_matcher.string();
                set req.url = path_matcher.sub(req.url, "\1");
        }
  }

As described above, sets in the RE2 library are formed as the "or"
(``|``) of all of the regular expressions that are added to it. When
the optional ``save`` parameter is set to ``true``, each individual
expression is also compiled and stored, making it available for
rewrites with the ``.sub()`` method. As with VCL's ``regsub()``
function, a backreference such as ``\1`` can be used in the
substitution string for the captured group in the match.

Like VCL's function, the ``.sub()`` method replaces the first matching
portion of the target string with the substitution string.  VMOD re2
sets also have a ``.suball()`` method, analogous to VCL's
``regsuball()``, that replaces every non-overlapping match.

An additional rewriting method ``.extract()`` can be used in re2 to
construct an arbitrary string, without applying substitutions to the
matched string. An alternative to the example above uses
``.extract()`` for its solution::

  import re2;

  sub vcl_init {
  	# In this version, we use two capturing groups, one to
        # construct the Host header, and the other to replace
        # the URL path.
  	new path_rewrite = re2.set(anchor=both);
        path_rewrite.add("^/(foo)(/.*)$", save=true);
        path_rewrite.add("^/(bar)(/.*)$", save=true);
        path_rewrite.add("^/(baz)(/.*)$", save=true);
        path_rewrite.add("^/(quux)(/.*)$", save=true);
  }

  sub vcl_recv {
  	if (path_rewrite.match(req.url)) {
        	set req.http.Host = path_matcher.extract(req.url, "www.\1.com");
                set req.url = path_matcher.extract(req.url, "\2");
        }
  }

In this example, when the path ``/foo/subpath`` is matched, the first
captured group (``\1``) is ``"foo"``, and is used by the first
``.extract()`` invocation to construct the Host header
``"www.foo.com"``.  The second group (``\2``) is ``"/subpath"``, which
replaces the URL path.

In VMOD selector, elements of a set are fixed strings rather than
regular expressions that can be used for rewrites. But a similar
technique can be applied by associating a standard VCL regular
expression with the elements of the set. In the case of selector,
(compiled) regular expressions are another type of data that can be
retrieved after a match::

  import selector;
  
  sub vcl_init {
  	# In the VMOD selector version, save a compiled
        # regular expression with each element using the
        # regex parameter.
  	new path_rewrite = selector.set();
        path_rewrite.add("/foo", regex="^/foo(/.*)$", string="www.foo.com");
        path_rewrite.add("/bar", regex"^/bar(/.*)$", string="www.bar.com");
        path_rewrite.add("/baz", regex"^/baz(/.*)$", string="www.baz.com");
        path_rewrite.add("/quux", regex"^/quux(/.*)$", string="www.quux.com");
  }

  sub vcl_recv {
  	if (path_rewrite.hasprefix(req.url)) {
        	set req.http.Host = path_matcher.string();
                set req.url = path_matcher.sub(req.url, "\1");
        }
  }

The ``.sub()`` method for VMOD selector is only legal if a regular
expression was specified with the ``regex`` parameter in the
``.add()`` method. Otherwise, the same principles apply: each portion
of the target string that matches the regex is replaced by the
substitution string, which may contain backreferences for capturing
groups. The "substitute all" effect is achieved with VMOD selector by
using the optional parameter ``all=true`` in the ``.sub()`` method.

Note some of the differences in the use of rewrites and regular
expressions in VMODs re2 and selector:

.. _PCRE2: https://www.pcre.org/
.. _re2_syntax: https://github.com/google/re2/wiki/Syntax

* VMOD re2 implements regular expressions using the `re2 library from
  Google <libre2_>`_, while selector uses Varnish's implementation
  based on `PCRE2`_. For many common uses in VCL, the two regex
  languages can be used in the same way, but there are some
  `differences in legal syntax <re2_syntax_>`_ that should be
  taken into consideration.

* The rewrite methods of VMOD re2 re-use the regular expression that
  is an element of the set, and is used for the match operation. But
  for VMOD selector, the saved regex is separate from the string to
  be matched, and can be quite different from it.

Since the regular expressions saved for elements of VMOD selector sets
form additional matching patterns, the method ``.re_match()`` can be
used to execute a second match::

  import selector;

  sub vcl_init {
  	new path_matcher = selector.set();
        path_matcher.add("/foo", regex="^www\.(bar|baz)\.com$");
        # ... and so on ...
  }

  sub vcl_recv {
  	if (path_matcher.hasprefix(req.url) {
		if (path_matcher.re_match(req.http.Host)) {
                	# ... do if the URL path begins with /foo
                        # and the Host is either www.bar.com or
                        # www.baz.com ...
                }
  }

The ``.re_match()`` method, only available for VMOD selector, runs a
match against the regex that was saved for the string that matched in
the most recent invocation of ``.match()`` or ``.hasprefix()``, in the
same client or backend scope.

Arbritrary logic with associated subroutines
--------------------------------------------

We have seen that sets in the two VMODs make it possible to replace
lengthy and poorly scalable ``if-elsif-elsif`` sequences of string
matches with short and efficient code. But the examples thus far have
followed rigid patterns: matches followed by a backend or TTL
assignment, or a string rewrite, and always the same operation after a
match.

But real-world VCL deployments are often more complicated than that.
Requirements call for a variety of actions to be taken, that can
rarely be condensed into one common sequence::

  if (req.url ~ "^/foo") {
  	set req.backend_hint = foo_backend;
        return(pass):
  }
  elsif (req.url ~ "^/bar") {
  	set req.backend_hint = bar_backend;
        return(pass):
  }
  elsif (req.url ~ "^/baz") {
  	set req.backend_hint = baz_backend;
  }
  elsif (req.url ~ "^/quux") {
  	set req.backend_hint = baz_backend;
        set req.http.Host = "www.quux.com";
  }
  # ... and so on ...

How could we handle this with sets from the two VMODs? Each of the
matches is for a URL prefix, which could be performed by selector's
``.hasprefix()``. But what do we do after a successful match? All
of the clauses above set a backend, but some return ``pass`` while
others do not, and one of them assigns the Host header.

One approach would be to split the patterns to match into sets that do
lead to common actions. Despite the variation in the example above,
the first two clauses do lead for the same code pattern. Long
``if-elsif`` sequences in real-world deployments may well include
groups with similar function. For the example, we could combine the
``"/foo"`` and ``"/bar"`` prefixes in a set and implement a common
clause. It would result in an ``if-elsif`` sequence with 3 matches
instead of 4.

However, the two VMODs provide a way to execute different code for
elements of a set after a single match: call a subroutine saved with a
matching element. This is another example of sets used as associative
arrays, in this case using a VCL subroutine as the associated data::

  import selector;

  sub return_pass {
  	return(pass);
  }

  sub set_host {
  	set req.http.Host = path_matcher.string();
  }

  sub no_op {
  }

  sub vcl_init {
  	# The sub parameter associates a subroutine with each element.
  	new path_matcher = selector.set();
        path_matcher.add("/foo", sub=return_pass, backend=foo_backend);
        path_matcher.add("/bar", sub=return_pass, backend=bar_backend);
        path_matcher.add("/baz", sub=no_op, backend=baz_backend);
        path_matcher.add("/quux", sub=set_host, string="www.quux.com");
  }

  sub vcl_recv {
  	if (path_matcher.hasprefix(req.url)) {
        	set req.backend_hint = path_matcher.backend();
                call path_matcher.subroutine();
        }
  }

In the example, we define three subroutines that are specified for
each element of the set with the ``sub`` parameter in the ``.add()``
method. Since ``req.backend_hint`` is set for any match, a backend is
assigned in all matching cases with the ``.backend()`` method.  Then a
subroutine is called that is associated with the matching prefix to
execute specific logic.

One of the associated subroutines invokes ``return(pass)`` (to exit
``vcl_recv``), and applies to two of the prefix cases. Another one
assigns the Host header using the ``.string()`` method; note that
``.string()``, like other "associative array" methods, returns the
data associated with the matching prefix from the ``hasprefix()``
method that led to the subroutine call. In another matching case,
there is no other requirement besides assigning the backend, so the
subroutine that is called (``no_op``) does nothing.

Calling an associated VCL subroutine makes it possible to fulfill a
variety of requirements, and yet with one matching operation.  This is
especially convenient if the logic after a match can be condensed to a
manageable number of subroutines.  The ``.subroutine()`` method is
available in both of the VMODs re2 and selector.

There is a very important caveat concerning the use of callable
subroutine objects as shown here. In standard VCL, subroutine calls
are checked at compile time for whether they may be legally invoked in
context. For example, it is not legal to call a subroutine that
references ``bereq.*`` variables from a client-side subroutine such as
``vcl_recv``. VCL code with an illegal subroutine call is rejected by
the compiler, so that the call can never lead to a runtime error.  But
calls to subroutine objects as shown above *can only be checked at
runtime*.

So it is *crucial* to ensure that the ``.subroutine()`` method as used
above is always legal in its context. An illegal call leads to VCL
failure at runtime, which ordinarily results in a 503 error response.
But that is an avoidable error.

.. _vcl-var: https://varnish-cache.org/docs/trunk/reference/vcl-var.html

The legality of a subroutine call depends on the VCL variables that it
references; this is documented in the `vcl-var`_ manual. For example,
if a subroutine reads the value of a ``req.*`` variable, the
documentation states that it must be readable from any client-side
subroutine (any ``vcl_*`` subroutine that does not begin with
``vcl_backend_*``). For some variables, the specific ``vcl_*`` subs in
which they may be read or written are listed.

This means that the legality of VCL variable references must be
verified at development time in order to properly use the
``.subroutine()`` method. The VCL compiler can't do it for you.

To make this easier to manage, both of the VMODs provide the
``.check_call()`` method, which returns true if an associated
subroutine may be called legally after a match, false otherwise::

  import std;

  sub vcl_recv {
  	if (path_matcher.hasprefix(req.url)) {
        	if (!path_matcher.check_call()) {
                	std.log("Subroutine call is illegal");
                        call handle_error;
                }
                call path_matcher.subroutine();
        }
  }

Using ``.check_call()`` makes graceful error handling and debugging
easier, if an illegal use of the ``.subroutine()`` method turns up
at runtime.

Selecting the match
-------------------

Astute readers will have noticed that the discussion and example thus
far have glossed over a potential problem. We have spoken of matches
against sets of patterns or strings as if only one element of the set
matches. But that is not necessarily true of all possible sets.

This is easiest to see with prefix matches for VMOD selector, when
the elements of the set overlap::

  import selector;
  
  sub vcl_init {
  	new overlap = selector.set();
        overlap.add("/foo");
        overlap.add("/foo/bar");
        overlap.add("/foo/bar/baz");
  }

If the string ``"/foo/bar/bar/quux"`` is matched with ``.hasprefix()``
against this set, which of the prefixes match? All of them do.

With VMOD re2, multiple matches can happen in many ways. In an
earlier example we saw::

  import re2;

  sub vcl_init {
  	new static = re2.set();
        static.add("^/assets");
        static.add("\.html$");
        # ... and so on ...
  }

If the string to be matched is ``/assets/foo.html``, then both
patterns in the set match.

The question does not present itself for the ``.match()`` method of
VMOD selector, which matches strings exactly. A string is either
identical to an element of a set or not (adding the same string twice
is illegal in VMOD selector). But it may be an issue for re2's
``.match()`` or selector's ``.hasprefix()`` methods.

If the use case only calls for matching strings, but for none of the
other features of the VMODs, then multiple matches are unproblematic::

  if (host_matcher.hasprefix(req.http.Host)) {
  	# Multiple matches don't matter, because nothing depends
        # on which element of the set matched.
  	return(pass);
  }

But multiple matches must be clarified when we use sets in their
function as "associative arrays", to retrieve objects such as a
string, integer, regular expression or subroutine for the matching set
element. These must be uniquely specified.

The ``if-elsif-elsif`` has an implicit and natural solution to this
question -- the match is whatever comes first. Suppose we choose a
strategy for URL path prefixes according to which, when the prefixes
overlap, the "most specific" path takes precedence -- that is, the
match against the longest prefix. Then we arrange for these to be
matched first::

  if (req.url ~ "^/foo/bar/baz") {
  	set req.http.Specific = "most";
  }
  elsif (req.url ~ "^/foo/bar") {
  	set req.http.Specific = "middle";
  }
  elsif (req.url ~ "^/foo") {
  	set req.http.Specific = "least";
  }

Strategies such as this are realized in the VMODs with the ``select``
parameter of methods that require a uniquely specified element
(``select`` is the inspiration for one of the VMOD's names). The
effect of the ordered sequence above is achieved by using
``select=LONGEST`` in the ``.string()`` method::

  import selector;

  sub vcl_init {
  	new path_matcher = selector.set();
        path_matcher.add("/foo",         string="least");
        path_matcher.add("/foo/bar",     string="middle");
        path_matcher.add("/foo/bar/baz", string="most");
  }

  sub vcl_recv {
  	if (path_matcher.hasprefix(req.url)) {
        	set req.http.Specific = path_matcher.string(select=LONGEST);
        }
  }

For a path like ``/foo/bar/quux``, the longest matching prefix in the
set is ``/foo/bar``. This is the element chosen for ``.string()`` and
other "associative" methods.

The values for ``select`` are enums, and three values are common to
both of the VMODS:

* ``UNIQUE``: an element of the set is required to match uniquely. If
  there are multiple matches, then the operation fails with VCL error
  (usually a 503 error response).

* ``FIRST``: for multiple matches, choose the element that was added
  first with the ``.add()`` method in ``vcl_init``.

* ``LAST``: for multiple matches, choose the element that was added
  last with the ``.add()`` method in ``vcl_init``.

Three additional values for ``select`` may be used after
``.hasprefix()`` matches for VMOD selector sets:

* ``EXACT``: an element of the set is required to match exactly; the
  matched string may not have a suffix that is not in the set. VCL
  failure is invoked if there is no exact match. Thus in the example
  above, the ``.hasprefix()`` match for ``/foo/bar/quux`` would lead
  to VCL failure, but it would succeed for ``/foo/bar`` and select
  that element.

* ``SHORTEST``: for multiple matches, choose the shortest matching
  prefix.

* ``LONGEST``: for multiple matches, choose the longest matching
  prefix.

The ``select`` parameter may be used in many of the VMOD methods that
we have seen so far, where an element of the set must be uniquely
specified. These include:

* ``.backend()``
* ``.string()``
* ``.integer()``
* ``.sub()``
* ``.subroutine()``
* ``.check_call()``
* re2's ``.suball()`` and ``.extract()``
* selector's ``.re_match()``

As indicated above, the ``select`` values ``UNIQUE`` and ``EXACT`` set
the restriction that multiple matches are not permitted, otherwise
VCL failure is invoked. Hence these should only be used if you're sure
that your sets and strings to be matched fit the requirement. The
default value of ``select`` (used when the parameter is not explicitly
specified) is ``UNIQUE``; so uniqueness has in fact been required for
all of the examples prior to this section.

VMOD selector has the means to ensure that overlapping prefixes do not
appear in the set, by setting the parameter ``allow_overlap=false`` in
the contructor::

  import selector;

  sub vcl_init {
  	new non_overlap = selector.set(allow_overlap=false);
        non_overlap.add("/foo");
        # Strings such /foo/bar and /foo/bar/baz are now illegal.
  }

If ``allow_overlap`` is set to false and strings with overlapping
prefixes are added, the VCL compile fails, thus ensuring that no
runtime error can occur when ``select`` is set to ``UNIQUE`` after
a ``hasprefix()`` match.

Some examples
-------------

Sets in VMODs re2 and selector probably have their greatest value when
they eliminate the long ``if-elsif-elsif`` sequences that can
proliferate in large-scale VCL deployments. But to close we share a
few practical examples of the use of the VMOD in real-world projects.

It usually makes sense to use space in the cache efficiently by
compressing backend responses before storing them. But compression
has little advantage for objects such as images or other media. Here
we use VMOD selector to decide whether to compress a response, based
on the media type in its Content-Type header::

  import selector;

  sub vcl_init {
        new compressible = selector.set();
        compressible.add("text/");
        compressible.add("application/javascript");
        compressible.add("application/x-javascript");
        compressible.add("application/json");
        compressible.add("application/html");
        compressible.add("application/xhtml");
        compressible.add("application/xml");
        compressible.add("application/rss");
        compressible.add("image/svg");
        compressible.add("image/x-icon");
        compressible.add("font/woff");
  }

  sub vcl_backend_response {
  	# Compress a response if indicated by Content-Type.
        if (compressible.hasprefix(beresp.http.Content-Type)) {
                set beresp.do_gzip = true;
        }
  }

This is a very simple way to whitelist request methods permitted for a
REST API::

  import selector;

  sub vcl_init {
        new rest_methods = selector.set();
        rest_methods.add("GET");
        rest_methods.add("HEAD");
        rest_methods.add("POST");
        rest_methods.add("PUT");
        rest_methods.add("PATCH");
  }

  sub vcl_recv {
        if (!rest_methods.match(req.method)) {
                return(synth(405));
        }
  }
  
Of course it isn't difficult or costly to compare ``req.method`` to
five strings with standard string equality. But the perfact hash match
for this small set is very fast (on the order of two-digit nanoseconds
on server-class machines), and the code using the VMOD is much
shorter.

Redirect rules are a common source of long ``if-elsif-elsif``
sequences in VCL. The use of an integer as associated data supports
indivdual decisions about the HTTP response status for redirect that
should be used::

  import re2;

  sub vcl_init {
  	# The integer is the HTTP response status + 1000. Varnish
        # truncates these to a three-digit number.
	new redirect = re2.set();
        redirect.add("^/foo/bar", string="/foobar", integer=1301);
        redirect.add("^/baz/[^/]+/quux", string="/baz/quux", integer=1302);
        # ... and so on ...
  }

  sub vcl_recv {
  	# Set Location in the request header. In the synthetic
        # response, this will be copied to the response header.
  	if (redirect.match(req.url)) {
        	set req.http.Location = "http://" + req.http.Host +
                                        redirect.string();
                return(synth(redirect.integer()));
        }
  }

  sub vcl_synth {
  	# If the status is in the range above 1300, this is a redirect
        # response that was recognized in vcl_recv.
  	if (resp.status > 1300) {
        	set resp.http.Location = resp.http.Location;
                return(deliver);
        }
  }

In many ways large and small, sets in the VMODs re2 and selector can
be the basis for compact efficient solutions to string manipulation
requirements in VCL.
