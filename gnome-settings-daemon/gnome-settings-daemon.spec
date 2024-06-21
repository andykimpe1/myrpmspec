%define _default_patch_fuzz 999

Name:		gnome-settings-daemon
Version:	2.28.2
Release:	39%{?dist}
Summary:	The daemon sharing settings from GNOME to GTK+/KDE applications

Group:		System Environment/Daemons
License:	GPLv2+
URL:		http://download.gnome.org/sources/%{name}
Source0:	http://download.gnome.org/sources/%{name}/2.28/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# "gnome-settings-daemon-wacom-config-v2" is to make sure that the Wacom
# component of both gnome-settings-daemon and control-center take their
# configuration from the same path
# https://bugzilla.gnome.org/show_bug.cgi?id=674792
%ifnarch s390 s390x
Provides: gnome-settings-daemon-wacom-config-v2
%endif

Requires(pre): GConf2 >= 2.14
Requires(preun): GConf2 >= 2.14
Requires(post): GConf2 >= 2.14
Requires: control-center-filesystem
%ifnarch s390 s390x
Requires: libwacom >= 0.3-7
Requires: xorg-x11-drv-wacom >= 0.12.99
Requires: hwdata
%endif

BuildRequires:	dbus-glib-devel
BuildRequires:	GConf2-devel
BuildRequires:	gtk2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gnome-desktop-devel >= 2.25.5
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libgnome-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:	libgnomekbd-devel
BuildRequires:	libnotify-devel
BuildRequires:	gettext intltool
BuildRequires:  fontconfig-devel
BuildRequires:	libcanberra-devel
BuildRequires: automake, autoconf, libtool, intltool
BuildRequires: automake, autoconf, libtool, intltool
BuildRequires: pkgconfig(nss)
BuildRequires:	libgudev1-devel
%ifnarch s390 s390x
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	libwacom-devel >= 0.3-7
BuildRequires:	xorg-x11-drv-wacom-devel >= 0.12.99
%endif

# https://bugzilla.gnome.org/show_bug.cgi?id=596136
Patch0: 0002-Use-a-rounded-instead-of-curved-rectangle.patch
Patch1: 0003-Improve-the-media-keys-overlay-design.patch
# change font rendering
Patch3: slight-hinting.patch
#
# https://bugzilla.gnome.org/show_bug.cgi?id=604918
Patch9: osd-spam.patch

# related 548978
# https://bugzilla.gnome.org/show_bug.cgi?id=606794
Patch10: left-handed-single-button.patch

# http://bugzilla.gnome.org/614024
Patch11: gsd-dir-prefix.patch

# http://bugzilla.gnome.org/616327
Patch12: smartcard-plugin.patch

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=589207
Patch13: gnome-settings-daemon-translations.patch
# more translations
# https://bugzilla.redhat.com/show_bug.cgi?id=1333641
Patch40: gnome-settings-daemon-2.28.2-EL6.9_translations.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=621046
# https://bugzilla.redhat.com/show_bug.cgi?id=582564
Patch14: fix-hotplug-configuration.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=623223
# https://bugzilla.redhat.com/show_bug.cgi?id=595763
Patch15: gsd-windows-p-handling.patch
Patch16: gsd-use-virtual-modifier.patch

# http://bugzilla.gnome.org/769464
Patch17: wacom-plugin.patch

# http://bugzilla.redhat.com/693843
Patch18: ignore-gdm.patch

# Wacom tool XRandR version check
Patch19: gsd-wacom-fix-xrandr-version-check.patch

# Wacom tool XRandR version check
Patch20: gsd-wacom-fix-for-cintiq-without-xrandr.patch

# Wacom tool add NV-CONTROL support and backport LED support from upstream
Patch21: gsd-wacom-add-twinview-and-led-support.patch

# Wacom tool make tablet configuration be per-machine
Patch22: gsd-wacom-set-per-machine-settings.patch

# Wacom tool fix sysfs path for status_led?_select/wacom_led
# https://bugzilla.redhat.com/show_bug.cgi?id=805064
# https://bugzilla.gnome.org/show_bug.cgi?id=676558
Patch23: gsd-wacom-fix-modeswitch-led.patch

