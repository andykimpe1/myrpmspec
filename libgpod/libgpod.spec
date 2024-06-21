%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Library to access the contents of an iPod
Name: libgpod
Version: 0.7.2
Release: 6%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.gtkpod.org/libgpod.html
Source0: http://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# See http://www.redhat.com/archives/fedora-selinux-list/2009-January/msg00005.html
Patch0: 0001-Use-var-run-hald-as-mount-dir-for-hal-callout.patch
# http://gitorious.org/~teuf/libgpod/teuf-sandbox/commit/3847494a513b5ef04d7abbe55c3d95dbcd836ef6
# https://bugzilla.redhat.com/show_bug.cgi?id=517642
Patch1: libgpod-utf16-parsing.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=542176
Patch2: libgpod-handle-partial-utf16.patch
# Numerous gtkpod crashes are attributed to misuse of xmlCleanupParser()
Patch3: 0001-Remove-calls-to-xmlCleanupParser.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: docbook-style-xsl
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: gettext
BuildRequires: hal-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt
BuildRequires: perl(XML::Parser)
BuildRequires: pygobject2-devel
Buildrequires: python-devel
Buildrequires: python-mutagen
Buildrequires: sg3_utils-devel
Buildrequires: swig
Requires: hal

%description
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.


%package devel
Summary: Development files for the libgpod library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel
Requires: gtk2-devel
Requires: pkgconfig

%description devel
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.

This package contains the files required to develop programs that will use
libgpod.


%package doc
Summary: API documentation for the libgpod library
Group: Documentation
License: GFDL
%if 0%{?fedora} > 10 || 0%{?rhel} >= 6
BuildArch: noarch
%endif
Requires: %{name} = %{version}-%{release}
Requires: gtk-doc

%description doc
Libgpod is a library to access the contents of an iPod. It supports playlists,
smart playlists, playcounts, ratings, podcasts, album artwork, photos, etc.

This package contains the API documentation.


%package -n python-gpod
Summary: Python module to access iPod content
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: python-mutagen

%description -n python-gpod
A python module to access iPod content.  This module provides bindings to the
libgpod library.


%prep
%setup -q
%patch0 -p1 -b .selinux
%patch1 -p1 -b .utf16
%patch2 -p1 -b .partial-utf16
%patch3 -p1 -b .xmlCleanupParser

# remove execute perms on the python examples as they'll be installed in %doc
%{__chmod} -x bindings/python/examples/*.py


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
%find_lang %{name}

# remove Makefiles from the python examples dir
%{__rm} -rf bindings/python/examples/Makefile*


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/hal/scripts/*
%{_datadir}/hal/fdi/policy/20thirdparty/*.fdi


%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gpod-1.0/
%{_libdir}/pkgconfig/libgpod-1.0.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%files doc
%defattr(-, root, root, 0755)
%{_datadir}/gtk-doc/html/libgpod


%files -n python-gpod
%defattr(-, root, root, 0755)
%doc COPYING bindings/python/README bindings/python/examples
%{python_sitearch}/gpod
%exclude %{python_sitearch}/gpod/*.a
%exclude %{python_sitearch}/gpod/*.la


%changelog
* Mon Feb 15 2010 Bastien Nocera <bnocera@redhat.com> 0.7.2-6
- Handle partial UTF-16 strings (#542176)
- Fix xmlCleanupParser() usage
Related: rhbz#565546

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.7.2-5.1
- Fix conditional for RHEL

* Mon Oct 19 2009 Bastien Nocera <bnocera@redhat.com> 0.7.2-5
- Fix UTF-16 string parsing patch again

* Mon Oct 19 2009 Bastien Nocera <bnocera@redhat.com> 0.7.2-4
- Update UTF-16 string parsing patch

* Sat Oct 17 2009 Bastien Nocera <bnocera@redhat.com> 0.7.2-3
- Fix crasher when parsing UTF-16 strings with a BOM (#517642)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Todd Zullinger <tmz@pobox.com> - 0.7.2-1
- Update to 0.7.2
- Make doc subpackage noarch (on Fedora >= 10)
- Drop --with-hal-callouts-dir from configure, the upstream default works now

* Tue Apr 28 2009 Dan Horak <dan[at]danny.cz> - 0.7.0-3
- rebuild for sg3_utils 1.27

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Todd Zullinger <tmz@pobox.com> - 0.7.0-1
- Update to 0.7.0
- BR libxml2-devel

* Wed Jan 14 2009 Todd Zullinger <tmz@pobox.com> - 0.6.0-10
- Fix path to hal callout (this should help setup the SysInfoExtended
  file automagically)
- Use /var/run/hald as mount dir for hal callout
- Require hal
- Require main package for the -doc subpackage

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.0-9
- Rebuild for Python 2.6

* Thu Oct 02 2008 Todd Zullinger <tmz@pobox.com> - 0.6.0-8
- The -devel package should require gtk2-devel as well
- Add gdk-pixbuf-2.0 to the pkg-config file requirements

* Thu Aug 28 2008 Todd Zullinger <tmz@pobox.com> - 0.6.0-7
- Ensure patches apply with no fuzz

* Mon Jun 30 2008 Dan Horak <dan[at]danny.cz> - 0.6.0-6
- add patch for sg3_utils 1.26 and rebuild

* Wed May 14 2008 Todd Zullinger <tmz@pobox.com> - 0.6.0-5
- Make libgpod-devel require glib2-devel (#446442)

* Tue Feb 12 2008 Todd Zullinger <tmz@pobox.com> - 0.6.0-4
- rebuild for gcc 4.3

* Wed Dec 19 2007 Todd Zullinger <tmz@pobox.com> - 0.6.0-3
- BR docbook-style-xsl to ensure the python docs are built correctly

* Wed Dec 19 2007 Todd Zullinger <tmz@pobox.com> - 0.6.0-2
- add the NEWS file, which contains some info on getting newer iPods working
- split out API docs into a separate package
- set %%defattr for python-gpod

* Wed Nov 21 2007 Todd Zullinger <tmz@pobox.com> - 0.6.0-1
- update to 0.6.0
- apply a few upstream patches that just missed the release

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 0.5.2-2
- Rebuild for build ID

* Sat Aug 04 2007 Todd Zullinger <tmz@pobox.com> - 0.5.2-1
- update to 0.5.2
- replace %%makeinstall with %%{__make} DESTDIR=%%{buildroot} install
- build python bindings, merging python-gpod package from extras
- make %%setup quiet
- patch to fixup building of the python docs, BR libxslt
- update license tag

* Tue Jan 16 2007 Alexander Larsson <alexl@redhat.com> - 0.4.2-1
- update to 0.4.2
- Change %%description to reflect newer features
- Remove TODO file from %%doc as it's not included anymore
- Explicitly disable the python bindings, they are in the python-gpod package in
  Extras until the Core/Extras merge

* Mon Nov 20 2006 Alexander Larsson <alexl@redhat.com> - 0.4.0-2
- Add ldconfig calls in post/postun

* Mon Nov 13 2006 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0
- Include docs in the -devel package
- Don't ship static libraries

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-3.1
- rebuild

* Tue Jun 06 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-3
- Add missing BR of perl-XML-Parser

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 04 2006 John (J5) Palmieri <johnp@redhat.com> 0.3.0-2
- Modified Matthias Saou's SPEC file found on freshrpms.net
- Added to Fedora Core

* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Initial RPM release.

