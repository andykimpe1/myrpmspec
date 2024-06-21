Name:           numatop
Version:        1.0.3
Release:        2%{?dist}
Summary:        Memory access locality characterization and analysis
Group:          System Environment/Base

License:        BSD
URL:            https://01.org/numatop
Source0:        https://01.org/sites/default/files/%{name}_linux_%{version}.tar.gz
Patch0:         0001-Fix-LMA-on-Westmere-EP.patch
BuildRequires:  numactl-devel ncurses-devel glibc-devel gcc
Requires:       glibc numactl ncurses-libs kernel >= 2.6.32-584
ExclusiveArch:  %{ix86} x86_64

%description
NumaTOP is an observation tool for runtime memory locality
characterization and analysis of processes and threads
running on a NUMA system. It helps the user characterize
the NUMA behavior of processes and threads and identify
where the NUMA-related performance bottlenecks reside.

NumaTOP supports the Intel Xeon processors.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man8
make install PREFIXDIR=%{buildroot}%{_prefix} MANDIR=%{buildroot}%{_mandir}/man8

%files
%doc AUTHORS README COPYING
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Tue Oct 18 2016 Petr Oros <poros@redhat.com> 1.0.3-2
- Fix LMA on Westmere EP
- Resolves: #1308627

* Tue Sep 1 2015 Petr Oros <poros@redhat.com> 1.0.3-1
- New upstream release with support for Haswell processors
- Resolves: #1238316

* Tue Jun 3 2014 Petr Oros <poros@redhat.com>
- spec: added requires kernel with PEBS Load Latency support
- Resolves: #1066152

* Tue Jun 3 2014 Petr Oros <poros@redhat.com>
- spec: build arch exclusive
- Resolves: #1066152

* Tue Jun 3 2014 Petr Oros <poros@redhat.com>
- Fix spec: source url, build arch
- Resolves: #1066152

* Tue Jun 3 2014 Petr Oros <poros@redhat.com>
- Fixes for spec file
- Resolves: #1066152

* Thu May 29 2014 Petr Oros <poros@redhat.com>
- Initial packaging.
- Resolves: #1066152
