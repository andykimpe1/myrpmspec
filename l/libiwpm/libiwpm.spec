Name:     libiwpm
Version:  1.0.3
Release:  5%{?dist}
Summary:  iWarp Port Mapper userspace daemon
Group:    System Environment/Daemons
License:  GPLv2 or BSD
Url:      http://www.openfabrics.org/
Source:   https://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Source1:  iwpmd.init
Patch0:   do-not-install-the-header-files.patch
Patch1:   license.patch

BuildRequires:    libnl3-devel

Requires(post):   chkconfig
Requires(preun):  chkconfig
Requires(preun):  initscripts
Requires(postun): initscripts

%description
libiwpm provides a userspace service for iWarp drivers to claim
tcp ports through the standard socket interface.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -Dp -m 0755 %{SOURCE1} %{buildroot}%{_initddir}/iwpmd
install -Dp -m 0644 iwpmd.conf %{buildroot}%{_sysconfdir}/iwpmd.conf

%post
/sbin/chkconfig --add iwpmd

%preun
if [ $1 -eq 0 ]; then 
    /sbin/service iwpmd stop >/dev/null 2>&1
    /sbin/chkconfig --del iwpmd
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service iwpmd condrestart >/dev/null 2>&1 || :
fi

%files
%doc AUTHORS COPYING README
%{_bindir}/iwpmd
%{_initddir}/iwpmd
%config(noreplace) %{_sysconfdir}/iwpmd.conf

%changelog
* Tue Jan 12 2016 Honggang Li <honli@redhat.com> - 1.0.3-5
- Rewrite initscript
- Replace upstream blank "COPYING" file with GPLv2 license

* Sat Jan  9 2016 Honggang Li <honli@redhat.com> - 1.0.3-4
- Update the changelog

* Sat Jan  9 2016 Honggang Li <honli@redhat.com> - 1.0.3-3
- Do not install the header files

* Fri Jan  8 2016 Honggang Li <honli@redhat.com> - 1.0.3-2
- Rewrite the spec file as Michal Schmidt (mschmidt@redhat.com) suggested

* Fri Dec 18 2015 Honggang Li <honli@redhat.com> - 1.0.3-1
- Import libiwpm for RHEL-6.8

* Wed Oct 14 2015 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 1.0.3
- Fix for the init script to enable the service to start automatically
  after boot on SLES11 SP4
- Releasing libiwpm-1.0.3 to be included in OFED-3.18-1

* Fri Aug 14 2015 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 1.0.3rc1
- Adding iwpmd.conf file to enable changing the size
  of the netlink socket receive buffer
- Including a fix for failing to send netlink messages

* Thu Jul 2 2015 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 1.0.2
- Fixes for the iwpmd start-up scripts with systemd
- A change to enable multi devices per port mapper client
- Releasing libiwpm-1.0.2 to be included in OFED-3.18

* Fri Oct 31 2014 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 1.0.1
- Releasing libiwpm-1.0.1 to be included in OFED-3.18

* Mon Jun 10 2013 Tatyana Nikolova <tatyana.e.nikolova@intel.com> - 1.0.0
- Releasing iWarp Port Mapper Version 1.0.0 