# Wacom tool fix crash when using a shortcut with the Shift key
# https://bugzilla.redhat.com/show_bug.cgi?id=839328
# https://bugzilla.gnome.org/show_bug.cgi?id=679736
Patch24: gsd-wacom-fix-shift-key-shortcut-crash.patch

# Wacom tool match builtin monitor if edid-matching fails for screen tablets
# but do not save display value if no match is found
# https://bugzilla.redhat.com/show_bug.cgi?id=826128
# https://bugzilla.gnome.org/show_bug.cgi?id=676006
Patch25: gsd-wacom-fix-display-value-if-no-match-is-found.patch

# Wacom tool tablet integration improvements from upstream
# https://bugzilla.redhat.com/show_bug.cgi?id=772728
Patch26: gsd-wacom-dont-set-touchscreens-into-relative-mode.patch
Patch27: gsd-wacom-fix-crash-and-leak-on-hotplug.patch
Patch28: gsd-wacom-do-not-rotate-pad-devices.patch
Patch29: gsd-wacom-install-test-apps.patch

# Mouse plug-in in gnome-settings-daemon interferes with Wacom devices
# https://bugzilla.redhat.com/show_bug.cgi?id=853181
Patch30: gsd-mouse-do-not-interfere-with-wacom-devices.patch

# Wacom plug-in does not enable touch devices by default
# https://bugzilla.redhat.com/show_bug.cgi?id=858255
Patch31: gsd-wacom-fix-touch-devices.patch

# Wacom tool update input transformation matrix on screen changes
# https://bugzilla.redhat.com/show_bug.cgi?id=861890
# https://bugzilla.gnome.org/show_bug.cgi?id=668614
Patch32: gsd-wacom-update-input-matrix-on-monitor-changes.patch

# Wacom multiple mode-switch buttons mode selection
# http://bugzilla.gnome.org/show_bug.cgi?id=690157
# https://bugzilla.redhat.com/show_bug.cgi?id=886922
Patch33: 0001-wacom-multiple-mode-switch-buttons-mode-selection.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=649222
# https://bugzilla.redhat.com/show_bug.cgi?id=812363
Patch50: 0001-common-Use-defines-instead-of-variables-for-ranges.patch
Patch51: 0001-common-Fix-function-keys-not-being-grabbed.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=677472
# https://bugzilla.redhat.com/show_bug.cgi?id=824757
Patch52: 0001-xrandr-explicitly-set-clone-state-variable-when-gene.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=668776
# https://bugzilla.redhat.com/show_bug.cgi?id=1098370
Patch53: 0001-housekeeping-plug-a-mem-leak.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1196044
Patch54: 0001-xrandr-Avoid-crash-when-Fn-F7-is-pressed-on-some-sys.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1167519
Patch55: 0001-media-keys-Handle-XF86AudioMicMute.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1095019
Patch56: 0001-wacom-Fix-type-of-data-passed-to-XIChangeDevicePrope.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=966658
Patch57: gsd-wacom-no-per-machine-config-file.patch

%description
A daemon to share settings from GNOME to other applications. It also
handles global keybindings, as well as a number of desktop-wide settings.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	dbus-glib-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .osd-rounded-rectangle
%patch1 -p1 -b .osd-visual-refresh
%patch3 -p1 -b .slight-hinting
%patch9 -p1 -b .osd-spam
%patch10 -p1 -b .single-button
%patch11 -p1 -b .dir-prefix
%patch12 -p1 -b .smartcard-plugin
%patch13 -p1 -b .translations
%patch40 -p2 -b .translations2
%patch14 -p1 -b .fix-hotplug-configuration
%patch15 -p1 -b .windows-p
%patch16 -p1 -b .virtual
%patch17 -p1 -b .wacom
%patch18 -p1 -b .ignore-gdm
%patch19 -p1 -b .xrandr-version-check
%patch20 -p1 -b .cintiq-without-xrandr
%patch21 -p1 -b .twinview-and-led-support
%patch22 -p1 -b .per-machine-settings
%patch23 -p1 -b .modeswitch-led
%patch24 -p1 -b .shift-key-crash
%patch25 -p1 -b .no-edid-match
%patch26 -p1 -b .touchscreens
%patch27 -p1 -b .leak-on-hotplug
%patch28 -p1 -b .no-rotate-pad
%patch29 -p1 -b .install-test-apps
%patch30 -p1 -b .mouse-ignore-wacom
%patch31 -p1 -b .enable-touch
%patch32 -p1 -b .update-input-matrix
%patch33 -p1 -b .multiple-modeswitches
%patch50 -p1 -b .define
%patch51 -p1 -b .function-keys
%patch52 -p1 -b .fn-f8
%patch53 -p1 -b .housekeeping-mem-leak
%patch54 -p1 -b .fnf7-crash
%patch55 -p1 -b .micmute
%patch56 -p1 -b .wacom-reset-touch-buttons
%patch57 -p1 -b .no-per-machine-config-file

