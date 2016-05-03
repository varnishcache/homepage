.. _tips:

Tips & Tricks
=============

301/302 Redirects
-----------------

Synthetic responses can be used to generate 30x redirects, and
the usual way is to stash the new location in req.http.something,
and move that to resp.location in ``vcl_synth{}``.

Here is a slightly neater way, exploiting the fact that ``return(synth())``
takes two arguments::

	sub vcl_recv {
	    if (req.url ~ "^/installation/ubuntu") {
		return (synth(301, "/releases/install_ubuntu.html"));
	    }
	    if (req.url ~ "^/installation/debian") {
		return (synth(302, "/releases/install_redhat.html"));
	    }
	}

	sub vcl_synth {
	    if (resp.status == 301 || resp.status == 302) {
		set resp.http.location = resp.reason;
		set resp.reason = "Moved";
		return (deliver);
	    }
	}

.. toctree::
	:hidden:
