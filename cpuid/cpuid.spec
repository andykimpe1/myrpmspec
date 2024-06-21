Name:           cpuid
Version:        20160814
Release:        1%{?dist}
Summary:        Dumps information about the CPU(s)

License:        GPLv2+
URL:            http://www.etallen.com/cpuid.html
Source0:        http://www.etallen.com/%{name}/%{name}-%{version}.src.tar.gz
# Specific to RHEL
Patch1:         disclaimer.patch

ExclusiveArch:  %{ix86} x86_64

%description
cpuid dumps detailed information about x86 CPU(s) gathered from the CPUID
instruction, and also determines the exact model of CPU(s). It supports Intel,
AMD, and VIA CPUs, as well as older Transmeta, Cyrix, UMC, NexGen, and Rise
CPUs. 

%prep
%setup -q
%patch1 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DVERSION=%{version}"

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0755 cpuinfo2cpuid %{buildroot}%{_bindir}/cpuinfo2cpuid
install -Dp -m 0644 %{name}.man.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -Dp -m 0644 cpuinfo2cpuid.man.gz %{buildroot}%{_mandir}/man1/cpuinfo2cpuid.1.gz


%files
%doc ChangeLog FUTURE LICENSE
%{_mandir}/man1/*%{name}.1*
%{_bindir}/*%{name}

%changelog
* Thu Sep  8 2016 Jirka Hladky <jhladky@redhat.com> - 20160814-1
- Update to new upstream version 20160814
- It includes new tool cpuinfo2cpuid which enables to process /proc/cpuinfo
- Rebuilt for RHEL6 (rhbz#1316998)

* Wed Jun 22 2016 Jirka Hladky <jhladky@redhat.com> - 20151017-4
- Fixed license field

* Wed Jun 01 2016 Jirka Hladky <jhladky@redhat.com> - 20151017-3
- Rebuilt for RHEL7 (rhbz#1307043)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20151017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Fabian Affolter <mail@fabian-affolter.ch> - 20151017-1
- Update to new upstream version 20151017 (rhbz#1272715)

* Fri Jun 26 2015 Fabian Affolter <mail@fabian-affolter.ch> - 20150606-1
- Update to new upstream version 20150606

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Fabian Affolter <mail@fabian-affolter.ch> - 20140123-1
- Update to new upstream version 20130123

* Tue Jan 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 20140114-1
- Update to new upstream version 20130114

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130610-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 20130610-1
- Update to new upstream version 20130610

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120601-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120601-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Fabian Affolter <mail@fabian-affolter.ch> - 20120601-1
- Update to new upstream version 20120601

* Sun Feb 26 2012 Fabian Affolter <mail@fabian-affolter.ch> - 20120225-1
- Update to new upstream version 20120225

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110305-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 06 2011 Fabian Affolter <mail@fabian-affolter.ch> - 20110305-1
- Update to new upstream version 20110305

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 06 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20101010-1
- Update to new upstream version 20101002

* Thu Sep 02 2010 Fabian Affolter <mail@fabian-affolter.ch> - 20100901-1
- Update to new upstream version 20100901

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060917-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20060917-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Fabian Affolter <mail@fabian-affolter.ch> - 20060917-4
- Change %%build section acc. #469590 comment #5

* Sat Nov 08 2008 Fabian Affolter <mail@fabian-affolter.ch> - 20060917-3
- Change %%build section and License acc. #469590 comment #3
- Fix %%doc in changelog

* Tue Nov 04 2008 Fabian Affolter <mail@fabian-affolter.ch> - 20060917-2
- Switch to ExclusiveArch
- Remove %%doc from man page and general changes to the man page installation

* Sun Nov 02 2008 Fabian Affolter <mail@fabian-affolter.ch> - 20060917-1
- Initial package for Fedora