%build
autoreconf -f -i
%configure --enable-static=no --enable-profiling --disable-esd --with-pnp-ids-path=/usr/share/hwdata/pnp.ids
make %{?_smp_mflags}

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p %{name}.pot > $p.out
# Force the creation date to be static so it's not different between multilib variants
  sed -i -e 's/"POT-Creation-Date: .*\\n"/"POT-Creation-Date: 2012-03-07 00:01-0400\\n"/' $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas \
	%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas \
	%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas \
	%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas \
	%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas \
	%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas \
	%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_wacom.schemas \
	>& /dev/null || :
touch %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%pre
if [ "$1" -gt 1 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_wacom.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_wacom.schemas \
			>& /dev/null || :
	fi
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas \
		%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas \
		%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas \
		%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas \
		>& /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_touchpad.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_smartcard.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_default_editor.schemas \
			>& /dev/null || :
	fi
	if [ -f %{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_wacom.schemas ] ; then
		gconftool-2 --makefile-uninstall-rule \
			%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_wacom.schemas \
			>& /dev/null || :
	fi
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_keybindings.schemas \
		%{_sysconfdir}/gconf/schemas/apps_gnome_settings_daemon_screensaver.schemas \
		%{_sysconfdir}/gconf/schemas/desktop_gnome_font_rendering.schemas \
		%{_sysconfdir}/gconf/schemas/gnome-settings-daemon.schemas \
		>& /dev/null || :
fi

%postun
touch %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/gnome-settings-daemon-2.0
%{_libexecdir}/gnome-settings-daemon
%{_libexecdir}/gsd-locate-pointer
%{_datadir}/gnome-settings-daemon/
%{_datadir}/gnome-control-center/keybindings/50-accessibility.xml
%{_datadir}/dbus-1/services/org.gnome.SettingsDaemon.service
%{_sysconfdir}/xdg/autostart/gnome-settings-daemon.desktop
%{_datadir}/icons/hicolor/*/apps/gsd-xrandr.*
%ifnarch s390 s390x
%{_libexecdir}/gsd-wacom-led-helper
%{_libexecdir}/gsd-test-wacom
%{_libexecdir}/gsd-list-wacom
%{_datadir}/polkit-1/actions/org.gnome.settings-daemon.plugins.wacom.policy
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/gnome-settings-daemon-2.0
%{_libdir}/pkgconfig/gnome-settings-daemon.pc

%changelog
* Wed Feb 08 2017 Ray Strode <rstrode@redhat.com> - 2.28.2-39
- Another smartcard update to support drivers that don't
  announce already inserted smartcards at startup
  Related: #1299992

* Wed Jan 25 2017 Bastien Nocera <bnocera@redhat.com> - 2.28.2-38
- Add translation patch
  Resolves: #1333641

* Tue Nov 29 2016 Ray Strode <rstrode@redhat.com> - 2.28.2-37
- Small update to slot id 0 smartcard fix from 2.28.2-35
  Resolves: #1299992
  Related: 966658

* Fri Oct 14 2016 Carlos Garnacho <cgarnach@redhat.com> - 2.28.2-36
- Check ~/.config/gnome-settings-daemon/no-per-machine-config for wacom settings
  Resolves: #966658

* Tue Jan 19 2016 Ray Strode <rstrode@redhat.com> - 2.28.2-35
- Allow slot id 0 as a valid slot id
  Resolves: #1139296

* Mon Dec 08 2015 Carlos Garnacho <cgarnach@redhat.com> 2.28.2-34
- wacom: Fix memory overread in call to XDeviceChangeProperty
  Resolves: #1095019

* Wed Nov 18 2015 Bastien Nocera <bnocera@redhat.com> 2.28.2-33
- Add support for XF86MicMute key
  Resolves: #1167519

* Wed Nov 18 2015 Bastien Nocera <bnocera@redhat.com> 2.28.2-32
- Fix possible Fn+F7 crash
  Resolves: #1196044

* Fri Jan 23 2015 Bastien Nocera <bnocera@redhat.com> 2.28.2-31
- housekeeping: plug a mem leak
  Resolves: #1098370

* Mon Dec 17 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-30
- wacom: Fix multiple mode-switch buttons as found on Cintiq 24HD (#886922)
  Resolves: #886922

* Tue Oct  2 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-29
- wacom: Update input transformation matrix on monitor changes (#861890)
  wacom: Re-fix LED as per latest discussions on linuxwacom-devel (#805064)
  Resolves: #805064 #861890

* Wed Sep 19 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-28
- common: Update grab fix to avoid grabbing regular unmodified keys
  Related: #812363

* Tue Sep 18 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-27
- wacom: enable touch devices (#858255)
  Resolves: #858255

* Mon Sep 10 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-26
- mouse: ignore Wacom devices (#853181)
  Resolves: #853181

* Thu Sep 06 2012 Bastien Nocera <bnocera@redhat.com> 2.28.2-25
- display: Update hotkey fix, thanks to Olivier for the updated patch
  Resolves: #824757

* Wed Sep 05 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-24
- wacom: tablet integration improvements from upstream (#772728)
  Resolves: #772728

* Tue Sep 04 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-23
- wacom: fix sysfs pach for status_led?_select/wacom_led (#805064)
- wacom: fix crash when using a shortcut with the Shift key (#839328)
- wacom: match builtin monitor if edid-matching fails for screen
  tablets (#826128)
  Resolves: #805064 #839328 #826128

* Thu Aug 30 2012 Bastien Nocera <bnocera@redhat.com> 2.28.2-22
- Fix "Display" hot key not working in some circumstances
  Resolves: #824757

* Tue Aug 07 2012 Bastien Nocera <bnocera@redhat.com> 2.28.2-21
- common: Fix unmodified function keys not being captured
  Resolves: #812363

* Fri Apr 27 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-20
- wacom: Make tablet configuration be per-machine
  Resolves: #816646

* Wed Mar 28 2012 Peter Hutterer <peter.hutterer@redhat.com> 2.28.2-19
- Update libwacom requires to new libwacom with Intuos5 support
  Related: #769464

* Thu Mar 22 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-18
- wacom: fix build on s390/s390x
  Related: #805064

* Thu Mar 22 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-17
- wacom: add support for NV-CONTROL extension (#805036)
- wacom: fix button mapping (#805042)
- wacom: add LED support from upstream (#805064)
  Resolves: #805036 #805042 #805064

* Wed Mar 07 2012 Ray Strode <rstrode@redhat.com> 2.28.2-16
- Fix recently introduced multilib snafu
  Related: #769464

* Wed Mar  7 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-15
- wacom: add fix for Cintiq with non-XRandR driver
  Related: #769464

* Tue Mar  6 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-14
- wacom: add fix for XRandR version
  Related: #769464

* Mon Mar 05 2012 Ray Strode <rstrode@redhat.com> 2.28.2-13
- GDM doesn't handle keyboard selection for the session anymore,
  yet it still claims to.  Ignore what it says.
  Resolves: #693843

* Fri Mar  5 2012 Olivier Fourdan <ofourdan@redhat.com> 2.28.2-12
- Add wacom support
  Resolves: #769464

* Tue Jul 27 2010 Ray Strode <rstrode@redhat.com> 2.28.2-11
- Add a sanity check to prevent the "p" key and related
  from ever getting grabbed on accident.
  Related: #595763

* Sat Jul 24 2010 Ray Strode <rstrode@redhat.com> 2.28.2-10
- Fix 25 second delay in video switching
  Related: #595763

* Fri Jul 23 2010 Ray Strode <rstrode@redhat.com> 2.28.2-9
- Add small fix to previous commit
  Resolves: #595763

* Thu Jul 22 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-8
- Add support for the Windows+P keyboard shortcut
Resolves: rhbz#595763

* Fri Jul 16 2010 Ray Strode <rstrode@redhat.com> 2.28.2-7
- Update smartcard plugin to work better in the face
  of multiple modules.
  Resolves: #614639

* Mon Jun 28 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-6
- Don't remove the sound plugin if we want the samples to be dropped
  when needed
Resolves: rhbz#591902

* Tue Jun 08 2010 Ray Strode <rstrode@redhat.com> 2.28.2-5
- Restore monitor configuration on hotplug
  Resolves: #582564

* Mon May 10 2010 Matthias Clasen <mclasen@redhat.com> 2.28.2-4
- Updated translations
Resolves: #589207

* Mon Apr 19 2010 Ray Strode <rstrode@redhat.com> 2.28.2-3
- Add smart card plugin
Related: #581506

* Fri Mar 26 2010 Ray Strode <rstrode@redhat.com> 2.28.2-2
Resolves: #577278
- Support relocatable .gnome2 dir

* Tue Mar 16 2010 Bastien Nocera <bnocera@redhat.com> 2.28.2-1
- Update to 2.28.2
- Fix keyboard settings on hotplug
Related: rhbz#573006

* Mon Jan  4 2010 Matthias Clasen <mclasen@redhat.com> 2.28.1-10
- Avoid warning messages from the OSD code

* Tue Dec 15 2009 Matthias Clasen <mclasen@redhat.com> 2.28.1-9
- Survive when running without XKB (#547780)

* Thu Nov 12 2009 Matthias Clasen <mclasen@redhat.com> 2.28.1-8
- Avoid a 'whitespace leak' around the display statusicon (gnome #601696)

* Mon Nov  9 2009 Matthias Clasen <mclasen@redhat.com> 2.28.1-7
- React to screen changes when showing the background (gnome #601203)

* Thu Nov 05 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-6
- Fix the volume going over 100% in the OSD

* Wed Oct 28 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-5
- Update OSD code again

* Tue Oct 27 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-4
- Fix bluriness in OSD

* Mon Oct 26 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-3
- Change default font rendering to use slight hinting

* Mon Oct 26 2009 Peter Hutterer <peter.hutterer@redhat.com> 2.28.1-2
- left-handed-touchpad.patch: change physical touchpad buttons to
  left-handed, not tapping though (#498249)

* Mon Oct 19 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1
- Update to 2.28.1

* Thu Oct  1 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-4
- Fix keyboard variant handling

* Fri Sep 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-3
- Align the OSD visuals with the notification theme

* Tue Sep 22 2009 Adam Jackson <ajax@redhat.com> 2.28.0-2
- BuildRequires: libcanberra-devel

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Wed Sep 09 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-2
- Update left-hand touchpad patch

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Sun Aug 30 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-3
- Make 'Locate Pointer' work with metacity again

* Wed Aug 26 2009 Peter Hutterer <peter.hutterer@redhat.com> 2.27.91-2
- buttonmapping.patch: Don't check for IsXExtensionDevice, only skip button
  mappings for core devices instead (#502129).

* Mon Aug 24 2009 Bastien Nocera <bnocera@redhat.com> 2.27.91-1
- Update to 2.27.91

* Fri Aug 14 2009 Bastien Nocera <bnocera@redhat.com> 2.27.90-2
- Update gnome-volume-control code

* Fri Aug 14 2009 Bastien Nocera <bnocera@redhat.com> 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> 2.27.5-1
- Update to 2.27.5

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-3
- Make locate-pointer not interfere with media keys

* Wed Jul 15 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-2
- Rebuild against new libgnomekbd

* Tue Jul 14 2009 Matthias Clasen <mclasen@redhat.com> 2.27.4-1
- Update ot 2.27.4

* Tue Jun 30 2009 Matthias Clasen <mclasen@redhat.com> 2.27.3-2
- Rebuild against new libxklavier

* Tue Jun 16 2009 Matthias Clasen <mclasen@redhat.com> 2.27.3-1
- Update to 2.27.3

* Mon Jun  8 2009 Matthias Clasen <mclasen@redhat.com> 2.27.1-2
- Make the 'locate pointer' effect cope with changing compositing
  managers

* Sat May 16 2009 Matthias Clasen <mclasen@redhat.com> 2.27.1-1
- Update to 2.27.1

* Fri May 08 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-4
- Remove useless patch, see:
http://bugzilla.gnome.org/show_bug.cgi?id=580761 for details

* Wed Apr 29 2009 Bastien Nocera <bnocera@redhat.com> 2.26.1-3
- Don't set touchpads to be left-handed, otherwise the tap
  behaves like the 2nd mouse button (#483639)

* Mon Apr 27 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.1-2
- Don't drop schemas translations from po files

* Tue Apr 14 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Wed Apr  8 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.0-2
- Support touchpads

* Mon Mar 16 2009 Matthias Clasen  <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb  5 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.90-2
- Fix a warning (#484132)

* Wed Feb  4 2009 Matthias Clasen  <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Mon Jan 19 2009 - Ray Strode <rstrode@redhat.com> - 2.25.3-4
- Update fade patch for new gnome-desktop release

* Thu Dec 18 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-3
- Rebuild

* Thu Dec 18 2008 - Ray Strode <rstrode@redhat.com> - 2.25.3-2
- Drop touchpad patch for now

* Thu Dec 18 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.3-1
- Update to 2.25.3

* Thu Dec 18 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.2-11
- Fix touchpad patches

* Wed Dec 17 2008 Matthias Clasen  <mclasen@redhat.com> - 2.25.2-10
- Rebuild against new gnome-desktop

* Wed Dec 10 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-9
- Don't call SetPointerMapping when using Xinput since
  it duplicates effort but gets touchpads wrong (bug 324721)

* Wed Dec 10 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-8
- Shutdown cleanly when bus goes away (bug 445898 again)

* Wed Dec 10 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-7
- Don't map touch pad tap to right-click for left-handed
  users (bug 324721)

* Wed Dec 10 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-6
- Listen for DeviceAdded signals when configuring mouse
  (in addition to DeviceEnabled).  This may help with
  bug 474758.

* Tue Dec  9 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-5
- Shutdown cleanly on TERM signal (bug 445898)

* Sun Dec  7 2008 Behdad Esfahbod <besfahbo@redhat.com> - 2.25.2-4
- Add gnome-settings-daemon-2.24.1-umask.patch

* Thu Dec  4 2008 Ray Strode <rstrode@redhat.com> - 2.25.2-2
- Rebase fade patch to apply with Behdad's updates to
  g-s-d

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-1
- Ypdate to 2.25.2

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-4
- Rebuild

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-2
- Update to 2.25.1

* Fri Oct 24 2008 Ray Strode <rstrode@redhat.com> - 2.24.0-14
- At fontconfig-devel buildrequires (bug 468304)

* Wed Oct 15 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-13
- Save some space

* Tue Oct 14 2008 Ray Strode <rstrode@redhat.com> - 2.24.0-12
- Hold off on settings-daemon fade if nautilus is going to do
  it anyway.

* Tue Oct 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-11
- Show the shutdown dialog when the power button is pressed

* Tue Oct 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-9
- Drop a patch that is no longer needed with the evdev ruleset
  in xkeyboard-config

* Sun Oct 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-7
- Try harder not to override peoples configured keyboard layouts

* Sun Oct 12 2008 Ray Strode <rstrode@redhat.com> - 2.24.0-6
- Update fade patch to skip crossfade when changing frames in
  slideshow background.

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-5
- Fix the picking up of the gdm keyboard layout even more

* Tue Sep 30 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-3
- Fix the picking up of the gdm keyboard layout

* Wed Sep 28 2008 Ray Strode <rstrode@redhat.com> - 2.24.0-2
- Don't draw background twice at startup

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Thu Sep 18 2008 Ray Strode <rstrode@redhat.com> - 2.23.92-3
- When switching desktop backgrounds fade between them

* Thu Sep 11 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.92-2
- Fix various bugs in the fn-F7 support

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Fri Sep  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-5
- Try harder to use the keyboard layout that gdm tells us

* Tue Sep 04 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.91-4
- Use the fn-F7 key, not the F7 key.

* Wed Sep 03 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.91-3
- Bump gnome-desktop requirement

* Wed Sep 03 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.91-2
- Add patch to do fn-f7 cycling

* Mon Sep 01 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Thu Aug 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.91-0.2008.08.28.2
- BuildRequires libnotify-devel

* Thu Aug 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.91-0.2008.08.28.1
- Update to snapshot

* Fri Aug 22 2008 Matthias Clasen <mclasne@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Thu Aug 14 2008 Lennart Poettering <lpoetter@redhat.com> - 2.23.6-3
- Rerun autotools after patching configure.ac

* Thu Aug 14 2008 Lennart Poettering <lpoetter@redhat.com> - 2.23.6-2
- Apply patch from gnome bug 545386. This hasn't been accepted in this form yet
  by upstream, will however very likely be merged in a similar form.
- Disable esd/sounds module since we don't need it to start PA anymore

* Tue Aug  5 2008 Matthias Clasen <mclasne@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Fri Jul 25 2008 Matthias Clasen <mclasne@redhat.com> - 2.23.5-3
- Use standard icon names in the volume OSD
 
* Fri Jul 25 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.5-2
- Fix build, call gtk-update-icon-cache as required

* Thu Jul 24 2008 Soren Sandmann <sandmann@redhat.com> - 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue Jun 17 2008 Colin Walters <walters@redhat.com> - 2.23.3-2
- Add (now upstreamed) patch to legacy ESD preference; see
  http://bugzilla.gnome.org/show_bug.cgi?id=533198
  https://bugzilla.redhat.com/show_bug.cgi?id=430624

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3-1
- Update to 2.23.3

* Wed May 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-0.2008.05.14.2
- Fix BuildRequires

* Wed May 14 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-0.2008.05.14.1
- Build snapshot

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1-5
- Rebuild

* Mon May  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1-4
- Pick up the keyboard layout from the login screen

* Mon May  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1-3
- Fix background drawing without nautilus

* Tue Apr 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1.1-2
- Add patch from upstream to avoid the Stop button triggering an Eject (#346201)

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1.1-1
- Update to 2.23.1.1

* Tue Apr 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-2008.03.26.6
- Make the xrandr plugin survive the absence of Xrandr

* Sat Apr 5 2008 - Soren Sandmann <sandmann@redhat.com> - 2.22.1-2008.03.26.5
- Update randr plugin

* Mon Mar 31 2008 - Ray Strode <rstrode@redhat.com> - 2.22.1-0.2008.03.26.4
- Over the releases we've accumulated default.png, default-wide.png default-5_4.png
  and default.jpg.  We haven't been able to drop them because it would leave some
  users with white backgrounds on upgrade.  This patch just falls back to the
  default image if the user's background doesn't exist.

* Wed Mar 26 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.1-0.2008.03.26.3
- Add patch for the mouse plugin not to eat multimedia key events (#438942)

* Wed Mar 26 2008 Jon McCann <jmccann@redhat.com> - 2.22.1-0.2008.03.26.2
- Rebuild

* Wed Mar 26 2008 Jon McCann <jmccann@redhat.com> - 2.22.1-0.2008.03.26.1
- Update to snapshot
- Enable profiling

* Wed Mar 26 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-3
- apps_gnome_settings_daemon_default_editor.schemas is obsolete (#438937)

* Thu Mar 20 2008 Matthias Clasen <mclasen@redhat.com> 2.22.0-2
- Fix interaction between "Locate Pointer" and volume keys

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> 2.22.0-1
- Update to 2.22.0

* Sun Mar  9 2008 Ray Strode <rstrode@redhat.com> - 2.21.92-3
- Don't set keyboard model on startup from gconf if evdev is being used.
  Evdev needs to use its own keyboard model to work right.

* Sun Mar  2 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.92-2
- Update randr patch to handle video key

* Fri Feb 29 2008 Jon McCann <jmccann@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Soren Sandmann <sandmann@redhat.com> - 2.21.91-3
- Add patch to make the xrandr plugin listen for client messages from
  the control panel and reread the configuration file.

* Mon Feb 11 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-2
- Remove obsolete control-center translations

* Mon Feb 11 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.91-1
- Update to 2.21.91
- Remove obsolete patches

* Thu Feb  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90.1-3
- Load xkb settings initially

* Thu Jan 31 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90.1-2
- Fix the path for g-s-d, from upstream patch

* Tue Jan 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90.1-1
- Update to 2.21.90.1

* Tue Jan 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Tue Jan 15 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.5.2-2
- Incorporate review feedback (#428833)

* Tue Jan 15 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.5.2-1
- Update to 2.21.5.2

* Tue Jan 15 2008  Matthias Clasen <mclasen@redhat.com> - 2.21.5.1-1
- Update to 2.21.5.1
- Fix up BuildRequires

* Thu Dec 06 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.5-1
- First package

