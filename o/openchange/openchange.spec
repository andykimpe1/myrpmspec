%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global samba4_version 4.0.0
%global talloc_version 2.0.5
%global nickname BORG

%global build_python_package 0
%global build_server_package 0

### Abstract ###

# Licensing Note: The code is GPLv3+ and the IDL files are public domain.

Name: openchange
Version: 1.0
Release: 7.0.1%{?dist}
Group: Applications/System
Summary: Provides access to Microsoft Exchange servers using native protocols
License: GPLv3+ and Public Domain
URL: http://www.openchange.org/
Source0: http://tracker.openchange.org/attachments/download/180/openchange-%{version}-%{nickname}.tar.gz
Source1: doxygen_to_devhelp.xsl
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

### Build Dependencies ###

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: doxygen
BuildRequires: file-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libical-devel
BuildRequires: libldb-devel
BuildRequires: libtalloc-devel >= %{talloc_version}
BuildRequires: libtdb-devel
BuildRequires: pkgconfig
BuildRequires: libxslt
BuildRequires: popt-devel
BuildRequires: python-devel
BuildRequires: samba4-devel >= %{samba4_version}
BuildRequires: samba4-pidl >= %{samba4_version}
BuildRequires: sqlite-devel
BuildRequires: zlib-devel

# Certain versions of libtevent have incorrect
# internal ABI versions
Conflicts: libtevent < 0.9.13

# Obsolete multilib version of this package,
# since samba4-libs is no longer multilib.
Obsoletes: openchange < 1.0-4

### Patches ###

# OpenChange's libmapi conflicts with Zarafa's libmapi.
# Zarafa is older than OpenChange, so it wins.
Patch0: libmapi-0.8.2-libmapi-conflict.patch

# RH bug #552984
Patch1: openchange-0.9-generate-xml-doc.patch

# Use system's popt.h
Patch2: openchange-1.0-popt.patch

Patch3: openchange-1.0-OC_RULE_ADD-fix.patch

# http://tracker.openchange.org/issues/397
Patch4: openchange-1.0-uninit-crash.patch

# http://tracker.openchange.org/issues/398
Patch5: openchange-1.0-symbol-clash.patch

# RH-bug #870405
Patch6: openchange-1.0-writestream.patch

# RH-bug #665967
Patch7: openchange-1.0-freebusy.patch

# Fix connection arguments for newer samba
Patch8: openchange-1.0-fix-connection-args.patch

%description
OpenChange provides libraries to access Microsoft Exchange servers
using native protocols.

%package devel
Summary: Developer tools for OpenChange libraries
Group: Development/Libraries
Requires: openchange = %{version}-%{release}

%description devel
This package provides the development tools and headers for
OpenChange, providing libraries to access Microsoft Exchange servers
using native protocols.

%package devel-docs
Summary: Developer documentation for OpenChange libraries
Group: Development/Libraries
Requires: devhelp
Requires: openchange = %{version}-%{release}

%description devel-docs
This package contains developer documentation for Openchange.

%package client
Summary: User tools for OpenChange libraries
Group: Applications/System
Requires: openchange = %{version}-%{release}

%description client
This package provides the user tools for OpenChange, providing access to
Microsoft Exchange servers using native protocols.

%if %{build_python_package}
%package python
Summary: Python bindings for OpenChange libraries
Group: Development/Libraries
Requires: openchange = %{version}-%{release}

%description python
This module contains a wrapper that allows the use of OpenChange via Python.
%endif

%if %{build_server_package}
%package server
Summary: Server-side modules for OpenChange
Group: Applications/System
Requires: openchange = %{version}-%{release}
Requires: sqlite

%description server
This package provides the server elements for OpenChange.
%endif

%prep
%setup -q -n %{name}-%{version}-%{nickname}
%patch0 -p1 -b .libmapi-conflict
%patch1 -p1 -b .generate-xml-doc
%patch2 -p1 -b .popt
%patch3 -p1 -b .OC_RULE_ADD-fix
%patch4 -p1 -b .uninit-crash
%patch5 -p1 -b .symbol-clash
%patch6 -p1 -b .writestream
%patch7 -p1 -b .freebusy
%patch8 -p1 -b .fix-connection-args

%build
./autogen.sh
%configure \
%if %{build_python_package}
	--enable-pymapi \
%endif
	--with-modulesdir=%{_libdir}/samba/modules

