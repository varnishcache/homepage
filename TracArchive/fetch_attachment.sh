#!/bin/sh

set -e

mkdir -p RawAttachment

for i in RawTicket/*
do
	if ! grep 'href="/trac/attachment/ticket/' $i > _atmp ; then
		continue
	fi
 	for f in `sed 's/.*href=".trac.attachment.ticket.\([^"]*\).*/\1/' _atmp | sort -u`
	do
		d=`dirname $f`
		b=`basename $f`
		mkdir -p RawAttachment/$d
		if [ ! -f RawAttachment/$d/$b ] ; then
			fetch -o RawAttachment/$d/$b http://varnish-cache.org/trac/attachment/ticket/$f
		fi
	done
done
