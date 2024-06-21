Name:           libwacom
Version:        0.16
Release:        2%{?dist}
Summary:        Tablet Information Client Library
Requires:       %{name}-data

Group:          System Environment/Libraries
License:        MIT
URL:            http://linuxwacom.sourceforge.net

Source0:        http://prdownloads.sourceforge.net/linuxwacom/%{name}/%{name}-%{version}.tar.bz2

Patch01:        0001-Add-support-for-the-ExpressKey-Remote.patch
Patch02:        0002-data-make-all-buttons-on-the-EKR-left-buttons.patch

BuildRequires:  autoconf automake libtool doxygen
BuildRequires:  glib2-devel libgudev1-devel

%description
%{name} is a library that provides information about Wacom tablets and
tools. This information can then be used by drivers or applications to tweak
the UI or general settings to match the physical tablet.

%package devel
Summary:        Tablet Information Client Library Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Tablet information client library library development package.

%package data
Summary:        Tablet Information Client Library Library Data Files
BuildArch:      noarch

%description data
Tablet information client library library data files.

%prep
%setup -q -n %{name}-%{version}
%patch01 -p1
%patch02 -p1

%build
autoreconf --force -v --install || exit 1
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
install -d ${RPM_BUILD_ROOT}/lib/udev/rules.d
# auto-generate the udev rule from the database entries
pushd tools
./generate-udev-rules > ${RPM_BUILD_ROOT}/lib/udev/rules.d/65-libwacom.rules
popd

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README 
%{_libdir}/libwacom.so.*
/lib/udev/rules.d/65-libwacom.rules
%{_bindir}/libwacom-list-local-devices

%files devel
%defattr(-,root,root,-)
%doc COPYING
%dir %{_includedir}/libwacom-1.0/
%dir %{_includedir}/libwacom-1.0/libwacom
%{_includedir}/libwacom-1.0/libwacom/libwacom.h
%{_libdir}/libwacom.so
%{_libdir}/pkgconfig/libwacom.pc

%files data
%defattr(-,root,root,-)
%doc COPYING
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%dir %{_datadir}/libwacom/layouts
%{_datadir}/libwacom/layouts/*.svg

%changelog
* Wed Mar 16 2016 Peter Hutterer <peter.hutterer@redhat.com> 0.16-2
- Add data file for the Expresskey Remote (#1318027)

* Fri Nov 13 2015 Peter Hutterer <peter.hutterer@redhat.com> 0.16-1
- libwacom 0.16 (#1250769)

* Thu Apr 24 2014 Adam Jackson <ajax@redhat.com> 0.8-1
- libwacom 0.8

* Thu Jun 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.5-5
- Add ISDv 0x90 description (#847427)

* Tue Sep 18 2012 Olivier Fourdan <ofourdan@redhat.com> 0.5-4
- Add Cintiq 22HD definition (#857073)

* Mon May 07 2012 Olivier Fourdan <ofourdan@redhat.com> 0.5-3
- Add generic eraser to Bamboo Pen & Touch in libwacom-0.5 (#817091)

* Wed May 02 2012 Olivier Fourdan <ofourdan@redhat.com> 0.5-2
- Fix generic stylus missing an eraser in libwacom-0.5 (#817091)

* Wed May 02 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.5-1
- libwacom 0.5 for bluetooth multiple matches (#817091)

* Wed Mar 28 2012 Olivier Fourdan <ofourdan@redhat.com> 0.3-8
- Update udev rule automatically from the libwacom database entries
- Update database for Bamboo Pen and Touch styli

* Wed Mar 28 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.3-7
- Update device database for Intuos, Graphire, Cintiq and DTU/DTF series

* Tue Mar 20 2012 Olivier Fourdan <ofourdan@redhat.com> 0.3-6
- Fix generated udev rule file (#804633)

* Thu Mar 08 2012 Olivier Fourdan <ofourdan@redhat.com> 0.3-5
- Mark data subpackage as noarch and make it a requirement for libwacom
- Use generated udev rule file to list only known devices from libwacom
  database

* Tue Mar 06 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.3-4
- libwacom-0.3-add-list-devices.patch: add API to list devices
- libwacom-0.3-add-udev-generator.patch: add a udev rules generater tool
- libwacom-0.3-add-bamboo-one.patch: add Bamboo One definition

* Tue Feb 21 2012 Peter Hutterer <peter.hutterer@redhat.com> 0.3-3
- Source is type .bz2, not .xz

* Tue Feb 21 2012 Olivier Fourdan <ofourdan@redhat.com> - 0.3-2
- Add udev rules to identify Wacom as tablets for libwacom

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 0.3-1
- Update to 0.3

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 0.2-1
- Update to 0.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.1-1
- Initial import (#768800)
