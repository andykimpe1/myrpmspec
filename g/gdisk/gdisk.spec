Summary:       An fdisk-like partitioning tool for GPT disks
Name:          gdisk
Version:       0.8.10
Release:       1%{?dist}
License:       GPLv2
URL:           http://www.rodsbooks.com/gdisk/
Group:         System Environment/Base
Source0:       http://downloads.sourceforge.net/gptfdisk/gptfdisk-%{version}.tar.gz
BuildRequires: popt-devel
BuildRequires: libuuid-devel
BuildRequires: ncurses-devel
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%setup -q -n gptfdisk-%{version}
chmod 0644 gdisk_test.sh

%build
%{__make} CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"

%install
%{__rm} -rf %{buildroot}
for f in gdisk sgdisk cgdisk fixparts ; do 
    %{__install} -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    %{__install} -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc COPYING README gdisk_test.sh
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/cgdisk.8*
%{_mandir}/man8/sgdisk.8*
%{_mandir}/man8/fixparts.8*

%changelog
* Mon May 19 2014 Tomas Bzatek <tbzatek@redhat.com> - 0.8.10-1
- Update to 0.8.10

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.8.6-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.8.6-3
- Mass rebuild 2013-12-27

* Thu Sep 26 2013 Tomas Bzatek <tbzatek@redhat.com> - 0.8.6-2
- Range check -i option (#1007761)

* Fri Jan 25 2013 Orion Poplawski <orion@cora.nwra.com> - 0.8.6-1
- Update to 0.8.6

* Sat Nov 17 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.5-1
- 0.8.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.4-1
- 0.8.4

* Sat Apr 21 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 0.8.2-3
- Rebuild for libicu 49.1.1

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for c++ ABI breakage

* Sun Jan 29 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.2-1
- 0.8.2

* Thu Jan 05 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-3
- Add patch to build with gcc 4.7

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-2
- Add cgdisk and fixparts

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.8.1-1
- 0.8.1
- Add ncurses-devel to buildreq

* Thu Sep 08 2011 Orion Poplawski <orion@cora.nwra.com> - 0.7.2-2
- Rebuild for libicu 4.8.1

* Sun Jul 10 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.7.2-1
- 0.7.2

* Mon Apr 12 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.7.1-1
- 0.7.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 0.6.14-1
- 0.6.14

* Thu Nov 11 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.13-1
- 0.6.13

* Fri Jun 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.8-1
- 0.6.8

* Thu Mar 25 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.6-1
- 0.6.6
- Compile with -D_FILE_OFFSET_BITS=64, recommended upstream

* Sat Mar 20 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.5-1
- 0.6.5
- Add alignment patch (bz #575297)

* Thu Mar 11 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-2
- Fix source url

* Sun Feb 14 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.3-1
- 0.6.3

* Sun Jan 31 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.2-1
- 0.6.2

* Mon Jan 25 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.6.1-1
- 0.6.1
- add popt-devel to buildreq
- random clean up

* Fri Jan 15 2010 R Smith <rodsmith@rodsbooks.com> - 0.6.0
- created spec file for 0.6.0 release
