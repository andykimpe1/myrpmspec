Name: flightrecorder
Version: 0.91
Release: 5%{?dist}
Summary: flightrecorder - runs trace-cmd to enable ftrace with predefined events

Group: Development/Tools
License: LGPLv2
URL: http://www.kernel.org/pub/linux/analysis/trace-cmd/
Source0:http://www.kernel.org/pub/linux/analysis/trace-cmd/%{name}-%{version}.tar.gz

Patch1: flightrecorder-trace-cmd.config-Add-the-i-option.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

#BuildRequires:
Requires: trace-cmd
Requires: chkconfig

%description
flightrecorder - runs trace-cmd to enable ftrace with events defined in /etc/sysconfig/trace-cmd

%prep
%setup -q
%patch1 -p1

%preun
chkconfig --del trace-cmd

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
chkconfig --add trace-cmd
chkconfig --level 345 trace-cmd on
chkconfig --level 0126 trace-cmd off

%files
%defattr(-,root,root,-)
%{_initrddir}/*
%{_sysconfdir}/sysconfig/*
%{_sysconfdir}/logrotate.d/*

%changelog
* Mon Sep 12 2016 John Kacur - 0.91-5
- Fix postun script failure when doing rpm -e flightrecorder
Resolves: rhbz#1324526

* Fri Dec 18 2015 John Kacur - 0.91-4
- flightrecorder: trace-cmd.config Add the -i option
Resolves: rhbz#1292404

* Tue Nov 10 2015 - John Kacur <jkacur@redhat.com>
- Make flightrecorder noarch since it is a shell-script
Resolves: rhbz#1278887

* Fri Nov 06 2015 - John Kacur <jkacur@redhat.com>
- Make flightrecorder depend on chkconfig
Resolves: rhbz#712342

* Thu Jul 29 2010 - John Kacur <jkacur@redhat.com>
- Fix syntax error that prevents chkconfig from working correctly

* Mon Jun 21 2010 - John Kacur <jkacur@redhat.com>
- Initial version of flightrecorder
