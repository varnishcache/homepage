#!/usr/bin/env python

from __future__ import print_function

import glob
import json

vmods = {}

for fn in glob.glob("vmod_*.json"):
	print(fn)
	fi = open(fn)
	j = json.loads(fi.read())
	assert "name" in j
	assert j["name"] not in vmods
	vmods[j["name"]] = j

nms = vmods.keys()
nms.sort()

#######################################################################
# Polish

for i in nms:
	v = vmods[i]
	v["link1"] = ""
	v["link2"] = ""
	if "github" in v:
		v["repos"] = "https://github.com/" + v["github"][0] + "/" + v["github"][1]
		v["link1"] += " `Github <%s>`_ " % v["repos"]
	elif "repos" in v:
		v["link1"] += " `Repos <%s>`_ " % v["repos"]
	elif "product" in v:
		v["link1"] = "`Product <" + v["product"] + ">`_"
	if "rev" in v:
		for j in v["rev"]:
			u = v["rev"][j]["url_vcc"]
			v["link2"] += " `%s <%s>`_ " % (j, u)
	if "support" in v and v["support"] == "Uplex":
		v["support"] = ":ref:`business_uplex`"
	if "support" in v and v["support"] == "Varnish Software":
		v["support"] = ":ref:`business_varnish_software`"

#######################################################################
# Size columns

h = ["VMOD", "License", "Status", "Support", "Link", "VCC"]
f = ["name", "license", "status", "support", "link1", "link2"]
w = [0] * len(h)

for i in nms:
	v = vmods[i]
	for j in range(len(w)):
		if f[j] in v:
			v[f[j]] = v[f[j]].strip()
			w[j] = max(w[j], len(v[f[j]]))

#######################################################################
# Emit output


fo = open("index.rst", "w")

fo.write('''
.. _vmods:

Varnish Modules
---------------

VMODs are extensions written for Varnish Cache. This page serves as a
directory of maintained VMODs.

If you have written a VMOD and want it listed here please send a PR 
to `this github repo <https://github.com/varnishcache/homepage/>`__ and
we will be happy to include it.

For other Varnish Cache related projects and utilities, please see the
:ref:`Varnish Extras <extras>`

''')

def sep(ln="-"):
	for i in w:
		fo.write("+" + ln * (i + 2))
	fo.write("+\n")

sep("-")
for i in range(len(h)):
	fo.write("| " + h[i].ljust(w[i]) + " ")
fo.write("|\n")
sep("-")

for i in nms:
	v = vmods[i]
	for j in range(len(w)):
		if f[j] in v:
			fo.write("| " + v[f[j]].ljust(w[j]) + " ")
		else:
			fo.write("| " + "".ljust(w[j]) + " ")
	fo.write("|\n")
	sep()

exit (0)

