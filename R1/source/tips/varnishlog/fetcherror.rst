.. _fetcherror:

Backend fetch failures and the FetchError tag
=============================================

*Why am I getting a ... Backend Fetch Error? ... 503 response code?
... Guru Meditation?*

**Always look for the FetchError tag in logs of backend transactions.**

When a backend fetch encounters a problem, a log message describing
the error is saved using the ``FetchError`` tag::

  $ varnishlog -b -q 'FetchError'
  *   << BeReq    >> 4711 
  -   Begin          bereq 5180 pass
  -   Timestamp      Start: 1466083875.265667 0.000000 0.000000
  -   BereqMethod    GET
  -   BereqURL       /foo/bar/baz
  [...]
  -   FetchError     http first read error: EOF
  [...]
  -   End            

Some common contents of a ``FetchError`` line are:

* ``http first read error: EOF``: Usually this indicates a first byte
  timeout. In less common cases, the backend may have closed the
  connection before the first byte of the response could be read.
* ``http read error: EOF``: Usually a between-bytes timeout; rarely, a
  backend connection while the response is being read.
* ``no backend connection``: This may mean that the backend is
  unhealthy (or all of the backends in a director are unhealthy), or
  that the connection timeout expired. In the latter case (connection
  timeout), the backend fetch timestamps will show that about exactly
  as much time expired as is defined for ``connect_timeout``. In the
  former case (unhealthy backends), Varnish decides immediately to
  fail the fetch, so the timestamps show no time expired.
