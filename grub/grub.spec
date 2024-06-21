Name: grub
Version: 0.97
Release: 99%{?dist}
Epoch: 1
Summary: Grand Unified Boot Loader.
Group: System Environment/Base
License: GPLv2+

ExclusiveArch: i686 x86_64 ia64
BuildRequires: binutils >= 2.9.1.0.23, ncurses-devel, ncurses-static, texinfo
BuildRequires: autoconf /usr/lib/crt1.o automake
BuildRequires: gnu-efi >= 3.0e-9
BuildRequires: /usr/lib/libc.a
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires: mktemp
Requires: system-logos
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

URL: http://www.gnu.org/software/%{name}/
Source0: ftp://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

# This is from
# http://git.kernel.org/?p=boot/grub-fedora/grub-fedora.git;a=summary
Patch0: grub-fedora-9.patch
Patch1: grub-keystatus.patch

# Various bugfixes
# http://fedorapeople.org/~lkundrak/grub-fedora.git/
Patch2: 0001-Get-rid-of-usr-bin-cmp-dependency.patch
Patch3: 0002-Add-strspn-strcspn-and-strtok_r.patch
Patch4: 0003-Allow-passing-multiple-image-files-to-the-initrd-com.patch
Patch5: 0004-Obey-2.06-boot-protocol-s-cmdline_size.patch

Patch6: grub-0.97-printf_hex.patch
Patch7: grub-0.97-eficd.patch
Patch8: grub-0.97-xfs-buildfix.patch
Patch9: grub-0.97-efigraph-use-blt.patch
Patch10: grub-0.97-efislice.patch
Patch11: grub-0.97-efistatus.patch
Patch12: grub-0.97-fat-lowercase.patch
Patch13: grub-0.97-efipxe.patch
Patch14: grub-0.97-tolower.patch
Patch15: grub-low-memory.patch
Patch16: grub-install_virtio_blk_support.patch
Patch17: grub-fix-memory-corruption.patch
Patch18: grub-ext4-support.patch
Patch19: grub-0.97-xfs-writable-strings.patch
Patch20: grub-0.97-partitionable-md.patch
Patch21: grub-0.97-relocatable-kernel-on-x86_64-uefi.patch
Patch22: grub-0.97-use-gnuefi.patch
Patch23: grub-0.97-gate-a20.patch
Patch24: grub-0.97-efi-graphics-mode-selection.patch
Patch25: grub-silent.patch
Patch26: grub-0.97-invert-highlighted-menu-line-rhbz613153.patch
Patch27: grub-0.97-better-get-memory-map-rhbz607213.patch
Patch28: grub-0.97-add-strnchr.patch
Patch29: grub-0.97-efimap.patch
Patch30: grub-efi-large-memory-map.patch
Patch31: grub-0.97-devpath-parsing-error-rhbz626447.patch
Patch32: grub-0.97-bz553741-sha2.patch
Patch33: grub-0.97-support-4k-sector-size.patch
Patch34: grub-0.97-128-drives-support.patch
Patch35: grub-0.97-bz677468-properly-align-stack.patch
Patch36: grub-0.97-bz736833-cciss-no-partitionin.patch
Patch37: grub-0.97-bz746106-Accept-vendor-paths.patch
Patch38: grub-0.97-bz670266-find-active-pxe-handle.patch
Patch39: grub-0.97-bz670266-handle-bad-TFTP_GET_FILE_SIZE.patch
Patch40: grub-0.97-efipxeipv6.patch
Patch41: grub-0.97-bz814014-Scan-for-virtio-disks.patch
Patch42: grub-0.97-bz737732-Let-user-specify-efi-boot-disk-as-root.patch
Patch43: grub-0.97-bz825054-Pass-high-order-address-bits-to-EFI-maps.patch
Patch44: grub-0.97-bz870420-Do-not-resolve-symlinks-in-dev-mapper-dir.patch
Patch45: grub-0.97-bz876519-Check-if-pxe-Mode-is-not-NULL.patch
Patch46: 0001-Disable-the-watchdog-timer-on-EFI-platforms.patch
Patch47: 0002-Add-MACAPPEND-command.patch
Patch48: 0003-Retry-getting-memory-map-and-exit-boot-services-on-f.patch
Patch49: 0004-Fixed-regexps-for-matching-devices-in-device.map-and.patch
Patch50: 0005-Remove-grub.info-when-make-clean-is-called.patch
Patch51: 0006-If-the-title-is-too-long-print-remaining-seconds-on-.patch
Patch52: 0007-Recognize-virtio-blk-devices-when-running-on-OVMF.patch
Patch53: 0001-efi-allocate-size-of-struct-instead-of-size-of-point.patch
Patch54: 0001-grub-install-Add-support-for-NVMe-to-grub-install.patch
Patch55: 0008-grub-proper-graphics-initialization.patch
Patch56: 0009-grub-handle-uppercase-lowercase-command.patch
Patch57: 0010-grub-install-add-regex-for-partition-and-multipath-w.patch
Patch58: 0011-return-proper-disk-operation-status.patch
Patch59: 0012-efigraph-stick-with-default-GOP-mode-unless-resoluti.patch
Patch60: 0013-avoid-using-uefi-supplied-device-paths-on-CD.patch
Patch61: 0014-fix-booting-without-vga.patch
Patch62: 0015-Properly-expand-IPv6-address.patch
Patch63: 0016-Parse-MAC-address-from-various-packet-types.patch
Patch64: 0017-Fix-ext4-loading-ineffectiveness.patch
Patch65: 0018-Workaround-for-SGI-UV100-1000-UEFI-TFTP-read.patch
Patch66: 0019-grub-install-more-than-1-letter-in-device-name.patch

