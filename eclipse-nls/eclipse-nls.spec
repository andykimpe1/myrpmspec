%global eclipse_data %{_datadir}/eclipse
# Disable repacking of jars, since it takes forever for all the little jars, 
# and we don't need multilib anyway:
%global __jar_repack %{nil}

%global debug_package %{nil}

Name: eclipse-nls 
Summary: Babel language packs for the Eclipse platform and various plug-ins
# note: try to keep this group the same as eclipse's rpm:
Group: Text Editors/Integrated Development Environments (IDE)
License: EPL
URL: http://www.eclipse.org/babel/

Version: 3.6.0.v20120721114722
Release: 2%{?dist}
# Babel language pack (zipped p2 update site) via: http://www.eclipse.org/babel/downloads.php
Source0: http://download.eclipse.org/technology/babel/update-site/R0.10.0/babel-R0.10.0-helios.zip
Requires:   eclipse-platform >= 1:3.6

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
%if %{defined fedora}
BuildArch:  noarch
%endif
%endif

%description
Babel language packs include translations for the Eclipse platform and other 
Eclipse-related packages.

%files
%dir %{eclipse_data}/dropins/babel
%dir %{eclipse_data}/dropins/babel/eclipse
#% {eclipse_data}/dropins/babel/eclipse/artifacts.jar
#% {eclipse_data}/dropins/babel/eclipse/content.jar
#% dir %{eclipse_data}/dropins/babel/eclipse/features
%dir %{eclipse_data}/dropins/babel/eclipse/plugins


# %1 subpackage id (ie Linux locale id)
# %2 Java locale id (mostly the same as Linux)
# %3 language name
%define lang_meta_pkg() \
%package %1 \
Summary:    Eclipse/Babel language pack for %3 \
Group:      Text Editors/Integrated Development Environments (IDE) \
Requires:   eclipse-nls = %{version}-%{release} \
Obsoletes:  eclipse-sdk-nls-%1 < 3.2.1-4 \
Provides:   eclipse-sdk-nls-%1 = %{version}-%{release} \
\
%description %1 \
This language pack for %3 \
contains user-contributed translations of the \
strings in all Eclipse projects. Please see the http://babel.eclipse.org/ \
Babel project web pages for a full how-to-use explanation of these \
translations as well as how you can contribute to \
the translations of this and future versions of Eclipse. \
Note that English text will be displayed if Babel doesn't \
have a translation for a given string. \
\
%files %1 \
#% {eclipse_data}/dropins/babel/eclipse/features/org.eclipse.babel.nls_*_%{2}_%{version} \
%doc eclipse/features/*_%{2}_%{version} \
%{eclipse_data}/dropins/babel/eclipse/plugins/*.nl_%{2}_%{version}.jar

%define spc() %(echo -n ' ')

%lang_meta_pkg ar ar Arabic
%lang_meta_pkg bg bg Bulgarian
%lang_meta_pkg ca ca Catalan
%lang_meta_pkg zh zh Chinese%{spc}(Simplified)
%lang_meta_pkg zh_TW zh_TW Chinese%{spc}(Traditional)
%lang_meta_pkg cs cs Czech
%lang_meta_pkg da da Danish
%lang_meta_pkg nl nl Dutch
%lang_meta_pkg en_AU en_AU English%{spc}(Australian)
%lang_meta_pkg en_CA en_CA English%{spc}(Canadian)
%lang_meta_pkg et et Estonian
%lang_meta_pkg fa fa Farsi
%lang_meta_pkg fi fi Finnish
%lang_meta_pkg fr fr French
%lang_meta_pkg de de German
%lang_meta_pkg el el Greek
# NB 'he' is 'iw' as far as Java is concerned.
# similarly, yi -> ji, id -> in
%lang_meta_pkg he iw Hebrew
%lang_meta_pkg hi hi Hindi
%lang_meta_pkg hu hu Hungarian
%lang_meta_pkg id id Indonesian
%lang_meta_pkg it it Italian
%lang_meta_pkg ja ja Japanese
# tl should be Tagalog.  Klingon has < 1% coverage at present in Babel.  Tagalog is unsupported.
#% lang_meta_pkg tlh tl Klingon
%lang_meta_pkg ko ko Korean
%lang_meta_pkg ku ku Kurdish
%lang_meta_pkg mn mn Mongolian
%lang_meta_pkg no no Norwegian
%lang_meta_pkg pl pl Polish
%lang_meta_pkg pt pt Portuguese
%lang_meta_pkg pt_BR pt_BR Portuguese%{spc}(Brazilian)
%lang_meta_pkg ro ro Romanian
%lang_meta_pkg ru ru Russian
%lang_meta_pkg es es Spanish
%lang_meta_pkg sk sk Slovak
%lang_meta_pkg sl sl Slovene
%lang_meta_pkg sq sq Albanian
%lang_meta_pkg sv sv Swedish
%lang_meta_pkg sr sr Serbian
%lang_meta_pkg tr tr Turkish
%lang_meta_pkg uk uk Ukrainian
%lang_meta_pkg en_AA en_AA Pseudo%{spc}Translations

