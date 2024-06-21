#!/bin/sh
rel=$1
tag=`echo $rel | sed -e 's/\./_/g'`
echo $tag
mkdir -p temp
pushd temp
rm -rf autotools
svn export svn://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/autotools/tags/$rel autotools
pushd autotools
pwd
rm -rf org.eclipse.linuxtools.cdt.autotools.tests
rm -rf org.eclipse.linuxtools.cdt.autotools.ui.tests
tar -czvf eclipse-cdt-fetched-src-autotools-$tag.tar.gz org.eclipse.linuxtools.cdt.autotools*
popd
popd
