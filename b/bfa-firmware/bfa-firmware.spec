Name:		bfa-firmware
Summary:	Brocade Fibre Channel HBA Firmware
Version:	3.2.23.0
Release:	2%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
Source0:	LICENSE
# These files were taken from:
# http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
# No direct link is available.
Source1:	bfa_firmware_linux-3.0.0.0-0.tgz
Source2:	bfa_firmware_linux-3.0.3.1-0.tgz
Source3:	bfa_fw_update_to_v3.1.2.1.tgz
Source4:	bfa_fw_update_to_v3.2.21.1.tgz
Source5:	bfa_fw_update_to_v3.2.1.1.tgz
Source6:	firmware_3.2.23.0.tgz
URL:		http://www.brocade.com/sites/dotcom/services-support/drivers-downloads/CNA/Linux.page
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
# Needed for /lib/firmware
Requires:	udev

%description
Brocade Fibre Channel HBA Firmware.

%prep
unpack_bfa_firmware() {
	filename=$1
	version=$2
	dir=$3
	installversion=${4:-$version}

	tar xvf $1
	pushd $3
	for i in cbfw ctfw ct2fw; do
		if [ -f $i.bin ]; then
			mv $i.bin $i-$installversion.bin;
		elif [ "$installversion" != "$version" ]; then
			mv $i-$version.bin $i-$installversion.bin
		fi
	done
	popd
}

unpack_bfa_firmware %{SOURCE6} 3.2.3.0 .
unpack_bfa_firmware %{SOURCE5} 3.2.1.1 bfa_fw_update_to_v3.2.1.1
unpack_bfa_firmware %{SOURCE4} 3.2.1.0 bfa_fw_update_to_v3.2.21.1
unpack_bfa_firmware %{SOURCE3} 3.1.0.0 bfa_fw_v3.1.2.1
unpack_bfa_firmware %{SOURCE2} 3.0.3.1 .
unpack_bfa_firmware %{SOURCE1} 3.0.0.0 3.0_GA_firwmare_image

%build
# Firmware, do nothing.

%install
install_bfa_firmware() {
	ver=$1
	dir=$2

	pushd $dir
	install -m0644 cbfw-$ver.bin ct2fw-$ver.bin ctfw-$ver.bin %{buildroot}/lib/firmware/
	popd
}

link_bfa_firmware() {
	dstver=$2
	srcver=$1

	pushd %{buildroot}/lib/firmware/
		ln -s cbfw$srcver.bin cbfw$dstver.bin
		ln -s ct2fw$srcver.bin ct2fw$dstver.bin
		ln -s ctfw$srcver.bin ctfw$dstver.bin
	popd
}

mkdir -p %{buildroot}/lib/firmware/

install_bfa_firmware 3.2.3.0 .
install_bfa_firmware 3.2.1.1 bfa_fw_update_to_v3.2.1.1
install_bfa_firmware 3.2.1.0 bfa_fw_update_to_v3.2.21.1
install_bfa_firmware 3.1.0.0 bfa_fw_v3.1.2.1
install_bfa_firmware 3.0.3.1 .

# RHEL 6.3 uses unversioned filenames
# RHEL 6.4 starting with 3.0.3.1 uses versioned filenames
%if 0%{?rhel}
	install_bfa_firmware 3.0.0.0 3.0_GA_firwmare_image
	link_bfa_firmware "-3.0.0.0"
%else
# Upstream starting with 3.1.0.0 uses versioned filenames
#  so link the old version to the old names as expected
	link_bfa_firmware "-3.0.3.1"
%endif

install -m 644 -D %{SOURCE0} $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/LICENSE

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/doc/%{name}-%{version}/LICENSE
/lib/firmware/cbfw.bin
/lib/firmware/ctfw.bin
/lib/firmware/ct2fw.bin
/lib/firmware/cbfw-3.2.3.0.bin
/lib/firmware/ctfw-3.2.3.0.bin
/lib/firmware/ct2fw-3.2.3.0.bin
/lib/firmware/cbfw-3.2.1.1.bin
/lib/firmware/ctfw-3.2.1.1.bin
/lib/firmware/ct2fw-3.2.1.1.bin
/lib/firmware/cbfw-3.2.1.0.bin
/lib/firmware/ctfw-3.2.1.0.bin
/lib/firmware/ct2fw-3.2.1.0.bin
/lib/firmware/cbfw-3.1.0.0.bin
/lib/firmware/ctfw-3.1.0.0.bin
/lib/firmware/ct2fw-3.1.0.0.bin
/lib/firmware/cbfw-3.0.3.1.bin
/lib/firmware/ctfw-3.0.3.1.bin
/lib/firmware/ct2fw-3.0.3.1.bin
%if 0%{?rhel}
/lib/firmware/cbfw-3.0.0.0.bin
/lib/firmware/ctfw-3.0.0.0.bin
/lib/firmware/ct2fw-3.0.0.0.bin
%endif

%changelog
* Fri May 23 2014 Kyle McMartin <kmcmarti@redhat.com> - 3.2.23.0-2
- fix LICENSE permissions.

* Fri May 23 2014 Kyle McMartin <kmcmarti@redhat.com> - 3.2.23.0-1
- update to 3.2.3.0
  Resolves: rhbz#1054467

* Fri Sep 27 2013 Kyle McMartin <kmcmarti@redhat.com> - 3.2.21.1-2
- update to 3.2.1.1
  Resolves: rhbz#1002770

* Tue May 21 2013 Kyle McMartin <kmcmarti@redhat.com> - 3.2.21.1-1
- update to 3.2.21.1, linked to 3.2.1.0 based on Brocade's submission
  for 3.11 ( http://marc.info/?l=linux-scsi&m=136843872927453&w=2 )
  Resolves: rhbz#928990

* Fri Jan 11 2013 Kyle McMartin <kmcmarti@redhat.com> 3.1.2.1-1
- update to 3.1.2.1
- add some shell functions to make life easier for multi-versioned firmware
  filenames that are now upstream

* Thu Sep  6 2012 Tom Callaway <spot@fedoraproject.org> 3.0.3.1-1
- update to 3.0.3.1

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 07 2011 Tom Callaway <spot@fedoraproject.org> 3.0.0.0-1
- update to 3.0.0.0

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Tom Callaway <spot@fedoraproject.org> 2.3.2.3-1
- update to 2.3.2.3

* Mon Mar  8 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-2
- Add missing Requires: udev

* Fri Jan 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.2.1-1
- Initial package for Fedora
