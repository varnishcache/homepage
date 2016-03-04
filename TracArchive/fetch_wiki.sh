
set -e
#fetch -o __wikiindex https://www.varnish-cache.org/trac/wiki/TitleIndex

mkdir -p Raw
sed '
s/href/\
href/g
' __wikiindex | sed '
/^href/!d
/trac\/wiki\//!d
s/trac\/wiki\///
s/^href="//
s/".*//
' | sort -u |
while read p
do
	d=`dirname RawWiki/$p`
	mkdir -p $d
	fetch -o RawWiki/${p}.html https://www.varnish-cache.org/trac/wiki$p
done
