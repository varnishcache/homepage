#!/bin/sh

D=/usr/local/www/apache24/data/trac

rm -rf $D
mkdir -p $D
rm Dest
ln -s $D Dest

mkdir -p Dest/ticket
mkdir -p Dest/attachment/ticket

find static pygments -print | cpio -dump $D

sh cook_ticket.sh
sh cook_attachment.sh

find Dest/. -type d -print |
while read d
do
	echo "Nothing to see here" > $d/index.html
done

sh cook_wiki.sh
