%define udev_scriptdir /lib/udev

%define dbus_version 1.1
%define dbus_glib_version 0.86-3

%define gtk2_version	2.14.0
%define glib2_version	2.16.0
%define wireless_tools_version 1:28-0pre9
%define libnl_version 1.1

%global ppp_version 2.4.5

%define snapshot .git20100811
%define applet_snapshot .git20100811
%define realversion 0.8.1

Name: NetworkManager
Summary: Network connection manager and user applications
Epoch: 1
Version: 0.8.1
Release: 113%{?dist}
Group: System Environment/Base
License: GPLv2+
URL: http://www.gnome.org/projects/NetworkManager/

Source: %{name}-%{realversion}%{snapshot}.tar.bz2
Source1: network-manager-applet-%{realversion}%{applet_snapshot}.tar.bz2
Source2: NetworkManager.conf
Patch1: nm-applet-internal-buildfixes.patch
Patch2: explain-dns1-dns2.patch
Patch3: nm-applet-no-notifications.patch
Patch4: nm-dbus-glib-disable-legacy-property-access.patch
Patch10: nm-applet-mobile-status-in-panel-later.patch
Patch11: nm-ignore-hostname-localhost.patch
Patch12: rh589230-nm-i18n-fixes.patch
Patch13: rh589230-applet-i18n-fixes.patch
Patch14: rh633501-applet-fix-context-menu-sensitivity.patch
Patch15: rh636877-wifi-peap-gtc-proactive-key-caching.patch
Patch16: rh662730-dispatcher-lease-change-events.patch
Patch17: rh626337-validate-WiFi-WWAN-enabling.patch
Patch18: rh584271-preserve-wifi-state.patch
Patch19: rh665027-respect-GATEWAYDEV-for-ibft.patch
Patch20: rh666078-ifcfg-ipv6-gateway.patch
Patch21: rh668830-stop-touching-etc-hosts.patch
Patch22: rh634152-applet-display-ipv6-info.patch
Patch23: rh692578-applet-dont-save-always-ask-passwords.patch
Patch24: rh713283-nl80211-and-background-scanning.patch
Patch25: rh696585-applet-enter-confirms-secrets.patch
Patch26: rh696916-applet-gconf-fix-freed-memory-access.patch
Patch27: rh590096-send-hostname-to-dhcp-by-default.patch
Patch28: rh660666-core-ctc-devices.patch
Patch29: rh660666-plugins-libnm-util-ctc-devices.patch
Patch30: rh715494-wifi-share-auth.patch
Patch31: rh706338-suppress-get-property-warning.patch
Patch32: rh737338-ifcfg-shvar-filter-newline-chars.patch
Patch33: rh747066-wifi-adhoc-frequency.patch
Patch34: rh748075-wifi-nl80211-scan-quality.patch
Patch35: rh659685-vpn-dbus-interface-fixup.patch
Patch36: rh685096-ipoib.patch
Patch37: rh773590-prevent-user-proxy-init-warning.patch
Patch38: rh787084-suppress-dispatcher-hostname-warning.patch
Patch39: rh209339-eap-fast.patch
Patch40: rh717475-bonding.patch
Patch41: rh798294-editor-indicate-no-VPN-plugins.patch
Patch42: rh756758-dont-reconnect-WPA2-Enterprise-with-wrong-password.patch
Patch43: rh747649-update-system-connection-timestamps.patch
Patch44: rh696967-applet-about-dialog-URL-open-failure.patch
Patch45: rh719892-applet-notify-connection-failure.patch
Patch46: rh663820-dhcp-manager-allow-overriding-timeout.patch
Patch47: rh673476-dhcp-support-RFC3442-routes.patch
Patch48: rh712302-vlan.patch
Patch49: libnm-util-glib-soname-bump.patch
Patch50: bond-vlan-switch.patch
Patch51: rh809784-routes-i18n.patch
Patch52: rh717926-coverity.patch
Patch53: rh801744-dhcp-handle-same-state-changes.patch
Patch54: rh833199-ifcfg-rh-fix-eap-leap.patch
Patch55: rh834349-applet-preserve-wpa.patch
Patch56: rh813573-wpa-proto-combo.patch
Patch57: rh834444-wpa-eap-always-okc.patch
Patch58: rh840580-suppress-bluez-warning.patch
Patch59: rh465345-connection-editor-gtkbuilder.patch
Patch60: rh465345-connection-editor-tree.patch
Patch61: rh685096-connection-editor-ipoib.patch
Patch62: rh717475-bond-fixes.patch
Patch63: rh465345-connection-editor-bond.patch
Patch64: rh712302-vlan-fixes.patch
Patch65: rh712302-connection-editor-vlan.patch
Patch66: rh837056-8021x-credentials-requested-twice.patch
Patch67: rh817660-dhcp-old-leasefile-fallback.patch
Patch68: rh829499-retry-autoconnect-after-5-minutes.patch
Patch69: rh558983-bridging.patch
Patch70: rh558983-applet-bridge-bond-vlan.patch
Patch71: rh901662-bond-more-options.patch
Patch72: rh922558-dhclient-request-static-routes-option.patch
Patch73: rh906133-editor-hide-BSSID-for-adhoc.patch
Patch74: rh867273-applet-infiniband.patch
Patch75: rh713975-eap-password-ui-fix.patch
Patch76: rh973245-use-keyfile-plugin.patch
Patch77: rh923648-editor-slave-sensitive-autoconnect.patch
Patch78: rh953076-editor-bonding-mode.patch
Patch79: rh953123-editor-fix-saving-MAC-MTU.patch
Patch80: rh969363-nm-online-help.patch
Patch81: rh602265-editor-lcp-echo-options-preserve.patch
Patch82: rh602265-pppoe-reconnect-delay.patch
Patch83: rh902372-ensure-clean-bridge-bond-state-at-startup.patch
Patch84: rh905059-honor-master-autoconnect-inhibit.patch
Patch85: rh694789-gateway-ping-timeout.patch
Patch86: rh701381-wifi-rfkill-fixes.patch
Patch87: rh896198-ifcfg-fix-gateway-handling.patch
Patch88: rh919242-editor-indicate-bond-bridge-vlan-disabled.patch
Patch89: rh990310-interface-aliases.patch
Patch90: rh981325-kernel-header-workaround.patch
Patch91: rh836993-vpn-secrets-ask.patch
Patch92: rh564467-add-man-for-nm-applet-and-nm-connection-editor.patch
Patch93: rh991341-ipv6-default-route.patch
Patch94: rh758076-remove-nag-dialog-1.patch
Patch95: rh758076-remove-nag-dialog-2.patch
Patch96: rh758076-remove-nag-dialog-3.patch
Patch97: rh713975-fix-loading-security-info-1.patch
Patch98: rh713975-fix-loading-security-info-2.patch
Patch99: rh713975-fix-loading-security-info-3.patch
Patch100: rh713975-fix-loading-security-info-4.patch
Patch101: rh1010501-vpn-fix.patch
Patch102: rh1020310-fix-applet-editor-crash-addr-labels.patch
Patch103: rh1021947-ifcfg-rh-fix-bond-slave-crash.patch
Patch104: rh1021953-libnm-glib-device-VLAN-ID.patch
Patch105: rh1000839-warnings.patch
Patch106: rh1034860-pppoe-userland.patch
Patch107: rh958365-log-states-textual.patch
Patch108: rh1002138-say-adhoc.patch
Patch109: rh678079-applet-indicate-no-VPN-plugin.patch
Patch110: rh996566-gsm-validate-apn-whitespace.patch
Patch111: 0111-fix-make-check-failure.patch
Patch112: rh1025009-wol.patch
Patch113: rh1112505-applet-fix-ifname-display.patch
Patch114: rh1113996-ifcfg-rh-writer-ip4-fix.patch
Patch115: rh1111672-ifcfg-rh-routes-no-gateway.patch
Patch116: rh1111664-dbus-add-connection-return.patch
Patch117: rh1135017-ifcfgrh-bridge-stp-read-fix.patch
Patch118: rh902820-editor-bridge-support.patch
Patch119: rh902820-ifcfg-rh-fix-reading-VLAN-as-bond-slaves.patch
Patch120: rh1059698-legacy-slave-compat.patch
Patch121: rh979181-NM_CONTROLLED-by-ifname.patch
Patch122: rh1076169-ip6-unsolicited-RA-flags.patch
Patch123: rh1085015-applet-translations.patch
Patch124: rh1156564-gconf-connection-type.patch
Patch125: rh1156564-ethernet-without-wired.patch
Patch126: rh1102642-ifcfg-rh-trailing-spaces.patch
Patch127: rh1181207-fix-assert-on-slave-changes.patch
Patch128: rh1056790-arping.patch
Patch129: rh1173245-editor-always-ask-system-cons.patch
Patch130: rh1046074-bridge-multicast-snooping.patch
Patch131: rh1046074-bridge-multicast-snooping-editor.patch
Patch132: rh905641-editor-IP-treeview-improvements.patch
Patch133: rh962449-ipv6-link-local-dns-server.patch
Patch134: rh1201412-editor-addr-route-navigation-fix.patch
Patch135: rh1201416-editor-additional-error-validation-fix.patch
Patch136: 0136-covescan-fix-1.patch
Patch137: rh1063661-connection-added-signal.patch
Patch138: rh1063661-create-devices-on-status-change.patch
Patch139: rh1063661-allow-vlans-on-bonds-and-bridges.patch
Patch140: rh1063661-finish-activation-without-l3-configuration.patch
Patch141: rh1063661-allow-no-l3-configuration-for-non-ethernet.patch
Patch142: rh1063661-editor-leave-system-connection-checkbox-enabled.patch
Patch143: rh953131-applet-con-info-addresses.patch
Patch144: rh1197154-ip6-require-link-local.patch
Patch145: rh1157867-ifcfg-rh-alias-file-removing-fix.patch
Patch146: rh896200-editor-mnemonic-collisions.patch
Patch147: rh1069313-VPN-never-default.patch
Patch148: rh1207599-check-duped-addresses.patch
Patch149: rh1167491-editor-gateway-check.patch
Patch150: rh1213327-nmcli-hang-fix.patch
Patch151: rh1200131-dns-options.patch
Patch152: rh1003877-bond-primary-option-fixes.patch
Patch153: rh1213118-read-sysctl-d.patch
Patch154: rh1254070-wifi-band-locking.patch
Patch155: rh1258218-editor-vlan-id.patch
Patch156: rh787733-hide-WPA-for-adhoc.patch
Patch157: rh895591-wifi-no-secrets.patch
Patch158: rh1212553-pkcs8-priv-keys.patch
Patch159: rh1212553-editor-pkcs8-priv-keys.patch
Patch160: rh1212553-editor-private-key.patch
Patch161: rh951399-ignore-slave-devices-state.patch
Patch162: rh1202539-dns-searches.patch
Patch163: rh1286742-build-on-fedora.patch
Patch164: rh1198325-ibft-port-iBFT-standalone-plugin.patch
Patch165: rh1272617-ifcfg-rh-delay-deletions.patch
Patch166: rh1292753-initscripts-ifcfg-bbv-fixes.patch
Patch167: rh1292502-do-not-assume-bond-masters.patch
Patch168: rh887771-translations.patch
Patch169: rh1308730-dns-none.patch
Patch170: rh1331314-core-downgrade-unknown-driver-warning.patch
Patch171: rh1353033-infiniband-compare-mac.patch
Patch172: rh1321723-translations.patch
Patch173: rh1321723-translations-fixup.patch
Patch174: rh1261893-ibft-trickery.patch
Patch175: rh1412388-ui-semicolon-text.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): chkconfig
Requires(preun): chkconfig
Requires: dbus >= %{dbus_version}
Requires: dbus-glib >= %{dbus_glib_version}
Requires: glib2 >= %{glib2_version}
Requires: iproute
Requires: dhclient >= 12:4.1.0
Requires: wpa_supplicant >= 1:0.6.8-4
Requires: libnl >= %{libnl_version}
Requires: %{name}-glib = %{epoch}:%{version}-%{release}
Requires: ppp = %{ppp_version}
# No rp-pppoe on S390
%ifnarch s390 s390x
Requires: rp-pppoe
%endif
Requires: avahi-autoipd
Requires: dnsmasq
Requires: udev
Requires: mobile-broadband-provider-info >= 0.20090602
Requires: ModemManager >= 0.3-3.git20100317
Obsoletes: dhcdbd

Conflicts: NetworkManager-vpnc < 1:0.7.0.99-1
Conflicts: NetworkManager-openvpn < 1:0.7.0.99-1
Conflicts: NetworkManager-pptp < 1:0.7.0.99-1
Conflicts: NetworkManager-openconnect < 0:0.7.0.99-1

BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: dbus-glib-devel >= %{dbus_glib_version}
BuildRequires: wireless-tools-devel >= %{wireless_tools_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: libglade2-devel
BuildRequires: GConf2-devel
BuildRequires: gnome-keyring-devel
BuildRequires: gettext-devel
BuildRequires: pkgconfig
BuildRequires: wpa_supplicant
BuildRequires: libnl-devel >= %{libnl_version}
BuildRequires: libnotify-devel >= 0.4
BuildRequires: perl(XML::Parser)
BuildRequires: automake autoconf intltool libtool
BuildRequires: ppp >= 2.4.5
BuildRequires: ppp-devel >= 2.4.5
BuildRequires: nss-devel >= 3.11.7
BuildRequires: polkit-devel
BuildRequires: dhclient
BuildRequires: gtk-doc
BuildRequires: libudev-devel
BuildRequires: libuuid-devel
BuildRequires: libgudev1-devel >= 143
BuildRequires: desktop-file-utils
# No bluetooth on s390
%ifnarch s390 s390x
BuildRequires: gnome-bluetooth-libs-devel >= 2.27.7.1-1
%endif

%description
NetworkManager is a system network service that manages your network devices
and connections, attempting to keep active network connectivity when available.
It manages ethernet, WiFi, mobile broadband (WWAN), and PPPoE devices, and
provides VPN integration with a variety of different VPN services.


%package devel
Summary: Libraries and headers for adding NetworkManager support to applications
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: dbus-devel >= %{dbus_version}
Requires: dbus-glib >= %{dbus_glib_version}
Requires: pkgconfig

%description devel
This package contains various headers accessing some NetworkManager functionality
from applications.


%package gnome
Summary: GNOME applications for use with NetworkManager
Group: Applications/Internet
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-glib = %{epoch}:%{version}-%{release}
Requires: dbus >= %{dbus_version}
Requires: dbus-glib >= %{dbus_glib_version}
Requires: libnotify >= 0.4.3
Requires: gnome-keyring
Requires: nss >= 3.11.7
Requires: gnome-icon-theme
Requires(post): gtk2 >= %{gtk2_version}

%description gnome
This package contains GNOME utilities and applications for use with
NetworkManager, including a panel applet for wireless networks.


%package glib
Summary: Libraries for adding NetworkManager support to applications that use glib.
Group: Development/Libraries
Requires: dbus >= %{dbus_version}
Requires: dbus-glib >= %{dbus_glib_version}

%description glib
This package contains the libraries that make it easier to use some NetworkManager
functionality from applications that use glib.


%package glib-devel
Summary: Header files for adding NetworkManager support to applications that use glib.
Group: Development/Libraries
Requires: %{name}-devel = %{epoch}:%{version}-%{release}
Requires: %{name}-glib = %{epoch}:%{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig
Requires: dbus-glib-devel >= %{dbus_glib_version}

%description glib-devel
This package contains the header and pkg-config files for development applications using
NetworkManager functionality from applications that use glib.


%prep
%setup -q -n NetworkManager-%{realversion}

# unpack the applet and nmcli
tar -xjf %{SOURCE1}

%patch1 -p1 -b .buildfix %{?_rawbuild}
%patch2 -p1 -b .explain-dns1-dns2
%patch3 -p1 -b .no-notifications
%patch4 -p1 -b .dbus-glib-no-legacy-props
%patch10 -p1 -b .applet-mobile-status-later
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-mb-roam.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-3g.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-cdma-1x.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-edge.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-evdo.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-gprs.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-hspa.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-tech-umts.png
%{__rm} -f ./network-manager-applet-0.8.1/icons/22/nm-wwan-tower.png
%patch11 -p1 -b .ignore-hostname-localhost
%patch12 -p1 -b .nm-translations
%patch13 -p1 -b .applet-translations
%patch14 -p1 -b .applet-context-sensitivity
%patch15 -p1 -b .peap-gtc-proactive-key-caching
%patch16 -p1 -b .dispatcher-lease-change
%patch17 -p1 -b .validate-WiFi-WWAN
%patch18 -p1 -b .preserve-wifi-state
%patch19 -p1 -b .respect-GATEWAYDEV-ibft
%patch20 -p1 -b .ipv6-manual-gateway
%patch21 -p1 -b .stop-touching-etc-hosts
%patch22 -p1 -b .display-ipv6-info
%patch23 -p1 -b .dont-save-always-ask
%patch24 -p1 -b .nl80211-bgscan
%patch25 -p1 -b .applet-enter-confirms-secrets
%patch26 -p1 -b .applet-gconf-freed-memory
%patch27 -p1 -b .hostname-to-dhcp
%patch28 -p1 -b .core-ctc-devices
%patch29 -p1 -b .plugins-libnm-util-ctc-devices
%patch30 -p1 -b .wifi-share-auth
%patch31 -p1 -b .suppress-get-property-warning
%patch32 -p1 -b .filter-newline-chars
%patch33 -p1 -b .adhoc-freq
%patch34 -p1 -b .nl80211-scan-quality
%patch35 -p1 -b .vpn-dbus-fixup
%patch36 -p1 -b .ipoib
%patch37 -p1 -b .user-proxy-init
%patch38 -p1 -b .dispatcher-hostname-warning
%patch39 -p1 -b .eap-fast
%patch40 -p1 -b .bonding
%patch41 -p1 -b .no-VPN-plugins
%patch42 -p1 -b .WPA2-Enterprise-wrong-password
%patch43 -p1 -b .system-connection-timestamps
%patch44 -p1 -b .about-dialog-URL
%patch45 -p1 -b .applet-notify-con-failure
%patch46 -p1 -b .dhcp-override-timeout
%patch47 -p1 -b .dhcp-support-RFC3442
%patch48 -p1 -b .vlan
%patch49 -p1 -b .libnm-util-glib-soname
%patch50 -p1 -b .bond-vlan-switch
%patch51 -p1 -b .routes
%patch52 -p1 -b .coverity
%patch53 -p1 -b .dhclient-same-state
%patch54 -p1 -b .ifcfgrh-eap-leap
%patch55 -p1 -b .applet-preserve-wpa
%patch56 -p1 -b .wpa-proto-combo
%patch57 -p1 -b .wpa-eap-always-okc
%patch58 -p1 -b .suppress-bluez-warning
%patch59 -p1 -b .gtkbuilder
%patch60 -p1 -b .tree
%patch61 -p1 -b .ce-ipoib
%patch62 -p1 -b .bond-fixes
%patch63 -p1 -b .ce-bond
%patch64 -p1 -b .vlan-fixes
%patch65 -p1 -b .ce-vlan
%patch66 -p1 -b .8021x-twice
%patch67 -p1 -b .inherity-leasefiles
%patch68 -p1 -b .retry-connections
%patch69 -p1 -b .bridging
%patch70 -p1 -b .applet-bridge-bond-vlan
%patch71 -p1 -b .bond-more-options
%patch72 -p1 -b .dhclient-static-routes
%patch73 -p1 -b .editor-hide-adhoc-BSSID
%patch74 -p1 -b .applet-infiniband
%patch75 -p1 -b .eap-password-ui
%patch76 -p1 -b .keyfile
%patch77 -p1 -b .sensitive-autoconnect
%patch78 -p1 -b .editor-bonding-mode
%patch79 -p1 -b .editor-vlan-mac-mtu
%patch80 -p1 -b .nm-online-help
%patch81 -p1 -b .editor-lcp-echo-options
%patch82 -p1 -b .pppoe-reconnect-delay
%patch83 -p1 -b .clean-bridge-bond
%patch84 -p1 -b .master-autoconnect-inhibit
%patch85 -p1 -b .gateway-ping-timeout
%patch86 -p1 -b .wifi-rfkill
%patch87 -p1 -b .ifcfg-fix-gateway-handling
%patch88 -p1 -b .editor-bbv-disabled
%patch89 -p1 -b .interface-aliases
%patch90 -p1 -b .kernel-header-workaround
%patch91 -p1 -b .vpn-secrets-ask
%patch92 -p1 -b .add-man-for-nm-applet-and-nm-connection-editor
%patch93 -p1 -b .ipv6-default-route
%patch94 -p1 -b .remove-nag-dialog-1
%patch95 -p1 -b .remove-nag-dialog-2
%patch96 -p1 -b .remove-nag-dialog-3
%patch97 -p1 -b .fix-loading-security-info-1
%patch98 -p1 -b .fix-loading-security-info-2
%patch99 -p1 -b .fix-loading-security-info-3
%patch100 -p1 -b .fix-loading-security-info-4
%patch101 -p1 -b .vpn-fix
%patch102 -p1 -b .fix-applet-editor-addr-labels
%patch103 -p1 -b .ifcfg-rh-fix-bond-slave-crash
%patch104 -p1 -b .libnm-glib-device-VLAN-ID
%patch105 -p1 -b .warnings
%patch106 -p1 -b .pppoe-userland
%patch107 -p1 -b .log-states-textual
%patch108 -p1 -b .adhoc
%patch109 -p1 -b .rh678079-applet-indicate-no-VPN-plugin
%patch110 -p1 -b .0110-rh996566-gsm-validate-apn-whitespace.orig
%patch111 -p1 -b .0111-fix-make-check-failure.orig
%patch112 -p1 -b .wol
%patch113 -p1 -b .rh1112505-applet-fix-ifname-display
%patch114 -p1 -b .rh1113996-ifcfg-rh-writer-ip4-fix
%patch115 -p1 -b .rh1111672-ifcfg-rh-routes-no-gateway
%patch116 -p1 -b .rh1111664-dbus-add-connection-return
%patch117 -p1 -b .rh1135017-ifcfgrh-bridge-stp-read-fix
%patch118 -p1 -b .rh902820-editor-bridge-support
%patch119 -p1 -b .rh902820-ifcfg-rh-fix-reading-VLAN-as-bond-slaves
%patch120 -p1 -b .rh1059698-legacy-slave-compat
%patch121 -p1 -b .rh979181-NM_CONTROLLED-by-ifname
%patch122 -p1 -b .rh1076169-ip6-unsolicited-RA-flags
%patch123 -p1 -b .rh1085015-applet-translations
%patch124 -p1 -b .rh1156564-gconf-connection-type
%patch125 -p1 -b .rh1156564-ethernet-without-wired
%patch126 -p1 -b .rh1102642-ifcfg-rh-trailing-spaces
%patch127 -p1 -b .rh1181207-fix-assert-on-slave-changes
%patch128 -p1 -b .rh1056790-arping
%patch129 -p1 -b .rh1173245-editor-always-ask-system-cons
%patch130 -p1 -b .rh1046074-bridge-multicast-snooping
%patch131 -p1 -b .rh1046074-bridge-multicast-snooping-editor
%patch132 -p1 -b .rh905641-editor-IP-treeview-improvements
%patch133 -p1 -b .rh962449-ipv6-link-local-dns-server.orig
%patch134 -p1 -b .rh1201412-editor-addr-route-navigation-fix
%patch135 -p1 -b .rh1201416-editor-additional-error-validation-fix
%patch136 -p1 -b .0136-covescan-fix-1
%patch137 -p1 -b .rh1063661-connection-added-signal
%patch138 -p1 -b .rh1063661-create-devices-on-status-change
%patch139 -p1 -b .rh1063661-allow-vlans-on-bonds-and-bridges
%patch140 -p1 -b .rh1063661-finish-activation-without-l3-configuration
%patch141 -p1 -b .rh1063661-allow-no-l3-configuration-for-non-ethernet
%patch142 -p1 -b .rh1063661-editor-leave-system-connection-checkbox-enabled
%patch143 -p1 -b .rh953131-applet-con-info-addresses
%patch144 -p1 -b .rh1197154-ip6-require-link-local
%patch145 -p1 -b .rh1157867-ifcfg-rh-alias-file-removing-fix
%patch146 -p1 -b .rh896200-editor-mnemonic-collisions
%patch147 -p1 -b .rh1069313-VPN-never-default
%patch148 -p1 -b .rh1207599-check-duped-addresses
%patch149 -p1 -b .rh1167491-editor-gateway-check
%patch150 -p1 -b .rh1213327-nmcli-hang-fix
%patch151 -p1 -b .rh1200131-dns-options
%patch152 -p1 -b .rh1003877-bond-primary-option-fixes
%patch153 -p1 -b .rh1213118-read-sysctl-d
%patch154 -p1 -b .rh1254070-wifi-band-locking
%patch155 -p1 -b .rh1258218-editor-vlan-id
%patch156 -p1 -b .rh787733-hide-WPA-for-adhoc
%patch157 -p1 -b .rh895591-wifi-no-secrets
%patch158 -p1 -b .rh1212553-pkcs8-priv-keys
%patch159 -p1 -b .rh1212553-editor-pkcs8-priv-keys
%patch160 -p1 -b .rh1212553-editor-private-key
%patch161 -p1 -b .rh951399-ignore-slave-devices-state
%patch162 -p1 -b .rh1202539-dns-searches
%patch163 -p1 -b .rh1286742-build-on-fedora
%patch164 -p1 -b .rh1198325-ibft-port-iBFT-standalone-plugin
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-dns1
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-dns2
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-entry
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-gateway
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-ipaddr
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-bad-record
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-dhcp
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-static
chmod +x system-settings/plugins/ibft/tests/iscsiadm-test-vlan
%patch165 -p1 -b .rh1272617-ifcfg-rh-delay-deletions
%patch166 -p1 -b .rh1292753-initscripts-ifcfg-bbv-fixes.orig
%patch167 -p1 -b .rh1292502-do-not-assume-bond-masters.orig
%patch168 -p1 -b .rh887771-translations.orig
%patch169 -p1 -b .rh1308730-dns-none.orig
%patch170 -p1 -b .rh1331314-core-downgrade-unknown-driver-warning.orig
%patch171 -p1 -b .rh1353033-infiniband-compare-mac.orig
%patch172 -p1 -b .rh1321723-translations.orig
%patch173 -p1 -b .rh1321723-translations-fixup.orig
%patch174 -p1 -b .rh1261893-ibft-trickery.orig
%patch175 -p1 -b .rh1412388-ui-semicolon-text.orig

%build

# back up pristine docs and use them instead of generated ones, which make
# multilib unhappy due to different timestamps in the generated content
%{__cp} -R docs ORIG-docs

autoreconf -i
%configure \
	--disable-static \
	--with-distro=redhat \
	--with-dhclient=yes \
	--with-dhcpcd=no \
	--with-crypto=nss \
%if (0%{?fedora} && 0%{?fedora} >= 21)
	--enable-more-warnings=yes \
%else
	--enable-more-warnings=error \
%endif
	--with-docs=yes \
	--with-system-ca-path=/etc/pki/tls/certs \
	--with-tests=yes \
	--with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version} \
	--with-dist-version=%{version}-%{release}

# Make sure docs are completely regenerated by cleaning prebuild stuff
pushd docs/libnm-glib
	make clean
	rm -rf html tmpl
popd
pushd docs/libnm-util
	make clean
	rm -rf html tmpl
popd

# Build NetworkManager
make %{?_smp_mflags}

# build the applet
pushd network-manager-applet-%{realversion}
	autoreconf -i
	intltoolize --force
	%configure \
%if (0%{?fedora} && 0%{?fedora} >= 21)
		--enable-more-warnings=yes \
%else
		--enable-more-warnings=error \
%endif
		--disable-static
	make %{?_smp_mflags}
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT

# install NM
make install DESTDIR=$RPM_BUILD_ROOT

%{__cp} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

# install the applet
pushd network-manager-applet-%{realversion}
  make install DESTDIR=$RPM_BUILD_ROOT
popd

# create a VPN directory
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/VPN

# create a keyfile plugin system settings directory
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/NetworkManager/system-connections

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/gnome-vpn-properties

%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/lib/NetworkManager

%find_lang %{name}
%find_lang nm-applet
cat nm-applet.lang >> %{name}.lang

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/pppd/%{ppp_version}/*.la
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/gnome-bluetooth/plugins/*.la

install -m 0755 test/.libs/nm-online %{buildroot}/%{_bindir}

# install the pristine docs
%{__cp} ORIG-docs/libnm-glib/html/* $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/libnm-glib/
%{__cp} ORIG-docs/libnm-util/html/* $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/libnm-util/

# don't autostart in KDE on F13+ (#541353)
%if 0%{?fedora} > 12
echo 'NotShowIn=KDE;' >>$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%endif

# validate the autostart .desktop file
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/nm-applet.desktop


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%post
if [ "$1" == "1" ]; then
	/sbin/chkconfig --add NetworkManager
	/sbin/chkconfig NetworkManager resetpriorities
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service NetworkManager stop >/dev/null 2>&1
    killall -TERM nm-system-settings >/dev/null 2>&1
    /sbin/chkconfig --del NetworkManager
fi

%triggerun -- NetworkManager < 1:0.7.0-0.9.2.svn3614
/sbin/service NetworkManagerDispatcher stop >/dev/null 2>&1
/sbin/chkconfig --del NetworkManagerDispatcher
exit 0

%post	glib -p /sbin/ldconfig
%postun	glib -p /sbin/ldconfig

%pre gnome
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  if [ -f "%{_sysconfdir}/gconf/schemas/nm-applet.schemas" ]; then
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/nm-applet.schemas >/dev/null
  fi
fi

%preun gnome
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  if [ -f "%{_sysconfdir}/gconf/schemas/nm-applet.schemas" ]; then
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/nm-applet.schemas >/dev/null
  fi
fi

%post gnome
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
if [ -f "%{_sysconfdir}/gconf/schemas/nm-applet.schemas" ]; then
  gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/nm-applet.schemas >/dev/null
fi

%postun gnome
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc COPYING NEWS AUTHORS README CONTRIBUTING TODO
%{_sysconfdir}/dbus-1/system.d/NetworkManager.conf
%{_sysconfdir}/dbus-1/system.d/nm-dhcp-client.conf
%{_sysconfdir}/dbus-1/system.d/nm-avahi-autoipd.conf
%{_sysconfdir}/dbus-1/system.d/nm-dispatcher.conf
%{_sysconfdir}/dbus-1/system.d/nm-ifcfg-rh.conf
%config %{_sysconfdir}/rc.d/init.d/NetworkManager
%{_sbindir}/%{name}
%{_bindir}/nmcli
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/dispatcher.d
%dir %{_sysconfdir}/%{name}/VPN
%config(noreplace) %{_sysconfdir}/%{name}/NetworkManager.conf
%{_bindir}/nm-tool
%{_bindir}/nm-online
%{_libexecdir}/nm-dhcp-client.action
%{_libexecdir}/nm-avahi-autoipd.action
%{_libexecdir}/nm-dispatcher.action
%dir %{_libdir}/NetworkManager
%{_libdir}/NetworkManager/*.so*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{_localstatedir}/run/NetworkManager
%dir %{_localstatedir}/lib/NetworkManager
%{_prefix}/libexec/nm-crash-logger
%dir %{_datadir}/NetworkManager
%{_datadir}/NetworkManager/gdb-cmd
%dir %{_sysconfdir}/NetworkManager/system-connections
%{_datadir}/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
%{_libdir}/pppd/%{ppp_version}/nm-pppd-plugin.so
%{_datadir}/polkit-1/actions/*.policy
%{udev_scriptdir}/rules.d/*.rules

%files devel
%defattr(-,root,root,0755)
%doc ChangeLog docs/spec.html
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_includedir}/%{name}/NetworkManagerVPN.h
%{_libdir}/pkgconfig/%{name}.pc

%files gnome
%defattr(-,root,root,0755)
%{_sysconfdir}/dbus-1/system.d/nm-applet.conf
%{_bindir}/nm-applet
%{_bindir}/nm-connection-editor
%{_datadir}/applications/*.desktop
%{_datadir}/nm-applet/
%{_datadir}/icons/hicolor/16x16/apps/*.png
%{_datadir}/icons/hicolor/22x22/apps/*.png
%{_datadir}/icons/hicolor/32x32/apps/*.png
%{_datadir}/icons/hicolor/48x48/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_mandir}/man1/*
%{_sysconfdir}/xdg/autostart/nm-applet.desktop
%dir %{_datadir}/gnome-vpn-properties
%{_sysconfdir}/gconf/schemas/nm-applet.schemas
%ifnarch s390 s390x
%if !(0%{?fedora} && 0%{?fedora} >= 21)
%{_libdir}/gnome-bluetooth/plugins/*
%endif
%endif

%files glib
%defattr(-,root,root,0755)
%{_libdir}/libnm-glib.so.*
%{_libdir}/libnm-glib-vpn.so.*
%{_libdir}/libnm-util.so.*

%files glib-devel
%defattr(-,root,root,0755)
%dir %{_includedir}/libnm-glib
%{_includedir}/libnm-glib/*.h
%{_includedir}/%{name}/nm-*.h
%{_libdir}/pkgconfig/libnm-glib.pc
%{_libdir}/pkgconfig/libnm-glib-vpn.pc
%{_libdir}/pkgconfig/libnm-util.pc
%{_libdir}/libnm-glib.so
%{_libdir}/libnm-glib-vpn.so
%{_libdir}/libnm-util.so
%dir %{_datadir}/gtk-doc/html/libnm-glib
%{_datadir}/gtk-doc/html/libnm-glib/*
%dir %{_datadir}/gtk-doc/html/libnm-util
%{_datadir}/gtk-doc/html/libnm-util/*

%changelog
* Thu Jan 12 2017 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-113
- ibft: don't break down when a dynamic connection without address (rh #1261893)

* Thu Jan 12 2017 Thomas Haller <thaller@redhat.com> - 1:0.8.1-112
- po: fix invalid texts in UI containing trailing semicolon (rh #1412388)

* Mon Dec 19 2016 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-111
- ibft: rework the connection matching to use addressing data (rh #1261893)

* Thu Dec 15 2016 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-110
- ibft: always commit the initial configuration right away (rh #1261893)

* Mon Dec 12 2016 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-109
- ibft: avoid deconfiguring ibft-managed interfaces on startup (rh #1261893)

* Thu Oct 13 2016 Beniamino Galvani <bgalvani@redhat.com> - 1:0.8.1-108
- dns: added new dns=none option to disable updating of resolv.conf (rh #1308730)
- core: downgrade message level for unknown device driver (rh #1331314)
- infiniband: compare only last 8 octects for MAC address (rh #1353033)
- po: update translation (rh #1321723)

* Wed Mar 16 2016 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-107
- wifi: move the Ad-Hoc WPA check to the correct place (rh #787733)

* Sun Mar  6 2016 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-106
- po: update translations (rh #887771)

* Mon Jan 11 2016 Beniamino Galvani <bgalvani@redhat.com> - 1:0.8.1-105
- ifcfg-rh: delay handling of deletion events (rh #1272617)
- ifcfg-rh: load connections during GetIfcfgDetails avoiding ifup race (rh #1292753)
- ifcfg-rh: leave bridge/bond/vlan to initscripts when support disabled (rh #1292753)
- bond: avoid assuming connections on bond masters that are not up (rh #1292502)

* Tue Dec  1 2015 Thomas Haller <thaller@redhat.com> - 1:0.8.1-104
- core: ignore slave devices when deciding global state (rh #951399)
- dns: don't override DHCP-supplied search order with domain (rh #1202539)
- build: fix building source package on recent Fedora (rh #1286742)
- ibft: add settings plugin (rh #1198325)

* Thu Nov  5 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-103
- libnm-util/editor: recognize PKCS#8 private keys and check passwords (rh #1212553)
- wifi: show certificate files with the *.key extension (rh #1212553)

* Wed Nov  4 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-102
- wifi: don't retry activation of connections with wrong secrets (rh #895591)

* Mon Aug 31 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-101
- wifi: support locking connections to a band (5GHz or 2GHz) (rh #1254070)
- editor: allow VLAN id <0-4095> (rh #1258218)
- wifi: disable Ad-Hoc WPA connections (rh #787733)

* Tue Aug 18 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-100
- initscript: Make NetworkManager process /etc/sysctl.d/* (rh #1213118)

* Fri May 22 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-99
- editor: add bond 'primary' option (rh #1003877)

* Thu May 14 2015 Beniamino Galvani <bgalvani@redhat.com> - 1:0.8.1-98
- add support for DNS options (rh #1200131)

* Mon Apr 13 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-97
- vpn: let plugins forbid VPN connections from getting the default route (rh #1069313)
- core: don't duplicate addresses (and other) info in IP configs (rh #1207599)
- editor: check gateway to be in the network specified by addr/prefix (rh #1167491)
- cli: fix 'nmcli con' hang if both NetworkManager and nm-applet are stopped (rh #1213327)

* Wed Apr  8 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-96
- ifcfg-rh: don't remove base connection if an alias file is removed (rh #1157867)
- editor: fix mnemonic collisions (rh #896200)

* Fri Apr  3 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-95
- ip6-manager: ensure we don't get past GOT_LINK_LOCAL if we don't have a link-local address (rh #1197154)

* Mon Mar 30 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-94
- editor: additional fix for navigation in address/route treeview (rh #1201412)

* Wed Mar 25 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-93
- applet: display all addresses in "Connection Information" dialog (rh #953131)

* Wed Mar 18 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-92
- rh1063661-allow-no-l3-configuration-for-non-ethernet.patch: fix a use-after-free() (rh #1063661)

* Wed Mar 18 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-91
- Add support for vlans over bonds and fix associated issues:
- rh1113996-ifcfg-rh-writer-ip4-fix.patch: canonicalize paths (rh #1063661)
- rh558983-bridging.patch: fix NM_BOND_BRIDGE_VLAN_ENABLED parsing (rh #1063661)
- rh919242-editor-indicate-bond-bridge-vlan-disabled.patch: fix dbus call (rh #1063661)
- system-settings: for non-ethernet devices, lacking BOOTPROTO implies no L3 configuration (rh #1063661)
- device: allow vlans on bond and bridges (rh #1063661)
- ifcfg-rh: always signal connection added when loading a connection (rh #1063661)
- manager: try to create virtual devices on device state changes (rh #1063661)
- connection-editor,vlan: don't disable the system connection checkbox if the connection is not valid (rh #1063661)
- device: make the activation succeed if no L3 configuration is desired (rh #1063661)

* Wed Mar 18 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-90
- editor: improve navigation in address/route treeview (rh #1201412)
- editor: fix on-the-fly color validation for 0.0.0.0/:: (rh #1201416)

* Wed Mar 11 2015 Thomas Haller <thaller@redhat.com> - 1:0.8.1-89
- dns: handle scope-id for IPv6 link-local dns servers (rh #962449)

* Wed Mar  4 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-88
- editor: improved IP/routes editing and error highlighting (rh #905641)

* Mon Mar  2 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-87
- editor: support bridge multicast_snooping option (rh #1046074)

* Thu Feb 26 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-86
- core: support bridge multicast_snooping option (rh #1046074)

* Wed Feb 25 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-85
- editor: disable "Ask for this password every time" for system connections (rh #1173245)

* Fri Feb 20 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-84
- device: send ARPs when configuring static IPv4 addresses (rh #1056790)

* Thu Feb 19 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-83
- device: do not crash on removing slave ifcfg files (rh #1181207)

* Wed Jan 14 2015 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-82
- ifcfg-rh: strip trailing whitespace from ifcfg files (rh #1102642)
- Don't use rp-pppoe dependency on s390/s390x (rh #1181205)

* Tue Jan 13 2015 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-81
- libnm: avoid using incomplete connections from GConf (rh #1156564)
- ethernet: don't crash on ethernet connections without wired settings (rh #1156564)

* Mon Dec 15 2014 Dan Winship <danw@redhat.com> - 1:0.8.1-80
- applet, connection-editor: updated translations (rh #1085015)

* Fri Dec 05 2014 Lubomir Rintel <lrintel@redhat.com> - 1:0.8.1-79
- ip6: Process RA flags from an unsolicited RA as well (rh #1076169)
- Add a dependency on pppoe (rh #1159369)

* Fri Nov 21 2014 Dan Winship <danw@redhat.com> - 1:0.8.1-78
- ifcfg-rh: write bond slaves backward-compatibly with "ifup" (rh #1059698)
- ifcfg-rh: allow marking configs NM_CONTROLLED=no by DEVICE (rh #979181)

* Thu Aug 28 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-77
- ifcfg-rh: ensure missing STP property is interpreted as "off" (rh #1135017)
- editor: enhance nm-connection-editor to support bridges (rh #902820)
- ifcfg-rh: fix handling VLAN connections as bond/bridge slaves (rh #902820)

* Mon Aug 25 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-76
- ifcfg-rh: allow missing and 0.0.0.0 GATEWAYn lines in ifcfg-routes (rh #1111672)
- core: add AddConnectionReturn() method to system settings service (rh #1111664)

* Mon Jun 30 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-75
- fcfg-rh: fix assertion on missing IP4 setting while writing connection (rh #1113996)

* Tue Jun 24 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-74
- applet: display interface names with underscores correctly (rh #1112505)

* Wed Jun 11 2014 Dan Winship <danw@redhat.com> - 1:0.8.1-73
- core: don't take down Wake-on-LAN devices when suspending (rh #1025009)

* Fri May 30 2014 Thomas Haller <thaller@redhat.com> - 1:0.8.1-72
- core: validate GSM APN setting and remove spaces (rh #996566)

* Wed May 28 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-71
- applet: don't offer VPN connections when no VPN plugin installed (rh #678079)

* Mon May 19 2014 Dan Winship <danw@redhat.com> - 1:0.8.1-70
- applet: clarify that created wireless networks are ad-hoc (rh #1002138)

* Wed Apr 30 2014 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-69
* core: log device/vpn states as codes and descriptive text (rh #958365)

* Fri Apr  4 2014 Dan Winship <danw@redhat.com> - 1:0.8.1-68
- ppp-manager: use userland pppoe (rh #1034860)

* Thu Dec  5 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-67
- core: remove some spurious warnings (rh #1000839)

* Tue Oct 22 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-66
- libnm-glib: fix getting VLAN ID for NM clients (rh #1021953)

* Tue Oct 22 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-65
- ifcfg-rh: fix a crash when writing bonding slave connection (rh #1021947)

* Fri Oct 18 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-64
- applet/editor: fix a crash while handling user connections in GConf (rh #1020310)

* Fri Sep 27 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-63
- vpn: fix connecting to VPN (rh #1010501)

* Tue Sep 17 2013 Thomas Haller <thaller@redhat.com> - 1:0.8.1-62
- fix segfault in nm-applet when having devices without description (rh #1008884)

* Fri Sep 13 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-61
- fix ifcfg IP aliases interaction with nm-connection-editor (rh #990310)

* Thu Sep 12 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-60
- core: bump libnm-glib and libnm-glib-vpn sonames for new API (rh #836993)

* Thu Sep 12 2013 Thomas Haller <thaller@redhat.com> - 1:0.8.1-59
- applet: remove nag dialog for missing CA certificate (rh #758076)
- connection-editor: fixup preserve EAP passwords between options (rh #713975)

* Tue Sep 10 2013 Thomas Haller <thaller@redhat.com> - 1:0.8.1-58
- man: add manual pages for nm-applet (rh #564465)
- man: add manual pages for nm-connection-editor (rh #564467)
- core: don't fight with the kernel over the default IPv6 route (rh #991341)

* Mon Sep  9 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-57
- core: allow VPN plugins to request new secrets while connecting (rh #836993)

* Wed Aug 28 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-56
- build: workaround problem in a kernel header (rh #981325)

* Wed Aug  7 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-55
- support interface aliases specified in ifcfg files (rh #990310)

* Fri Jul 19 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-54
- core: add option to delay signalling connections until gateway can be pinged (rh #694789)
- core: better handling of rfkill and Enable Wireless checkbox (rh #701381)
- ifcfg-rh: fix handling of generic GATEWAY property to match iniscripts (rh #896198)
- editor: indicate when Bond/Bridge/VLAN is disabled (rh #919242)

* Fri Jul 12 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-53
- core: add PPPoE reconnect delay to fix reconnection issues (rh #602265)
- editor: preserve PPP LCP echo options (rh #602265)
- core: ensure clean bridge/bond state at startup (rh #902372)
- core: ensure master interface autoconnect setting is honored when starting slaves (rh #905059)

* Fri Jul 12 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-52
- nm-online: describe '--timeout' option more exactly (rh #969363)

* Wed Jul 10 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-52
- connection-editor: save cloned MAC and MTU for VLAN connections (rh #953123)

* Mon Jul  8 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-52
- connection-editor: fix saving bonding modes (rh #953076)

* Thu Jul  4 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-51
- connection-editor: sensitive autoconnect for bond slaves (rh #923648)

* Wed Jun 12 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-50
- settings: support system-wide wwan/vpn connections (#973245)

* Tue Jun  4 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-49
- connection-editor: preserve EAP passwords between options (rh #713975)

* Fri May 31 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-48
- applet: show InfiniBand devices in nm-applet (rh #867273)

* Fri May 31 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-47
- editor: hide BSSID for Ad-Hoc connections (rh #906133)

* Thu May 30 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-46
- dhcp: make dhclient request 'static-routes' option from DHCP server (rh #922558)

* Thu May 30 2013 Jiří Klimeš <jklimes@redhat.com> - 1:0.8.1-45
- libnm-util: fix handling 'primary' bonding option (rh #905532)
- ifcfg-rh: fix sanitizing 'arp_ip_target' bonding option (rh #905532)
- core: better detect 'miimon' and 'arp_interval' zero values (rh #905532)

* Fri May 24 2013 Dan Winship <danw@redhat.com> - 1:0.8.1-44
- applet: fix bridge/bond/vlan support (rh #915480)

* Wed Jan 23 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-43
- core: handle addition bond options (rh #901662)

* Wed Jan 23 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-42
- core: ensure NM_BRIDGE_BOND_VLAN_ENABLED applies to bridges (rh #558983)

* Tue Jan 22 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-41
- core: additional fixes for bridging and bonding operation (rh #558983)
- applet: add support for Bridge, Bond, and VLAN devices

* Fri Jan 18 2013 Dan Williams <dcbw@redhat.com> - 1:0.8.1-40
- core: fixes for bridging and bonding operation (rh #558983)

* Tue Oct 16 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-39
- core: bump libnm-util and libnm-glib soname minor versions for new API

* Mon Oct 15 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-38
- core: add support for bridge interfaces (rh #558983)

* Tue Oct  9 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-37
- core: fix 802.1x credentials being requested twice (rh #837056)
- core: inherit leasefiles from the initramfs (rh #817660)
- core: periodically retry connections even if they have failed (rh #829499)

* Thu Oct  4 2012 Dan Winship <danw@redhat.com> - 1:0.8.1-36
- connection-editor: add VLAN support (rh #712302)
- libnm-util: add API for VLAN connection editor
- core: add more checks to VLAN creation
- ifcfg-rh: fix writing of VLAN connections
- misc other small connection editor UI updates

* Fri Sep 14 2012 Dan Winship <danw@redhat.com> - 1:0.8.1-35
- ifcfg-rh: fix writing of bond connections (rh #717475, rh #838907)
- ifcfg-rh: fix reading of InfiniBand bond slaves (rh #717475)
- connection-editor: add bond support (rh #465345)

* Thu Sep 13 2012 Dan Winship <danw@redhat.com> - 1:0.8.1-34
- connection-editor: switch from notebook to tree (part of rh #465345)
- connection-editor: add InfiniBand support (rh #685096)

* Thu Sep  6 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-34
- core: always use Opportunistic Key Caching with WPA-Enterprise (rh #834444)
- core: suppress warning when Bluez is not installed (rh #840580)
- ifcfg-rh: fix handling of EAP-LEAP connections (rh #833199)
- applet: preserve WPA protocol and ciphers when editing connections (rh #834349)
- applet: show WPA protocol widget when GConf key is set (rh #813573)

* Wed May 16 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-33
- core: fix handling of dhclient same-state transitions (rh #801744)

* Tue May  1 2012 Dan Winship <danw@redhat.com> - 1:0.8.1-32
- Fix bugs noticed by Coverity (rh #717926)

* Mon Apr 30 2012 Dan Williams <dcbw@redhat.com> - 1:0.8.1-31
- core: fix carrier handling on devices that don't support carrier detection
- core: fix handling of bond/VLAN enable config option (rh #804797)

* Tue Apr 10 2012 Dan Winship <danw@redhat.com> - 1:0.8.1-30
- applet: fix translation of "Routes..." button (rh #809784)

* Thu Apr  5 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-29
- core: fix libnl error handling for libnl compatible layer (rh #712302)

* Fri Mar 23 2012 Dan Williams <dcbw@redhat.com> - 0.8.1-28
- core: turn bond/VLAN support off by default (rh #804797)

* Thu Mar 15 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-27
- core: add keyfile plugin support for InfiniBand (rh #685096)
- core: use capital 'B' in InfiniBand name (rh #685096)
- docs: fix some docs generation errors (rh #685096) (rh #717475) (rh #712302)

* Fri Mar  9 2012 Dan Williams <dcbw@redhat.com> - 0.8.1-26
- libnm-glib/libnm-util: bump library minor version for API additions

* Fri Mar  9 2012 Dan Williams <dcbw@redhat.com> - 0.8.1-25
- core: rebase bonding patch to latest upstream git master (rh #717475)
- core: add support for VLAN interfaces (rh #712302)
- docs/cli: fix some infiniband omissions (rh #685096)

* Mon Mar  5 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-24
- dhcp: add support for classless static routes (RFC3442) (rh #673476)

* Sun Mar  4 2012 Dan Williams <dcbw@redhat.com> - 0.8.1-23
- core: rebase bonding patch to latest upstream git master (rh #717475)

* Fri Mar  2 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-22
- applet: show an error dialog when "about" dialog URL is clicked without installed browser (rh #696967)
- applet: display notifications for connection failures (rh #719892)
- dhcp: allow overriding DHCP timeout with an option from dhcp configuration (rh #663820)

* Wed Feb 29 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-21
- editor: add describing tooltip for "Add" button when no VPN plugins are installed (rh #798294)
- wifi: don't allow re-connecting to WPA2 Enterprise networks with wrong password (rh #756758)
- core: update system connection timestamps ('Last Used' column in the editor) (rh #747649)

* Fri Feb 24 2012 Thomas Graf <tgraf@redhat.com> - 0.8.1-20
- Initial bonding support (rh #717475)

* Thu Feb 23 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-19
- core/gui: add EAP-FAST authentication (rh #209339)

* Mon Feb 20 2012 Dan Williams <dcbw@redhat.com> - 0.8.1-18
- core: misc IPoIB fixes (rh #685096)

* Wed Feb 15 2012 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-17
- core: don't yield a warning when initializing user settings proxy (rh #773590)
- dispatcher: suppress invalid warnings for 'hostname' action (rh #787084)

* Tue Dec 13 2011 Dan Winship <danw@redhat.com> - 1:0.8.1-16
- Initial IP-over-Infiniband support (rh #685096)

* Wed Oct 26 2011 Dan Williams <dcbw@redhat.com> - 0.8.1-15
- wifi: calculate quality correctly with nl80211/mac80211 drivers (rh #748075)
- wifi: fix Ad-Hoc associations when using nl80211/mac80211 drivers (rh #747066)
- vpn: fix D-Bus interface properties export (rh #659685)

* Fri Sep 23 2011 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-14
- ifcfg-rh: CVE-2011-3364: filter newline characters when writing into ifcfg-* files (rh #737338)

* Thu Sep 22 2011 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-13
- ifcfg-rh: CVE-2011-3364: filter newline characters when writing into ifcfg-* files (rh #737338)

* Mon Aug 15 2011 Dan Williams <dcbw@redhat.com> - 0.8.1-12
- libnm-glib: suppress warnings when D-Bus device property request fails (rh #706338)

* Wed Jul 27 2011 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-11
- core: CVE-2011-2176: check for authorization when activating shared wifi connections (rh #709662)

* Tue Jul 26 2011 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-10
- wifi: use nl80211 supplicant driver and background scanning (rh #713283)
- applet: pressing Enter in secrets dialogs comfirms them (rh #696585)
- applet: fix freed memory access on reading gconf entries (rh #696916)
- core: send hostname to DHCP server by default (rh #590096)
- core: handle s390 CTC-type devices (rh #660666)

* Mon May  2 2011 Dan Williams <dcbw@redhat.com> - 0.8.1-9
- applet: don't save passwords marked "always ask" (rh #692578)

* Wed Apr  6 2011 Jiří Klimeš <jklimes@redhat.com> - 0.8.1-8
- applet: display IPv6 info under applet's 'Connection Information' (rh #634152)
- applet,nm: fix translations (rh #589230)

* Thu Feb  3 2011 Dan Williams <dcbw@redhat.com> - 0.8.1-7
- core: add DHCP lease-change events to the dispatcher (rh #662730)
- core: validate Enable/Disable WiFi and WWAN requests (rh #626337)
- core: don't update /etc/hosts with current hostname (rh #668830)
- wifi: ensure Enabled state is preserved regardless of rfkill (rh #584271)
- ifcfg-rh: respect GATEWAYDEV for ibft/iSCSI configs (rh #665027)
- ifcfg-rh: handle IPv6 gateway correctly for static addressing configs (rh #666078)

* Tue Sep 28 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-6
- core: enable proactive key caching when using PEAP-GTC (rh #636877)
- applet: fix inital sensitivity of context menu checkboxes (rh #633501)
- applet: fix Punjabi translations (rh #589230)

* Wed Aug  11 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-5
- core: quiet annoying warnings (rh #612991)
- core: fix retrieval of various IP options in libnm-glib (rh #611141)
- core: ship NetworkManager.conf instead of deprecated nm-system-settings.conf (rh #606160)
- core: add short hostname to /etc/hosts too (rh #621910)
- core: recheck autoactivation when new system connections appear
- cli: wait a bit for NM's permissions check to complete (rh #614866)
- ifcfg-rh: ignore BRIDGE and VLAN configs and treat as unmanaged (rh #619863)
- man: add manpage for nm-online
- applet: fix crash saving ignore-missing-CA-cert preference (rh #619775)
- applet: hide PIN/PUK by default in the mobile PIN/PUK dialog (rh #615085)
- applet: ensure Enter closes the PIN/PUK dialog (rh #611831)
- applet: fix another crash in ignore-CA-certificate handling (rh #557495)
- editor: fix handling of Wired/s390 connections (rh #618620)

* Wed Jul 28 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-4
- core: enable DHCPv6-only configurations (rh #612445)
- core: don't fail connection immediately if DHCP lease expires (rh #616084) (rh #590874)
- core: read deprecated nm-system-settings.conf first (rh #606160)
- core: fix editing of PPPoE system connections
- core: work around twitchy frequency reporting of various wifi drivers
- core: don't tear down user connections on console changes (rh #614556)
- editor: fix crash when canceling editing in IP address pages (rh #610891)
- editor: fix handling of s390-specific options

* Wed Jul 14 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-3
- core: fix access to NMAccessPoint objects HwAddress property (rh #606147)
- core: more cleanly handle s390-specific options
- core: better behavior when missing firmware appears (rh #609587)
- core: map hostname to current IP address (rh #613821)
- ifcfg-rh: match initscripts behavior for persistent hostnames (rh #613841)
- editor: fix crash checking permissions during editor window close (rh #603566) (rh #614057)
- editor: fix listing of connections on ppc64 (rh #608663)
- applet: fix remembering "Don't warn me again" for missing CA certs (rh #610084)

* Mon Jun 28 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-2
- core: fix crash getting IPv6 nameservers via D-Bus
- core: fix possible crash updating VPN secrets (rh #587784)
- cli: print IPv6 settings too
- dhcp: look for interface-specific options in /etc/dhcp too (rh #607759)

* Sun Jun 27 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-1
- core: allow S390 subchannels for connection locking (rh #591533)
- core: don't request wifi scans when connection is BSSID-locked
- core: handle MAC spoofing/cloning (rh #447827)
- core: add domain part of hostname to resolv.conf search list (rh #600407)
- core: protect various network functions via PolicyKit (rh #585182)

* Fri Jun 25 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-0.4
- Update to 0.8.1 release candidate
- core: fix WWAN hardware enable state tracking (rh #591622)
- core: fix Red Hat initscript return value on double-start (rh #584321)
- core: add multicast route entry for IPv4 link-local connections
- core: fix connection sharing in cases where a dnsmasq config file exists
- core: fix handling of Ad-Hoc wifi connections to indicate correct network
- core: ensure VPN interface name is passed to dispatcher when VPN goes down
- ifcfg-rh: fix handling of ASCII WEP keys
- ifcfg-rh: fix double-quoting of some SSIDs (rh #606518)
- applet: ensure deleted connections are actually forgotten (rh #618973)
- applet: don't crash if the AP's BSSID isn't availabe (rh #603236)
- editor: don't crash on PolicyKit events after windows are closed (rh #572466)

* Wed May 26 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-0.3
- core: fix nm-online crash (rh #593677)
- core: fix failed suspend disables network (rh #589108)
- core: print out missing firmware errors (rh #594578)
- applet: fix device descriptions for some mobile broadband devices
- keyfile: bluetooth fixes
- applet: updated translations (rh #589230)

* Wed May 19 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-0.2.git20100519
- core: use GIO in local mode only (rh #588745)
- core: updated translations (rh #589230)
- core: be more lenient in IPv6 RDNSS server expiry (rh #590202)
- core: fix headers to be C++ compatible (rh #592783)
- core: rebuild to fix D-Bus property access (for dbus-glib CVE-2010-1172)
- applet: updated translations (rh #589230)
- applet: lock connections with well-known SSIDs to their specific AP

* Mon May 10 2010 Dan Williams <dcbw@redhat.com> - 0.8.1-0.1.git20100510
- core: fix handling of IPv6 RA flags when router goes away (rh #588560)
- bluetooth: fix crash configuring DUN connections from the wizard (rh #590666)

* Sun May  9 2010 Dan Williams <dcbw@redhat.com> - 0.8-13.git20100509
- core: restore initial accept_ra value for IPv6 ignored connections (rh #588619)
- bluetooth: fix bad timeout on PAN connections (rh #586961)
- applet: updated translations

* Wed May  5 2010 Dan Williams <dcbw@redhat.com> - 0.8-12.git20100504
- core: treat missing IPv6 configuration as ignored (rh #588814)
- core: don't flush IPv6 link-local routes (rh #587836)
- cli: update output formatting

* Mon May  3 2010 Dan Williams <dcbw@redhat.com> - 0.8-11.git20100503
- core: allow IP configuration as long as one method completes (rh #567978)
- core: don't prematurely remove IPv6 RDNSS nameservers (rh #588192)
- core: ensure router advertisements are only used when needed (rh #588613)
- editor: add IPv6 gateway editing capability

* Sun May  2 2010 Dan Williams <dcbw@redhat.com> - 0.8-10.git20100502
- core: IPv6 autoconf, DHCP, link-local, and manual mode fixes
- editor: fix saving IPv6 address in user connections

* Thu Apr 29 2010 Dan Williams <dcbw@redhat.com> - 0.8-9.git20100429
- core: fix crash when IPv6 is enabled and interface is deactivated

* Mon Apr 26 2010 Dan Williams <dcbw@redhat.com> - 0.8-8.git20100426
- core: fix issues with IPv6 router advertisement mishandling (rh #530670)
- core: many fixes for IPv6 RA and DHCP handling (rh #538499)
- core: ignore WWAN ethernet devices until usable (rh #585214)
- ifcfg-rh: fix handling of WEP passphrases (rh #581718)
- applet: fix crashes (rh #582938) (rh #582428)
- applet: fix crash with multiple concurrent authorization requests (rh #585405)
- editor: allow disabling IPv4 on a per-connection basis
- editor: add support for IPv6 DHCP-only configurations

* Thu Apr 22 2010 Dan Williams <dcbw@redhat.com> - 0.8-7.git20100422
- core: fix crash during install (rh #581794)
- wifi: fix crash when supplicant segfaults after resume (rh #538717)
- ifcfg-rh: fix MTU handling for wired connections (rh #569319)
- applet: fix display of disabled mobile broadband devices

* Thu Apr  8 2010 Dan Williams <dcbw@redhat.com> - 0.8-6.git20100408
- core: fix automatic WiFi connections on resume (rh #578141)

* Thu Apr  8 2010 Dan Williams <dcbw@redhat.com> - 0.8-5.git20100408
- core: more flexible logging
- core: fix crash with OLPC mesh devices after suspend
- applet: updated translations
- applet: fix continuous password requests for 802.1x connections (rh #576925)
- applet: many updated translations

* Thu Mar 25 2010 Dan Williams <dcbw@redhat.com> - 0.8-4.git20100325
- core: fix modem enable/disable
- core: fix modem default route handling

* Tue Mar 23 2010 Dan Williams <dcbw@redhat.com> - 0.8-3.git20100323
- core: don't exit early on non-fatal state file errors
- core: fix Bluetooth connection issues (rh #572340)
- applet: fix some translations (rh #576056)
- applet: better feedback when wrong PIN/PUK is entered
- applet: many updated translations
- applet: PIN2 unlock not required for normal modem functionality
- applet: fix wireless secrets dialog display

* Wed Mar 17 2010 Dan Williams <dcbw@redhat.com> - 0.8-2.git20100317
- man: many manpage updates
- core: determine classful prefix if non is given via DHCP
- core: ensure /etc/hosts is always up-to-date and correct (rh #569914)
- core: support GSM network and roaming preferences
- applet: startup speed enhancements
- applet: better support for OTP/token-based WiFi connections (rh #526383)
- applet: show GSM and CDMA registration status and signal strength when available
- applet: fix zombie GSM and CDMA devices in the menu
- applet: remove 4-character GSM PIN/PUK code limit
- applet: fix insensitive WiFi Create... button (rh #541163)
- applet: allow unlocking of mobile devices immediately when plugged in

* Fri Feb 19 2010 Dan Williams <dcbw@redhat.com> - 0.8-1.git20100219
- core: update to final 0.8 release
- core: fix Bluetooth DUN connections when secrets are needed
- ifcfg-rh: add helper for initscripts to determine ifcfg connection UUIDs
- applet: fix Bluetooth connection secrets requests
- applet: fix rare conflict with other gnome-bluetooth plugins

* Thu Feb 11 2010 Dan Williams <dcbw@redhat.com> - 0.8-0.4.git20100211
- core: fix mobile broadband PIN handling (rh #543088) (rh #560742)
- core: better handling of /etc/hosts if hostname was already added by the user
- applet: crash less on D-Bus property errors (rh #557007)
- applet: fix crash entering wired 802.1x connection details (rh #556763)

* Tue Feb 09 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.8-0.3.git20100129
- core: validate the autostart .desktop file
- build: fix nmcli for the stricter ld (fixes FTBFS)
- build: fix nm-connection-editor for the stricter ld (fixes FTBFS)
- applet: don't autostart in KDE on F13+ (#541353)

* Fri Jan 29 2010 Dan Williams <dcbw@redhat.com> - 0.8-0.2.git20100129
- core: add Bluetooth Dial-Up Networking (DUN) support (rh #136663)
- core: start DHCPv6 on receipt of RA 'otherconf'/'managed' bits
- nmcli: allow enable/disable of WiFi and WWAN

* Fri Jan 22 2010 Dan Williams <dcbw@redhat.com> - 0.8-0.1.git20100122
- ifcfg-rh: read and write DHCPv6 enabled connections (rh #429710)
- nmcli: update

* Thu Jan 21 2010 Dan Williams <dcbw@redhat.com> - 0.7.999-2.git20100120
- core: clean NSS up later to preserve errors from crypto_init()

* Wed Jan 20 2010 Dan Williams <dcbw@redhat.com> - 0.7.999-1.git20100120
- core: support for managed-mode DHCPv6 (rh #429710)
- ifcfg-rh: gracefully handle missing PREFIX/NETMASK
- cli: initial preview of command-line client
- applet: add --help to explain what the applet is (rh #494641)

* Wed Jan  6 2010 Dan Williams <dcbw@redhat.com> - 0.7.998-1.git20100106
- build: fix for new pppd (rh #548520)
- core: add WWAN enable/disable functionality
- ifcfg-rh: IPv6 addressing and routes support (rh #523288)
- ifcfg-rh: ensure connection is updated when route/key files change
- applet: fix crash when active AP isn't found (rh #546901)
- editor: fix crash when editing connections (rh #549579)

* Mon Dec 14 2009 Dan Williams <dcbw@redhat.com> - 0.7.997-2.git20091214
- core: fix recognition of standalone 802.1x private keys
- applet: clean notification text to ensure it passes libnotify validation

* Mon Dec  7 2009 Dan Williams <dcbw@redhat.com> - 0.7.997-1
- core: remove haldaemon from initscript dependencies (rh #542078)
- core: handle PEM certificates without an ending newline (rh #507315)
- core: fix rfkill reporting for ipw2x00 devices
- core: increase PPPoE timeout to 30 seconds
- core: fix re-activating system connections with secrets
- core: fix crash when deleting automatically created wired connections
- core: ensure that a VPN's DNS servers are used when sharing the VPN connection
- ifcfg-rh: support routes files (rh #507307)
- ifcfg-rh: warn when device will be managed due to missing HWADDR (rh #545003)
- ifcfg-rh: interpret DEFROUTE as never-default (rh #528281)
- ifcfg-rh: handle MODE=Auto correctly
- rpm: fix rpmlint errors
- applet: don't crash on various D-Bus and other errors (rh #545011) (rh #542617)
- editor: fix various PolicyKit-related crashes (rh #462944)
- applet+editor: notify user that private keys must be protected

* Fri Nov 13 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-7.git20091113
- nm: better pidfile handing (rh #517362)
- nm: save WiFi and Networking enabled/disabled states across reboot
- nm: fix crash with missing VPN secrets (rh #532084)
- applet: fix system connection usage from the "Connect to hidden..." dialog
- applet: show Bluetooth connections when no other devices are available (rh #532049)
- applet: don't die when autoconfigured connections can't be made (rh #532680)
- applet: allow system administrators to disable the "Create new wireless network..." menu item
- applet: fix missing username connecting to VPNs the second time
- applet: really fix animation stuttering
- editor: fix IP config widget tooltips
- editor: allow unlisted countries in the mobile broadband wizard (rh #530981)
- ifcfg-rh: ignore .rpmnew files (rh #509621)

* Wed Nov 04 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-6.git20091021
- nm: fix PPPoE connection authentication (rh #532862)

* Wed Oct 21 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-5.git20091021
- install: better fix for (rh #526519)
- install: don't build Bluetooth bits on s390 (rh #529854)
- nm: wired 802.1x connection activation fixes
- nm: fix crash after modifying default wired connections like "Auto eth0"
- nm: ensure VPN secrets are requested again after connection failure
- nm: reset 'accept_ra' to previous value after deactivating IPv6 connections
- nm: ensure random netlink events don't interfere with IPv6 connection activation
- ifcfg-rh: fix writing out LEAP connections
- ifcfg-rh: recognize 'static' as a valid BOOTPROTO (rh #528068)
- applet: fix "could not find required resources" error (rh #529766)

* Fri Oct  2 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-4.git20091002
- install: fix -gnome package pre script failures (rh #526519)
- nm: fix failures validating private keys when using the NSS crypto backend
- applet: fix crashes when clicking on menu but not associated (rh #526535)
- editor: fix crash editing wired 802.1x settings
- editor: fix secrets retrieval when editing connections

* Mon Sep 28 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-3.git20090928
- nm: fix connection takeover when carrier is not on
- nm: handle certificate paths (CA chain PEM files are now fully usable)
- nm: defer action for 4 seconds when wired carrier drops
- ifcfg-rh: fix writing WPA passphrases with odd characters
- editor: fix editing of IPv4 settings with new connections (rh #525819)
- editor: fix random crashes when editing due to bad widget refcounting
- applet: debut reworked menu layout (not final yet...)

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> - 0.7.996-3.git20090921
- Install GConf schemas

* Mon Sep 21 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-2.git20090921
- nm: allow disconnection of all device types
- nm: ensure that wired connections are torn down when their hardware goes away
- nm: fix crash when canceling a VPN's request for secrets
- editor: fix issues changing connections between system and user scopes
- editor: ensure changes are thrown away when editing is canceled
- applet: ensure connection changes are noticed by NetworkManager
- applet: fix crash when creating new connections
- applet: actually use wired 802.1x secrets after they are requested

* Wed Aug 26 2009 Dan Williams <dcbw@redhat.com> - 0.7.996-1.git20090826
- nm: IPv6 zeroconf support and fixes
- nm: port to polkit (rh #499965)
- nm: fixes for ehea devices (rh #511304) (rh #516591)
- nm: work around PPP bug causing bogus nameservers for mobile broadband connections
- editor: fix segfault with "Unlisted" plans in the mobile broadband assistant

* Thu Aug 13 2009 Dan Williams <dcbw@redhat.com> - 0.7.995-3.git20090813
- nm: add iSCSI support
- nm: add connection assume/takeover support for ethernet (rh #517333)
- nm: IPv6 fixes
- nm: re-add OLPC XO-1 mesh device support (removed with 0.7.0)
- applet: better WiFi dialog focus handling

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 0.7.995-2.git20090804
- Add patch to fix service detection on phones

* Tue Aug  4 2009 Dan Williams <dcbw@redhat.com> - 0.7.995-1.git20090804
- nm: IPv6 support for manual & router-advertisement modes

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.7.995-1.git20090728
- Move some big docs to -devel to save space

* Tue Jul 28 2009 Dan Williams <dcbw@redhat.com> - 0.7.995-0.git20090728
- Update to upstream 'master' branch
- Use modem-manager for better 3G modem support
- Integrated system settings with NetworkManager itself
- Use udev instead of HAL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.1-9.git20090708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Dan Williams <dcbw@redhat.com> - 0.7.1-8.git20090708
- applet: fix certificate validation in hidden wifi networks dialog (rh #508207)

* Wed Jul  8 2009 Dan Williams <dcbw@redhat.com> - 0.7.1-7.git20090708
- nm: fixes for ZTE/Onda modem detection
- nm: prevent re-opening serial port when the SIM has a PIN
- applet: updated translations
- editor: show list column headers

* Thu Jun 25 2009 Dan Williams <dcbw@redhat.com> - 0.7.1-6.git20090617
- nm: fix serial port settings

* Wed Jun 17 2009 Dan Williams <dcbw@redhat.com> - 0.7.1-5.git20090617
- nm: fix AT&T Quicksilver modem connections (rh #502002)
- nm: fix support for s390 bus types (rh #496820)
- nm: fix detection of some CMOtech modems
- nm: handle unsolicited wifi scans better
- nm: resolv.conf fixes when using DHCP and overriding search domains
- nm: handle WEP and WPA passphrases (rh #441070)
- nm: fix removal of old APs when none are scanned
- nm: fix Huawei EC121 and EC168C detection and handling (rh #496426)
- applet: save WEP and WPA passphrases instead of hashed keys (rh #441070)
- applet: fix broken notification bubble actions
- applet: default to WEP encryption for Ad-Hoc network creation
- applet: fix crash when connection editor dialogs are canceled
- applet: add a mobile broadband provider wizard

* Tue May 19 2009 Karsten Hopp <karsten@redhat.com> 0.7.1-4.git20090414.1
- drop ExcludeArch s390 s390x, we need at least the header files

* Tue May 05 2009 Adam Jackson <ajax@redhat.com> 1:0.7.1-4.git20090414
- nm-save-the-leases.patch: Use per-connection lease files, and don't delete
  them on interface deactivate.

* Thu Apr 16 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.1-3.git20090414
- ifcfg-rh: fix problems noticing changes via inotify (rh #495884)

* Tue Apr 14 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.1-2.git20090414
- ifcfg-rh: enable write support for wired and wifi connections

* Sun Apr 12 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.1-1
- nm: update to 0.7.1
- nm: fix startup race with HAL causing unmanaged devices to sometimes be managed (rh #494527)

* Wed Apr  8 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.100-2.git20090408
- nm: fix recognition of Option GT Fusion and Option GT HSDPA (nozomi) devices (rh #494069)
- nm: fix handling of spaces in DHCP 'domain-search' option
- nm: fix detection of newer Option 'hso' devices
- nm: ignore low MTUs returned by broken DHCP servers

* Sun Apr  5 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.100-1
- Update to 0.7.1-rc4
- nm: use PolicyKit for system connection secrets retrieval
- nm: correctly interpret errors returned from chmod(2) when saving keyfile system connections
- editor: use PolicyKit to get system connection secrets

* Thu Mar 26 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-5
- nm: fix crashes with out-of-tree modules that provide no driver link (rh #492246)
- nm: fix USB modem probing on recent udev versions

* Tue Mar 24 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-4
- nm: fix communication with Option GT Max 3.6 mobile broadband cards
- nm: fix communication with Huawei mobile broadband cards (rh #487663)
- nm: don't look up hostname when HOSTNAME=localhost unless asked (rh #490184)
- nm: fix crash during IP4 configuration (rh #491620)
- nm: ignore ONBOOT=no for minimal ifcfg files (f9 & f10 only) (rh #489398)
- applet: updated translations

* Wed Mar 18 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-3.5
- nm: work around unhandled device removals due to missing HAL events (rh #484530)
- nm: improve handling of multiple modem ports
- nm: support for Sony Ericsson F3507g / MD300 and Dell 5530
- applet: updated translations

* Mon Mar  9 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-3
- Missing ONBOOT should actually mean ONBOOT=yes (rh #489422)

* Mon Mar  9 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-2
- Fix conflict with NetworkManager-openconnect (rh #489271)
- Fix possible crash when resynchronizing devices if HAL restarts

* Wed Mar  4 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.99-1
- nm: make default wired "Auto ethX" connection modifiable if an enabled system settings
    plugin supports modifying connections (rh #485555)
- nm: manpage fixes (rh #447233)
- nm: CVE-2009-0365 - GetSecrets disclosure
- applet: CVE-2009-0578 - local users can modify the connection settings
- applet: fix inability to choose WPA Ad-Hoc networks from the menu
- ifcfg-rh: add read-only support for WPA-PSK connections

* Wed Feb 25 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.98-1.git20090225
- Fix getting secrets for system connections (rh #486696)
- More compatible modem autodetection
- Better handle minimal ifcfg files

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0.97-6.git20090220
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.97-5.git20090220
- Use IFF_LOWER_UP for carrier detect instead of IFF_RUNNING
- Add small delay before probing cdc-acm driven mobile broadband devices

* Thu Feb 19 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.97-4.git20090219
- Fix PEAP version selection in the applet (rh #468844)
- Match hostname behavior to 'network' service when hostname is localhost (rh #441453)

* Thu Feb 19 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.97-2
- Fix 'noreplace' for nm-system-settings.conf

* Wed Feb 18 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0.97-1
- Update to 0.7.1rc1
- nm: support for Huawei E160G mobile broadband devices (rh #466177)
- nm: fix misleading routing error message (rh #477916)
- nm: fix issues with 32-character SSIDs (rh #485312)
- nm: allow root to activate user connections
- nm: automatic modem detection with udev-extras
- nm: massive manpage rewrite
- applet: fix crash when showing the CA certificate ignore dialog a second time
- applet: clear keyring items when deleting a connection
- applet: fix max signal strength calculation in menu (rh #475123)
- applet: fix VPN export (rh #480496)

* Sat Feb  7 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0-2.git20090207
- applet: fix blank VPN connection message bubbles
- applet: better handling of VPN routing on update
- applet: silence pointless warning (rh #484136)
- applet: desensitize devices in the menu until they are ready (rh #483879)
- nm: Expose WINS servers in the IP4Config over D-Bus
- nm: Better handling of GSM Mobile Broadband modem initialization
- nm: Handle DHCP Classless Static Routes (RFC 3442)
- nm: Fix Mobile Broadband and PPPoE to always use 'noauth'
- nm: Better compatibility with older dual-SSID AP configurations (rh #445369)
- nm: Mark nm-system-settings.conf as config (rh #465633)
- nm-tool: Show VPN connection information
- ifcfg-rh: Silence message about ignoring loopback config (rh #484060)
- ifcfg-rh: Fix issue with wrong gateway for system connections (rh #476089)

* Fri Jan  2 2009 Dan Williams <dcbw@redhat.com> - 1:0.7.0-1.git20090102
- Update to 0.7.1 pre-release
- Allow connections to be ignored when determining the default route (rh #476089)
- Own /usr/share/gnome-vpn-properties (rh #477155)
- Fix log flooding due to netlink errors (rh #459205)
- Pass connection UUID to dispatcher scripts via the environment
- Fix possible crash after deactivating a VPN connection
- Fix issues with editing wired 802.1x connections
- Fix issues when using PKCS#12 certificates with 802.1x connections

* Fri Nov 21 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.12.svn4326
- API and documentation updates
- Fix PIN handling on 'hso' mobile broadband devices

* Tue Nov 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.12.svn4296
- Fix PIN/PUK issues with high-speed Option HSDPA mobile broadband cards
- Fix desensitized OK button when asking for wireless keys

* Mon Nov 17 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.12.svn4295
- Fix issues reading ifcfg files
- Previously fixed:
- Doesn't send DHCP hostname (rh #469336)
- 'Auto eth0' forgets settings (rh #468612)
- DHCP renewal sometimes breaks VPN (rh #471852)
- Connection editor menu item in the wrong place (rh #471495)
- Cannot make system-wide connections (rh #471308)

* Fri Nov 14 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.12.svn4293
- Update to NetworkManager 0.7.0 RC2
- Handle gateways on a different subnet from the interface
- Clear VPN secrets on connection failure to ensure they are requested again (rh #429287)
- Add support for PKCS#12 private keys (rh #462705)
- Fix mangling of VPN's default route on DHCP renew
- Fix type detection of qemu/kvm network devices (rh #466340)
- Clear up netmask/prefix confusion in the connection editor
- Make the secrets dialog go away when it's not needed
- Fix inability to add system connections (rh #471308)

* Mon Oct 27 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4229
- More reliable mobile broadband card initialization
- Handle mobile broadband PINs correctly when PPP passwords are also used
- Additional PolicyKit integration for editing system connections
- Close the applet menu if a keyring password is needed (rh #353451)

* Tue Oct 21 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4201
- Fix issues with hostname during anaconda installation (rh #461933)
- Fix Ad-Hoc WPA connections (rh #461197)
- Don't require gnome-panel or gnome-panel-devel (rh #427834)
- Fix determination of WPA encryption capabilities on some cards
- Fix conflicts with PPTP and vpnc plugins
- Allow .cer file extensions when choosing certificates

* Sat Oct 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4175
- Fix conflicts for older PPTP VPN plugins

* Sat Oct 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4174
- Ensure that mobile broadband cards are powered up before trying to use them
- Hostname changing support (rh #441453)
- Fix mobile broadband secret requests to happen less often
- Better handling of default devices and default routes
- Better information in tooltips and notifications
- Various UI cleanups; hide widgets that aren't used (rh #465397, rh #465395)
- Accept different separators for DNS servers and searches
- Make applet's icon accurately reflect signal strength of the current AP

* Wed Oct  1 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4022.4
- Fix connection comparison that could cause changes to get overwritten (rh #464417)

* Tue Sep 30 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4022.3
- Fix handling of VPN settings on upgrade (rh #460730, bgo #553465)

* Thu Sep 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4022.2
- Fix hang when reading system connections from ifcfg files

* Thu Sep  4 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4022.1
- Fix WPA Ad-Hoc connections

* Wed Aug 27 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn4022
- Fix parsing of DOMAIN in ifcfg files (rh #459370)
- Fix reconnection to mobile broadband networks after an auth failure
- Fix recognition of timeouts of PPP during mobile broadband connection
- More compatible connection sharing (rh #458625)
- Fix DHCP in minimal environments without glibc locale information installed
- Add support for Option mobile broadband devices (like iCON 225 and iCON 7.2)
- Add IP4 config information to dispatcher script environment
- Merge WEP ASCII and Hex key types for cleaner UI
- Pre-fill PPPoE password when authentication fails
- Fixed some changes not getting saved in the connection editor
- Accept both prefix and netmask in the conection editor's IPv4 page

* Mon Aug 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn3930
- Fix issue with mobile broadband connections that don't require authentication

* Mon Aug 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn3927
- Expose DHCP-returned options over D-Bus and to dispatcher scripts
- Add support for customized static routes
- Handle multiple concurrent 3G or PPPoE connections
- Fix GSM/CDMA username and password issues
- Better handling of unmanaged devices from ifcfg files
- Fix timeout handling of errors during 3G connections
- Fix some routing issues (rh #456685)
- Fix applet crashes after removing a device (rh #457380)

* Thu Jul 24 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn3846
- Convert stored IPv4 static IP addresses to new prefix-based scheme automatically
- Fix pppd connections to some 3G providers (rh #455348)
- Make PPPoE "Show Password" option work
- Hide IPv4 config options that don't make sense in certain configurations

* Fri Jul 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.11.svn3830
- Expose server-returned DHCP options via D-Bus
- Use avahi-autoipd rather than old built-in IPv4LL implementation
- Send hostname to DHCP server if provided (DHCP_HOSTNAME ifcfg option)
- Support sending DHCP Client Identifier to DHCP server
- Allow forcing 802.1x PEAP Label to '0'
- Make connection sharing more robust
- Show status for shared and Ad-Hoc connections if no other connection is active

* Fri Jul 11 2008 Matthias Clasen <mclasen@redhat.com> - 1:0.7.0-0.10.svn3801
- Drop explicit hal dep in -gnome

* Wed Jul 02 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.10.svn3801
- Move VPN configuration into connection editor
- Fix mobile broadband username/password issues
- Fix issues with broken rfkill setups (rh #448889)
- Honor APN setting for GSM mobile broadband configurations
- Fix adding CDMA connections in the connection editor

* Wed Jun 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.10.svn3747
- Update to latest SVN
- Enable connection sharing
- Respect VPN-provided routes

* Wed Jun  4 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.4.svn3675
- Move NM later in the shutdown process (rh #449070)
- Move libnm-util into a subpackage to allow NM to be removed more easily (rh #351101)

* Mon May 19 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.3.svn3675
- Read global gateway from /etc/sysconfig/network if missing (rh #446527)
- nm-system-settings now terminates when dbus goes away (rh #444976)

* Wed May 14 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.3.svn3669
- Fix initial carrier state detection on devices that are already up (rh #134886)

* Tue May 13 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.3.svn3667
- Restore behavior of marking wifi devices as "down" when disabling wireless
- Fix a crash on resume when a VPN was active when going to sleep

* Tue May 13 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.3.svn3665
- Fix issues with the Fedora plugin not noticing changes made by
    system-config-network (rh #444502)
- Allow autoconnection of GSM and CDMA connections
- Multiple IP address support for user connections
- Fixes for Mobile Broadband cards that return line speed on connect
- Implement PIN entry for GSM mobile broadband connections
- Fix crash when editing unencrypted WiFi connections in the connection editor

* Wed Apr 30 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.3.svn3623
- Clean up the dispatcher now that it's service is gone (rh #444798)

* Wed Apr 30 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3623
- Fix asking applets for the GSM PIN/PUK

* Wed Apr 30 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3622
- Guess WEP key type in applet when asking for new keys
- Correct OK button sensitivity in applet when asking for new WEP keys

* Wed Apr 30 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3620
- Fix issues with Mobile Broadband connections caused by device init race patch

* Tue Apr 29 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3619
- Fix device initialization race that caused ethernet devices to get stuck on
    startup
- Fix PPPoE connections not showing up in the applet
- Fix disabled OK button in connection editor some wireless and IP4 settings
- Don't exit if HAL isn't up yet; wait for it
- Fix a suspend/resume crash

* Sun Apr 27 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3614
- Don't ask for wireless keys when the driver sends disconnect events during
	association; wait until the entire assocation times out
- Replace dispatcher daemon with D-Bus activated callout
- Fix parsing of DNS2 and DNS3 ifcfg file items
- Execute dispatcher scripts in alphabetical order
- Be active at runlevel 2
- Hook up MAC address widgets for wired & wireless; and BSSID widget for wireless
- Pre-populate anonymous identity and phase2 widgets correctly
- Clear out unused connection keys from GConf

* Tue Apr 22 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3590
- Don't select devices without a default gateway as the default route (rh #437338)
- Fill in broadcast address if not specified (rh #443474)
- Respect manual VPN IPv4 configuration options
- Show Connection Information for the device with the default route only

* Fri Apr 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3578
- Add dbus-glib-devel BuildRequires for NetworkManager-glib-devel (rh #442978)
- Add PPP settings page to connection editor
- Fix a few crashes with PPPoE
- Fix active connection state changes that confused clients 

* Thu Apr 17 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3571
- Fix build in pppd-plugin

* Thu Apr 17 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3570
- PPPoE authentication fixes
- More robust handing of mobile broadband device communications

* Wed Apr 16 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.2.svn3566
- Honor options from /etc/sysconfig/network for blocking until network is up

* Wed Apr 16 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3566
- Turn on Add/Edit in the connection editor
- Don't flush or change IPv6 addresses or routes
- Enhance nm-online tool
- Some serial communication fixes for mobile broadband

* Wed Apr  9 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3549
- Fix issues with VPN passwords not getting found

* Tue Apr  8 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3548
- Fix builds due to glib2 breakage of GStaticMutex with gcc 4.3

* Tue Apr  8 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3547
- Fix WEP key index handling in UI
- Fix handling of NM_CONTROLLED in ifcfg files
- Show device managed state in applet menu
- Show wireless enabled state in applet menu
- Better handling of default DHCP connections for wired devices
- Fix loading of connection editor on KDE (rh #435344)

* Wed Apr  2 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3527
- Honor MAC address locking for wired & wireless devices

* Mon Mar 31 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3521
- Show VPN failures
- Support Static WEP key indexes
- Fix parsing of WEP keys from ifcfg files
- Pre-fill wireless security UI bits in connection editor and applet

* Tue Mar 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3476
- Grab system settings from /etc/sysconfig/network-scripts, not from profiles

* Tue Mar 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3473
- Fix crashes when returning VPN secrets from the applet to NM

* Tue Mar 18 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3472
- Fix crashes on suspend/resume and exit (rh #437426)
- Ensure there's always an option to chose the wired device
- Never set default route via an IPv4 link-local addressed device (rh #437338)

* Wed Mar 12 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3440
- Fix DHCP rebind behavior
- Preliminary PPPoE support

* Mon Mar 10 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.9.1.svn3417
- Fix gnome-icon-theme Requires, should be on gnome subpackage

* Mon Mar 10 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3417
- Honor DHCP rebinds
- Multiple active device support
- Better error handling of mobile broadband connection failures
- Allow use of interface-specific dhclient config files
- Recognize system settings which have no TYPE item

* Sun Mar  2 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3370
- Fix crash of nm-system-settings on malformed ifcfg files (rh #434919)
- Require gnome-icon-theme to pick up lock.png (rh #435344)
- Fix applet segfault after connection removal via connection editor or GConf

* Fri Feb 29 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3369
- Don't create multiple connections for hidden access points
- Fix scanning behavior

* Thu Feb 14 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3319
- Rework connection editor connection list

* Tue Feb 12 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3312
- Better handling of changes in the profile directory by the system settings
	serivce

* Thu Feb  7 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3302
- Enable system settings service
- Allow explicit disconnection of mobile broadband devices
- Fix applet memory leaks (rh #430178)
- Applet Connection Information dialog tweaks (gnome.org #505899)
- Filter input characters to passphrase/key entry (gnome.org #332951)
- Fix applet focus stealing prevention behavior

* Mon Jan 21 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3261
- Add CDMA mobile broadband support (if supported by HAL)
- Rework applet connection and icon handling
- Enable connection editor (only for deleting connections)

* Fri Jan 11 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3235
- Fix crash when activating a mobile broadband connection
- Better handling of non-SSID-broadcasting APs on kernels that support it
    (gnome.org #464215) (rh #373841)
- Honor DHCP-server provided MTU if present (gnome.org #332953)
- Use previous DNS settings if the VPN concentrator doesn't provide any
    (gnome.org #346833)

* Fri Jan  4 2008 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3204
- Fix WPA passphrase hashing on big endian (PPC, Sparc, etc) (rh #426233)

* Tue Dec 18 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3181
- Fixes to work better with new libnl (rh #401761)

* Tue Dec 18 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3180
- Fix WPA/WPA2 Enterprise Phase2 connections (rh #388471)

* Wed Dec  5 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3138
- Fix applet connection comparison which failed to send connection updated
    signals to NM in some cases
- Make VPN connection applet more robust against plugin failures

* Tue Dec  4 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3134
- 64-bit -Wall compile fixes

* Tue Dec  4 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.8.svn3133
- Fix applet crash when choosing to ignore the CA certificate (rh #359001)
- Fix applet crash when editing VPN properties and VPN connection failures (rh #409351)
- Add file filter name in certificate file picker dialog (rh #410201)
- No longer start named when starting NM (rh #381571)

* Tue Nov 27 2007 Jeremy Katz <katzj@redhat.com> - 1:0.7.0-0.8.svn3109
- Fix upgrading from an earlier rawhide snap

* Mon Nov 26 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.6.svn3109
- Fix device descriptions shown in applet menu

* Mon Nov 26 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.5.svn3109
- Fix crash when deactivating VPN connections

* Mon Nov 19 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.5.svn3096
- Fix crash and potential infinite nag dialog loop when ignoring CA certificates

* Mon Nov 19 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.4.svn3096
- Fix crash when ignoring CA certificate for EAP-TLS, EAP-TTLS, and EAP-PEAP

* Mon Nov 19 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.3.svn3096
- Fix connections when picking a WPA Enterprise AP from the menu
- Fix issue where applet would provide multiple same connections to NM

* Thu Nov 15 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.3.svn3094
- Add support for EAP-PEAP (rh #362251)
- Fix EAP-TLS private key handling

* Tue Nov 13 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.2.svn3080
- Clarify naming of WPA & WPA2 Personal encryption options (rh #374861, rh #373831)
- Don't require a CA certificate for applicable EAP methods (rh #359001)
- Fix certificate and private key handling for EAP-TTLS and EAP-TLS (rh #323371)
- Fix applet crash with USB devices (rh #337191)
- Support upgrades from NM 0.6.x GConf settings

* Thu Nov  1 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.6.1.svn3030
- Fix applet crash with USB devices that don't advertise a product or vendor
    (rh #337191)

* Sat Oct 27 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.5.svn3030
- Fix crash when getting WPA secrets (rh #355041)

* Fri Oct 26 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.4.svn3030
- Bring up ethernet devices by default if no connections are defined (rh #339201)
- Fix crash when switching networks or bringing up secrets dialog (rh #353091)
- Fix crash when editing VPN connection properties a second time
- Fix crash when cancelling the secrets dialog if another connection was
    activated in the mean time
- Fix disembodied notification bubbles (rh #333391)

* Thu Oct 25 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.4.svn3020
- Handle PEM certificates
- Hide WPA-PSK Type combo since it's as yet unused
- Fix applet crash when AP security options changed and old secrets are still
    in the keyring
- Fix applet crash connecting to unencrypted APs via the other network dialog

* Wed Oct 24 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn3020
- Fix WPA Enterprise connections that use certificates
- Better display of SSIDs in the menu

* Wed Oct 24 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn3016
- Fix getting current access point
- Fix WPA Enterprise connections
- Wireless dialog now defaults to sensible choices based on the connection
- Tell nscd to restart if needed, don't silently kill it

* Tue Oct 23 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn3014
- Suppress excessive GConf updates which sometimes caused secrets to be cleared
    at the wrong times, causing connections to fail
- Various EAP and LEAP related fixes

* Tue Oct 23 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn3008
- Make WPA-EAP and Dynamic WEP options connect successfully
- Static IPs are now handled correctly in NM itself

* Mon Oct 22 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2995
- Add Dynamic WEP as a supported authentication/security option

* Sun Oct 21 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2994
- Re-enable "Connect to other network"
- Switch to new GUI bits for wireless security config and password entry

* Tue Oct 16 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2983
- Add rfkill functionality
- Fix applet crash when choosing wired networks from the menu

* Wed Oct 10 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2970
- Fix segfault with deferred connections
- Fix default username with vpnc VPN plugin
- Hidden SSID fixes

* Tue Oct  9 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2962
- Fix merging of non-SSID-broadcasting APs into a device's scan list
- Speed up opening of the applet menu

* Tue Oct  9 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2961
- New snapshot
	- Add timestamps to networks to connect to last used wireless network
	- Turn autoconnect on in the applet
	- Hidden SSID support
	- Invalidate failed or cancelled connections again
	- Fix issues with reactivation of the same device
	- Handle connection updates in the applet (ex. find new VPN connections)
	- Fix vertical sizing of menu items
	- Fix AP list on wireless devices other than the first device in the applet
	- Fix matching of current AP with the right menu item

* Fri Sep 28 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2914
- New snapshot
	- Add WPA passphrase support to password dialog
	- Applet now reflects actual VPN behavior of one active connection
	- Applet now notices VPN active connections on startup
	- Fix connections with some WPA and WEP keys

* Thu Sep 27 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2907
- New snapshot
	- VPN support (only vpnc plugin ported at this time)

* Tue Sep 25 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2886
- New snapshot
	- Make wired device carrier state work in the applet
	- Fix handling of errors with unencrypted APs
	- Fix "frozen" applet icon by reporting NM state better
	- Fix output of AP frequency in nm-tool

* Tue Sep 25 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2880
- New snapshot
	- Fix applet icon sizing on start (mclasen)
	- Fix nm-tool installation (mclasen)
	- Fix 'state' method call return (#303271)
	- Fix 40-bit WEP keys (again)
	- Fix loop when secrets were wrong/invalid
	- Fix applet crash when clicking Cancel in the password dialog
	- Ensure NM doesn't get stuck waiting for the supplicant to re-appear
		if it crashes or goes away
	- Make VPN properties applet work again
	- Increase timeout for network password entry

* Fri Sep 21 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2852
- New snapshot (fix unencrypted & 40 bit WEP)

* Fri Sep 21 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2849
- New snapshot

* Fri Sep 21 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.3.svn2844
- New snapshot

* Thu Sep 20 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.2.svn2833
- New SVN snapshot of 0.7 that sucks less

* Thu Aug 30 2007 Dan Williams <dcbw@redhat.com> - 1:0.7.0-0.1.svn2736
- Update to SVN snapshot of 0.7

* Mon Aug 13 2007 Christopher Aillon <caillon@redhat.com> 1:0.6.5-9
- Update the license tag

* Wed Aug  8 2007 Christopher Aillon <caillon@redhat.com> 1:0.6.5-8
- Own /etc/NetworkManager/dispatcher.d and /etc/NetworkManager/VPN (#234004)

* Wed Jun 27 2007 Dan Williams <dcbw@redhat.com> 1:0.6.5-7
- Fix Wireless Enabled checkbox when no killswitches are present

* Thu Jun 21 2007 Dan Williams <dcbw@redhat.com> 1:0.6.5-6
- Update to stable branch snapshot:
    - More fixes for ethernet link detection (gnome #354565, rh #194124)
    - Support for HAL-detected rfkill switches

* Sun Jun 10 2007 Dan Williams <dcbw@redhat.com> 1:0.6.5-5
- Fix applet crash on 64-bit platforms when choosing
    "Connect to other wireless network..." (gnome.org #435036)
- Add debug output for ethernet device link changes

* Thu Jun  7 2007 Dan Williams <dcbw@redhat.com> 1:0.6.5-4
- Fix ethernet link detection (gnome #354565, rh #194124)
- Fix perpetual credentials request with private key passwords in the applet
- Sleep a bit before activating wireless cards to work around driver bugs

* Mon Jun  4 2007 Dan Williams <dcbw@redhat.com> 1:0.6.5-3
- Don't spawn wpa_supplicant with -o

* Wed Apr 25 2007 Christopher Aillon <caillon@redhat.com> 1:0.6.5-2
- Fix requires macro (237806)

* Thu Apr 19 2007 Christopher Aillon <caillon@redhat.com> 1:0.6.5-1
- Update to 0.6.5 final
- Don't lose scanned security information

* Mon Apr  9 2007 Dan Williams <dcbw@redhat.com> - 1:0.6.5-0.7.svn2547
- Update from trunk
	* Updated translations
	* Cleaned-up VPN properties dialogs
	* Fix 64-bit kernel leakage issues in WEXT
	* Don't capture and redirect wpa_supplicant log output

* Wed Mar 28 2007 Matthew Barnes  <mbarnes@redhat.com> 1:0.6.5-0.6.svn2474
- Close private D-Bus connections. (#232691)

* Sun Mar 25 2007 Matthias Clasen <mclasen@redhat.com> 1:0.6.5-0.5.svn2474
- Fix a directory ownership issue.  (#233763)

* Thu Mar 15 2007 Dan Williams <dcbw@redhat.com> - 1:0.6.5-0.4.svn2474
- Update to pre-0.6.5 snapshot

* Thu Feb  8 2007 Christopher Aillon <caillon@redhat.com> - 1:0.6.5-0.3.cvs20061025
- Guard against D-Bus LimitExceeded messages

* Fri Feb  2 2007 Christopher Aillon <caillon@redhat.com> - 1:0.6.5-0.2.cvs20061025
- Move .so file to -devel package

* Sat Nov 25 2006 Matthias Clasen <mclasen@redhat.com> 
- Own the /etc/NetworkManager/dispatcher.d directory
- Require pkgconfig for the -devel packages
- Fix compilation with dbus 1.0

* Wed Oct 25 2006 Dan Williams <dcbw@redhat.com> - 1:0.6.5-0.cvs20061025
- Update to a stable branch snapshot
    - Gnome applet timeout/redraw suppression when idle
    - Backport of LEAP patch from HEAD (from Thiago Bauermann)
    - Backport of asynchronous scanning patch from HEAD
    - Make renaming of VPN connections work (from Tambet Ingo)
    - Dial down wpa_supplicant debug spew
    - Cleanup of key/passphrase request scenarios (from Valentine Sinitsyn)
    - Shut down VPN connections on logout (from Robert Love)
    - Fix WPA passphrase hashing on PPC

* Thu Oct 19 2006 Christopher Aillon <caillon@redhat.com> - 1:0.6.4-6
- Own /usr/share/NetworkManager and /usr/include/NetworkManager

* Mon Sep  4 2006 Christopher Aillon <caillon@redhat.com> - 1:0.6.4-5
- Don't wake up to redraw if NM is inactive (#204850)

* Wed Aug 30 2006 Bill Nottingham <notting@redhat.com> - 1:0.6.4-4
- add epochs in requirements

* Wed Aug 30 2006 Dan Williams <dcbw@redhat.com> - 1:0.6.4-3
- Fix FC-5 buildreqs

* Wed Aug 30 2006 Dan Williams <dcbw@redhat.com> - 1:0.6.4-2
- Revert FC6 to latest stable NM
- Update to stable snapshot
- Remove bind/caching-nameserver hard requirement

* Tue Aug 29 2006 Christopher Aillon <caillon@redhat.com> - 0.7.0-0.cvs20060529.7
- BuildRequire wireless-tools-devel and perl-XML-Parser
- Update the BuildRoot tag

* Wed Aug 16 2006 Ray Strode <rstrode@redhat.com> - 0.7.0-0.cvs20060529.6
- add patch to make networkmanager less verbose (bug 202832)

* Wed Aug  9 2006 Ray Strode <rstrode@redhat.com> - 0.7.0-0.cvs20060529.5
- actually make the patch in 0.7.0-0.cvs20060529.4 apply

* Fri Aug  4 2006 Ray Strode <rstrode@redhat.com> - 0.7.0-0.cvs20060529.4
- Don't ever elect inactive wired devices (bug 194124).

* Wed Jul 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.7.0-0.cvs20060529.3
- Add patch to fix deprecated dbus functions

* Tue Jul 18 2006 John (J5) Palmieri <johnp@redhat.com> - 0.7.0-0.cvs20060529.2
- Add BR for dbus-glib-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.7.0-0.cvs20060529.1.1
- rebuild

* Mon May 29 2006 Dan Williams <dcbw@redhat.com> - 0.7.0-0.cvs20060529
- Update to latest CVS
	o Gnome.org #333420: dialog do not have window icons
	o Gnome.org #336913: HIG tweaks for vpn properties pages
	o Gnome.org #336846: HIG tweaks for nm-vpn-properties
	o Gnome.org #336847: some bugs in nm-vpn-properties args parsing
	o Gnome.org #341306: nm-vpn-properties crashes on startup
	o Gnome.org #341263: Version 0.6.2-0ubuntu5 crashes on nm_device_802_11_wireless_get_type
	o Gnome.org #341297: displays repeated keyring dialogs on resume from suspend
	o Gnome.org #342400: Building libnm-util --without-gcrypt results in linker error
	o Gnome.org #342398: Eleminate Gnome dependency for NetworkManager
	o Gnome.org #336532: declaration of 'link' shadows a global declaration
- Specfile fixes (#rh187489#)

* Sun May 21 2006 Dan Williams <dcbw@redhat.com> - 0.7.0-0.cvs20060521
- Update to latest CVS
- Drop special-case-madwifi.patch, since WEXT code is in madwifi-ng trunk now

* Fri May 19 2006 Bill Nottingham <notting@redhat.com> - 0.6.2-3.fc6
- use the same 0.6.2 tarball as FC5, so we have the same VPN interface
  (did he fire ten args, or only nine?)

* Thu Apr 27 2006 Jeremy Katz <katzj@redhat.com> - 0.6.2-2.fc6
- use the hal device type instead of poking via ioctl so that wireless 
  devices are properly detected even if the kill switch has been used

* Thu Mar 30 2006 Dan Williams <dcbw@redhat.com> - 0.6.2-1
- Update to 0.6.2:
	* Fix various WPA-related bugs
	* Clean up leaks
	* Increased DHCP timeout to account for slow DHCP servers, or STP-enabled
		switches
	* Allow applet to reconnect on dbus restarts
	* Add "Dynamic WEP" support
	* Allow hiding of password/key entry text
	* More responsive connection switching

* Tue Mar 14 2006 Peter Jones <pjones@redhat.com> - 0.6.0-3
- Fix device bringup on resume

* Mon Mar  6 2006 Dan Williams <dcbw@redhat.com> 0.6.0-2
- Don't let wpa_supplicant perform scanning with non-WPA drivers

* Mon Mar  6 2006 Dan Williams <dcbw@redhat.com> 0.6.0-1
- Update to 0.6.0 release
- Move autostart file to /usr/share/gnome/autostart

* Thu Mar  2 2006 Jeremy Katz <katzj@redhat.com> - 0.5.1-18.cvs20060302
- updated cvs snapshot.  seems to make airo much less neurotic

* Thu Mar  2 2006 Christopher Aillon <caillon@redhat.com>
- Move the unversioned libnm_glib.so to the -devel package

* Wed Mar  1 2006 Dan Williams <dcbw@redhat.com> 0.5.1-18.cvs20060301
- Fix VPN-related crash
- Fix issue where NM would refuse to activate a VPN connection once it had timed out
- Log wpa_supplicant output for better debugging

* Tue Feb 28 2006 Christopher Aillon <caillon@redhat.com> 0.5.1-17.cvs20060228
- Tweak three-scan-prune.patch

* Mon Feb 27 2006 Christopher Aillon <caillon@redhat.com> 0.5.1-16.cvs20060227
- Don't prune networks until they've gone MIA for three scans, not one.

* Mon Feb 27 2006 Christopher Aillon <caillon@redhat.com> 0.5.1-15.cvs20060227
- Update snapshot, which fixes up the libnotify stuff.

* Fri Feb 24 2006 Dan Williams <dcbw@redhat.coM> 0.5.1-14.cvs20060221
- Move libnotify requires to NetworkManager-gnome, not core NM package

* Tue Feb 21 2006 Dan Williams <dcbw@redhat.com> 0.5.1-13.cvs20060221
- Add BuildRequires: libnl-devel (#rh179438#)
- Fix libnm_glib to not clobber an application's existing dbus connection
	(#rh177546#, gnome.org #326572)
- libnotify support
- AP compatibility fixes

* Mon Feb 13 2006 Dan Williams <dcbw@redhat.com> 0.5.1-12.cvs20060213
- Minor bug fixes
- Update to VPN dbus API for passing user-defined routes to vpn service

* Sun Feb 12 2006 Christopher Aillon <caillon@redhat.com> 0.5.1-11.cvs20060205
- Rebuild

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.5.1-10.cvs20060205.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb  5 2006 Dan Williams <dcbw@redhat.com> 0.5.1-10.cvs20060205
- Workarounds for madwifi/Atheros cards
- Do better with non-SSID-broadcasting access points
- Fix hangs when access points change settings

* Thu Feb  2 2006 Dan Williams <dcbw@redhat.com> 0.5.1-9.cvs20060202
- Own /var/run/NetworkManager, fix SELinux issues

* Tue Jan 31 2006 Dan Williams <dcbw@redhat.com> 0.5.1-8.cvs20060131
- Switch to autostarting the applet instead of having it be session-managed
- Work better with non-broadcasting access points
- Add more manufacturer default SSIDs to the blacklist

* Tue Jan 31 2006 Dan Williams <dcbw@redhat.com> 0.5.1-7.cvs20060131
- Longer association timeout
- Fix some SELinux issues
- General bug and cosmetic fixes

* Fri Jan 27 2006 Dan Williams <dcbw@redhat.com> 0.5.1-6.cvs20060127
- Snapshot from CVS
- WPA Support!  Woohoo!

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec 01 2005 John (J5) Palmieri <johnp@redhat.com> - 0.5.1-5
- rebuild for new dbus

* Fri Nov 18 2005 Peter Jones <pjones@redhat.com> - 0.5.1-4
- Don't kill the network connection when you upgrade the package.

* Fri Oct 21 2005 Christopher Aillon <caillon@redhat.com> - 0.5.1-3
- Split out the -glib subpackage to have a -glib-devel package as well
- Add epoch to version requirements for bind and wireless-tools
- Update URL of project

* Wed Oct 19 2005 Christopher Aillon <caillon@redhat.com> - 0.5.1-2
- NetworkManager 0.5.1

* Mon Oct 17 2005 Christopher Aillon <caillon@redhat.com> - 0.5.0-2
- NetworkManager 0.5.0

* Mon Oct 10 2005 Dan Williams <dcbw@redaht.com> - 0.4.1-5.cvs20051010
- Fix automatic wireless connections
- Remove usage of NMLoadModules callout, no longer needed
- Try to fix deadlock when menu is down and keyring dialog pops up

* Sun Oct 09 2005 Dan Williams <dcbw@redhat.com> - 0.4.1-4.cvs20051009
- Update to latest CVS
	o Integrate connection progress with applet icon (Chris Aillon)
	o More information in "Connection Information" dialog (Robert Love)
	o Shorten time taken to sleep
	o Make applet icon wireless strength levels a bit more realistic
	o Talk to named using DBUS rather than spawning our own
		- You need to add "-D" to the OPTIONS line in /etc/sysconfig/named
		- You need to set named to start as a service on startup

* Thu Sep 22 2005 Dan Williams <dcbw@redhat.com> - 0.4.1-3.cvs20050922
- Update to current CVS to fix issues with routing table and /sbin/ip

* Mon Sep 12 2005 Jeremy Katz <katzj@redhat.com> - 0.4.1-2.cvs20050912
- update to current CVS and rebuild (workaround for #168120)

* Fri Aug 19 2005 Dan Williams <dcbw@redhat.com> - 0.4.1-2.cvs20050819
- Fix occasional hang in NM caused by the applet

* Wed Aug 17 2005 Dan Williams <dcbw@redhat.com> - 0.4.1
- Update to NetworkManager 0.4.1

* Tue Aug 16 2005 Dan Williams <dcbw@redhat.com> - 0.4-36.cvs20050811
- Rebuild against new cairo/gtk

* Thu Aug 11 2005 Dan Williams <dcbw@redhat.com> - 0.4-35.cvs20050811
- Update to latest CVS
	o Use DHCP server address as gateway address if the DHCP server doesn't give
		us a gateway address #rh165698#
	o Fixes to the applet (Robert Love)
	o Better caching of information in the applet (Bill Moss)
	o Generate automatic suggested Ad-Hoc network name from machine's hostname
		(Robert Love)
	o Update all network information on successfull connect, not just 
		authentication method

* Fri Jul 29 2005 Ray Strode  <rstrode@redhat.com> - 0.4-34.cvs20050729
- Update to latest CVS to get fix for bug 165683.

* Mon Jul 11 2005 Dan Williams <dcbw@redhat.com> - 0.4-34.cvs20050629
- Move pkgconfig file to devel package (#162316, thanks to Michael Schwendt)

* Wed Jun 29 2005 David Zeuthen <davidz@redhat.com> - 0.4-33.cvs20050629
- Update to latest CVS to get latest VPN interface settings to satisfy
  BuildReq for NetworkManager-vpnc in Fedora Extras Development
- Latest CVS also contains various bug- and UI-fixes

* Fri Jun 17 2005 Dan Williams <dcbw@redhat.com> - 0.4-32.cvs20050617
- Update to latest CVS
	o VPN connection import/export capability
	o Fix up some menu item names
- Move nm-vpn-properties.glade to the gnome subpackage

* Thu Jun 16 2005 Dan Williams <dcbw@redhat.com> - 0.4-31.cvs20050616
- Update to latest CVS
	o Clean up wording in Wireless Network Discovery menu
	o Robert Love's applet beautify patch

* Wed Jun 15 2005 Dan Williams <dcbw@redhat.com> - 0.4-30.cvs20050615
- Update to latest CVS

* Mon May 16 2005 Dan Williams <dcbw@redhat.com> - 0.4-15.cvs30050404
- Fix dispatcher and applet CFLAGS so they gets compiled with FORTIFY_SOURCE

* Mon May 16 2005 Dan Williams <dcbw@redhat.com> - 0.4-14.cvs30050404
- Fix segfault in NetworkManagerDispatcher, add an initscript for it

* Mon May 16 2005 Dan Williams <dcbw@redhat.com> - 0.4-13.cvs30050404
- Fix condition that may have resulted in DHCP client returning success
	when it really timed out

* Sat May 14 2005 Dan Williams <dcbw@redhat.com> - 0.4-12.cvs20050404
- Enable OK button correctly in Passphrase and Other Networks dialogs when
	using ASCII or Hex WEP keys

* Thu May  5 2005 Dan Williams <dcbw@redhat.com> - 0.4-11.cvs20050404
- #rh154391# NetworkManager dies on startup (don't force-kill nifd)

* Wed May  4 2005 Dan Williams <dcbw@redhat.com> - 0.4-10.cvs20050404
- Fix leak of a socket in DHCP code

* Wed May  4 2005 Dan Williams <dcbw@redhat.com> - 0.4-9.cvs20050404
- Fix some memory leaks (Tom Parker)
- Join to threads rather than spinning for their completion (Tom Parker)
- Fix misuse of a g_assert() (Colin Walters)
- Fix return checking of an ioctl() (Bill Moss)
- Better detection and matching of hidden access points (Bill Moss)
- Don't use varargs, and therefore don't crash on PPC (Peter Jones)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 0.4-8.cvs20050404
- fix build with newer dbus

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 0.4-7.cvs20050404
- silence %%post

* Mon Apr  4 2005 Dan Williams <dcbw@redhat.com> 0.4-6.cvs20050404
- #rh153234# NetworkManager quits/cores just as a connection is made

* Sat Apr  2 2005 Dan Williams <dcbw@redhat.com> 0.4-5.cvs20050402
- Update from latest CVS HEAD

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 0.4-4.cvs20050315
- Update the GTK+ theme icon cache on (un)install

* Tue Mar 15 2005 Ray Strode <rstrode@redhat.com> 0.4-3.cvs20050315
- Pull from latest CVS HEAD

* Tue Mar 15 2005 Ray Strode <rstrode@redhat.com> 0.4-2.cvs20050315
- Upload new source tarball (woops)

* Tue Mar 15 2005 Ray Strode <rstrode@redhat.com> 0.4-1.cvs20050315
- Pull from latest CVS HEAD (hopefully works again)

* Mon Mar  7 2005 Ray Strode <rstrode@redhat.com> 0.4-1.cvs20050307
- Pull from latest CVS HEAD
- Commit broken NetworkManager to satisfy to dbus dependency

* Fri Mar  4 2005 Dan Williams <dcbw@redhat.com> 0.3.4-1.cvs20050304
- Pull from latest CVS HEAD
- Rebuild for gcc 4.0

* Tue Feb 22 2005 Dan Williams <dcbw@redhat.com> 0.3.3-2.cvs20050222
- Update from CVS

* Mon Feb 14 2005 Dan Williams <dcbw@redhat.com> 0.3.3-2.cvs20050214.x.1
- Fix free of invalid pointer for multiple search domains

* Mon Feb 14 2005 Dan Williams <dcbw@redhat.com> 0.3.3-2.cvs20050214
- Never automatically choose a device that doesn't support carrier detection
- Add right-click menu to applet, can now "Pause/Resume" scanning through it
- Fix DHCP Renew/Rebind timeouts
- Fix frequency cycling problem on some cards, even when scanning was off
- Play better with IPv6
- Don't send kernel version in DHCP packets, and ensure DHCP packets are at
	least 300 bytes in length to work around broken router
- New DHCP options D-BUS API by Dan Reed
- Handle multiple domain search options in DHCP responses

* Wed Feb  2 2005 Dan Williams <dcbw@redhat.com> 0.3.3-1.cvs20050202
- Display wireless network name in applet tooltip
- Hopefully fix double-default-route problem
- Write out valid resolv.conf when we exit
- Make multi-domain search options work
- Rework signal strength code to be WEXT conformant, if strength is
	still wierd then its 95% surely a driver problem
- Fix annoying instances of suddenly dropping and reactivating a
	wireless device (Cisco cards were worst offenders here)
- Fix some instances of NetworkManager not remembering your WEP key
- Fix some races between NetworkManager and NetworkManagerInfo where
	NetworkManager wouldn't recognize changes in the allowed list
- Don't shove Ad-Hoc Access Point MAC addresses into GConf

* Tue Jan 25 2005 Dan Williams <dcbw@redhat.com> 0.3.3-1.cvs20050125
- Play nice with dbus 0.23
- Update our list of Allowed Wireless Networks more quickly

* Mon Jan 24 2005 Dan Williams <dcbw@redhat.com> 0.3.3-1.cvs20050124
- Update to latest CVS
- Make sure we start as late as possible so that we ensure dbus & HAL
	are already around
- Fix race in initial device activation

* Mon Jan 24 2005 Than Ngo <than@redhat.com> 0.3.3-1.cvs20050112.4
- rebuilt against new wireless tool

* Fri Jan 21 2005 <dcbw@redhat.com> - 0.3.3-1.cvs20050118
- Fix issue where NM wouldn't recognize that access points were
	encrypted, and then would try to connect without encryption
- Refine packaging to put client library in separate package
- Remove bind+caching-nameserver dep for FC-3, use 'nscd -i hosts'
	instead.  DNS queries may timeout now right after device
	activation due to this change.

* Wed Jan 12 2005 <dcbw@redhat.com> - 0.3.3-1.cvs20050112
- Update to latest CVS
- Fixes to DHCP code
- Link-Local (ZeroConf/Rendezvous) support
- Use bind in "caching-nameserver" mode to work around stupidity
	in glibc's resolver library not recognizing resolv.conf changes
- #rh144818# Clean up the specfile (Patch from Matthias Saou)
- Ad-Hoc mode support with Link-Local addressing only (for now)
- Fixes for device activation race conditions
- Wireless scanning in separate thread

* Wed Dec  8 2004 <dcbw@redhat.com> - 0.3.2-4.3.cvs20041208
- Update to CVS
- Updates to link detection, DHCP code
- Remove NMLaunchHelper so we start up faster and don't
	block for a connection.  This means services that depend
	on the network may fail if they start right after NM
- Make sure DHCP renew/rebinding works

* Wed Nov 17 2004 <dcbw@redhat.com> - 0.3.2-3.cvs20041117
- Update to CVS
- Fixes to link detection
- Better detection of non-ESSID-broadcasting access points
- Don't dialog-spam the user if a connection fails

* Thu Nov 11 2004 <dcbw@redhat.com> - 0.3.2-2.cvs20041115
- Update to CVS
- Much better link detection, works with Open System authentication
- Blacklist wireless cards rather than whitelisting them

* Fri Oct 29 2004 <dcbw@redhat.com> - 0.3.2-2.cvs20041029
- #rh134893# NetworkManagerInfo and the panel-icon life-cycle
- #rh134895# Status icon should hide when in Wired-only mode
- #rh134896# Icon code needs rewrite
- #rh134897# "Other Networks..." dialog needs implementing
- #rh135055# Menu highlights incorrectly in NM
- #rh135648# segfault with cipsec0
- #rh135722# NetworkManager will not allow zaurus to sync via usb0
- #rh135999# NetworkManager-0.3.1 will not connect to 128 wep
- #rh136866# applet needs tooltips
- #rh137047# lots of applets, yay!
- #rh137341# Network Manager dies after disconnecting from wired network second time
- Better checking for wireless devices
- Fix some memleaks
- Fix issues with dhclient declining an offered address
- Fix an activation thread deadlock
- More accurately detect "Other wireless networks" that are encrypted
- Don't bring devices down as much, won't hotplug-spam as much anymore
	about firmware
- Add a "network not found" dialog when the user chooses a network that could
	not be connected to

* Tue Oct 26 2004 <dcbw@redhat.com> - 0.3.1-2
- Fix escaping of ESSIDs in gconf

* Tue Oct 19 2004  <jrb@redhat.com> - 0.3.1-1
- minor point release to improve error handling and translations

* Fri Oct 15 2004 Dan Williams <dcbw@redhat.com> 0.3-1
- Update from CVS, version 0.3

* Tue Oct 12 2004 Dan Williams <dcbw@redhat.com> 0.2-4
- Update from CVS
- Improvements:
	o Better link checking on wireless cards
	o Panel applet now a Notification Area icon
	o Static IP configuration support

* Mon Sep 13 2004 Dan Williams <dcbw@redhat.com> 0.2-3
- Update from CVS

* Sat Sep 11 2004 Dan Williams <dcbw@redhat.com> 0.2-2
- Require gnome-panel, not gnome-panel-devel
- Turn off by default

* Thu Aug 26 2004 Dan Williams <dcbw@redhat.com> 0.2-1
- Update to 0.2

* Thu Aug 26 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- spec-changes to req glib2 instead of glib

* Fri Aug 20 2004 Dan Williams <dcbw@redhat.com> 0.1-3
- First public release

