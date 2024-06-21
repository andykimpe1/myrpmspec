# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python_sitearch}/.*\.so$
%filter_setup
}

Summary: HP Linux Imaging and Printing Project
Name: hplip
Version: 3.14.6
Release: 4%{?dist}.1
License: GPLv2+ and MIT
Group: System Environment/Daemons
Conflicts: system-config-printer < 0.6.132
Obsoletes: hpoj <= 0.91
Obsoletes: xojpanel <= 0.91

Url: http://hplip.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/hplip/hplip-%{version}.tar.gz
Source1: hpcups-update-ppds.sh
Source2: copy-deviceids.py
Patch1: hplip-pstotiff-is-rubbish.patch
Patch2: hplip-strstr-const.patch
Patch3: hplip-ui-optional.patch
Patch4: hplip-no-asm.patch
Patch5: hplip-deviceIDs-drv.patch
Patch6: hplip-udev-rules.patch
Patch7: hplip-retry-open.patch
Patch8: hplip-snmp-quirks.patch
Patch9: hplip-hpijs-marker-supply.patch
Patch10: hplip-clear-old-state-reasons.patch
Patch11: hplip-hpcups-sigpipe.patch
Patch12: hplip-logdir.patch
Patch13: hplip-bad-low-ink-warning.patch
Patch14: hplip-deviceIDs-ppd.patch
Patch15: hplip-ppd-ImageableArea.patch
Patch16: hplip-scan-tmp.patch
Patch17: hplip-codec.patch
Patch18: hplip-log-stderr.patch
Patch19: hplip-avahi-parsing.patch
Patch20: hplip-reportlab.patch
Patch21: hplip-uninit.patch
Patch22: hplip-device_open.patch
Patch23: hplip-strncpy.patch
Patch24: hplip-do-not-crash-on-usb-failure.patch

