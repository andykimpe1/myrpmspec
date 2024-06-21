Name: libpcap
Epoch: 14
Version: 1.4.0
Release: 4.20130826git2dbcaa1%{?dist}
Summary: A system-independent interface for user-level packet capture
Group: Development/Libraries
License: BSD with advertising
URL: http://www.tcpdump.org
BuildRequires: glibc-kernheaders >= 2.2.0 bison flex bluez-libs-devel autoconf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: libpcap-1.4.0-20130826git2dbcaa1.tar.gz
Source1: generate-tarball.sh
# These manpages are not included upstream yet
Source2: pcap_set_tstamp_precision.3pcap.in
Source3: pcap_get_tstamp_precision.3pcap.in

Patch1: libpcap-man.patch
Patch2: libpcap-multilib.patch
Patch3: libpcap-s390.patch
Patch4: libpcap-makefile-in.patch
Patch5: libpcap-configure-in.patch
Patch6: libpcap-tstamp-precision-list-deadcode.patch
Patch7: libpcap-tstamp-precision-list-init.patch
Patch8: libpcap-tstamp-type-list-leak.patch
Patch9:  0001-Introduce-bpf_filter1-function.patch
Patch10: 0002-Use-BPF-extensions-in-compiled-filters.patch
Patch11: 0003-More-descriptive-name-for-bpf_filter1.patch
Patch12: 0004-Get-rid-of-unused-variable.patch
Patch13: 0005-Move-the-socket-ops-out-of-gencode.c.patch
Patch14: 0006-There-s-no-pcap_t-argument-to-code-generator-routine.patch
Patch15: 0007-Fix-compilation-failure-on-RHEL6-where-TP_STATUS_VLA.patch
Patch16: 0008-Fix-issues-discovered-by-coverity.patch
Patch17: 0009-Initialize-len-before-calling-getsockopt.patch

%description
Libpcap provides a portable framework for low-level network
monitoring.  Libpcap can provide network statistics collection,
security monitoring and network debugging.  Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

Install libpcap if you need to do low-level network traffic monitoring
on your network.

%package devel
Summary: Libraries and header files for the libpcap library
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Libpcap provides a portable framework for low-level network
monitoring.  Libpcap can provide network statistics collection,
security monitoring and network debugging.  Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

This package provides the libraries, include files, and other 
resources needed for developing libpcap applications.
 
%prep
%setup -q -n libpcap-%{version}

cp %{SOURCE2} .
cp %{SOURCE3} .

%patch1 -p1 -b .man 
%patch2 -p1 -b .multilib
%patch3 -p1 -b .s390
%patch4 -p1 -b .makefile-in
%patch5 -p1 -b .configure-in
%patch6 -p1 -b .deadcode
%patch7 -p1 -b .tstamp-precision-list-init
%patch8 -p1 -b .tstamp-type-list-leak
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

#sparc needs -fPIC 
%ifarch %{sparc}
sed -i -e 's|-fpic|-fPIC|g' configure
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing $(getconf LFS_CFLAGS)"
autoreconf -f -i
%configure --enable-ipv6 --enable-bluetooth
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/libpcap.a

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE README CHANGES CREDITS
%{_libdir}/libpcap.so.*
%{_mandir}/man7/pcap*.7*

%files devel
%defattr(-,root,root)
%{_bindir}/pcap-config
%{_includedir}/pcap*.h
%{_includedir}/pcap
%{_libdir}/libpcap.so
%{_mandir}/man1/pcap-config.1*
%{_mandir}/man3/pcap*.3*
%{_mandir}/man5/pcap*.5*

%changelog
* Wed Jan 28 2015 Michal Sekletar <msekleta@redhat.com> - 14:1.4.0-4.20130826git2dbcaa1
- fix one more issue reported by coverity

* Wed Jan 28 2015 Michal Sekletar <msekleta@redhat.com> - 14:1.4.0-3.20130826git2dbcaa1
- fix issue discovered by coverity

* Tue Jan 27 2015 Michal Sekletar <msekleta@redhat.com> - 14:1.4.0-2.20130826git2dbcaa1
- fix filtering when vlan keyword is used in filter expression (#1025841, #1063328)

* Wed Aug 28 2013 Michal Sekletar <msekleta@redhat.com> 14:1.4.0-20130826git2dbcaa1
- update to snapshot 20130826git2dbcaa1 (#916749)

* Fri Jun 18 2010 Miroslav Lichvar <mlichvar@redhat.com> 14:1.0.0-6.20091201git117cb5
- compile with -fno-strict-aliasing (#605080)

* Wed Dec 16 2009 Miroslav Lichvar <mlichvar@redhat.com> 14:1.0.0-5.20091201git117cb5
- update to snapshot 20091201git117cb5

* Sat Oct 17 2009 Dennis Gilmore <dennis@ausil.us> 14:1.0.0-4.20090922gite154e2
- use -fPIC on sparc arches

* Wed Sep 23 2009 Miroslav Lichvar <mlichvar@redhat.com> 14:1.0.0-3.20090922gite154e2
- update to snapshot 20090922gite154e2
- drop old soname

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:1.0.0-2.20090716git6de2de
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Miroslav Lichvar <mlichvar@redhat.com> 14:1.0.0-1.20090716git6de2de
- update to 1.0.0, git snapshot 20090716git6de2de

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14:0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jun 27 2008 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.8-3
- use CFLAGS when linking (#445682)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 14:0.9.8-2
- Autorebuild for GCC 4.3

* Wed Oct 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.8-1
- update to 0.9.8

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.7-3
- update license tag

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 14:0.9.7-2
- Rebuild for RH #249435

* Tue Jul 24 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.7-1
- update to 0.9.7

* Tue Jun 19 2007 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.6-1
- update to 0.9.6

* Tue Nov 28 2006 Miroslav Lichvar <mlichvar@redhat.com> 14:0.9.5-1
- split from tcpdump package (#193657)
- update to 0.9.5
- don't package static library
- maintain soname
