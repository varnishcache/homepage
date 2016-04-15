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

for i in nms:
	v = vmods[i]
	if "repos" in v:
		v["link"] = "`Repository <" + v["repos"] + ">`_"
	elif "product" in v:
		v["link"] = "`Product <" + v["product"] + ">`_"


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

w = [0, 0, 0, 0, 0]
h = ["VMOD", "License", "Status", "Support", "Link"]
for i in nms:
	v = vmods[i]
	w[0] = max(w[0], len(i))
	w[1] = max(w[1], len(v["license"]))
	w[2] = max(w[2], len(v["status"]))
	if "support" in v:
		w[3] = max(w[3], len(v["support"]))
	if "link" in v:
		w[4] = max(w[4], len(v["link"]))

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
	fo.write("| " + i.ljust(w[0]))
	fo.write(" | " + v["license"].ljust(w[1]))
	fo.write(" | " + v["status"].ljust(w[2]))
	if "support" in v:
		fo.write(" | " + v["support"].ljust(w[3]))
	else:
		fo.write(" | " + "".ljust(w[3]))
	if "link" in v:
		fo.write(" | " + v["link"].ljust(w[4]))
	else:
		fo.write(" | " + "".ljust(w[4]))
	fo.write(" |\n")
	sep()

exit (0)

