Summary:       Hardware lister
Name:          lshw
Version:       B.02.17
Release:       4%{?dist}
License:       GPLv2
Group:         Applications/System
URL:           http://ezix.org/project/wiki/HardwareLiSter
Source0:       http://www.ezix.org/software/files/lshw-%{version}.tar.gz
Source1:       lshw.desktop
Source2:       org.ezix.lshw.gui.policy
Source3:       lshw-gui
Patch0:        lshw-B.02.17-scan-fat-mem-bug.patch
Patch1:        no_smbios_unsupp.patch
Patch2:        0dff3470.patch
BuildRequires: sqlite-devel
Requires:      hwdata

%description
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory configuration,
firmware version, mainboard configuration, CPU version and speed, cache
configuration, bus speed, etc. on DMI-capable x86 systems and on some
PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%package       gui
Summary:       Graphical hardware lister
Group:         Applications/System
Requires:      polkit
Requires:      %{name} = %{version}-%{release}
BuildRequires: gtk2-devel >= 2.4
BuildRequires: desktop-file-utils

%description   gui
Graphical frontend for the hardware lister (lshw) tool.
If desired, hardware information can be saved to file in
plain, XML or HTML format.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%{__make} %{?_smp_mflags} SBINDIR="%{_sbindir}" RPM_OPT_FLAGS="%{optflags}" SQLITE=1 gui 

# Replace copyrighted icons
pushd src
%{__make} nologo

%install
%{__make} install              \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        SQLITE=1               \
        STRIP="/bin/true"      \
        INSTALL="%{__install} -p"

%{__make} install-gui          \
        DESTDIR="%{buildroot}" \
        PREFIX="%{_prefix}"    \
        SBINDIR="%{_sbindir}"  \
        MANDIR="%{_mandir}"    \
        SQLITE=1               \
        STRIP="/bin/true"      \
        INSTALL="%{__install} -p"

%{__ln_s} -f gtk-lshw %{buildroot}%{_sbindir}/lshw-gui

# don't package these copies, use the ones from hwdata instead
%{__rm} -f %{buildroot}%{_datadir}/%{name}/pci.ids
%{__rm} -f %{buildroot}%{_datadir}/%{name}/usb.ids
# don't package these copies, they're not actually used by the app,
# and even if they were, should use the hwdata versions
%{__rm} -f %{buildroot}%{_datadir}/%{name}/oui.txt
%{__rm} -f %{buildroot}%{_datadir}/%{name}/manuf.txt

# desktop icon
%{__install} -D -m 0644 -p ./src/gui/artwork/logo.svg \
     %{buildroot}%{_datadir}/pixmaps/%{name}-logo.svg
desktop-file-install %{?vendortag:--vendor fedora} \
  --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

# PolicyKit
%{__install} -D -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
%{__install} -D -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/lshw-gui

# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/fr/

#files -f %{name}.lang
%files
%doc COPYING README docs/*
%doc %{_mandir}/man1/lshw.1*
%{_sbindir}/%{name}

%files gui
%doc COPYING
%{_bindir}/%{name}-gui
%{_sbindir}/gtk-%{name}
%{_sbindir}/%{name}-gui
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}-logo.svg
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy

%changelog
* Tue Jan 12 2016 Petr Oros <poros@redhat.com> - B.02.17-4
- Report the vendor_id field for x86 cpu's
- Resolves: #1215246

* Mon Feb 9 2015 Petr Oros <poros@redhat.com> - B.02.17-3
- Resolves: #1101592
- Initial package for RHEL6.7

