.. _varnishlog:

Reading the varnishlog
======================

*What do the lines in varnishlog output mean?*

See ``man vsl(7)`` for full documentation of the format and contents
of Varnish log tags (or see the `online link
</docs/trunk/reference/vsl.html>`_, in this
case for current trunk, or for your Varnish version).

*How do I filter varnishlog output to make it more manageable?*

`man vsl-query(7)
</docs/trunk/reference/vsl-query.html>`_ shows
you how to use VSL queries to pick out log transactions with contents
you specify. See also `man varnishlog(1)
</docs/trunk/reference/varnishlog.html>`_ for
command-line options that restrict the output for each
transaction. Some useful ones are:

* ``-i``: only show log lines with certain tags
* ``-I``: only show lines matching a list of tags and a regular expression
* ``-x``: don't show lines with certain tags
* ``-X``: don't show lines matching a list of tags and a regular expression

Multiple options are allowed on the command line for each of these.
  
.. toctree::
   fetcherror