# Parallel builds prohibited by makefile
make
make doxygen

xsltproc -o openchange-libmapi.devhelp --stringparam "booktitle" "MAPI client library (libmapi)" --stringparam "bookpart" "libmapi" %{SOURCE1} apidocs/xml/libmapi/index.xml
xsltproc -o openchange-libmapiadmin.devhelp --stringparam "booktitle" "MAPI administration libraries (libmapiadmin)" --stringparam "bookpart" "libmapiadmin" %{SOURCE1} apidocs/xml/libmapiadmin/index.xml
xsltproc -o openchange-libocpf.devhelp --stringparam "booktitle" "OpenChange Property Files (libocpf)" --stringparam "bookpart" "libocpf" %{SOURCE1} apidocs/xml/libocpf/index.xml
xsltproc -o openchange-mapitest.devhelp --stringparam "booktitle" "MA regression test framework (mapitest)" --stringparam "bookpart" "mapitest" %{SOURCE1} apidocs/xml/mapitest/index.xml
xsltproc -o openchange-mapiproxy.devhelp --stringparam "booktitle" "MAPIProxy project (mapiproxy)" --stringparam "bookpart" "mapiproxy" %{SOURCE1} apidocs/xml/mapiproxy/index.xml
xsltproc -o openchange-libmapi++.devhelp --stringparam "booktitle" "C++ bindings for libmapi (libmapi++)" --stringparam "bookpart" "libmapi++" %{SOURCE1} apidocs/xml/libmapi++/index.xml

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

cp -r libmapi++ $RPM_BUILD_ROOT%{_includedir}

rm -rf $RPM_BUILD_ROOT%{_libdir}/nagios/check_exchange
rm -rf $RPM_BUILD_ROOT%{_prefix}/modules
rm -rf $RPM_BUILD_ROOT%{_datadir}/js
rm -rf $RPM_BUILD_ROOT%{_datadir}/setup
rm -rf $RPM_BUILD_ROOT%{_libdir}/libmapiproxy.so.*

# This makes the right links, as rpmlint requires that the
# ldconfig-created links be recorded in the RPM.
/sbin/ldconfig -N -n $RPM_BUILD_ROOT/%{_libdir}

mkdir $RPM_BUILD_ROOT%{_mandir}
cp -r doc/man/man1 $RPM_BUILD_ROOT%{_mandir}

# Skip man3 for now, it doesn't work anyway
# cp -r apidocs/man/man3 $RPM_BUILD_ROOT%{_mandir}
rm -r apidocs/man/man3

%if !%{build_python_package} && !%{build_server_package}
rm $RPM_BUILD_ROOT%{_bindir}/check_fasttransfer
%endif

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi
cp openchange-libmapi.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi
cp -r apidocs/html/libmapi/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin
cp openchange-libmapiadmin.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin
cp -r apidocs/html/libmapiadmin/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapiadmin

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf
cp openchange-libocpf.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf
cp -r apidocs/html/libocpf/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libocpf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest
cp openchange-mapitest.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest
cp -r apidocs/html/mapitest/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapitest

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy
cp openchange-mapiproxy.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy
cp -r apidocs/html/mapiproxy/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-mapiproxy

