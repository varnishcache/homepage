#!/bin/sh

set -e

for d in RawAttachment/*
do
	tn=`basename $d`
	mkdir -p Dest/attachment/ticket/$tn
	for f in $d/*
	do
		if [ ! -f $f ] ; then
			echo "???? $f"
			exit 2
		fi
		bn=`basename $f`
		sed '
		/link rel="search"/d
		/link rel="prev"/d
		/link rel="next"/d
		/link rel="last"/d
		/link rel="help"/d
		/link rel="alternate"/d
		/link rel="start"/d
		/link rel="first"/d
		/link rel="shortcut icon"/d
		/link rel="icon"/d
		/link type="application.opensearchdescription"/d
		s/static.varnish_trac.css/trac\/static\/css\/varnish_trac.css/
		s/static.logo-v2/trac\/&/
		s/<script type="text.javascript" src="[^"]*"><.script>//g
		s/javascript/INTERCAL/g
		/<div id="altlinks/,+8d
		/<form id="search"/,+6d
		/Login.*Preferences.*Help.*Guide.*About/d
		/Wiki.*Timeline.*Roadmap.*Browse Source/d
		/<div once="true" id="footer"/,+7d
		s/<a class="timeline.*title="\([^ ]*\) in Timeline[^<]*<\/a>/\1/g
		/cdn.blix.eu/d
		/mainnav/a\
<h1>NB: This is a frozen copy of the old ticket from Trac</h1>
		' $f > Dest/attachment/ticket/${tn}/${bn}
	done
done