%prep
# extract langpack zips from tarball
%setup -q -n helios
# remove unused p2 metadata
rm -rf mirrors/ artifacts.jar content.jar
# rearrange directories to be like the old extracted zips
mkdir eclipse
mv features/ plugins/ eclipse/
# remove unsupported langpacks (currently Klingon)
unsupported="tl"
for locale in $unsupported; do
  rm -f eclipse/features/*_${locale}_%{version}.jar
  rm -f eclipse/plugins/*.nl_${locale}_%{version}.jar
done
# extract feature jars to feature dirs (like the old extracted zips)
for feature in eclipse/features/*.jar; do
  feature_dir=${feature%.jar}
  unzip -qq $feature -d $feature_dir
  rm -f $feature
done

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{eclipse_data}/dropins/babel/eclipse/
mv eclipse/plugins/ $RPM_BUILD_ROOT%{eclipse_data}/dropins/babel/eclipse

%changelog
* Wed Sep 19 2012 Sean Flanigan <sflaniga@redhat.com> - 3.6.0.v20120721114722-2
- Switched to zipped p2 update site instead of using fetch-babel.sh
- Resolves: rhbz#692358

* Fri Sep 7 2012 Sean Flanigan <sflaniga@redhat.com> - 3.6.0.v20120721114722-1
- Updated from upstream to R0.10.0 (3.6.0.v20120721114722)
- Resolves: rhbz#692358

* Fri Jul  1 2011 Jens Petersen <petersen@redhat.com> - 3.6.0.v20100814043401-2
- update langpacks to eclipse-3.6 with backport from Fedora 14 (#692358)

* Mon Nov 29 2010 Sean Flanigan <sflaniga@redhat.com> - 3.6.0.v20100814043401-1
- Updated from upstream to 0.8.0 (3.6.0.v20100814043401); added fa, removed en_CA

* Wed Aug 4 2010 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20100729072834-1
- Updated from upstream to 0.8.0 RC1 (3.5.0.v20100731072648)

* Mon Aug 2 2010 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20100729072834-1
- Updated from upstream; added locales ca, en_CA and id.

* Thu Jun 10 2010 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20090620043401-3
- Marked eclipse-nls as not having debuginfo (#564482)

* Fri Jan 22 2010 Jens Petersen <petersen@redhat.com> - 3.5.0.v20090620043401-3
- only build for x86_64 and i686 like eclipse
  Resolves: #557742

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.5.0.v20090620043401-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.0.v20090620043401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20090620043401-1
- Updated to Babel's release "0.7"
- Created a new fetch-babel.sh to automate the zip downloads

* Wed May 27 2009 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20090423085802-1
- Updated from upstream; added Estonian.
- Fixed names/descriptions for languages with two word names such as "Portuguese (Brazilian)".
- Added Babel metadata files (artifact.jar and content.jar) to make P2 happier (presently disabled)
- Made the base package owner of dropins/babel and subdirectories

* Thu Apr 23 2009 Sean Flanigan <sflaniga@redhat.com> - 3.5.0.v20090417091040-1
- Updated to use Babel's zipped langpacks instead of fetch-babel.sh
- Changed versioning scheme to match changes in upstream versioning
- Updated to latest upstream langpacks for Eclipse 3.5 / Galileo

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.6.20080807snap
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 Sean Flanigan <sflaniga@redhat.com> - 0.2.0-0.5.20080807snap
- Applied another tidy-up patch from Jens Petersen and added a comment
 about the licence doc files

* Wed Sep 10 2008 Sean Flanigan <sflaniga@redhat.com> - 0.2.0-0.4.20080807snap
- Applied Jens Petersen's suggested patch to remove eclipse_version macro and 
  unnecessary buildroot checks

* Tue Sep 9 2008 Sean Flanigan <sflaniga@redhat.com> - 0.2.0-0.3.20080807snap
- Added eclipse_version macro
- Changed the Obsoletes version to be slightly higher than the last release of 
  eclipse-sdk-nls

* Mon Aug 11 2008 Sean Flanigan <sflaniga@redhat.com> - 0.2.0-0.2.20080807snap
- Fixed version in changelog
- Updated snapshot of Babel translation plugins
- Changed code for Hebrew to he (not iw); changed fetch-babel.sh to compensate
- Renamed eclipse_base macro to eclipse_data

* Fri Jul 25 2008 Sean Flanigan <sflaniga@redhat.com> - 0.2.0-0.1.20080720snap
- Initial rpm package