mkdir -p $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++
cp openchange-libmapi++.devhelp $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++
cp -r apidocs/html/libmapi++/* $RPM_BUILD_ROOT%{_datadir}/devhelp/books/openchange-libmapi++

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if %{build_server_package}
%post server -p /sbin/ldconfig

%postun server -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING IDL_LICENSE.txt VERSION
%{_libdir}/libmapi-openchange.so.*
%{_libdir}/libmapiadmin.so.*
%if %{build_python_package} || %{build_server_package}
%{_libdir}/libmapiproxy.so.*
%{_libdir}/libmapistore.so.*
%endif
%{_libdir}/libocpf.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files devel-docs
%defattr(-,root,root,-)
#%{_mandir}/man3/*
%doc %{_datadir}/devhelp/books/*
%doc apidocs/html/libmapi
%doc apidocs/html/libocpf
%doc apidocs/html/overview
%doc apidocs/html/index.html

%files client
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/mapitest/*

%if %{build_python_package}
%files python
%defattr(-,root,root,-)
%{python_sitearch}/openchange
%endif

%if %{build_server_package}
%files server
%defattr(-,root,root,-)
%{_libdir}/libmapiserver.so.*
%{_libdir}/samba/dcerpc_server/dcesrv_mapiproxy.so
%{_libdir}/samba/modules/*
%if !0%{?rhel}
%{_libdir}/nagios/check_exchange
%endif
%{_datadir}/setup/*
%endif

%changelog
* Thu Mar 23 2017 Johnny Hughes <johnny@centos.org> - 1.0-7.0.1
- Need to build against the latest samba4 .. no code changes

* Thu Apr 07 2016 Milan Crha <mcrha@redhat.com> - 1.0-7
- Add a patch to fix connection string (Related: #1322688)

* Wed Oct 16 2013 Milan Crha <mcrha@redhat.com> - 1.0-6
- Add a patch for RH bug #665967 (Free/busy fails to be fetched)

* Thu Jan 17 2013 Milan Crha <mcrha@redhat.com> - 1.0-4
- Use current version (1.0-4) for a multilib obsolete (RH bug #881698).

* Tue Jan 08 2013 Milan Crha <mcrha@redhat.com> - 1.0-3
- Add patch to be able to send large messages (RH bug #870405)

* Mon Jan 07 2013 Matthew Barnes <mbarnes@redhat.com> - 1.0-2
- Drop multilib by obsoleting openchange < 0.9 (RH bug #881698).

* Wed Oct 03 2012 Matthew Barnes <mbarnes@redhat.com> - 1.0-1
- Rebase to 1.0 using the rpm spec from Fedora 18.

* Fri Jun 25 2010 Milan Crha <mcrha@redhat.com> - 0.9-7
- Backport unicode and properties support (RH bug #605364).

* Thu Jun 24 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-6
- Disable python and server subpackages (RH bug #603688).

* Tue Jun 23 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-5
- Spec file cleanups.

* Fri May 28 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-4
- Re-fix the file conflict avoidance.

* Mon May 24 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-3
- Avoid a file conflict with man-pages package.

* Sat Jan 09 2010 Matthew Barnes <mbarnes@redhat.com> - 0.9-2
- Add a devel-docs subpackage (RH bug #552984).

* Sat Dec 26 2009 Matthew Barnes <mbarnes@redhat.com> - 0.9-1
- Update to 0.9 (COCHRANE)
- Bump samba4 requirement to alpha10.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-3
- Rename libmapi so as not to conflict with Zarafa (RH bug #505783).

* Thu May 07 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-2
- Do not own the pkgconfig directory (RH bug #499655).

* Tue Mar 31 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8.2-1
- Update to 0.8.2
- Add a server subpackage.
- Add BuildRequires: sqlite-devel (for server)

* Sun Mar 08 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-6
- Fix build breakage.
- Explicitly require libldb-devel.
- Bump samba4 requirement to alpha7.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-5
- Rebuild with correct tarball.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-4
- Formal package review cleanups.

* Wed Feb 25 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-3
- Add documentation files.

* Thu Feb 19 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-2
- Add some missing build requirements.

* Thu Jan 20 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-1
- Update to 0.8 (ROMULUS)

* Sat Jan 17 2009 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.7.svn949
- Add missing BuildRequires: zlib-devel

* Sat Dec 27 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.6.svn949
- Update to SVN revision 949.

* Mon Dec 15 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.5.svn909
- Package review feedback (RH bug #453395).

* Fri Dec 12 2008 Matthew Barnes <mbarnes@redhat.com> - 0.8-0.4.svn909
- Update to SVN revision 909.
- Bump the samba4 requirement.

* Fri Aug 29 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.8-0.3.svn960.fc9
- Bump version
- Don't make the Samba4 version distro-dependent

* Sat Jul 26 2008 Brad Hards <bradh@frogmouth.net> - 0:0.8-0.2.svnr674.fc10
- Bump version
- Install documentation / man pages correctly
- Remove epoch (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Remove %%post and %%postun (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Remove talloc dependency (per https://bugzilla.redhat.com/show_bug.cgi?id=453395)
- Take out libmapiproxy, because we aren't up to server side yet.

* Sat Jul 12 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.7-0.2.svnr627.fc9
- Add popt-devel BR

* Mon Jun 30 2008 Andrew Bartlett <abartlet@samba.org> - 0:0.7-0.1.svnr627.fc9
- Initial package of OpenChange for Fedora
