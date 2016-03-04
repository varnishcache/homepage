#!/bin/sh

mkdir -p Dest/wiki
rm -rf Dest/wiki/*

for i in `cd RawWiki && find . -name '*.html' -print`
do
	d=`dirname $i`
	b=`echo $i | sed 's/[.]html$//'`
	if [ -d RawWiki/$b ] ; then
		b=$b/index.html
	fi
	# echo $i "---" $b
	d=`dirname $b`
	mkdir -p Dest/wiki/$d
done

for i in `cd RawWiki && find . -name '*.html' -print | grep -v '[?]'`
do
	d=`dirname $i`
	b=`echo $i | sed 's/[.]html$//'`
	if [ -d Dest/wiki/$b ] ; then
		b=$b/index.html
	fi
	echo $i "---" $b

	sed '
	s/static.varnish_trac.css/trac\/static\/css\/varnish_trac.css/
	s/static.logo-v2/trac\/&/
	s/<script type="text.javascript" src="[^"]*"><.script>//g
	s/javascript/INTERCAL/g

	/link rel="search"/d
	/link rel="prev"/d
	/link rel="next"/d
	/link rel="up"/d
	/link rel="last"/d
	/link rel="help"/d
	/link rel="alternate"/d
	/link rel="start"/d
	/link rel="first"/d
	/link rel="shortcut icon"/d
	/link rel="icon"/d
	/link type="application.opensearchdescription"/d

	/<form id="search"/,+6d

	/Login.*Preferences.*Help.*Guide.*About/d
	/Wiki.*Timeline.*Roadmap.*Browse Source/d

	/<div id="pagepath/,+2d
	/<div id="altlinks/,+7d
	/<div id="ctxtnav/,+6d
	/<div once="true" id="footer"/,+7d
	/cdn.blix.eu/d
	s/<a class="timeline.*title="\([^ ]*\) in Timeline[^<]*<\/a>/\1/

	/mainnav/a\
<h1>NB: This is a frozen copy of the wiki page from Trac</h1>

	' RawWiki/$i > Dest/wiki/$b
done

ln -s TitleIndex Dest/wiki/index.html
