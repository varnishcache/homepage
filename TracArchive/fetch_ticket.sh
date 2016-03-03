#!/bin/sh


mkdir -p RawTicket
for t in `jot 1865 1`
do
	if [ ! -f RawTicket/${t} ] ; then
		fetch -o RawTicket/${t} https://www.varnish-cache.org/trac/ticket/${t}
	fi
done
