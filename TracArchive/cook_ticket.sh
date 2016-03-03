#!/bin/sh

set -e

for i in RawTicket/*
do
	b=`basename $i`
	sed '
	s/static.varnish_trac.css/trac\/static\/css\/varnish_trac.css/
	s/static.logo-v2/trac\/&/
	s/<script type="text.javascript" src="[^"]*"><.script>//g
	s/javascript/INTERCAL/g
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
	/Login.*Preferences.*Help.*Guide.*About/d
	/Wiki.*Timeline.*Roadmap.*Browse Source/d
	/Previous Ticket.*Next Ticket/d
	/<form id="search"/,+6d
	/<div id="help".*Note:.*See/,+2d
	/<div id="altlinks/,+11d
	/<div once="true" id="footer"/,+7d
	/cdn.blix.eu/d
	s/<a class="timeline.*title="\([^ ]*\) in Timeline[^<]*<\/a>/\1/g
	/mainnav/a\
<h1>NB: This is a frozen copy of the old ticket from Trac</h1>
	' $i > /usr/local/www/apache24/data/trac/ticket/$b
done 
