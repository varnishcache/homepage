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
		i = self.j.get("repos")
		if i != None:
			return i
		g = self.j.get("github")
		if g != None:
			return "https://github.com/" + g["user"] + "/" + g["project"]

	def versions(self):
		r = self.j.get("rev")
		if r != None:
			return r.keys()
		g = self.j.get("github")
		if g != None:
			return g["branches"].keys()
		return list()

	def url_vcc(self, rev):
		r = self.j.get("rev")
		if r != None:
			return r[rev]["url_vcc"]
		g = self.j.get("github")
		if g != None:
			s = "https://raw.githubusercontent.com/"
			s += g["user"] + "/"
			s += g["project"] + "/"
			s += g["branches"][rev] + "/"
			s += g["vcc_path"]
			return s
		return None

	def version_links(self):
		s = ""
		for r in self.versions():
			vcc = self.url_vcc(r)
			s += " `%s <%s>`_ " % (r, vcc)

		return s

	def www_table(self):
		l = []
		l.append(":ref:`" + self.j.get("name") + " <vmods_" + self.j.get("name") + ">`")
		l.append(self.j.get("desc"))
		l.append(self.j.get("license"))
		l.append(self.j.get("status"))

		s = ""
		if "github" in self.j:
			s += " `Github <%s>`_ " % self.repos()
		elif "repos" in self.j:
			s += " `Repos <%s>`_ " % self.repos()
		l.append(s)

		l.append(self.version_links())

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
		v = vmod(fn)
		vmods[v.name()] = v
	return vmods

def make_www_table(vmods):

	nms = vmods.keys()
	nms.sort()

	l = []

	#######################################################################
	# Size columns

	h = ["VMOD", "Description", "License", "Status", "Link", "VCC", "Support"]
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

	for i in nms:
		fo.write("   " + i + ".rst\n")

	fo.write("\n")

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

def make_vmod_pages(vmods):

	nms = vmods.keys()

	for i in nms:
		vmod = vmods[i]
		name = vmod.j.get("name")
		fo = open(name + ".rst", "w")

		status = vmod.j.get("status") or ""
		license = vmod.j.get("license") or ""
		desc = vmod.j.get("desc") or ""
		repos = vmod.repos() or ""
		version_links = vmod.version_links()

		lst = [status, license, desc, repos, version_links]
		table_lines = "=" * len(max(lst, key=len))

		template = """
.. _vmods_{name}:

{name}
{headerlines}

{desc}

=========================== {table_lines}
Status:                     {status}
Licence:                    {license}
Varnish version supported:  {version_links}
Source repository URL:      {repos}
=========================== {table_lines}

"""
		fo.write(template.format(name =  name, headerlines = "=" * len(name), desc = desc, status = status, license = license, repos = repos, version_links = version_links, table_lines = table_lines))

if __name__ == "__main__":

	vmods = load_all()

	if len(sys.argv) == 1:
		make_www_table(vmods)
		make_vmod_pages(vmods)
	elif len(sys.argv) == 2 and sys.argv[1] == "--polish":
		vmods = load_all()
		for i in vmods:
			vmods[i].save()
