Name:		rds-tools
Summary:	RDS support tools 
Version:	2.0.6
Release:	4%{?dist}
License:	GPLv2 or BSD
Group:		Applications/System
URL:		http://oss.oracle.com/projects/rds/
Source0:	http://oss.oracle.com/projects/rds/dist/files/sources/%{name}-%{version}.tar.gz
Source1:	rds-tools-modprobe.conf
Patch0:		rds-tools-1.5-pfhack.patch
Patch1:		rds-tools-make.patch
Patch2:		rds-tools-2.0.6-ping-segfault.patch
Patch3:		rds-stress-send-msg-anysize.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:	s390 s390x

%description
Various tools for support of the RDS (Reliable Datagram Socket) API.  RDS
is specific to InfiniBand and iWARP networks and does not work on non-RDMA
hardware.

%prep
%setup -q
# Only try to define certain items if our build environment is old enough
# that it doesn't define them for us
%patch0 -p1
# Leave debugging info enabled so that we can get valid debug rpms
%patch1 -p1
# rds-ping can segfault due to reusing sockets too early, fix that
%patch2 -p1 -b .segfault
# rds-stress is failing to send messages of any size 
%patch3 -p1

%build
%configure
make CFLAGS="$CFLAGS -Iinclude" %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -fr %{buildroot}%{_includedir}
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d/rds.conf


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs examples
%{_bindir}/*
%{_mandir}/*/*
%{_sysconfdir}/modprobe.d/rds.conf

%changelog
* Thu Jan 21 2016 Donald Dutile <ddutile@redhat.com> - 2.0.6-4
- Fix rds-stress from failing to send msg of any size
- Resolves: bz746716

* Fri May 04 2012 Doug Ledford <dledford@redhat.com> - 2.0.6-3
- Fix segfault in rds-ping for real this time
- Resolves: bz804002

* Wed Mar 21 2012 Doug Ledford <dledford@redhat.com> - 2.0.6-2
- Fix segfault in rds-ping with short timeout values
- Resolves: bz804002

* Fri Jan 06 2012 Doug Ledford <dledford@redhat.com> - 2.0.6-1
- Update to latest upstream version
- Initial Fedora import
- Multiple fixes for package review
- Related: bz739138

* Fri Feb 04 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-3
- Update a few things for rpmdiff checks

* Thu Feb 03 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-2
- Add a modprobe conf file to automatically load rds_tcp and rds_rdma when
  we load the base rds module
- Resolves: bz643113

* Thu Feb 03 2011 Doug Ledford <dledford@redhat.com> - 2.0.4-1
- Update to latest upstream version
- Resolves: bz636908

* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 1.5-2
- Remove include file as we don't provide a real devel environment
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.5-1
- Update to latest upstream version
- Related: bz518218

* Tue Jul 21 2009 Doug Ledford <dledford@redhat.com> - 1.4-2
- Enable debug output during build so debuginfo package isn't empty
- Resolves: bz500627

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Initial version for Red Hat Enterprise Linux 5
- Related: bz459652