%define hpijs_epoch 1
Requires: hpijs%{?_isa} = %{hpijs_epoch}:%{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python-imaging
Requires: cups
Requires: wget
Requires: dbus-python
Requires: gnupg

BuildRequires: net-snmp-devel
BuildRequires: cups-devel
BuildRequires: python-devel
BuildRequires: libjpeg-devel
BuildRequires: desktop-file-utils
BuildRequires: libusb1-devel
BuildRequires: openssl-devel
BuildRequires: sane-backends-devel
BuildRequires: pkgconfig(dbus-1)

%description
The Hewlett-Packard Linux Imaging and Printing Project provides
drivers for HP printers and multi-function peripherals.

%package common
Summary: Files needed by the HPLIP printer and scanner drivers
Group: System Environment/Libraries
License: GPLv2+
Requires: udev

%description common
Files needed by the HPLIP printer and scanner drivers.

%package libs
Summary: HPLIP libraries
Group: System Environment/Libraries
License: GPLv2+ and MIT
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: python

%description libs
Libraries needed by HPLIP.

%package gui
Summary: HPLIP graphical tools
Group: Applications/System
License: BSD
Requires: PyQt4
Requires: python-reportlab
Requires: pygobject2
Requires(post): desktop-file-utils >= 0.2.92
Requires(postun): desktop-file-utils >= 0.2.92
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libsane-hpaio%{?_isa} = %{version}-%{release}

%description gui
HPLIP graphical tools.

%package -n hpijs
Summary: HP Printer Drivers
Group: Applications/Publishing
License: BSD
Epoch: %{hpijs_epoch}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: cups >= 1:1.4

%description -n hpijs
hpijs is a collection of optimized drivers for HP printers.
hpijs supports the DeskJet 350C, 600C, 600C Photo, 630C, Apollo 2000,
Apollo 2100, Apollo 2560, DeskJet 800C, DeskJet 825, DeskJet 900,
PhotoSmart, DeskJet 990C, and PhotoSmart 100 series.

%package -n libsane-hpaio
Summary: SANE driver for scanners in HP's multi-function devices
Group: System Environment/Daemons
License: GPLv2+
Obsoletes: libsane-hpoj <= 0.91
Requires: sane-backends
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
ExcludeArch: s390 s390x

%description -n libsane-hpaio
SANE driver for scanners in HP's multi-function devices (from HPOJ).

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
%setup -q

# The pstotiff filter is rubbish so replace it (launchpad #528394).
%patch1 -p1 -b .pstotiff-is-rubbish

# Fix compilation.
%patch2 -p1 -b .strstr-const

# Make utils.checkPyQtImport() look for the gui sub-package (bug #243273).
%patch3 -p1 -b .ui-optional

# Make sure to avoid handwritten asm.
%patch4 -p1 -b .no-asm

# Corrected several IEEE 1284 Device IDs using foomatic data.
# Color LaserJet CM1312nfi (bug #581005)
# Color LaserJet 3800 (bug #581935)
# Color LaserJet 2840 (bug #582215)
# Color LaserJet CP1518ni (bug #613689)
# Color LaserJet 2600n (bug #613712)
# Color LaserJet 2500/3700/4550/4600/4650/4700/5550/CP1515n/CP2025n
#                CP3525/CP4520 Series/CM2320nf (bug #659040)
# Color LaserJet CP2025dn (bug #651509)
# Color LaserJet CM4730 MFP (bug #658831)
# Color LaserJet CM3530 MFP (bug #659381)
# LaserJet 4050 Series/4100 Series/2100 Series/4350/5100 Series/8000 Series
#          P3005/P3010 Series/P4014/P4515 (bug #659039)
# LaserJet Professional P1606dn (bug #708472)
# LaserJet Professional M1212nf MFP (bug #742490)
# LaserJet M1536dnf MFP (bug #743915)
# LaserJet M1522nf MFP (bug #745498)
# LaserJet M1319f MFP (bug #746614)
# LaserJet M1120 MFP (bug #754139)
# LaserJet P1007 (bug #585272)
# LaserJet P1505 (bug #680951)
# LaserJet P2035 (Ubuntu #917703)
# PSC 1600 series (bug #743821)
# Officejet 6300 series (bug #689378)
# LaserJet Professional P1102w (bug #795958)
# Color LaserJet CM4540 MFP (bug #968177)
# Color LaserJet cp4005 (bug #980976)
%patch5 -p1 -b .deviceIDs-drv
chmod +x %{SOURCE2}
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%{SOURCE2} prnt/drv/hpcups.drv.in \
           prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
           > prnt/drv/hpijs.drv.in

# Don't add printer queue, just check plugin.
# Move udev rules from /etc/ to /usr/lib/ (bug #748208).
%patch6 -p1 -b .udev-rules

# Retry when connecting to device fails (bug #532112).
%patch7 -p1 -b .retry-open

# Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #581825).
%patch8 -p1 -b .snmp-quirks

# Fixed bogus low ink warnings from hpijs driver (bug #643643).
%patch9 -p1 -b .hpijs-marker-supply

# Clear old printer-state-reasons we used to manage (bug #510926).
%patch10 -p1 -b .clear-old-state-reasons

# Avoid busy loop in hpcups when backend has exited (bug #525944).
%patch11 -p1 -b .hpcups-sigpipe

# CUPS filters should use TMPDIR when available (bug #865603).
%patch12 -p1 -b .logdir

# Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).
%patch13 -p1 -b .bad-low-ink-warning

# Add Device ID for
# LaserJet 1200 (bug #577308)
# LaserJet 1320 series (bug #579920)
# LaserJet 2300 (bug #576928)
# LaserJet P2015 Series (bug #580231)
# LaserJet 4250 (bug #585499)
# Color LaserJet 2605dn (bug #583953)
# Color LaserJet 3800 (bug #581935)
# Color LaserJet 2840 (bug #582215)
# LaserJet 4050 Series/4100 Series/2100 Series/2420/4200/4300/4350/5100 Series
#          8000 Series/M3027 MFP/M3035 MFP/P3005/P3010 Series (bug #659039)
# Color LaserJet 2500/2550/2605dn/3700/4550/4600
#                4650/4700/5550/CP3525 (bug #659040)
# Color LaserJet CM4730 MFP (bug #658831)
# Color LaserJet CM3530 MFP (bug #659381)
# Designjet T770 (bug #747957)
# Color LaserJet CM4540 MFP (bug #968177)
# Color LaserJet cp4005 (bug #980976)
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch14 -p1 -b .deviceIDs-ppd
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Fix ImageableArea for Laserjet 8150/9000 (bug #596298).
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch15 -p1 -b .ImageableArea
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Scan to /var/tmp instead of /tmp (bug #1076954).
%patch16 -p1 -b .scan-tmp

# Fixed codec issue (bug #984167).
%patch17 -p1 -b .codec

# Treat logging before importing of logger module (bug #984699).
%patch18 -p1 -b .log-stderr

# Fix parsing of avahi-daemon output (bug #1096939).
%patch19 -p1 -b .parsing

# Fixed version comparisons for x.y.z-style versions such as
# reportlab (bug #1121433).
%patch20 -p1 -b .reportlab

# Fixed use of uninitialized value (bug #876066).
%patch21 -p1 -b .uninit

# Fixed incorrect name in function call in makeURI when a parallel
# port device is used (bug #1159161).
%patch22 -p1 -b .device_open

# Fixed uses of strncpy throughout.
%patch23 -p1 -b .strncpy

# hp/hpfax backends crash when no USB is available (bug#1297095).
%patch24 -p1 -b .hplip-usb-no-crash

sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in

# Change shebang /usr/bin/env python -> /usr/bin/python (bug #618351).
find -name '*.py' -print0 | xargs -0 \
    sed -i.env-python -e 's,^#!/usr/bin/env python,#!/usr/bin/python,'

%build
%configure \
        --enable-scan-build --enable-gui-build --enable-fax-build \
        --disable-foomatic-rip-hplip-install --enable-pp-build \
        --enable-qt4 --enable-hpcups-install --enable-cups-drv-install \
        --enable-foomatic-drv-install \
        --enable-hpijs-install \
        --disable-policykit --with-mimedir=%{_datadir}/cups/mime

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot}

# Remove unpackaged files
rm -rf  %{buildroot}%{_sysconfdir}/sane.d \
        %{buildroot}%{_docdir} \
        %{buildroot}%{_datadir}/hal/fdi \
        %{buildroot}%{_datadir}/hplip/pkservice.py \
        %{buildroot}%{_bindir}/hp-pkservice

rm -f   %{buildroot}%{_bindir}/foomatic-rip \
        %{buildroot}%{_libdir}/cups/filter/foomatic-rip \
        %{buildroot}%{_libdir}/*.la \
        %{buildroot}%{python_sitearch}/*.la \
        %{buildroot}%{_libdir}/libhpip.so \
        %{buildroot}%{_libdir}/sane/*.la \
        %{buildroot}%{_datadir}/cups/model/foomatic-ppds \
        %{buildroot}%{_datadir}/applications/hplip.desktop \
        %{buildroot}%{_datadir}/ppd/HP/*.ppd

mkdir -p %{buildroot}%{_datadir}/applications
sed -i -e '/^Categories=/d' hplip.desktop
# Encoding key is deprecated
sed -i -e '/^Encoding=/d' hplip.desktop
desktop-file-install --vendor HP                                \
        --dir %{buildroot}%{_datadir}/applications              \
        --add-category System                                   \
        --add-category Settings                                 \
        --add-category HardwareSettings                         \
        hplip.desktop

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/hpcups-update-ppds

%{__mkdir_p} %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Images in docdir should not be executable (bug #440552).
find doc/images -type f -exec chmod 644 {} \;

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
%{__mkdir_p} %{buildroot}%{_datadir}/hplip/prnt/plugins

# Remove files we don't want to package.
rm -f %{buildroot}%{_datadir}/hplip/hpaio.desc
rm -f %{buildroot}%{_datadir}/hplip/hplip-install
rm -rf %{buildroot}%{_datadir}/hplip/install.*
rm -f %{buildroot}%{_datadir}/hplip/uninstall.*
rm -f %{buildroot}%{_bindir}/hp-uninstall
rm -f %{buildroot}%{_datadir}/hplip/upgrade.*
rm -f %{buildroot}%{_bindir}/hp-upgrade
rm -f %{buildroot}%{_bindir}/hp-config_usb_printer
rm -f %{buildroot}%{_unitdir}/hplip-printer@.service
rm -f %{buildroot}%{_datadir}/hplip/config_usb_printer.*
rm -f %{buildroot}%{_datadir}/hplip/hpijs.drv.in.template
rm -f %{buildroot}%{_datadir}/cups/mime/pstotiff.types
rm -f %{buildroot}%{_datadir}/hplip/fax/pstotiff*

# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop

# Don't include systemd service.
rm -f %{buildroot}/usr/lib/systemd/system/hplip-printer@.service

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING doc/*
%{_bindir}/hp-align
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-faxsetup
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-logcapture
%{_bindir}/hp-makecopies
%{_bindir}/hp-makeuri
%{_bindir}/hp-plugin
%{_bindir}/hp-pqdiag
%{_bindir}/hp-printsettings
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-unload
%{_bindir}/hp-wificonfig
# Note: this must be /usr/lib not %%{_libdir}, since that's the
# CUPS serverbin directory.
/usr/lib/cups/backend/hp
/usr/lib/cups/backend/hpfax
/usr/lib/cups/filter/pstotiff
%{_datadir}/cups/mime/pstotiff.convs
# Files
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/logcapture.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/pqdiag.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%{_datadir}/hplip/scan.py*
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
%{_datadir}/hplip/wificonfig.py*
# Directories
%{_datadir}/hplip/base
%{_datadir}/hplip/copier
%{_datadir}/hplip/data/ldl
%{_datadir}/hplip/data/localization
%{_datadir}/hplip/data/pcl
%{_datadir}/hplip/data/ps
%{_datadir}/hplip/installer
%{_datadir}/hplip/pcard
%{_datadir}/hplip/prnt
%{_datadir}/hplip/scan
%{_localstatedir}/lib/hp

%files common
%defattr(-,root,root,-)
%doc COPYING
/lib/udev/rules.d/*.rules
%dir %{_sysconfdir}/hp
%config(noreplace) %{_sysconfdir}/hp/hplip.conf
%dir %{_datadir}/hplip
%dir %{_datadir}/hplip/data
%{_datadir}/hplip/data/models

%files libs
%defattr(-,root,root)
%{_libdir}/libhpip.so.*
# The so symlink is required here (see bug #489059).
%{_libdir}/libhpmud.so*
# Python extension
%{python_sitearch}/*

%files gui
%defattr(-,root,root,-)
%{_bindir}/hp-check
%{_bindir}/hp-doctor
%{_bindir}/hp-print
%{_bindir}/hp-systray
%{_bindir}/hp-toolbox
%{_datadir}/applications/*.desktop
# Files
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/doctor.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/systray.py*
%{_datadir}/hplip/toolbox.py*
# Directories
%{_datadir}/hplip/data/images
%{_datadir}/hplip/ui4

%files -n hpijs
%defattr(-,root,root)
%{_bindir}/hpijs
%{_bindir}/hpcups-update-ppds
%dir %{_datadir}/ppd/HP
%{_datadir}/ppd/HP/*.ppd.gz
%{_datadir}/cups/drv/*
# Note: this must be /usr/lib not %%{_libdir}, since that's the
# CUPS serverbin directory.
/usr/lib/cups/filter/hpcups
/usr/lib/cups/filter/hpcupsfax
/usr/lib/cups/filter/hpps

%files -n libsane-hpaio
%defattr(-,root,root)
%{_libdir}/sane/libsane-*.so*
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/hpaio

%post gui
/usr/bin/update-desktop-database &>/dev/null ||:

%postun gui
/usr/bin/update-desktop-database &>/dev/null ||:

%post -n hpijs
%{_bindir}/hpcups-update-ppds &>/dev/null ||:

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%changelog
* Wed May 18 2016 Jiri Popelka <jpopelka@redhat.com> - 3.14.6-4.1
- rebuilt

* Wed May 18 2016 Jiri Popelka <jpopelka@redhat.com> - 3.14.6-4
- hp/hpfax backends crash when no USB is available (bug #1297095).

* Wed Jan 21 2015 Tim Waugh <twugh@redhat.com> 3.14.6-3
- Fixes from Fedora:
  - Fixed incorrect name in function call in makeURI when a parallel
    port device is used (bug #1159161).
  - Fixed uses of strncpy throughout.

* Wed Jan 21 2015 Tim Waugh <twugh@redhat.com> 3.14.6-2
- Fixes from re-base:
  - restore update-desktop-database scriptlets
  - no need to ship /run/hplip

* Wed Jan 21 2015 Tim Waugh <twugh@redhat.com> 3.14.6-1
- Re-based to 3.14.6 (bug #1077121, bug #682814).
- Fixed use of uninitialized value (bug #876066).

* Mon Apr  7 2014 Tim Waugh <twugh@redhat.com> 3.12.4-6
- Move udev rules to /lib/udev/rules.d (bug #905143).

* Thu Sep 12 2013 Tim Waugh <twaugh@redhat.com> - 3.12.4-5
- Applied patch to avoid unix-process authorization subject when using
  polkit as it is racy (CVE-2013-4325).

* Tue Jan 22 2013 Tim Waugh <twaugh@redhat.com> - 3.12.4-4
- Applied patch to fix CVE-2013-0200, temporary file vulnerability
  (bug #902163).
- Fixed hpijs-marker-supply patch.

* Thu Nov 22 2012 Tim Waugh <twaugh@redhat.com> - 3.12.4-3
- Make 'hp-check' check for hpaio set-up correctly (bug #683007).

* Fri Aug 24 2012 Tim Waugh <twaugh@redhat.com> - 3.12.4-2
- Added more fixes from Fedora (bug #731900).

* Thu Aug 23 2012 Tim Waugh <twaugh@redhat.com> - 3.12.4-1
- Re-based to 3.12.4 with fixes from Fedora (bug #731900).  No longer
  need no-system-tray, openPPD, addgroup, emit-SIGNAL, fab-root-crash,
  newline, hpaio-segfault, dbus-threads, or cups-web patches.

* Thu Aug 23 2012 Tim Waugh <twaugh@redhat.com> - 3.10.9-4
- The hpijs sub-package no longer requires cupsddk-drivers (which no
  longer exists as a real package), but cups >= 1.4 (bug #829453).

* Wed Feb 23 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-3
- More shebang fixes (bug #608003).

* Wed Jan 12 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-2
- Applied patch to fix CVE-2010-4267, remote stack overflow
  vulnerability (bug #662740).

* Wed Jan 12 2011 Tim Waugh <twaugh@redhat.com> - 3.10.9-1
- Re-based to 3.10.9 with fixes from Fedora (bug #652255).
- Change shebang /usr/bin/env python -> /usr/bin/python (bug #608003).
- Added COPYING to common sub-package (bug #613707).
- Call cupsSetUser in cupsext's addPrinter method before connecting so
  that we can get an authentication callback (bug #616569).
- Fixed "CUPS Web Interface" button (bug #633899).

* Thu Jun 24 2010 Jiri Popelka <jpopelka@redhat.com> - 3.9.8-33
- Main package requires explicit version of hplip-libs (bug #601783).

* Wed Jun  9 2010 Tim Waugh <twaugh@redhat.com> - 3.9.8-32
- Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #580604).

* Mon Jun 07 2010 Jiri Popelka <jpopelka@redhat.com> - 3.9.8-31
- hplip-gui requires libsane-hpaio (bug #591636).

* Fri Apr  9 2010 Tim Waugh <twaugh@redhat.com> - 3.9.8-30
- Explicitly destroy tray icon on exit (bug #576282).
- Fixed duplex handling in hpcups.drv (bug #557515).

* Wed Mar  3 2010 Tim Waugh <twaugh@redhat.com> - 3.9.8-29
- Set defattr in gui sub-package file manifest.
- Avoid mixed use of spaces and tabs.

* Thu Feb 25 2010 Jiri Popelka <jpopelka@redhat.com> - 3.9.8-28
- Fixed crash when using Preferences dialog (bug #557099).
- Ship %%{_datadir}/hplip/prnt/plugins directory (bug #565875).

* Thu Jan  7 2010 Tim Waugh <twaugh@redhat.com> - 3.9.8-27
- Do ship pkit module even though the PolicyKit mechanism is not
  shipped (bug #554847).

* Thu Jan  7 2010 Tim Waugh <twaugh@redhat.com> 3.9.8-26
- Rebuilt.

* Thu Jan  7 2010 Tim Waugh <twaugh@redhat.com> 3.9.8-25
- Retry when connecting to device fails (bug #552582).
- Don't ship PolicyKit mechanism (bug #552536).
- Don't run automake/autoconf etc as it causes build failures.
- Reverted fix for bug #533462 until bug #541604 is solved (bug #553220).

* Thu Nov 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-24
- Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).

* Thu Nov 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-23
- Removed duplex constraints on page sizes with imageable areas larger
  than possible when duplexing (bug #541572).
- Fixed duplex reverse sides being horizontally flipped (bug #541604).

* Wed Nov 18 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-22
- Fixed duplex handling in hpcups.drv (bug #533462).

* Mon Nov  2 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-21
- Added 'requires proprietary plugin' to appropriate model names
  (bug #513283).

* Fri Oct 30 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-20
- Reverted retry patch until it can be tested some more.

* Thu Oct 29 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-19
- Retry when connecting to device fails (bug #528483).
- Avoid busy loop in hpcups when backend has exited (bug #525944).

* Wed Oct 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-18
- Set a printer-state-reason when there's a missing required plugin
  (bug #531330).

* Tue Sep 29 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-17
- Give up trying to print a job to a reconnected device (bug #515481).

* Wed Sep 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-16
- Enable parallel port support when configuring (bug #524979).

* Wed Sep 16 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-15
- Fixed hp-setup traceback when discovery page is skipped (bug #523685).

* Fri Aug 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-14
- Include missing base files.

* Fri Aug 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-13
- Use dll.d file instead of post scriptlet for hpaio (bug #519988).
- Fixed RequiresPageRegion patch (bug #518756).

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 3.9.8-12
- rebuilt with new openssl

* Wed Aug 26 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-11
- Set RequiresPageRegion in hpcups PPDs (bug #518756).

* Tue Aug 25 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-10
- Removed never-used definition of BREAKPOINT in scan/sane/common.h
  in hope of fixing the build.

* Tue Aug 25 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-9
- New common sub-package for udev rules and config file (bug #516459).
- Don't install base/*.py with executable bit set.

* Mon Aug 24 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-8
- Fixed typos in page sizes (bug #515469).
- Build no longer requires libudev-devel.
- Fixed state reasons handling problems (bug #501338).

* Wed Aug 19 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-6
- Make sure to avoid handwritten asm.
- Don't use obsolete configure options.

* Wed Aug 19 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-5
- Use upstream udev rules instead of hal policy (bug #518172).
- Removed unnecessary dependency on PyQt as we only use PyQt4 now.

* Wed Aug 12 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-4
- Upstream patch to fix paper size order and LJColor device class
  color space.

* Wed Aug 12 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-3
- The python-reportlab dependency was in the wrong sub-package.

* Thu Aug  6 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-2
- Removed access_control.grant_group line from HAL fdi file.

* Wed Aug  5 2009 Tim Waugh <twaugh@redhat.com> 3.9.8-1
- 3.9.8.

* Tue Aug  4 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-5
- Fix hpcups fax PPDs (bug #515356)

* Tue Jul 28 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-4
- Fixed ui-optional patch for qt4 code path (bug #500473).
- Fixed HWResolution for 'Normal' output from the hpcups driver
  (laundpad bug #405400).

* Mon Jul 27 2009 Tim Waugh <twaugh@redhat.com> 3.9.6b-2
- 3.9.6b.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-8
- Use existing libusb-using routines to try fetching Device ID.

* Thu Jul 23 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-7
- Error checking in the libudev device-id fallback code.

* Tue Jul 21 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-6
- Fixed device-id reporting.

* Wed Jun 24 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-5
- Set disc media for disc page sizes (bug #495672).

* Mon Mar  9 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-4
- Ship libhpmud.so (bug #489059).
- Fixed no-root-config patch (bug #489055).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Tim Waugh <twaugh@redhat.com> 3.9.2-2
- 3.9.2.  No longer need systray or quit patches.

* Tue Jan 27 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-7
- Only ship compressed PPD files.

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 2.8.12-6
- rebuild with new openssl

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-5
- Fixed Quit menu item in device manager (bug #479751).

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-4
- Prevent crash when DEVICE_URI/PRINTER environment variables are not
  set (bug #479808 comment 6).

* Tue Jan 13 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-3
- Make --qt4 the default for the systray applet, so that it appears
  in the right place, again (bug #479751).
- Removed hal preprobe rules as they were causing breakage
  (bug #479648).

* Mon Jan 12 2009 Tim Waugh <twaugh@redhat.com> 2.8.12-2
- Don't write to system-wide configuration file (bug #479178).

* Tue Dec 23 2008 Tim Waugh <twaugh@redhat.com> 2.8.12-1
- 2.8.12.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.10-2
- Rediff libsane patch.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.10-1
- 2.8.10.  No longer need gzip-n or quiet patches.

* Thu Dec 11 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-5
- Prevent backend crash when D-Bus not running (bug #474362).

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.8.7-4
- Rebuild for Python 2.6

* Tue Oct 21 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-3
- Ship PPDs in the correct location (bug #343841).

* Fri Sep 26 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-2
- Moved Python extension into libs sub-package (bug #461236).

* Mon Aug  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-1
- 2.8.7.
- Avoid hard-coded rpaths.
- New libs sub-package (bug #444016).

* Thu Jul 31 2008 Tim Waugh <twaugh@redhat.com>
- Move libhpip.so* to the main package to avoid libsane-hpaio
  depending on hpijs (bug #457440).

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.8.6b-2
- fix license tag

* Mon Jul 28 2008 Tim Waugh <twaugh@redhat.com> 2.8.6b-1
- 2.8.6b.

* Mon Jun 23 2008 Tim Waugh <twaugh@redhat.com> 2.8.6-1
- 2.8.6.  No longer need libm patch.

* Fri Jun  6 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-2
- Make --qt4 the default for the systray applet, so that it appears
  in the right place.  Requires PyQt4.

* Tue Jun  3 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-1
- 2.8.5.
- Configure with --enable-dbus.  Build requires dbus-devel.
- Fix chmod 644 line.
- Ship hp-systray in the gui sub-package, but don't ship the desktop
  launcher yet as the systray applet is quite broken.
- Don't run autoconf.

* Tue May 13 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-3
- Move installer directory to main package (bug #446171).

* Fri Apr  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-2
- Update hplip.fdi for Fedora 9: info.bus -> info.subsystem.
- Images in docdir should not be executable (bug #440552).

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-1
- 2.8.2.  No longer need alloc, unload-traceback or media-empty patches.
- Ship cupsddk driver.  The hpijs sub-package now requires cupsddk-drivers.

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-6
- Fixed marker-supply-low strings.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-5
- Rebuild for GCC 4.3.

* Fri Jan 25 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-4
- The hpijs compression module doesn't allocate enough memory (bug #428536).

* Wed Jan 23 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-3
- Really grant the ACL for the lp group (bug #424331).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-2
- Ship installer directory (bug #428246).
- Avoid multilib conflict (bug #341531).
- The hpijs sub-package requires net-snmp (bug #376641).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-1
- 2.7.12.  No longer need ljdot4 patch.

* Fri Jan  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.10-2
- Don't ship udev rules; instead, grant an ACL for group lp (bug #424331).

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.7.10-2
- Rebuild for deps

* Mon Oct 22 2007 Tim Waugh <twaugh@redhat.com> 2.7.10-1
- 2.7.10.

* Fri Oct 12 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-3
- Applied patch to fix remnants of CVE-2007-5208 (bug #329111).

* Tue Oct  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-2
- Use raw instead of 1284.4 communication for LJ4000 series (bug #249191).
- Build requires openssl-devel.

* Wed Oct  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-1
- 2.7.9.
- Adjusted udev rules to be less permissive.  We use ConsoleKit to add
  ACLs to the device nodes, so world-writable device nodes can be avoided.

* Tue Sep 25 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-5
- Prevent hpfax trying to load configuration files as user lp.

* Thu Sep  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-4
- Reverted udev rules change.
- Ship a HAL FDI file to get correct access control on the USB device
  nodes (bug #251470).
- Make libsane-hpaio requires the main hplip package, needed for
  libhpip.so (bug #280281).

* Thu Aug 30 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-3
- Updated udev rules to allow scanning by console user.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-2
- Better buildroot tag.
- More specific license tag.

* Fri Aug  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-1
- 2.7.7.

* Mon Jul 23 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-10
- Move libhpmud to hpijs package (bug #248978).

* Fri Jul 20 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-9
- Remove hplip service on upgrade.
- Updated selinux-policy conflict for bug #249014.
- Fixed the udev rules file (bug #248740, bug #249025).

* Tue Jul 17 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-8
- Fixed hp-toolbox desktop file (bug #248560).

* Mon Jul 16 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-7
- Low ink is a warning condition, not an error.

* Wed Jul 11 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-6
- Add hp-check back, but in the gui sub-package.
- Show the HP Toolbox menu entry again.

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-5
- Read system config when run as root (bug #242974).

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-4
- Moved reportlab requirement to gui sub-package (bug #189030).
- Patchlevel 1.

* Sat Jul  7 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-3
- Fixed pre scriptlet (bug #247349, bug #247322).

* Fri Jul  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-2
- Main package requires python-reportlab for hp-sendfax (bug #189030).
- Explicitly enable scanning.
- Main package requires python-imaging for hp-scan (bug #247210).

* Mon Jul  2 2007 Tim Waugh <twaugh@redhat.com>
- Updated selinux-policy conflict for bug #246257.

* Fri Jun 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-1
- 2.7.6.

* Thu Jun 28 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-3
- Another go at avoiding AVC messages on boot (bug #244205).

* Thu Jun 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-2
- Don't try to write a /root/.hplip.conf file when running as a CUPS
  backend (bug #244205).

* Wed Jun 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-1
- Don't put the version in the desktop file; let desktop-file-install do it.
- 1.7.4a.  No longer need marker-supply or faxing-with-low-supplies
  patches.  Cheetah and cherrypy directories no longer shipped in source
  tarball.

* Mon Jun 11 2007 Tim Waugh <twaugh@redhat.com>
- Don't ship hp-check (bug #243273).
- Moved hp-setup back to the base package, and put code in
  utils.checkPyQtImport() to check for the gui sub-package as well as
  PyQt (bug #243273).

* Fri Jun  8 2007 Tim Waugh <twaugh@redhat.com>
- Moved hp-setup to the ui package (bug #243273).
- Prevent SELinux audit message from the CUPS backends (bug #241776)

* Thu May 10 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-10
- Prevent a traceback when unloading a photo card (bug #238617).

* Fri May  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-9
- When faxing, low ink/paper is not a problem (bug #238664).

* Tue Apr 17 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-8
- Update desktop database on %%postun as well (bug #236163).

* Mon Apr 16 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-7
- Some parts can run without GUI support after all (bug #236161).
- Added /sbin/service and /sbin/chkconfig requirements for the scriptlets
  (bug #236445).
- Fixed %%post scriptlet's condrestart logic (bug #236445).

* Fri Apr 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-6
- Fixed dangling symlinks (bug #236156).
- Move all fax bits to the gui package (bug #236161).
- Don't ship fax PPD and backend twice (bug #236092).
- Run update-desktop-database in the gui package's %%post scriptlet
  (bug #236163).
- Moved desktop-file-utils requirement to gui package (bug #236163).
- Bumped selinux-policy conflict version (bug #236092).

* Thu Apr  5 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-5
- Better media-empty-error state handling: always set the state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-4
- Clear the media-empty-error printer state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-3
- Fixed typo in marker-supply-low patch.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-2
- Split out a gui sub-package (bug #193661).
- Build requires sane-backends-devel (bug #234813).

* Tue Apr  3 2007 Tim Waugh <twaugh@redhat.com>
- Change 'Hidden' to 'NoDisplay' in the desktop file, and use the System
  category instead of Utility (bug #170762).
- Link libsane-hpaio against libsane (bug #234813).

* Fri Mar 30 2007 Tim Waugh <twaugh@redhat.com>
- Use marker-supply-low IPP message.

* Thu Mar  1 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-1
- 1.7.2.

* Wed Feb 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.1-1
- 1.7.1.

* Wed Jan 10 2007 Tim Waugh <twaugh@redhat.com> 1.6.12-1
- 1.6.12.  No longer need broken-conf, loop, out-of-paper or
  sane-debug patches.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.6.10-7
- rebuild against python 2.5

* Wed Dec  6 2006 Tim Waugh <twaugh@redhat.com>
- Minor state fixes for out-of-paper patch.

* Thu Nov 23 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-6
- Report out-of-paper and offline conditions in CUPS backend (bug #216477).

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-5
- Fixed debugging patch.

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-4
- Allow debugging of the SANE backend.

* Mon Oct 30 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-3
- IPv6 support (bug #198377).  Local-only sockets are IPv4, and ought
  to be changed to unix domain sockets in future.

* Fri Oct 27 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-2
- 1.6.10.  No longer need compile patch.
- Fixed default config file (bug #211072).
- Moved libhpip to hpijs sub-package (bug #212531).

* Fri Sep 29 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-4
- Don't wake up every half a second (bug #204725).

* Mon Sep 25 2006 Tim Waugh <twaugh@redhat.com>
- Fixed package URL.

* Mon Aug 21 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-3
- Don't look up username in PWDB in the fax backend (removed redundant code).

* Mon Aug  7 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-2
- 1.6.7.
- Conflict with selinux-policy < 2.3.4 to make sure new port numbers are
  known about (bug #201357).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - (none):1.6.6a-3.1
- rebuild

* Tue Jul  4 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-3
- libhpip should link against libm (bug #197599).

* Wed Jun 28 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-2
- 1.6.6a.

* Mon Jun 26 2006 Tim Waugh <twaugh@redhat.com>
- Patchlevel 1.
- Fixed libsane-hpaio %%post scriptlet (bug #196663).

* Fri Jun 16 2006 Tim Waugh <twaugh@redhat.com> 1.6.6-2
- 1.6.6.

* Mon Jun 12 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-6
- Build requires autoconf (bug #194682).

* Fri May 26 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-5
- Include doc files (bug #192790).

* Mon May 15 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-4
- Patchlevel 2.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-3
- Move hpijs to 0.9.11 too.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-2
- 0.9.11.
- Keep hpijs at 0.9.8 for now.

* Fri Apr 21 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-6
- Patchlevel 2.

* Wed Apr 19 2006 Tim Waugh <twaugh@redhat.com>
- Don't package COPYING twice (bug #189162).

* Tue Apr 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-5
- Patchlevel 1.
- Fixed another case-sensitive match.
- Require hpijs sub-package (bug #189140).
- Don't package unneeded files (bug #189162).
- Put fax PPD in the right place (bug #186213).

* Tue Apr  4 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-4
- Use case-insensitive matching.  0.9.8 gave all-uppercase in some
  situations.
- Last known working hpijs comes from 0.9.8, so use that.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-3
- Always use /usr/lib/cups/backend.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-2
- 0.9.10.
- Ship PPDs.

* Fri Mar 24 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-7
- Include hpfax.
- Build requires libusb-devel.

* Thu Mar 23 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-6
- CUPS backend directory is always in /usr/lib.

* Mon Mar 13 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-4
- Quieten hpssd on startup.

* Sat Mar 11 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-3
- Patchlevel 1.

* Thu Mar  9 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-2
- 0.9.9.  No longer need quiet or 0.9.8-4 patches.

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 0.9.8-6
- Buildrequires: desktop-file-utils

* Mon Feb 27 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-5
- Patchlevel 4.

* Tue Feb 14 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-4
- Added Obsoletes: hpoj tags back in (bug #181476).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - (none):0.9.8-3.1
- bump again for double-long bug on ppc(64)

* Tue Feb  7 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-3
- Patchlevel 3.

* Fri Feb  3 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-2
- Patchlevel 2.

* Thu Feb  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-1
- 0.9.8.
- No longer need initscript patch.
- Don't package hpfax yet.

* Wed Jan 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-8
- Don't package PPD files.

* Thu Jan  5 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-7
- Fix initscript (bug #176966).

* Mon Jan  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-6
- Rebuild.

* Fri Dec 23 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-5
- Rebuild.

* Wed Dec 21 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-4
- Build requires python-devel, libjpeg-devel (bug #176317).

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Dec  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-3
- Use upstream patch 0.9.7-2.
- No longer need lpgetstatus or compile patches.

* Fri Nov 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-2
- Prevent LPGETSTATUS overrunning format buffer.

* Thu Nov 24 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-1
- 0.9.7.

* Fri Nov 18 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-7
- Fix compilation.

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 0.9.6-6
- rebuilt against new openssl

* Mon Nov  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-5
- Rebuilt.

* Wed Oct 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-4
- Ship initscript in %%{_sysconfdir}/rc.d/init.d.

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com>
- Install the desktop file with Hidden=True (bug #170762).

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-3
- Don't install desktop file (bug #170762).
- Quieten the hpssd daemon at startup (bug #170762).

* Wed Oct 12 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-2
- 0.9.6.

* Tue Sep 20 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-3
- Apply upstream patch to fix scanning in LaserJets and parallel InkJets.

* Mon Sep 19 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-2
- 0.9.5.
- No longer need condrestart patch.
- Fix compile errors.

* Tue Jul 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-3
- Fix condrestart in the initscript.

* Mon Jul 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-2
- Use 'condrestart' not 'restart' in %%post scriptlet.

* Fri Jul 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-1
- forward-decl patch not needed.
- 0.9.4.

* Fri Jul  1 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-8
- Removed Obsoletes: hpoj tags (bug #162222).

* Thu Jun 30 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-7
- Rebuild to get Python modules precompiled.

* Wed Jun 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-6
- For libsane-hpaio ExcludeArch: s390 s390x, because it requires
  sane-backends.

* Wed Jun 15 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-5
- Use static IP ports (for SELinux policy).

* Tue Jun 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-4
- Conflicts: hpijs from before this package provided it.
- Conflicts: system-config-printer < 0.6.132 (i.e. before HPLIP support
  was added)

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-3
- Added Obsoletes: for xojpanel and hpoj-devel (but we don't actually package
  devel files yet).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-2
- Add 'hpaio' to SANE config file, not 'hpoj' (bug #159954).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-1
- Use /usr/share/applications for putting desktop files in (bug #159932).
- Requires PyQt (bug #159932).

* Tue Jun  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-0.1
- Initial package, based on Mandriva spec file.
