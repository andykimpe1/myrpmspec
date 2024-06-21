#!/bin/sh

NAME=gnu-gs-fonts-other
DIR=fonts
VERSION=$1
rm -rf "$DIR"
tar zxf "$NAME"-"$VERSION".tar.gz
for file in					\
	bchb.afm				\
	bchb.pfa				\
	bchbi.afm				\
	bchbi.pfa				\
	bchr.afm				\
	bchr.pfa				\
	bchri.afm				\
	bchri.pfa
do
	rm "$DIR"/"$file"
done
tar zcf "$NAME"-"$VERSION"-nobch.tar.gz "$DIR"
rm -rf "$DIR"
