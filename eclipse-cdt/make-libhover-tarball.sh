#!/bin/sh
rel=$1
tag=`echo $rel | sed -e 's/\./_/g'`
echo $tag
mkdir -p temp
pushd temp
rm -rf libhover
svn export svn://dev.eclipse.org/svnroot/technology/org.eclipse.linuxtools/libhover/tags/$rel libhover
pushd libhover
pwd
# We don't want newlib libhover shipped unconditionally
rm -rf org.eclipse.linuxtools.cdt.libhover.newlib*
# We don't want texinfoparser tools
rm -rf org.eclipse.linuxtools.cdt.libhover.texinfoparsers*
tar -czvf eclipse-cdt-fetched-src-libhover-$tag.tar.gz org.eclipse.linuxtools.cdt.libhover*
popd
popd