%description
GRUB (Grand Unified Boot Loader) is an experimental boot loader
capable of booting into most free operating systems - Linux, FreeBSD,
NetBSD, GNU Mach, and others as well as most commercial operating
systems.

%prep
%setup -q
%patch0 -p1
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
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1

%build
autoreconf
autoconf
GCCVERS=$(gcc --version | head -1 | cut -d\  -f3 | cut -d. -f1)
CFLAGS="-Os -g -fno-strict-aliasing -Wall -Werror -Wno-shadow -Wno-unused"
if [ "$GCCVERS" == "4" ]; then
	CFLAGS="$CFLAGS -Wno-pointer-sign"
fi
export CFLAGS
%configure --sbindir=/sbin --disable-auto-linux-mem-opt --datarootdir=%{_datadir} --with-platform=efi
make
mv efi/grub.efi .
make clean
autoreconf
autoconf
CFLAGS="$CFLAGS -static" 
export CFLAGS
%configure --sbindir=/sbin --disable-auto-linux-mem-opt --datarootdir=%{_datadir}
make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall sbindir=${RPM_BUILD_ROOT}/sbin
mkdir -p ${RPM_BUILD_ROOT}/boot/grub
mkdir -m 0755 -p ${RPM_BUILD_ROOT}/boot/efi/EFI/redhat/
install -m 755 grub.efi ${RPM_BUILD_ROOT}/boot/efi/EFI/redhat/grub.efi

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%clean
rm -fr $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/grub.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz || :
fi

