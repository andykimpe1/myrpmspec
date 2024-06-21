
Name:           ps_mem
Version:        3.1
Release:        5%{?dist}
Summary:        Memory profiling tool
Group:          Applications/System
License:        LGPLv2
URL:            https://github.com/pixelb/scripts

Source0:        https://raw.github.com/pixelb/scripts/961ff24c805a474080520403409872b04e18f4d9/scripts/ps_mem.py
Source1:        http://www.gnu.org/licenses/lgpl-2.1.txt
Source2:        ps_mem.1

Patch0:         ps_mem-ennobling-the-s-switch.patch

BuildArch:      noarch

Requires:       python2


%description
The ps_mem tool can determine how much RAM is used per program
(not per process). In detail it reports:
sum(private RAM for program processes) + sum(Shared RAM for program processes)
The shared RAM is problematic to calculate, and the tool automatically
selects the most accurate method available for the running kernel.


%prep
%setup -q -T -c %{name}-%{version}

cp -p %{SOURCE0} %{name}
cp -p %{SOURCE1} LICENSE
cp -p %{SOURCE2} %{name}.1

# force python2
sed -i "s|/usr/bin/env python|/usr/bin/python2|" %{name}

%patch0 -p2


%install
install -Dpm755 %{name}   %{buildroot}%{_bindir}/%{name}
install -Dpm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Aug 14 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-5
- Replacing python2 macro with absolute path to python2

* Wed Aug 14 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-4
- RH man page scan (#989490)

* Thu Jul 25 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-3
- Patching shebang to force python2 (#987036)

* Thu May 30 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-2
- Preserving file timestamps

* Wed May 29 2013 Jaromir Capik <jcapik@redhat.com> - 3.1-1
- Initial package
