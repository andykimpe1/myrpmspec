Name:           libevdev
Version:        1.4.5
Release:        2%{?dist}
Summary:        Kernel Evdev Device Wrapper Library

Group:          System Environment/Libraries
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libevdev
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz

Patch01:        0001-tools-fix-coverty-may-be-used-uninitialized-warnings.patch
Patch02:        0002-tools-shut-up-coverity-about-a-potential-close-1.patch
Patch03:        0003-uinput-fix-race-condition-in-uinput-syspath-check.patch

BuildRequires:  automake libtool
BuildRequires:  python

%description
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package devel
Summary:        Kernel Evdev Device Wrapper Library Development Package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Kernel Evdev Device Wrapper Library Development Package.

%package utils
Summary:        Kernel Evdev Device Wrapper Library Utilities Package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities to handle and/or debug evdev devices.

%prep
%setup -q -n %{name}-%{version}
%patch01 -p1
%patch02 -p1
%patch03 -p1

%build
autoreconf --force -v --install || exit 1
%configure --disable-static --disable-silent-rules --disable-gcov
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# We intentionally don't ship *.la files
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING 
%{_libdir}/libevdev.so.*

%files devel
%dir %{_includedir}/libevdev-1.0/
%dir %{_includedir}/libevdev-1.0/libevdev
%{_includedir}/libevdev-1.0/libevdev/libevdev.h
%{_includedir}/libevdev-1.0/libevdev/libevdev-uinput.h
%{_libdir}/libevdev.so
%{_libdir}/pkgconfig/libevdev.pc
%{_mandir}/man3/libevdev.3*

%files utils
%{_bindir}/touchpad-edge-detector
%{_bindir}/mouse-dpi-tool
%{_bindir}/libevdev-tweak-device

%changelog
* Tue Dec 22 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4.5-2
- Fix coverity warnings
- Fix a potential race condition when checking uinput device's syspath

* Wed Nov 11 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4.5-1
- libevdev 1.4.5

* Tue Sep 01 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4.4-1
- libevdev 1.4.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4.2-1
- libevdev 1.4.2

* Wed Apr 08 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4.1-1
- libevdev 1.4.1

* Wed Mar 04 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.4-1
- libevdev 1.4

* Fri Dec 05 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.3.2-1
- libevdev 1.3.2

* Thu Nov 13 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.3.1-1
- libevdev 1.3.1

* Tue Sep 09 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.3-1
- libevdev 1.3

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.99.901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.2.99.901-1
- libevdev 1.3RC1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jun 05 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.2.2-1
- libevdev 1.2.2

* Wed May 14 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.2.1-1
- libevdev 1.2.1

* Tue May 13 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.2-5
- Bump release to fix the upgrade path from F20 which is now named
  1.2-04compat.

* Wed Apr 30 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.2-1
- libevdev 1.2

* Thu Apr 24 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.1.99.1-1
- libevdev 1.2 RC1

* Tue Mar 25 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.1-1
- libevdev 1.1

* Wed Mar 19 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.0.99.2-1
- libevdev 1.0.99.2

* Tue Mar 11 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.0.99.1-1
- libevdev 1.0.99.1
- Add libevdev-utils sub-package

* Fri Mar 07 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.0.1-1
- libevdev 1.0.1

* Tue Feb 18 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.0-1
- libevdev 1.0

* Wed Feb 05 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.9.1-1
- libevdev 1.0RC1

* Fri Jan 03 2014 Peter Hutterer <peter.hutterer@redhat.com> 0.6-3
- Restore deprecated constants LIBEVDEV_READ_* dropped from 0.6 (#1046426)

* Thu Dec 26 2013 Adam Williamson <awilliam@redhat.com> 0.6-2
- revert catastrophic upstream dropping of 'deprecated' functions - #1046426

* Mon Dec 23 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.6-1
- libevdev 0.6

* Fri Nov 22 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.5-1
- libevdev 0.5

* Fri Nov 01 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.4.1-1
- libevdev 0.4.1

* Wed Oct 02 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.4-2
- disable gcov (#1012180)
- disable unittests, we don't run them anyway

* Wed Sep 18 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.4-1
- libevdev 0.4

* Tue Aug 13 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.3-1
- libevdev 0.3

* Thu Jul 25 2013 Peter Hutterer <peter.hutterer@redhat.com> 0.2.1-1
- Initial package (#987204)

