Summary: The Reliable Event Logging Protocol library
Name: librelp
Version: 1.2.7
Release: 3%{?dist}.1
License: GPLv3+
Group: System Environment/Libraries
URL: http://www.rsyslog.com/
Source0: http://download.rsyslog.com/librelp/%{name}-%{version}.tar.gz
# patch sent upstream 2014-06-02
Patch0: librelp-1.2.7-keepalive-segv.patch
# patches 1..4 sent upstream 2014-06-03
Patch1: librelp-1.2.7-alloc-size.patch
Patch2: librelp-1.2.7-memleaks.patch
Patch3: librelp-1.2.7-realloc.patch
Patch4: librelp-1.2.7-misplaced-code.patch
Patch5: librelp-1.2.7-rhbz1561230-snprintf.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: gnutls-devel >= 1.4.0
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Librelp is an easy to use library for the RELP protocol. RELP (stands
for Reliable Event Logging Protocol) is a general-purpose, extensible
logging protocol.

%package devel
Summary: Development files for the %{name} package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Librelp is an easy to use library for the RELP protocol. The
librelp-devel package contains the header files and libraries needed
to develop applications using librelp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1 -b .snprintf

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun
if [ "$1" = "0" ] ; then
    /sbin/ldconfig
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README doc/*html
%{_libdir}/librelp.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/librelp.so
%{_libdir}/pkgconfig/relp.pc

%changelog
* Wed Mar 28 2018 Radovan Sroka <rsroka@redhat.com> 1.2.7-3.1
- fixed CVE-2018-1000140
- resolved: rhbz#1561230

* Mon Jun 02 2014 Tomas Heinrich <theinric@redhat.com> 1.2.7-3
- add patches to resolve issues reported by Coverity
  resolves: #966974

* Mon Jun 02 2014 Tomas Heinrich <theinric@redhat.com> 1.2.7-2
- add a patch to prevent a segfault when using TCP KEEPALIVE
  resolves: #966974

* Sun May 18 2014 Tomas Heinrich <theinric@redhat.com> 1.2.7-1
- rebase to 1.2.7
  resolves: #966974

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.1.1-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May  7 2008 Tomas Heinrich <theinric@redhat.com> 0.1.1-2
- removed "BuildRequires: autoconf automake"

* Tue Apr 29 2008 Tomas Heinrich <theinric@redhat.com> 0.1.1-1
- initial build
