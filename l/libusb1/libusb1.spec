Summary: A library which allows userspace access to USB devices
Name: libusb1
Version: 1.0.9
Release: 0.7.rc1%{?dist}
Source0: libusb-1.0.9-rc1.tar.bz2
#Source0: http://downloads.sourceforge.net/libusb/libusb-%{version}.tar.bz2

Patch1: 0001-Correctly-handle-LIBUSB_TRANSFER_OVERFLOW-in-libusb_.patch
Patch2: 0002-linux-Fix-cancel_transfer-return-value-when-cancelli.patch
Patch3: 0003-Don-t-print-errors-when-cancel_transfer-fails-with-N.patch
Patch4: 0004-linux-Fix-handling-of-urb-status-codes.patch
Patch5: 0005-linux-Translate-linux-iso-pkt-status-codes-to-libusb.patch
# For rhbz#830751
Patch6: 0006-linux_usbfs-Add-support-for-the-new-get_capabilities.patch
Patch7: 0007-linux_usbfs-Avoid-unnecessary-splitting-of-bulk-tran.patch
# For rhbz#820205
Patch8: 0008-detach-kernel-driver-return-ERROR_NOT_FOUND-if-usbfs.patch
Patch9: 0009-linux_usbfs-Work-around-a-driver-binding-race-in-res.patch
# For rhbz#596815
Patch10: 0010-linux-Assume-usbfs-path-dev-bus-usb-when-using-UDEV.patch

License: LGPLv2+
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://libusb.wiki.sourceforge.net/Libusb1.0
ExcludeArch: s390 s390x
BuildRequires: doxygen

%description
This package provides a way for applications to access USB devices. Note that
this library is not compatible with the original libusb-0.1 series.

%package devel
Summary: Development files for libusb
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb1.

%package static
Summary: Static development files for libusb
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries to develop applications that use libusb1.

%prep
%setup -q -n libusb-1.0.8
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%configure
make CFLAGS="$RPM_OPT_FLAGS"
pushd doc
make docs
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Our snapshot reports itself as 1.0.8, change the pkg-config file version to
# 1.0.9 so that configure checks by apps who need the new 1.0.9 succeed
sed -i 's/1\.0\.8/1.0.9/' %{buildroot}/%{_libdir}/pkgconfig/libusb-1.0.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc doc/html examples/*.c
%{_libdir}/pkgconfig/libusb-1.0.pc
%{_includedir}/*
%{_libdir}/*.so

%files static
%defattr(-,root,root)
%{_libdir}/*.a

%changelog
* Thu Dec 17 2015 Hans de Goede <hdegoede@redhat.com> - 1.0.9-0.7.rc1
- Fix libusb_init failure on systems with 0 usb busses
- Resolves: rhbz#596815

* Wed Aug 22 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.9-0.6.rc1
- Don't split bulk transfers unnecessary
- Resolves: rhbz#830751
- Don't let disconnect_kernel_driver detach the usbfs driver
- Resolves: rhbz#820205

* Wed Mar 14 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.9-0.5.rc1
- Add some small error handling fixes
- Related: rhbz#758094

* Tue Jan 17 2012 Hans de Goede <hdegoede@redhat.com> - 1.0.9-0.4.rc1
- Fix previous changelog entry to refer to the right bug
- Related: rhbz#758094

* Wed Jan 11 2012 Marc-Andre Lureau <marcandre.lureau@redhat.com> 1.0.9-0.3.rc1
- update to 1.0.9rc1, sync with f16
- Resolves: rhbz#758094

* Mon Sep 28 2009 Jindrich Novy <jnovy@redhat.com> 1.0.3-1
- update to 1.0.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Jindrich Novy <jnovy@redhat.com> 1.0.2-1
- update to 1.0.2

* Wed May 13 2009 Jindrich Novy <jnovy@redhat.com> 1.0.1-1
- update to 1.0.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 - Bastien Nocera <bnocera@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Nov 21 2008 - Bastien Nocera <bnocera@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Tue Sep 23 2008 Jindrich Novy <jnovy@redhat.com> 0.9.3-0.1
- update to 0.9.3

* Sun Jul 06 2008 - Bastien Nocera <bnocera@redhat.com> - 0.9.1
- Update to 0.9.1

* Mon May 26 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.4
- update to official beta

* Thu May 23 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.3.gitbef33bb
- update comment on how the tarball was created
- use abbreviated git hash within package name to avoid conflicts
- add to %%description that libusb1 is incompatible with libsub-0.1

* Thu May 22 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.2.gitbef33bb
- add info on how the snapshot tarball was created

* Wed May 21 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.1.gitbef33bb
- use proper version to denote it is a git snapshot

* Thu May 15 2008 Jindrich Novy <jnovy@redhat.com> 0.9.0-0.1
- initial packaging
