.. _vmods_reg:

How to register your VMOD
=========================

To get your VMOD listed on the Varnish Project homepage
you need to create a small JSON file which describes it
and submit a pull request to our
`homepage github repos <https://github.com/varnishcache/homepage/tree/master/R1/source/vmods>`_

There are a lot of JSON files there already, but they are
machine generated based on older registrations, so they are
not indicative of what we would like them to look like.

There are some examples at the bottom of this page.

At some point in the future we would like to be able to offer some
continuous integration facilities to help VMOD authors maintain
their code.  (A volunteer to implement this would be more than welcome)

The JSON file should have a single object ("dictionary")
and it should have members as described below.

All VMODS
---------

All VMODs MUST have these members:

name
~~~~

This is the name in the "import FOOBAR;" VCL statement.

date
~~~~

Format "YYYY-MM-DD", date entry was last revised.


desc
~~~~

Description, compact one-line description of what the VMOD does.
(Don't repeat the VMOD name here, it looks silly in the table.)


license
~~~~~~~

We prefer "FreeBSD", "Apache2", "GPLv2" in that order, but we are
not going to pass judgement, it's your choice.

status
~~~~~~

Allowed values:

* "included" -- those included in the varnish distro
* "prototype" -- Just playing around here...
* "development" -- API still subject to change
* "mature" -- We're trying to be serious here

Additionally the following optional members are possible:

maintainer
~~~~~~~~~~

Email address of VMOD maintainer

support
~~~~~~~

List of companies which will support this VMOD on commercial terms.

product
~~~~~~~

URL to product description web-page for commercial offerings

Github projects
---------------

Since the majority of VMODs are github projects, we have tried
to make that very easy.

In the toplevel object add a object member called "github" with
these members:

user
~~~~

Github username

project
~~~~~~~

Github project name

vcc_path
~~~~~~~~

Relative path to the VCC file for the VMOD

doc_path
~~~~~~~~

Relative path of the file documenting the VMOD (default: the VCC file)

branches
~~~~~~~~

An object mapping Varnish version to github branches.

If your github project has multiple branches corresponding to
varnish versions, it could look like this::

	"branches": {
	    "3.0": "3.0",
	    "4.0": "4.0",
	    "4.1": "master"
	},

If your VMOD only supports Varnish 3.0 from the github projects
master branch::
	
	"branches": {
	    "3.0": "master"
	},

Non Github projects
-------------------

You must these two members:

repos
~~~~~

URL of the repository


rev
~~~

An object mapping Varnish version to URL where the VCC and documentation
files can be found.

For instance:

	"rev": {
	    "3.0": {
		"url_vcc": "http://myvmod.example.com/source/3.0/vmod.vcc",
		"url_doc": "http://myvmod.example.com/docs/3.0/vmod.txt"
	    },
	    "4.1": {
		"url_vcc": "http://myvmod.example.com/source/4.1/vmod.vcc",
		"url_doc": "http://myvmod.example.com/docs/4.1/vmod.txt"
	    }
	}

Examples
--------

A github project::

	{
	    "date": "2016-04-14",
	    "desc": "Murphy Field Calibrator",
	    "github": {
		"branches": {
		    "3.0": "3.0"
		    "4.1": "master"
		},
		"project": "libvmod-murphy-cal",
		"user": "ACME engineering",
		"vcc_path": "src/vmod_murphy.vcc"
		"doc_path": "doc/vmod_murphy.rst"
	    },
	    "license": "FreeBSD",
	    "name": "murphy",
	    "status": "prototype",
	    "support": [ "ACME VMODs and Explosives Inc." ],
	    "maintainer": "Samuel.B.Nobody@example.com"
	}

A VMOD not on github::

	{
	    "date": "1999-12-31",
	    "desc": "Y2K fixer",
	    "license": "BeerWare",
	    "name": "Y2K",
	    "repos": "https://example.com/we/are/so/hosed",
	    "url_doc": "https://sales.example.com/QuantumMurphyCompensator",
	    "rev": {
		"4.1": {
		    "url_vcc": "https://example.com/we/are/so/hosed/vmod.vcc",
		    "url_doc": "https://example.com/we/are/so/hosed/README"
		}
	    },
	    "status": "prototype"
	}

