#!/usr/bin/env python

from __future__ import print_function

import glob
import json
import sys

class vmod(object):
	def __init__(self, filename):
		self.filename = filename
		self.load()

	def load(self):
		fi = open(self.filename)
		self.j = json.loads(fi.read())
		fi.close()

	def save(self):
		fo = open(self.filename, "w")
		fo.write(json.dumps(self.j, sort_keys=True, indent=4, separators=(",", ": ")))
		fo.close()

	def name(self):
		return self.j["name"]

	def repos(self):
		g = self.j.get("github")
		if g != None:
			return {"Github": "https://github.com/" + g["user"] + "/" + g["project"]}
		i = self.j.get("repos")
		if isinstance(i, dict):
			return i
		if i != None:
			return {"Repos": i}
		return None

	def versions(self):
		r = self.j.get("rev")
		g = self.j.get("github")
		v = None
		if r != None:
			v = r.keys()
		elif g != None:
			v = g["branches"].keys()
		if v != None:
			v.sort()
			return v
		return list()

	def url_vcc(self, rev):
		r = self.j.get("rev")
		if r != None:
			if "url_vcc" in r[rev]:
				return r[rev]["url_vcc"]
			fmt = self.j.get("fmt")
			if fmt != None and "url_vcc" in fmt:
				fmt = fmt["url_vcc"]
			else:
				fmt = None
			if fmt != None and "branch" in r[rev]:
				return fmt % r[rev]["branch"]
		g = self.j.get("github")
		if g != None:
			s = "https://raw.githubusercontent.com/"
			s += g["user"] + "/"
			s += g["project"] + "/"
			s += g["branches"][rev] + "/"
			s += g["vcc_path"]
			return s
		return None

	def url_doc(self, rev):
		r = self.j.get("rev")
		if r != None:
			if "url_doc" in r[rev]:
				return r[rev]["url_doc"]
			fmt = self.j.get("fmt")
			if fmt != None and "url_vcc" in fmt:
				fmt = fmt["url_doc"]
			else:
				fmt = None
			if fmt != None and "branch" in r[rev]:
				return fmt % r[rev]["branch"]
		g = self.j.get("github")
		if g != None and "doc_path" in g:
			s = "https://github.com/"
			s += g["user"] + "/"
			s += g["project"] + "/"
			s += "blob/"
			s += g["branches"][rev] + "/"
			s += g["doc_path"]
			return s
		return None

	def www_table(self):
		l = []
		l.append(self.j.get("name"))
		l.append(self.j.get("desc"))
		s = ""
		for r in self.versions():
			doc = self.url_doc(r)
			if doc !=  None:
				s += " `%s <%s>`__ " % (r, doc)
			else:
				vcc = self.url_vcc(r)
				s += " `%s <%s>`__ " % (r, vcc)
		l.append(s)
		l.append(self.j.get("license"))
		l.append(self.j.get("status"))

		s = ""
		i = self.repos()
		if i != None:
			for n in sorted(i.iterkeys()):
				s += " `%s <%s>`__ " % (n, i[n])
		l.append(s)

		s = ""
		for r in self.versions():
			vcc = self.url_vcc(r)
			s += " `%s <%s>`__ " % (r, vcc)
		l.append(s)

		i = self.j.get("support")
		s = ""
		if i != None:
			for j in i:
				if j == "Uplex":
					s += " :ref:`business_uplex`"
				elif j == "Varnish Software":
					s += ":ref:`business_varnish_software`"
				elif j != None:
					s += " " + j
		l.append(s)

		return l


def load_all():
	vmods = {}
	for fn in glob.glob("vmod_*.json"):
		try:
			v = vmod(fn)
		except:
			print("ERROR: couldn't load " + fn)
			continue
		vmods[v.name()] = v
	return vmods

def make_www_table():

	vmods = load_all()

	nms = vmods.keys()
	nms.sort()

	l = []

	#######################################################################
	# Size columns

	h = ["VMOD", "Description", "Docs", "License", "Status", "Link", "VCC", "Support"]
	w = [0] * len(h)

	for i in nms:
		x = vmods[i].www_table()
		l.append(x)
		for j in range(len(w)):
			if x[j] == None:
				x[j] = ""
			else:
				x[j] = x[j].strip()
				w[j] = max(w[j], len(x[j]))

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

Instructions :ref:`how to get your VMOD on this list <vmods_reg>`.

.. toctree::
   :hidden:

   howto.rst

''')

	def sep(ln="-"):
		for i in w:
			fo.write("+" + ln * (i + 2))
		fo.write("+\n")

	sep("-")
	for i in range(len(h)):
		fo.write("| " + h[i].ljust(w[i]) + " ")
	fo.write("|\n")
	sep("=")

	for i in l:
		for j in range(len(w)):
			fo.write("| " + i[j].ljust(w[j]) + " ")
		fo.write("|\n")
		sep()

if __name__ == "__main__":

	vmods = load_all()

	if len(sys.argv) == 1:
		make_www_table()
	elif len(sys.argv) == 2 and sys.argv[1] == "--polish":
		vmods = load_all()
		for i in vmods:
			vmods[i].save()