%preun
if [ "$1" = 0 ] ;then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/grub.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz || :
fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README COPYING TODO docs/menu.lst
/boot/grub
%attr(0755,root,root)/boot/efi/EFI/redhat
/sbin/grub
/sbin/grub-install
/sbin/grub-terminfo
/sbin/grub-md5-crypt
/sbin/grub-crypt
%{_bindir}/mbchk
%{_infodir}/grub*
%{_infodir}/multiboot*
%{_mandir}/man*/*
%{_datadir}/grub

%changelog
* Wed Nov  9 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 0.97-99
- Workaround for SGI UV100/1000 hardware updated to be more intuitive
  Related: #1124862

* Mon Sep 26 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 0.97-98
- Workaround for SGI UV100/1000 hardware (TFTP transfers in UEFI mode) added
  Resolves: #1124862
- Allow more than 1 letter in device name when using the grub-install script
  Resolves: #1349389

* Mon Apr 11 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 1:0.97-97
- Patch from previous commit c445aac0ee30f has been removed, because it did not
  fix the issues with some SGI hardware. Bumping up the release number, so the
  building of grub package is not affected in the future. For more info see:

  Related: #1325860 (https://bugzilla.redhat.com/show_bug.cgi?id=1325860)

* Tue Feb 23 2016 David Kaspar [Dee'Kej] <dkaspar@redhat.com> - 1:0.97-95
- Fix the ineffectiveness when loading fragmented initramfs from Ext4 filesystem
  Resolves: #1006373

* Thu Apr 07 2015 Jan Grulich <jgrulich@redhat.com> - 1:0.97-94
- Properly expand IPv6 address
  Resolves: bz#1177321
- Support various types of DHCP IPv6 packet for MAC address extraction
  Resolves: bz#1206542

* Fri Aug 29 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-93
- Fix booting wihout VGA
  Resolves: rhbz#1131205

* Wed Aug 27 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-92
- Avoid using uefi-supplied device paths on CD devices
  Resolves: rhbz#1129466

* Thu Aug 14 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-91
- Suppress failure message on EFI systems when loading splashscreen
  Resolves: rhbz#1129436
- Return proper disk operation status
  Resolves: rhbz#1130209
- Stick with default GOP mode unless resolution is absurdly small
  Resolves: rhbz#1130313

* Tue Aug 12 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-90
- Fix graphics initialization for non EFI systems
  Resolves: rhbz#1128137

* Thu Aug 07 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-89
- Another round of fixes for rhbz#1002809

* Wed Jul 30 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-88
- Fix previous patch which didn't work as expected
  Resolves: rhbz#1002809

* Fri Jul 25 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-87
- Enable and fix previous patch for handling upper/lowercase commands
  Resolves: rhbz#1002809

* Wed Jul 23 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-86
- grub-install: add regex for partition and multipath when
  use_friendly_names is off
  Resolves: rhbz#1121321
- Disable previous patch as it doesn't work properly

* Tue Jun 10 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-85
- Handle upper/lowercase commands
  Resolves: rhbz#1002809

* Thu May 08 2014 Jan Grulich <jgrulich@redhat.com> - 1:0.97-84
- Proper graphics initialization
  Resolves: rhbz#1048681
  Resolves: rhbz#1074914
  Resolves: rhbz#1094978

* Tue Oct 15 2013 Václav Pavlín <vpavlin@redhat.com> - 1:0.97-83
- Allocate size of struct instead of size of pointer
  Resolves: rhbz#1008305
- Add support for NVMe to grub-install
  Resolves: rhbz#1017296

* Tue Jul 23 2013 Václav Pavlín <vpavlin@redhat.com> - 1:0.97-82
- Disable the watchdog timer on EFI platforms
  Resolves: rhbz#911715
- Add MACAPPEND command
  Resolves: rhbz#848628
- Retry getting memory map and exit boot services on fail
  Resolves: rhbz#918824
- Fixed regexps for matching devices in device.map and resolve symlinks
  when getting stats for block device
  Resolves: rhbz#928938
- Remove grub.info when make clean is called to be sure that it is
  recreated with all changes.
  Resolves: rhbz#854652
- Replace glibc-static with /usr/lib/libc.a in BuildRequires
  Resolves: rhbz#922705
- If the title is too long, print remaining seconds to the new line
  Resolves: rhbz#851706
- Recognize virtio-blk devices when running on OVMF
  Resolves: rhbz#916016

* Thu Dec 06 2012 Václav Pavlín <vpavlin@redhat.com> - 1:0.97-81
- Check if pxe->Mode is not NULL
  Resolves: rhbz#876519

* Wed Nov 21 2012 Václav Pavlín <vpavlin@redhat.com> - 1:0.97-80
- Do not resolve symlinks if the file is in /dev/mapper
  Resolves: rhbz#870420

* Tue Oct 09 2012 Václav Pavlín <vpavlin@redhat.com> - 1:0.97-79
- Scan for virtio disks
  Resolves: rhbz#814014
- Let user specify efi boot disk as root
  Resolves: rhbz#737732
- Pass hig order bits to EFI system map and memory map
  Resolves: rhbz#825054

* Fri Aug 24 2012 Neil Horman <nhorman@redhat.com> - 0.97-78
- Add support for UEFI pxe boot over ipv6 (bz 642396)

* Wed Feb 29 2012 Peter Jones <pjones@redhat.com> - 0.97-77
- Fix error handling problem from -76.
  Related: rhbz#670266

* Tue Feb 14 2012 Peter Jones <pjones@redhat.com> - 0.97-76
- [UEFI] Iterate PXE objects and try to find an active one instead
  of letting the firmware pick for us.
  Resolves: rhbz#670266
- [UEFI] Handle tftp implementations that give invalid error codes
  from TFTP_GET_FILE_SIZE.
  Related: rhbz#670266

* Tue Oct 18 2011 Peter Jones <pjones@redhat.com> - 0.97-75
- Treat "vendor specific" storage devices as hard disks.
  Resolves: rhbz#746106

* Wed Sep 28 2011 Peter Jones <pjones@redhat.com> - 0.97-74
- Fix error on invocation of "grub-install /dev/cciss/c0d0" (patch from jnevill)
  Resolves: rhbz#736833

* Tue Aug 16 2011 Peter Jones <pjones@redhat.com> - 0.97-73
- Properly align the stack when calling UEFI functions.
  Resolves: rhbz#677468

* Sun Aug 14 2011 Peter Jones <pjones@redhat.com> - 0.97-72
- Roll back -71 for now
- Allow booting from higher drive numbers
  Resolves: rhbz#671355

* Wed Feb 23 2011 Peter Jones <pjones@redhat.com> - 0.97-71
- Fix UEFI Call wrapper alignment problems (Patch from Stuart Hayes)
  Resolves: rhbz#677468

* Fri Jan 21 2011 Peter Jones <pjones@redhat.com> - 0.97-70
- Boot from disks with 4kB sectors on UEFI.
  Resolves: rhbz#654869

* Fri Jan 14 2011 Peter Jones <pjones@redhat.com> - 0.97-69
- Add sha2 support for passwords (patch from mitr)
  Resolves: rhbz#553741

* Mon Aug 30 2010 Peter Jones <pjones@redhat.com> - 0.97-68
- Fix for a parsing error in devpath feature
  Resolves: rhbz#626447

* Thu Aug 19 2010 Peter Jones <pjones@redhat.com> - 0.97-67
- When the EFI memory map is too large, copy the parts we can to e820
  Resolves: rhbz#624806

* Wed Aug 04 2010 Peter Jones <pjones@redhat.com> - 0.97-66
- Allow drive remaping in UEFI mode so ordering changes don't cause failure
  Resolves: rhbz#598572

* Mon Jul 12 2010 Peter Jones <pjones@redhat.com> - 0.97-65
- Draw the inverted line correctly in the menu
  Resolves: rhbz#613153
- Don't fail to boot on UEFI when the memory map changes (shayes)
  Resolves: rhbz#607213

* Tue Jan 05 2010 Peter Jones <pjones@redhat.com> - 0.97-64
- Propogate the fix for the version number mishap in the F-12 tree to here...

* Tue Jan 05 2010 Peter Jones <pjones@redhat.com> - 0.97-63
- Clear the screen when the timeout finishes, not just if verbose is set.
  Patch from Eelko Berkenpies.

* Mon Nov 16 2009 Peter Jones <pjones@redhat.com> - 0.97-62
- Fix release number mishap.

* Fri Nov 13 2009 Peter Jones <pjones@redhat.com> - 0.97-622
- Update relocatable kernel support for UEFI/x86_64 .
  Related: rhbz #476230
- grub-0.97-gate-a20.patch: Patch from Suse. Make really, really sure that
  A20 is behaving itself. (mjg)
- add "silent" option (mjg)
- Rework EFI Graphics Output Protocol mode selection.

* Fri Nov 13 2009 Peter Jones <pjones@redhat.com> - 0.97-61
- This was a mistake in CVS.

* Wed Sep 16 2009 Peter Jones <pjones@redhat.com> - 0.97-60
- Fix a typo introduced in grub-fedora-9.patch that may effect UEFI
  Graphics Output Protocol.

* Thu Aug 20 2009 Peter Jones <pjones@redhat.com> - 0.97-59
- Correctly link against gnuefi.

* Tue Aug 11 2009 Peter Jones <pjones@redhat.com> - 0.97-58
- Dynamically choose load address for bzimage on 64-bit UEFI.

* Mon Jul 27 2009 Hans de Goede <hdegoede@redhat.com> - 0.97-57
- Fix building with new rpm (with auto buildroot cleaning)
- Update Exclusive arch for F-12 i586 -> i686 change

* Mon Jul 27 2009 Hans de Goede <hdegoede@redhat.com> - 0.97-56
- Actually apply support for partitionable md devices patch (#503698)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Peter Jones <pjones@redhat.com> - 0.97-54
- Add support for partitionable md devices.

* Tue Jun 30 2009 Peter Jones <pjones@redhat.com> - 0.97-53
- Don't assume that gcc provides us with writable strings in the xfs driver

* Mon Jun 29 2009 Peter Jones <pjones@redhat.com> - 0.97-52
- Add ext4 support (#486284)

* Thu Jun 04 2009 Peter Jones <pjones@redhat.com> - 0.97-51
- Fix memory corruptor in "setup" command. (#496093)

* Wed Apr 29 2009 Peter Jones <pjones@redhat.com> - 0.97-50
- Handle virtio_blk disks and their crazy new device name in grub-install
  (rhbz#479760)

* Thu Apr 16 2009 Peter Jones <pjones@redhat.com> - 0.97-49
- Fix efi booting on machines with continguous memory regions across
  the 1G boundary.

* Thu Apr 09 2009 Peter Jones <pjones@redhat.com> - 0.97-48
- remove test message Re: using network drive or not.

* Tue Apr 07 2009 Peter Jones <pjones@redhat.com> - 0.97-47
- Add more filenames to the tftp config file search list
- Tweak FAT filename comparison...
- Vomit.

* Mon Apr 06 2009 Peter Jones <pjones@redhat.com> - 0.97-46
- Update gnu-efi buildreq.
- Fix up pxe code for i386

* Fri Apr 03 2009 Peter Jones <pjones@redhat.com> - 0.97-45
- Add very basic PXE support for EFI.

* Mon Mar 30 2009 Matthew Garrett <mjg@redhat.com> - 0.97-44
- Recognise the 0xef partition type

* Wed Mar 11 2009 Peter Jones <pjones@redhat.com> - 0.97-43
- Use blt operations instead of memmove() on Efi Graphics Protocol systems.

* Tue Mar 03 2009 Peter Jones <pjones@redhat.com> - 0.97-42
- Switch from i386 to i586.
- BuildReq on glibc-static.

* Mon Mar 02 2009 Peter Jones <pjones@redhat.com> - 0.97-41
- Fix CD Booting on EFI.
- Fix XFS build on x86_64.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Peter Jones <pjones@redhat.com> - 0.97-39
- Remove chainloader timeout patch; fixing it in booty instead in order to
  address rhbz#468526 .
- Fix up some style weirdness in the .spec 
- Require newer gnu-efi so it'll build with newer binutils.

* Sun Jan 11 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.97-37
- Get rid of /usr/bin/cmp dependency (Ville Skyttä, #431351)
- Support multiple initrds (Jeff Layton, #179127)
- Obey 2.06 boot protocol's cmdline_size (Lubomir Rintel, #327541)

* Wed Oct 22 2008 Peter Jones <pjones@redhat.com> - 0.97-36
- Add force-chainloader patch from rstrode (rhbz #458576)

* Tue Oct 07 2008 Peter Jones <pjones@redhat.com> - 0.97-35
- Add dep on newer gnu-efi.

* Wed Jun 25 2008 Peter Jones <pjones@redhat.com> - 0.97-34
- Add keystatus patch from krh.

* Mon Apr 07 2008 Peter Jones <pjones@redhat.com> - 0.97-33
- Rewrite ia32 efi call wrapper to make the makefile simpler.

* Tue Apr 01 2008 Peter Jones <pjones@redhat.com> - 0.97-32
- Add graphics debug mode
- Fix screen geometry variable passing
- Fix broken efi call wrapper on x86_64 so UGA works there.

* Thu Mar 20 2008 Peter Jones <pjones@redhat.com> - 0.97-31
- Fix efifb setup.

* Wed Mar 19 2008 Peter Jones <pjones@redhat.com> - 0.97-30
- Fix the bootloader for ANOTHER random kernel ABI change on EFI+x86_64.

* Tue Mar 18 2008 Peter Jones <pjones@redhat.com> - 0.97-29
- Remove all the prot_mode_mem code from EFI loader on x86_64.

* Thu Mar 06 2008 Peter Jones <pjones@redhat.com> - 0.97-28
- Fix FAT/VFAT directory searching.
- Don't artificially limit the kernel's location to lowmem.

* Wed Mar 05 2008 Peter Jones <pjones@redhat.com> - 0.97-27
- Fix permissions on grub.efi so cpio doesn't error when it's on vfat.

* Tue Mar 04 2008 Peter Jones <pjones@redhat.com> - 0.97-26
- Move grub.efi to a more useful location.

* Wed Feb 27 2008 Peter Jones <pjones@redhat.com> - 0.97-25
- Fix memory allocation bug in EFI on i386 and x86_64.

* Wed Feb 27 2008 Peter Jones <pjones@redhat.com> - 0.97-24
- Fix build of xfs code on amd64.

* Wed Feb 27 2008 Peter Jones <pjones@redhat.com> - 0.97-23
- Enable EFI on i386, update to newest git head.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.97-22
- Autorebuild for GCC 4.3

* Fri Jan 25 2008 Jesse Keating <jkeating@redhat.com> - 0.97-21
- Add a patch from esandeen to support booting from 256byte inodes.

* Mon Nov 05 2007 Peter Jones <pjones@redhat.com> - 0.97-20
- Add EFI support from Intel on x86_64

* Thu Sep 20 2007 Peter Jones <pjones@redhat.com> - 0.97-19
- Fix dmraid detection on Intel (isw) controllers in grub-install .

* Wed Aug 22 2007 Peter Jones <pjones@redhat.com> - 0.97-18
- Fix license tag.

* Mon Aug 20 2007 Peter Jones <pjones@redhat.com> - 0.97-17
- Use --build-id=none instead of stripping out the build-id notes in the
  first and second stage loaders.

* Tue Aug 7 2007 Peter Jones <pjones@redhat.com> - 0.97-16
- Add ext[23] large inode support (patch from Eric Sandeen)
- Fix auto* breakage that happened when we switched from autoreconf to autoconf
- Move to original tarball + patch generated from git

* Mon Jul 16 2007 Peter Jones <pjones@redhat.com> - 0.97-15
- Support booting from GPT

* Fri Feb 23 2007 Bill Nottingham <notting@redhat.com> - 0.97-14
- fix scriplet errors when installed with --nodocs
- coax grub into building (-ltinfo, autoconf instead of autoreconf)

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.97-13
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Peter Jones <pjones@redhat.com> - 0.97-12
- Reenable patch 505, which fixes #116311

* Tue Aug 15 2006 Peter Jones <pjones@redhat.com> - 0.97-11
- Disable patch 505 (#164497)

* Wed Aug  2 2006 Peter Jones <pjones@redhat.com> - 0.97-10
- Fix grub-install for multipath

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.97-9.1
- rebuild

* Fri Jul  7 2006 Peter Jones <pjones@redhat.com> - 0.97-9
- fix broken error reporting from helper functions

* Mon Jun 12 2006 Peter Jones <pjones@redhat.com> - 0.97-8
- Fix BIOS keyboard handler to use extended keyboard interrupts, so the
  Mac Mini works.

* Mon Jun  5 2006 Jesse Keating <jkeating@redhat.com> - 0.97-7
- Added BuildRequires on a 32bit library

* Sat May 27 2006 Peter Jones <pjones@redhat.com> - 0.97-6
- Fix mactel keyboard problems, patch from Juergen Keil, forwarded by Linus.

* Mon Mar 13 2006 Peter Jones <pjones@redhat.com> - 0.97-5
- Fix merge error for "bootonce" patch (broken in 0.95->0.97 update)
- Get rid of the 0.97 "default" stuff, since it conflicts with our working
  method.

* Thu Mar 09 2006 Peter Jones <pjones@redhat.com> - 0.97-4
- Fix running "install" multiple times on the same fs in the same invocation
  of grub.  (bz #158426 , patch from lxo@redhat.com)

* Mon Feb 13 2006 Peter Jones <pjones@redhat.com> - 0.97-3
- fix partition names on dmraid

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.97-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Peter Jones <pjones@redhat.com> - 0.97-2
- add dmraid support

* Wed Dec 14 2005 Peter Jones <pjones@redhat.com> - 0.97-1
- update to grub 0.97

* Mon Dec  5 2005 Peter Jones <pjones@redhat.com> - 0.95-17
- fix configure conftest.c bugs
- add -Wno-unused to defeat gcc41 "unused" checking when there are aliases.

* Mon Aug  1 2005 Peter Jones <pjones@redhat.com> - 0.95-16
- minor fix to the --recheck fix.

* Mon Jul 25 2005 Peter Jones <pjones@redhat.com> 0.95-15
- Make "grub-install --recheck" warn the user about how bad it is,
  and keep a backup file, which it reverts to upon detecting some errors.

* Wed Jul  6 2005 Peter Jones <pjones@redhat.com> 0.95-14
- Fix changelog to be UTF-8

* Thu May 19 2005 Peter Jones <pjones@redhat.com> 0.95-13
- Make the spec work with gcc3 and gcc4, so people can test on existing
  installations.
- don't treat i2o like a cciss device, since its partition names aren't done
  that way. (#158158)

* Wed Mar 16 2005 Peter Jones <pjones@redhat.com> 0.95-12
- Make installing on a partition work again when not using raid

* Thu Mar  3 2005 Peter Jones <pjones@redhat.com> 0.95-11
- Make it build with gcc4

* Sun Feb 20 2005 Peter Jones <pjones@redhat.com> 0.95-10
- Always install in MBR for raid1 /boot/

* Sun Feb 20 2005 Peter Jones <pjones@redhat.com> 0.95-9
- Always use full path for mdadm in grub-install

* Tue Feb  8 2005 Peter Jones <pjones@redhat.com> 0.95-8
- Mark the simulation stack executable
- Eliminate the use of inline functions in stage2/builtins.c

* Tue Jan 11 2005 Peter Jones <pjones@redhat.com> 0.95-7
- Make grub ignore everything before the XPM header in the splash image,
  fixing #143879
- If the boot splash image is missing, use console mode instead 
  of graphics mode.
- Don't print out errors using the graphics terminal code if we're not
  actually in graphics mode.

* Mon Jan  3 2005 Peter Jones <pjones@redhat.com> 0.95-6
- reworked much of how the RAID1 support in grub-install works.  This version
  does not require all the devices in the raid to be listed in device.map,
  as long as you specify a physical device or partition rather than an md
  device.  It should also work with a windows dual-boot on the first partition.

* Fri Dec 17 2004 Peter Jones <pjones@redhat.com> 0.95-5
- added support for RAID1 devices to grub-install, partly based on a
  patch from David Knierim. (#114690)

* Tue Nov 30 2004 Jeremy Katz <katzj@redhat.com> 0.95-4
- add patch from upstream CVS to handle sparse files on ext[23]
- make geometry detection a little bit more robust/correct
- use O_DIRECT when reading/writing from devices.  use aligned buffers as 
  needed for read/write (#125808)
- actually apply the i2o patch
- detect cciss/cpqarray devices better (#123249)

* Thu Sep 30 2004 Jeremy Katz <katzj@redhat.com> - 0.95-3
- don't act on the keypress for the menu (#134029)

* Mon Jun 28 2004 Jeremy Katz <katzj@redhat.com> - 0.95-2
- add patch from Nicholas Miell to make hiddenmenu work more 
  nicely with splashimage mode (#126764)

* Fri Jun 18 2004 Jeremy Katz <katzj@redhat.com> - 0.95-1
- update to 0.95
- drop emd patch, E-MD isn't making forward progress upstream
- fix static build for x86_64 (#121095)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  9 2004 Jeremy Katz <katzj@redhat.com>
- require system-logos (#120837)

* Fri Jun  4 2004 Jeremy Katz <katzj@redhat.com>
- buildrequire automake (#125326)

* Thu May 06 2004 Warren Togami <wtogami@redhat.com> - 0.94-5
- i2o patch from Markus Lidel

* Wed Apr 14 2004 Jeremy Katz <katzj@redhat.com> - 0.94-4
- read geometry off of the disk since HDIO_GETGEO doesn't actually 
  return correct data with a 2.6 kernel

* Fri Mar 12 2004 Jeremy Katz <katzj@redhat.com>
- add texinfo buildrequires (#118146)

* Wed Feb 25 2004 Jeremy Katz <katzj@redhat.com> 0.94-3
- don't use initrd_max_address

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 0.94-2
- rebuilt

* Thu Feb 12 2004 Jeremy Katz <katzj@redhat.com> 0.94-1
- update to 0.94, patch merging and updating as necessary

* Sat Jan  3 2004 Jeremy Katz <katzj@redhat.com> 0.93-8
- new bootonce patch from Padraig Brady so that you don't lose 
  the old default (#112775)

* Mon Nov 24 2003 Jeremy Katz <katzj@redhat.com>
- add ncurses-devel as a buildrequires (#110732)

* Tue Oct 14 2003 Jeremy Katz <katzj@redhat.com> 0.93-7
- rebuild

* Wed Jul  2 2003 Jeremy Katz <katzj@redhat.com> 
- Requires: /usr/bin/cmp (#98325)

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 0.93-6
- add patch from upstream to fix build with gcc 3.3

* Wed Apr  2 2003 Jeremy Katz <katzj@redhat.com> 0.93-5
- add patch to fix support for serial terminfo (#85595)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Jeremy Katz <katzj@redhat.com> 0.93-3
- add patch from HJ Lu to support large disks (#80980, #63848)
- add patch to make message when ending edit clearer (#53846)

* Sun Dec 29 2002 Jeremy Katz <katzj@redhat.com> 0.93-2
- add a patch to reset the terminal type to console before doing 'boot' from
  the command line (#61069)

* Sat Dec 28 2002 Jeremy Katz <katzj@redhat.com> 0.93-1
- update to 0.93
- update configfile patch
- graphics patch rework to fit in as a terminal type as present in 0.93
- use CFLAGS="-Os -g"
- patch configure.in to allow building if host_cpu=x86_64, include -m32 in
  CFLAGS if building on x86_64
- link glibc static on x86_64 to not require glibc32
- include multiboot info pages
- drop obsolete patches, reorder remaining patches into some semblance of order

* Thu Sep  5 2002 Jeremy Katz <katzj@redhat.com> 0.92-7
- splashscreen is in redhat-logos now

* Tue Sep  3 2002 Jeremy Katz <katzj@redhat.com> 0.92-6
- update splashscreen again

* Mon Sep  2 2002 Jeremy Katz <katzj@redhat.com> 0.92-5
- update splashscreen

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.92-4
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.92-3
- automated rebuild

* Fri May  3 2002 Jeremy Katz <katzj@redhat.com> 0.92-2
- add patch from Grant Edwards to make vga16 + serial happier (#63491)

* Wed May  1 2002 Jeremy Katz <katzj@redhat.com> 0.92-1
- update to 0.92
- back to autoreconf
- make it work with automake 1.6/autoconf 2.53
- use "-falign-jumps=1 -falign-loops=1 -falign-functions=1" instead of
  "-malign-jumps=1 -malign-loops=1 -malign-functions=1"	to not use 
  deprecated gcc options

* Tue Apr  9 2002 Jeremy Katz <katzj@redhat.com> 0.91-4
- new splash screen

* Fri Mar  8 2002 Jeremy Katz <katzj@redhat.com> 0.91-3
- include patch from Denis Kitzmen to fix typo causing several options to 
  never be defined (in upstream CVS)
- include patch from upstream CVS to make displaymem always use hex for 
  consistency
- add patch from GRUB mailing list from Keir Fraser to add a --once flag to
  savedefault function so that you can have the equivalent of lilo -R 
  functionality (use 'savedefault --default=N --once' from the grub shell)
- back to autoconf

* Sun Jan 27 2002 Jeremy Katz <katzj@redhat.com> 
- change to use $grubdir instead of /boot/grub in the symlink patch (#58771)

* Fri Jan 25 2002 Jeremy Katz <katzj@redhat.com> 0.91-2
- don't ifdef out the auto memory passing, use the configure flag instead
- add a patch so that grub respects mem= from the kernel command line when 
  deciding where to place the initrd (#52558)

* Mon Jan 21 2002 Jeremy Katz <katzj@redhat.com> 0.91-1
- update to 0.91 final
- add documentation on splashimage param (#51609)

* Wed Jan  2 2002 Jeremy Katz <katzj@redhat.com> 0.91-0.20020102cvs
- update to current CVS snapshot to fix some of the hangs on boot related
  to LBA probing (#57503, #55868, and others)

* Fri Dec 21 2001 Erik Troan <ewt@redhat.com> 0.90-14
- fixed append patch to not require arguments to begin with
- changed to autoreconf from autoconf

* Wed Oct 31 2001 Jeremy Katz <katzj@redhat.com> 0.90-13
- include additional patch from Erich to add sync calls in grub-install to 
  work around updated images not being synced to disk
- fix segfault in grub shell if 'password --md5' is used without specifying
  a password (#55008)

* Fri Oct 26 2001 Jeremy Katz <katzj@redhat.com> 0.90-12
- Include Erich Boleyn <erich@uruk.org>'s patch to disconnect from the 
  BIOS after APM operations.  Should fix #54375

* Wed Sep 12 2001 Erik Troan <ewt@redhat.com>
- added patch for 'a' option in grub boot menu

* Wed Sep  5 2001 Jeremy Katz <katzj@redhat.com> 0.90-11
- grub-install: if /boot/grub/grub.conf doesn't exist but /boot/grub/menu.lst 
  does, create a symlink

* Fri Aug 24 2001 Jeremy Katz <katzj@redhat.com>
- pull in patch from upstream CVS to fix md5crypt in grub shell (#52220)
- use mktemp in grub-install to avoid tmp races

* Fri Aug  3 2001 Jeremy Katz <katzj@redhat.com>
- link curses statically (#49519)

* Thu Aug  2 2001 Jeremy Katz <katzj@redhat.com>
- fix segfault with using the serial device before initialization (#50219)

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- add --copy-only flag to grub-install

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- copy files in grub-install prior to device probe

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- original images don't go in /boot and then grub-install does the right
  thing

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- fix the previous patch
- put the password prompt in the proper location

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- reset the screen when the countdown is cancelled so text will disappear 
  in vga16 mode

* Mon Jul 16 2001 Jeremy Katz <katzj@redhat.com>
- change configfile defaults to grub.conf

* Sun Jul 15 2001 Jeremy Katz <katzj@redhat.com>
- updated to grub 0.90 final

* Fri Jul  6 2001 Matt Wilson <msw@redhat.com>
- modifed splash screen to a nice shade of blue

* Tue Jul  3 2001 Matt Wilson <msw@redhat.com>
- added a first cut at a splash screen

* Sun Jul  1 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix datadir mismatch between build and install phases

* Mon Jun 25 2001 Jeremy Katz <katzj@redhat.com>
- update to current CVS 
- forward port VGA16 patch from Paulo César Pereira de 
  Andrade <pcpa@conectiva.com.br>
- add patch for cciss, ida, and rd raid controllers
- don't pass mem= to the kernel

* Wed May 23 2001 Erik Troan <ewt@redhat.com>
- initial build for Red Hat
