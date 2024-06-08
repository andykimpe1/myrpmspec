#!/bin/bash
	
	
DATE=`date +%Y%m%d`
	
# use a real tag name here
	
VERSION=1.2.11.25
	
PKGNAME=389-ds-base
	
TAG=${TAG:-$PKGNAME-$VERSION}
	
#SRCNAME=$PKGNAME-$VERSION-$DATE
	
SRCNAME=$PKGNAME-$VERSION
	
 
	
test -d .git || {
	
    echo you must be in the ds git repo to use this
	
    echo bye
	
    exit 1
	
}
	
 
	
if [ -z "$1" ] ; then
	
	dir=.
	
else
	
	dir="$1"
	
fi
	
 
	
git archive --prefix=$SRCNAME/ $TAG | bzip2 > $dir/$SRCNAME.tar.bz2
