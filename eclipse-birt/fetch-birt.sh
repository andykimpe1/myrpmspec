#!/bin/sh

CVSTAG=BIRT_2_6_0_Release_201006171315 
RHINOTAG=v20090608
VERSION=2.6.0

rm -fr eclipse-birt-${VERSION}

mkdir -p eclipse-birt-${VERSION}
pushd eclipse-birt-${VERSION}

for f in \
features/org.eclipse.birt.chart.feature \
org.eclipse.birt.chart \
org.eclipse.birt.chart.device.extension \
org.eclipse.birt.chart.device.pdf \
org.eclipse.birt.chart.device.svg \
org.eclipse.birt.chart.device.swt \
org.eclipse.birt.chart.engine \
org.eclipse.birt.chart.engine.extension \
org.eclipse.birt.chart.examples.core \
org.eclipse.birt.chart.ui \
org.eclipse.birt.chart.ui.extension \
org.eclipse.birt.core \
org.eclipse.birt.core.ui \
; do
cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/birt \
export -r ${CVSTAG} source/$f;
done

cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/birt \
export -r ${RHINOTAG} source/org.mozilla.rhino

mv source/* .
rmdir source
popd

tar cjf eclipse-birt-${VERSION}-fetched-src.tar.bz2 eclipse-birt-${VERSION}
