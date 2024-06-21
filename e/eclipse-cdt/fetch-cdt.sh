#!/bin/sh -x

CDTTAG=cdt_7_0_1
#ECLIPSEBASE=$(rpm --eval %{_libdir})/eclipse

if test x`uname -i` = 'xi386'; then export plat=""; else export plat=-`uname -i`; fi

# eclipse -nosplash -consolelog -application org.eclipse.equinox.p2.director -repository http://download.eclipse.org/technology/subversive/0.7/pde-update-site/ -installIU org.eclipse.team.svn.pde.build.feature.group

mkdir -p temp && cd temp
TEMPDIR=$(pwd)
mkdir -p home
mkdir -p ws
# we need to use a special svn pde extension to fetch some parts for the cdt build so we unzip a fresh 3.6 SDK and add the
# special plug-in via the p2 director
rm -rf sdk
mkdir -p sdk
pushd sdk
wget http://download.eclipse.org/eclipse/downloads/drops/R-3.6-201006080911/eclipse-SDK-3.6-linux-gtk${plat}.tar.gz
tar -xzvf eclipse-SDK-3.6-linux-gtk${plat}.tar.gz
ECLIPSEBASE=$TEMPDIR/sdk/eclipse
# pushd eclipse
# ./eclipse -nosplash -consolelog -application org.eclipse.equinox.p2.director -repository http://download.eclipse.org/technology/subversive/0.7/pde-update-site/ -installIU org.eclipse.team.svn.pde.build.feature.group
# popd
pushd eclipse/plugins
wget http://download.eclipse.org/technology/subversive/0.7/pde-update-site/plugins/org.eclipse.team.svn.pde.build_0.7.8.I20090525-1500.jar
popd
popd

rm -rf org.eclipse.cdt-releng
cvs -d:pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r $CDTTAG org.eclipse.cdt-releng/org.eclipse.cdt.releng

cd org.eclipse.cdt-releng/org.eclipse.cdt.releng/

# The build.xml doesn't fetch master or testing features so we must add this ourselves.
sed --in-place -e'94,94i\\t\t<ant antfile="build.xml" dir="${pde.build.scripts}" target="fetch">\n\t\t\t<property name="builder" value="${basedir}/master"/>\n\t\t</ant>' build.xml
sed --in-place -e'94,94i\\t\t<ant antfile="build.xml" dir="${pde.build.scripts}" target="fetch">\n\t\t\t<property name="builder" value="${basedir}/testing"/>\n\t\t</ant>' build.xml
sed --in-place -e'71,71i\\t\t<ant antfile="build.xml" dir="${pde.build.scripts}" target="preBuild">\n\t\t\t<property name="builder" value="${basedir}/master"/>\n\t\t</ant>' build.xml
sed --in-place -e'71,71i\\t\t<ant antfile="build.xml" dir="${pde.build.scripts}" target="preBuild">\n\t\t\t<property name="builder" value="${basedir}/testing"/>\n\t\t</ant>' build.xml
sed --in-place -e'71,71i\\t\t<ant antfile="build.xml" dir="${pde.build.scripts}" target="preBuild">\n\t\t\t<property name="builder" value="${basedir}/codan"/>\n\t\t</ant>' build.xml

# Remove copying of binary jar in build.xml.  We remove this jar so this operation will fail.
sed --in-place -e "/copy file=\"\${buildDirectory}.*net\.sourceforge\.lpg/,/\/>/"d build.xml 

pushd codan
# the feature id does not match what is found in the customTargets.xml which causes pdebuild to stop so make it the same
sed --in-place -e "s,value=\"org.eclipse.cdt.codan\",value=\"org.eclipse.cdt.codan.feature\",g" customTargets.xml
popd

pushd maps
# fix the CVS locations to use pserver rather than expecting to be on the actual eclipse.org build machine
sed --in-place -e "s,/cvsroot/tools,:pserver:anonymous@dev.eclipse.org/cvsroot/tools,g" cdt.map
sed --in-place -e "s,/cvsroot/eclipse,:pserver:anonymous@dev.eclipse.org/cvsroot/eclipse,g" cdt.map
# never use HEAD...specify a tag
sed --in-place -e "s,HEAD,R3_6,g" cdt.map
popd

PDEBUILDVERSION=$(ls $ECLIPSEBASE/plugins | grep org.eclipse.pde.build_ | sed 's/org.eclipse.pde.build_//')
$ECLIPSEBASE/eclipse -nosplash \
     -Duser.home=../../home \
      -Dorg.eclipse.equinox.p2.reconciler.dropins.directory=$TEMPDIR/dropins \
-XX:CompileCommand="exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith" \
-XX:CompileCommand="exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>" \
-XX:CompileCommand="exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate" \
-XX:CompileCommand="exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding" \
     org.eclipse.core.launcher.Main             \
  -Dpde.build.scripts=$ECLIPSEBASE/plugins/org.eclipse.pde.build_$PDEBUILDVERSION/scripts \
  -application org.eclipse.ant.core.antRunner \
  -buildfile build.xml -DbaseLocation=$ECLIPSEBASE \
  -Dpde.build.scripts=$ECLIPSEBASE/plugins/org.eclipse.pde.build_$PDEBUILDVERSION/scripts \
  -Dorg.eclipse.equinox.p2.reconciler.dropins.directory=$TEMPDIR/dropins \
  -DcdtTag=$CDTTAG \
  -DdontUnzip=true fetch

find . -name net.*.jar -exec rm {} \;

cd .. && tar jcf eclipse-cdt-fetched-src-$CDTTAG.tar.bz2 org.eclipse.cdt.releng
