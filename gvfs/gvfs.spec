Summary: Backends for the gio framework in GLib
Name: gvfs
Version: 1.4.3
Release: 27%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
URL: http://www.gtk.org
Source: http://download.gnome.org/sources/gvfs/1.4/gvfs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: pkgconfig
BuildRequires: glib2-devel >= 2.22.5-6
BuildRequires: dbus-glib-devel
BuildRequires: /usr/bin/ssh
BuildRequires: libcdio-devel >= 0.78.2
# obexftp backend is the last user requiring hal
BuildRequires: hal-devel >= 0.5.10
BuildRequires: libgudev-devel
BuildRequires: libsoup-devel >= 2.25.2
BuildRequires: avahi-glib-devel >= 0.6
BuildRequires: gnome-keyring-devel
BuildRequires: intltool
BuildRequires: gettext-devel
BuildRequires: GConf2-devel
BuildRequires: gnome-disk-utility-devel >= 2.29.90-1
BuildRequires: PolicyKit-devel
# This is a hack until the xfce4-notifyd dependency issue is fixed
# https://fedorahosted.org/rel-eng/ticket/1788
#BuildRequires: notification-daemon


Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

# The patch touches Makefile.am files:
BuildRequires: automake autoconf
BuildRequires: libtool
# http://bugzilla.gnome.org/show_bug.cgi?id=567235
Patch0: gvfs-archive-integration.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=591005
Patch1: 0001-Add-AFC-backend.patch
# disable HAL volume monitor, yet still detect hal headers for obexftp
Patch2: disable-hal-monitor.patch
# [gvfs][ALL_LANG] Translation updates
# https://bugzilla.redhat.com/show_bug.cgi?id=589211
Patch3: translation-updates.patch

# from upstream
Patch12: gvfs-1.4.1-http-suport-stream-query-info.patch
Patch13: gvfs-1.4.1-http-soup-header-parsing.patch
Patch14: gvfs-1.5.1-dont-leak-mountoperation.patch
# Recognize gphoto2 cameras which don't implement get storageinfo
# https://bugzilla.redhat.com/show_bug.cgi?id=552856
Patch15: gvfs-1.5.1-gphoto2-no-storageinfo-support.patch
# from upstream
Patch16: gvfs-1.5.1-obexftp-dbus-private-connection.patch
Patch17: gvfs-1.5.2-trash-finalize.patch
Patch18: gvfs-1.5.2-archive-finalize.patch
Patch19: gvfs-1.5.2-ftp-symlink-target-not-defined.patch
Patch20: gvfs-1.5.2-ftp-name-data-connection-method.patch
Patch21: gvfs-1.5.2-ftp-separate-data-connection-method-supported.patch
Patch22: gvfs-1.5.2-ftp-PASV-v4.patch
Patch23: gvfs-1.5.2-ftp-PASV-EPASV-v4-v6.patch

# gvfsd-sftp crashes on unmount
# https://bugzilla.redhat.com/show_bug.cgi?id=557548
Patch24: gvfs-1.5.4-sftp-unmount.patch

# Fix stringv transfer over dbus
# https://bugzilla.redhat.com/show_bug.cgi?id=616145
Patch25: gvfs-1.6.5-stringv-dbus.patch
Patch26: gvfs-1.6.1-dbus-skip-malformed.patch

# Hide mounts having a path element starting with dot
# https://bugzilla.redhat.com/show_bug.cgi?id=624795
Patch27: gvfs-1.7.0-hide-dot-mounts.patch

# SELinux is preventing /usr/bin/ssh access to a leaked /dev/ptmx file descriptor
# https://bugzilla.redhat.com/show_bug.cgi?id=616838
Patch28: gvfs-1.7.0-sftp-close-pty-master.patch

# [abrt] crash in gvfs-archive-1.4.3-6.el6: Process /usr/libexec/gvfsd-archive was killed by signal 6 (SIGABRT)
# https://bugzilla.redhat.com/show_bug.cgi?id=645630
Patch29: gvfs-1.4.3-archive-duplicate-mount.patch

# AFC patches from upstream
Patch30: gvfs-1.4.1-afc-hide-dot-files.patch
Patch31: gvfs-1.4.1-afc-fast-mime.patch
Patch32: gvfs-1.4.1-afc-st_mtime.patch
Patch33: gvfs-1.4.1-afc-latest-libiphone-api.patch
Patch34: gvfs-1.4.1-afc-no-libgudev-dependency.patch
Patch35: gvfs-1.4.1-afc-mtime-setting.patch
Patch36: gvfs-1.4.1-afc-mtime-pre-3.1-devices.patch
Patch37: gvfs-1.4.1-afc-dont-leak-volumes.patch
Patch38: gvfs-1.4.1-afc-fix-mtime-setting.patch
Patch39: gvfs-1.4.1-afc-thumbnails.patch
Patch40: gvfs-1.4.1-afc-x-content-types.patch
Patch41: gvfs-1.4.1-afc-preview-icon.patch
Patch42: gvfs-1.4.1-afc-shadowed-mount.patch
Patch43: gvfs-1.4.1-afc-indentation.patch
Patch44: gvfs-1.5.3-afc-new-libiphone.patch
Patch45: gvfs-1.5.3-use-libimobiledevice.patch

# LVM2 patches from upstream
# https://bugzilla.redhat.com/show_bug.cgi?id=567743
Patch50: gvfs-1.5.4-comment-null-GduDevice.patch
Patch51: gvfs-1.5.4-not-removable-when-lacks-GduDevice.patch
Patch52: gvfs-1.5.4-handle-null-device-when-stopping.patch
Patch53: gvfs-1.5.4-g_strcmp0.patch
Patch54: gvfs-1.5.4-volume-add-has_presentable.patch
Patch55: gvfs-1.5.4-clarify-comment.patch
Patch56: gvfs-1.5.4-identify-by-presentable.patch

# Bug 667367 - typo in gvfs-mkdir --help
# https://bugzilla.redhat.com/show_bug.cgi?id=667367
Patch100: gvfs-1.5.1-mkdir-description.patch
# The following patch is a simple grep from gvfs git master
# to have updated translations
Patch101: gvfs-1.5.1-mkdir-description-translations.patch
# unexpected behaviour of Places -> luks device
# https://bugzilla.redhat.com/show_bug.cgi?id=599055
Patch102: gvfs-1.9.3-gdu-nohide-crypto-mounts.patch
# Defect revealed by Coverity scan
# https://bugzilla.redhat.com/show_bug.cgi?id=722465
Patch103: gvfs-1.9.3-afc-coverity.patch
Patch104: gvfs-1.9.3-obexftp-coverity.patch
# exitcodes of gvfs binaries
# https://bugzilla.redhat.com/show_bug.cgi?id=682799
Patch105: gvfs-1.5.5-tools-return-values.patch
# segfault when running gvfs-set-attribute with nonsense arg
# https://bugzilla.redhat.com/show_bug.cgi?id=746905
Patch106: gvfs-1.6.3-gvfs-set-attribute-arguments.patch
# gvfsd memory leak
# https://bugzilla.redhat.com/show_bug.cgi?id=809708
Patch107: gvfs-1.9.0-dbus-leak.patch
# Erasing DVD+/-RW/BD-RE with Brasero causes it to be unusable
# https://bugzilla.redhat.com/show_bug.cgi?id=669526
Patch108: gvfs-1.6.1-blank-cd.patch
Patch109: gvfs-1.4.3-bdre-formatted.patch
# wrong exit code gvfs-open
# https://bugzilla.redhat.com/show_bug.cgi?id=746978
Patch110: gvfs-1.9.4-gvfs-open-exitcode.patch
# exitcodes of gvfs binaries
# https://bugzilla.redhat.com/show_bug.cgi?id=682799
Patch111: gvfs-1.13.4-programs-exit-values.patch

# Fix gdbusutils name conflict with GIO
# https://bugzilla.redhat.com/show_bug.cgi?id=1071374
Patch112: gvfs-1.6.2-gdbusutils.h-name-conflict.patch

# Fix metadata traffic on nfs
# https://bugzilla.redhat.com/show_bug.cgi?id=902448
Patch113: gvfs-1.17.0-metadata-Be-more-resistive-to-broken-journal-files.patch
Patch114: gvfs-1.17.0-metadata-Force-tree-re-read-after-successful-flush.patch
Patch115: gvfs-1.17.0-metadata-Create-new-journal-if-it-doesn-t-exist.patch
Patch116: gvfs-1.17.0-metadata-Put-journal-in-XDG_RUNTIME_DIR-for-shared-N.patch
Patch117: gvfs-1.17.0-metadata-Use-shorter-writeout-timeout-on-NFS.patch
Patch118: gvfs-1.17.0-metadata-Flush-all-scheduled-writeouts-on-daemon-exi.patch
Patch119: gvfs-1.17.1-metadata-Fix-short-journal-check.patch

# Check GConf2 key before use to avoid error dialog
# https://bugzilla.redhat.com/show_bug.cgi?id=1049232
Patch120: gconf-key-check.patch

# Fix renaming files on webdav
# https://bugzilla.redhat.com/show_bug.cgi?id=1011835
Patch121: gvfs-1.9.0-re-root-a-given-path-with-a-mount_prefix.patch
Patch122: gvfs-1.9.0-pass-mount_info-to-async_path_call-callbacks.patch
Patch123: gvfs-1.9.0-re-root-the-path-in-set_display_name.patch

Patch124: gconf-allow-deprecated.patch

# Fix SFTP mounting with updated OpenSSH (from upstream)
# https://bugzilla.redhat.com/show_bug.cgi?id=1118325
Patch125: gvfs-1.6.4-sftp-use-poll-to-cope-with-openssh-5.6-changes.patch
Patch126: gvfs-1.6.4-sftp-fix-poll-timeout.patch

# gvfsd-trash is preventing autofs mounts from being expired when fs perms are o-rx
# https://bugzilla.redhat.com/show_bug.cgi?id=998061
Patch127: gvfs-1.22.1-trash-do-not-care-about-mount-points-without-read-ac.patch

# The gvfs-gdu-volume-monitor process was aborted during system shutdown
# https://bugzilla.redhat.com/show_bug.cgi?id=1140451
Patch128: gvfs-1.13.9-gdu-volume-monitor-Handle-gdu_pool_new-returning-NUL.patch
Patch129: gvfs-1.13.9-gdu-volume-monitor-Don-t-unref-possibly-NULL-object.patch

# Bug 1210203 - gvfsd-metadata causes high cpu and disk usage
# https://bugzilla.redhat.com/show_bug.cgi?id=1210203
Patch130: gvfs-1.21.92-metatree-avoid-endless-looping-when-the-entry-is-too.patch

# Bug 1165676 - gvfsd-gphoto2 crashes when iPhone is connected
# https://bugzilla.redhat.com/show_bug.cgi?id=1165676
Patch131: gvfs-1.5.1-fix-NULL-dereference.patch

# Fix handling of paths containing dots in archives
# https://bugzilla.redhat.com/show_bug.cgi?id=713179
Patch132: gvfs-1.7.3-archive-Skip-leading-.-from-pathnames-if-present.patch
Patch133: gvfs-1.21.2-archive-Ignore-filenames-consisting-of-a-single.patch
Patch134: gvfs-1.21.92-archive-Fix-some-memory-leaks.patch
Patch135: gvfs-1.21.92-archive-Allow-reading-files-with-.-in-the-path.patch

# Fix metadata daemon crashes
# https://bugzilla.redhat.com/show_bug.cgi?id=1110451
Patch136: gvfs-1.23.4-metadata-don-t-crash-if-meta_tree_init-fails.patch
Patch137: gvfs-1.23.91-metadata-return-if-meta_tree_refresh-failed.patch
Patch138: gvfs-1.23.91-metatree-always-clear-fd-to-1.patch
Patch139: gvfs-1.23.91-metadata-don-t-crash-if-tree-write-out-failed.patch

# Use native move operation on dav
# https://bugzilla.redhat.com/show_bug.cgi?id=1270031
Patch140: gvfs-1.21.1-dav-Use-the-native-MOVE-operation-for-moving.patch
Patch141: gvfs-1.23.2-dav-try-copy-and-delete-fallback-if-backup-couldn-t-.patch
Patch142: gvfs-1.23.5-dav-Fix-up-error-handling-when-moving.patch
Patch143: gvfs-1.23.5-dav-Fix-a-few-memory-leaks.patch
Patch144: gvfs-1.25.2-dav-Emit-progress-callbacks-when-copying-and-moving.patch

# Translation updates
# https://bugzilla.redhat.com/show_bug.cgi?id=1110451
# https://bugzilla.redhat.com/show_bug.cgi?id=1270031
# https://bugzilla.redhat.com/show_bug.cgi?id=1333640
Patch145: translation-updates2.patch
Patch146: translation-updates3.patch

Obsoletes: gnome-mount <= 0.8
Obsoletes: gnome-mount-nautilus-properties <= 0.8

%description
The gvfs package provides backend implementations for the gio
framework in GLib. It includes ftp, sftp, cifs.


%package devel
Summary: Development files for gvfs
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The gvfs-devel package contains headers and other files that are
required to develop applications using gvfs.


%package fuse
Summary: FUSE support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: fuse-devel
Requires: fuse

%description fuse
This package provides support for applications not using gio
to access the gvfs filesystems.


%package smb
Summary: Windows fileshare support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: libsmbclient-devel >= 3.2.0-1.pre2.8
BuildRequires: libtalloc-devel >= 1.3.0-0

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using gvfs.


%package archive
Summary: Archiving support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: libarchive-devel >= 2.7.1-1

%description archive
This package provides support for accessing files inside Zip and Tar archives,
as well as ISO images, to applications using gvfs.


%package gphoto2
Summary: gphoto2 support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
BuildRequires: libgphoto2-devel
BuildRequires: libusb-devel
BuildRequires: libexif-devel

%description gphoto2
This package provides support for reading and writing files on
PTP based cameras (Picture Transfer Protocol) and MTP based
media players (Media Transfer Protocol) to applications using gvfs.


%ifnarch s390 s390x
%package obexftp
Summary: ObexFTP support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: obex-data-server >= 0.3.4-6
BuildRequires: bluez-libs-devel >= 3.12
BuildRequires: expat-devel
Obsoletes: gnome-vfs2-obexftp <= 0.4

%description obexftp
This package provides support for reading files on Bluetooth mobile phones
and devices through ObexFTP to applications using gvfs.

%package afc
Summary: AFC support for gvfs
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: usbmuxd
BuildRequires: libimobiledevice-devel >= 0.9.7

%description afc
This package provides support for reading files on mobile devices
including phones and music players to applications using gvfs.
%endif


%prep
%setup -q
%patch0 -p1 -b .archive-integration
%patch1 -p1 -b .afc
%patch2 -p1 -b .disable-hal
%patch3 -p1 -b .translations
%patch12 -p1 -b .http-query-info
%patch13 -p1 -b .http-headers
%patch14 -p1 -b .moutop-leak
%patch15 -p1 -b .gphoto2-storageinfo
%patch16 -p1 -b .obexftp-dbus
%patch17 -p1 -b .trash-finalize
%patch18 -p1 -b .archive-finalize
%patch19 -p1 -b .ftp-symlink-target-not-defined
%patch20 -p1 -b .ftp-name-data-connection-method
%patch21 -p1 -b .ftp-separate-data-connection-method-supported
%patch22 -p1 -b .ftp-PASV-v4
%patch23 -p1 -b .ftp-PASV-EPASV-v4-v6
%patch24 -p1 -b .sftp-unmount
%patch25 -p1 -b .stringv-dbus
%patch26 -p1 -b .dbus-skip-malformed
%patch27 -p1 -b .hide-dot-mounts
%patch28 -p1 -b .close-pty-master
%patch29 -p1 -b .archive-duplicate-mount

%patch30 -p1 -b .afc-hide-dot-files
%patch31 -p1 -b .afc-fast-mime
%patch32 -p1 -b .afc-st_mtime
%patch33 -p1 -b .afc-latest-libiphone-api
%patch34 -p1 -b .afc-no-libgudev-dependency
%patch35 -p1 -b .afc-mtime-setting
%patch36 -p1 -b .afc-mtime-pre-3.1-devices
%patch37 -p1 -b .afc-dont-leak-volumes
%patch38 -p1 -b .afc-fix-mtime-setting
%patch39 -p1 -b .afc-thumbnails
%patch40 -p1 -b .afc-x-content-types
%patch41 -p1 -b .afc-preview-icon
%patch42 -p1 -b .afc-shadowed-mount
%patch43 -p1 -b .afc-indentation
%patch44 -p1 -b .afc-new-libiphone
%patch45 -p1 -b .use-libimobiledevice

%patch50 -p1 -b .comment-null-GduDevice
%patch51 -p1 -b .not-removable-when-lacks-GduDevice
%patch52 -p1 -b .handle-null-device-when-stopping
%patch53 -p1 -b .g_strcmp0
%patch54 -p1 -b .volume-add-has_presentable
%patch55 -p1 -b .clarify-comment
%patch56 -p1 -b .identify-by-presentable

%patch100 -p1 -b .mkdir-description
%patch101 -p1 -b .mkdir-description-translations
%patch102 -p1 -b .gdu-nohide-crypto-mounts
%patch103 -p1 -b .afc-coverity
%patch104 -p1 -b .obexftp-coverity
%patch105 -p1 -b .tools-return-values
%patch106 -p1 -b .gvfs-set-attribute-arguments
%patch107 -p1 -b .dbus-leak
%patch108 -p1 -b .blank-cd
%patch109 -p1 -b .bdre-formatted
%patch110 -p1 -b .gvfs-open-exitcode
%patch111 -p1 -b .programs-exit-values

%patch112 -p1 -b .rename-gdbusutils
mv common/gdbusutils.c common/gvfsdbusutils.c
mv common/gdbusutils.h common/gvfsdbusutils.h

%patch113 -p1 -b .metadata-be-more-resistive-to-broken-journal
%patch114 -p1 -b .metadata-force-tree-re-read-after-flush
%patch115 -p1 -b .metadata-create-new-journal-after-flush
%patch116 -p1 -b .metadata-put-journal-in-XDG_RUNTIME_DIR
%patch117 -p1 -b .metadata-use-shorter-writeout-on-NFS
%patch118 -p1 -b .metadata-flush-all-scheduled-writeouts
%patch119 -p1 -b .metadata-fix-short-journal-check

%patch120 -p1 -b .gconf-key-check
%patch121 -p1 -b .re-root-path
%patch122 -p1 -b .mount_info_to_async_path_call
%patch123 -p1 -b .re-root-path-set_display_name

%patch124 -p1 -b .gconf-allow-deprecated

%patch125 -p1 -b .sftp-use-poll
%patch126 -p1 -b .sftp-fix-poll-timeout

%patch127 -p1 -b .trash-ignore-mounts-without-read-access

%patch128 -p1 -b .handle-null-gdu-pool
%patch129 -p1 -b .handle-null-gdu-pool-on-finalize

%patch130 -p1 -b .avoid-metadata-looping
%patch131 -p1 -b .fix-null-dereference

%patch132 -p1 -b .archive-skip-leading-.-from-pathnames-if-present
%patch133 -p1 -b .archive-ignore-filenames-consisting-of-a-single
%patch134 -p1 -b .archive-fix-some-memory-leaks
%patch135 -p1 -b .archive-allow-reading-files-with-.-in-the-path

%patch136 -p1 -b .metadata-don-t-crash-if-meta_tree_init-fails
%patch137 -p1 -b .metadata-return-if-meta_tree_refresh-failed
%patch138 -p1 -b .metatree-always-clear-fd-to-1
%patch139 -p1 -b .metadata-don-t-crash-if-tree-write-out-failed

%patch140 -p1 -b .dav-use-the-native-move-operation-for-moving
%patch141 -p1 -b .dav-try-copy-and-delete-fallback-if-backup-couldn-t-
%patch142 -p1 -b .dav-fix-up-error-handling-when-moving
%patch143 -p1 -b .dav-fix-a-few-memory-leaks
%patch144 -p1 -b .dav-emit-progress-callbacks-when-copying-and-moving

%patch145 -p1 -b .translation-updates2
%patch146 -p1 -b .translation-updates3

%build

# Needed for gvfs-0.2.1-archive-integration.patch
libtoolize --force  || :
aclocal  || :
autoheader  || :
automake  || :
autoconf  || :

CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure --enable-gdu --with-bash-completion-dir=%{_sysconfdir}/bash_completion.d/
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang gvfs

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
# Reload .mount files:
killall -USR1 gvfsd >&/dev/null || :
# Update desktop files mime mappings:
update-desktop-database &> /dev/null ||:

%postun
/sbin/ldconfig
# Update desktop files mime mappings:
update-desktop-database &> /dev/null ||:

# Reload .mount files when single subpackage is installed:
%post smb
killall -USR1 gvfsd >&/dev/null || :
%post archive
killall -USR1 gvfsd >&/dev/null || :
%post gphoto2
killall -USR1 gvfsd >&/dev/null || :
%ifnarch s390 s390x
%post obexftp
killall -USR1 gvfsd >&/dev/null || :
%post afc
killall -USR1 gvfsd >&/dev/null || :
%endif

%files -f gvfs.lang
%defattr(-, root, root, -)
%doc AUTHORS COPYING NEWS README
%dir %{_datadir}/gvfs
%dir %{_datadir}/gvfs/mounts
%{_sysconfdir}/bash_completion.d/gvfs-bash-completion.sh
%{_datadir}/gvfs/mounts/sftp.mount
%{_datadir}/gvfs/mounts/trash.mount
%{_datadir}/gvfs/mounts/cdda.mount
%{_datadir}/gvfs/mounts/computer.mount
%{_datadir}/gvfs/mounts/dav.mount
%{_datadir}/gvfs/mounts/dav+sd.mount
%{_datadir}/gvfs/mounts/http.mount
%{_datadir}/gvfs/mounts/localtest.mount
%{_datadir}/gvfs/mounts/burn.mount
%{_datadir}/gvfs/mounts/dns-sd.mount
%{_datadir}/gvfs/mounts/network.mount
%{_datadir}/gvfs/mounts/ftp.mount
%{_datadir}/dbus-1/services/gvfs-daemon.service
%{_datadir}/dbus-1/services/gvfs-metadata.service
%{_datadir}/dbus-1/services/org.gtk.Private.GduVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/gdu.monitor
%{_libdir}/libgvfscommon.so.*
%{_libdir}/libgvfscommon-dnssd.so.*
%{_libdir}/gio/modules/libgioremote-volume-monitor.so
%{_libdir}/gio/modules/libgvfsdbus.so
%{_libdir}/gio/modules/libgiogconf.so
%{_libexecdir}/gvfsd
%{_libexecdir}/gvfsd-ftp
%{_libexecdir}/gvfsd-sftp
%{_libexecdir}/gvfsd-trash
%{_libexecdir}/gvfsd-cdda
%{_libexecdir}/gvfsd-computer
%{_libexecdir}/gvfsd-dav
%{_libexecdir}/gvfsd-http
%{_libexecdir}/gvfsd-localtest
%{_libexecdir}/gvfsd-burn
%{_libexecdir}/gvfsd-dnssd
%{_libexecdir}/gvfsd-network
%{_libexecdir}/gvfsd-metadata
%{_libexecdir}/gvfs-gdu-volume-monitor
%{_bindir}/gvfs-cat
%{_bindir}/gvfs-copy
%{_bindir}/gvfs-info
%{_bindir}/gvfs-less
%{_bindir}/gvfs-ls
%{_bindir}/gvfs-mkdir
%{_bindir}/gvfs-monitor-dir
%{_bindir}/gvfs-monitor-file
%{_bindir}/gvfs-mount
%{_bindir}/gvfs-move
%{_bindir}/gvfs-open
%{_bindir}/gvfs-rename
%{_bindir}/gvfs-rm
%{_bindir}/gvfs-save
%{_bindir}/gvfs-trash
%{_bindir}/gvfs-tree
%{_bindir}/gvfs-set-attribute

%files devel
%defattr(-, root, root, -)
%dir %{_includedir}/gvfs-client
%dir %{_includedir}/gvfs-client/gvfs
%{_includedir}/gvfs-client/gvfs/gvfsurimapper.h
%{_includedir}/gvfs-client/gvfs/gvfsuriutils.h
%{_libdir}/libgvfscommon.so
%{_libdir}/libgvfscommon-dnssd.so


%files fuse
%defattr(-, root, root, -)
%{_libexecdir}/gvfs-fuse-daemon


%files smb
%defattr(-, root, root, -)
%{_libexecdir}/gvfsd-smb
%{_libexecdir}/gvfsd-smb-browse
%{_datadir}/gvfs/mounts/smb-browse.mount
%{_datadir}/gvfs/mounts/smb.mount


%files archive
%defattr(-, root, root, -)
%dir %{_datadir}/applications/mount-archive.desktop
%{_libexecdir}/gvfsd-archive
%{_datadir}/gvfs/mounts/archive.mount


%files gphoto2
%defattr(-, root, root, -)
%{_libexecdir}/gvfsd-gphoto2
%{_datadir}/gvfs/mounts/gphoto2.mount
%{_libexecdir}/gvfs-gphoto2-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.Private.GPhoto2VolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/gphoto2.monitor


%ifnarch s390 s390x
%files obexftp
%defattr(-, root, root, -)
%{_libexecdir}/gvfsd-obexftp
%{_datadir}/gvfs/mounts/obexftp.mount

%files afc
%defattr(-, root, root, -)
%{_libexecdir}/gvfsd-afc
%{_datadir}/gvfs/mounts/afc.mount
%{_libexecdir}/gvfs-afc-volume-monitor
%{_datadir}/dbus-1/services/org.gtk.Private.AfcVolumeMonitor.service
%{_datadir}/gvfs/remote-volume-monitors/afc.monitor
%endif


%changelog
* Tue Nov 1 2016 Ondrej Holy <oholy@redhat.com> - 1.4.3-27
- Translation updates (#1333640)

* Fri Jan 8 2016 Ondrej Holy <oholy@redhat.com> - 1.4.3-26
- Translation updates (#1110451, #1270031)

* Thu Nov 19 2015 Ondrej Holy <oholy@redhat.com> - 1.4.3-25
- Use native move operation on dav (#1270031)

* Tue Nov 10 2015 Ondrej Holy <oholy@redhat.com> - 1.4.3-24
- Fix metadata daemon crashes (#1110451)

* Tue Nov 10 2015 Ondrej Holy <oholy@redhat.com> - 1.4.3-23
- Fix handling of paths containing dots in archives (#713179)

* Fri Apr 10 2015 Ondrej Holy <oholy@redhat.com> - 1.4.3-22
- Fix crash when iPhone is connected (#1165676)

* Thu Apr 9 2015 Ondrej Holy <oholy@redhat.com> - 1.4.3-21
- Avoid endless looping when the metatree entry is too large (#1210203)

* Thu Dec 17 2014 Ondrej Holy <oholy@redhat.com> - 1.4.3-20
- Handle gdu_pool_new() returning NULL gracefully (#1140451)

* Thu Dec 4 2014 Ondrej Holy <oholy@redhat.com> - 1.4.3-19
- Ignore mount points without read access from the trash backend (#998061)

* Thu Jul 17 2014 Ondrej Holy <oholy@redhat.com> - 1.4.3-18
- Fix GConf module building with updated GLib2 (#1118704)
- Fix SFTP mounting with updated OpenSSH (#1118325)

* Fri May 23 2014 Ondrej Holy <oholy@redhat.com> - 1.4.3-17
- Check GConf2 key before use to avoid error dialog (#1049232)
- Fix renaming files on webdav (#1011835)
- Fix libarchive dependency

* Fri May 23 2014 Ondrej Holy <oholy@redhat.com> - 1.4.3-16
- Fix gdbusutils name conflict with GIO (#1071374)
- Fix metadata traffic on nfs (#902448)

* Fri Jul 20 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-15
- Fix several memory leaks (#809708)
- Fix formatted BD-RE media detection (#669526)
- Fix gvfs-open exit code on error (#746978)
- Fix gvfs-info exit code on error (#746977)
- Fix gvfs-cat exit code on error (#749369)
- Fix gvfs-ls exit code on error (#749371)
- Fix gvfs-mount exit code on error (#749372)

* Fri Oct 21 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-14
- Fix gvfs-set-attribute segfaulting on certain arguments (#746905)

* Wed Aug 10 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-13
- Fix interaction with LUKS volumes with fstab records (#599055)
- Fix defects revealed by Coverity scan (#722465)
- Correct return values on error for programs (#682799)

* Wed Jan  5 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-12
- Fix wrong description in gvfs-mkdir (#667367)

* Tue Jan  4 2011 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-11
- archive: Fix crasher when archive is already mounted (#645630)

* Mon Dec 20 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-10
- Fix emblem handling in trash (#616145)
- Require new gnome-disk-utility (#636540)
- Hide mounts having a path element starting with dot (#624795)
- Fix SELinux while accessing a leaked /dev/ptmx file descriptor (#616838)

* Thu Jun  3 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-9
- Build with -fno-strict-aliasing (#596799)

* Thu May 13 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-8
- Translation updates (#589211)

* Wed Mar 10 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-7
- Better support for LVM2 volumes (#567743)

* Mon Feb 15 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-6
- SFTP: Fix crash on unmount
- FTP: Backport several PASV/EPSV fixes from upstream (#542205, #555033)
- AFC: Use new libimobiledevice library (#565567)

* Wed Feb  3 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-5
- archive: fix assertion on finalize (#557545)

* Thu Jan 21 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-4
- Don't build obexftp backend on s390 (#557209)

* Tue Jan 19 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-3
- Avoid crash on race to mount gvfstrash (#555337)

* Wed Jan 13 2010 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-2
- Nuke HAL volume monitor
- Don't leak mount job operation (#552842)
- Recognize gphoto2 cameras which don't implement get storageinfo (#552856)
- ObexFTP: Use a private D-Bus connection for obex-data-server (#539347)

* Tue Dec 15 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.3-1
- Update to 1.4.3

* Tue Dec  8 2009 David Zeuthen <davidz@redhat.com> - 1.4.2-3
- Backport fixes from git
- Correct wrong assumptions about how libgdu.so works
- Make LUKS volumes work with new mount(8) behavior
- Be more careful deciding what volumes to automatically mount

* Tue Dec  1 2009 Alexander Larsson <alexl@redhat.com> - 1.4.2-2
- Backport fixes from git:
- Don't leak metadata strings
- Don't access uninitialized data in ftp backend

* Mon Nov 30 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Mon Nov 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-7
- SMB: Fix free space calculation for Windows hosts

* Thu Nov 12 2009 Matthias Clasen <mclasen@redhat.com> 1.4.1-6
- Add obsoletes for gnome-mount

* Thu Nov 12 2009 Bastien Nocera <bnocera@redhat.com> 1.4.1-5
- Add obsoletes for gnome-vfs2-obexftp

* Tue Nov 10 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-4
- SMB: Support querying filesystem size and free space

* Tue Nov  3 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-3
- gdu-volume-monitor: don't crash on NULL devices (#529982)

* Mon Nov  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-2
- Reload .mount files when single package is installed

* Tue Oct 20 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Oct 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-7
- HTTP: Support g_file_input_stream_query_info()
- HTTP: Use libsoup header parsing function
- Set correct MIME type for MTP music players

* Wed Oct 14 2009 Bastien Nocera <bnocera@redhat.com> 1.4.0-6
- Fix crasher in ObexFTP (#528181)

* Fri Oct  9 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-5
- Don't always overwrite on trash restore
- Separate "Safely Remove Drive" from "Eject"
- Don't advertise can_poll for drives not using removable media
- Disallow mounting empty drives
- Disallow ejecting empty drives
- Silently drop eject error messages when detaching drive

* Thu Oct  8 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-4
- Fix Nautilus not displaying friendly icons for SSH-connected system (#526892)
- Actually apply the logical partitions patch

* Thu Oct  1 2009 Matthias Clasen <mclasen@redhat.com> - 1.4.0-3
- Consider logical partitions when deciding if a drive should be ignored

* Tue Sep 29 2009 Matthias Clasen <mclasen@redhat.com> - 1.4.0-2
- Fix the lack of icons in the http backend

* Mon Sep 21 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.6-2
- Rebuilt with new fuse

* Mon Sep  7 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.6-1
- Update to 1.3.6

* Wed Aug 26 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.5-2
- Don't mount interactively during login

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.5-1
- Update to 1.3.5

* Mon Aug 17 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.4-7
- Fix Nautilus can't create "untitled folder" on sftp mounts (#512611)

* Fri Aug 14 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-6
- Update AFC patch

* Thu Aug 13 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.4-5
- More complete fix for DAV mount path prefix issues

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-4
- Fix crash on startup for the afc volume monitor

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-3
- libgudev-devel is required for the gphoto2 monitor

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 1.3.4-2
- Add AFC backend

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Fri Aug  7 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.3-3
- Fix bad mount prefix stripping (part of #509612)
- Fix gvfsd-sftp segfault when asking a question
- Enable tar+xz in the archive mounter

* Tue Aug  4 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.3-2
- Fix gedit crashed with SEGV in strlen()
- Fix SMB protocol not handled when opening from a bookmark (#509832)

* Wed Jul 29 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.2-3
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.2-1
- Update to 1.3.2
- Drop upstreamed patches

* Mon Jun 22 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.3.1-2
- Bump version requirements
- Backport FTP and Computer backend patches from master

* Mon Jun 15 2009 Matthias Clasen <mclasen@redhat.com> - 1.3.1-1
- Update to 1.3.1
- Drop obsolete patches

* Fri Jun 12 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-3
- Move bash-completion out of profile.d (#466883)

* Mon Jun  8 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-2
- SFTP: Increase timeout (#504339)

* Mon May 18 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.3-1
- Update to 1.2.3
- Prevent deadlocks in dnssd resolver (#497631)

* Tue May 12 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.2-5
- Require separate libtalloc to fix libsmbclient
- Ref the infos in next_files_finish (gnome #582195)
- FTP: parse file sizes > 4GB correctly (#499286)
- CDDA: allow query well-formed filenames only (#499266)

* Sat May 02 2009 David Zeuthen <davidz@redhat.com> - 1.2.2-4
- Don't show drives that are supposed to be hidden (#498649)
- Only automount if media or drive was just inserted - this fixes
  a problem with spurious automounts when partitioning/formatting

* Wed Apr 15 2009 David Zeuthen <davidz@redhat.com> - 1.2.2-3
- Sync with the gdu-volume-monitor branch

* Mon Apr 13 2009 Alexander Larsson <alexl@redhat.com> - 1.2.2-2
- Add ssh-auth-sock patch from svn

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.2-1
- Update to 1.2.2
- Allow eject even on non-ejectable devices

* Sat Apr 11 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-5
- Don't show drives in computer:/// if media is available but
  no volumes are recognized (#495152)

* Sat Apr 11 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.1-4
- No need for bash completion to be executable

* Thu Apr  9 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-3
- Clean up gdu patches and bump BR for gdu to 0.3
- Avoiding showing volume for ignored mounts (#495033)

* Thu Apr  9 2009 David Zeuthen <davidz@redhat.com> - 1.2.1-2
- Avoid automounting device-mapper devices and similar (#494144)

* Thu Apr  2 2009 Matthias Clasen <mclasen@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Wed Mar 18 2009 David Zeuthen <davidz@redhat.com> - 1.2.0-2
- GNOME #575728 - crash in Open Folder: mounting a crypto volume

* Mon Mar 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Wed Mar 11 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.8-2
- Fix 100% cpu usage when connecting to a ssh key and denying key access
- Fix monitors leak

* Tue Mar 10 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.8-1
- Update to 1.1.8

* Mon Mar  9 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-5
- Expose device file attribute for all items in computer://

* Fri Mar  6 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-4
- Fix volume lists not filled correctly

* Wed Mar  4 2009 David Zeuthen <davidz@redhat.com> - 1.1.7-3
- Update GVfs gdu patch to fix mount detection confusion (#488399)

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 1.1.7-2
- Port to DeviceKit-disks

* Mon Mar  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.7-1
- Update to 1.1.7

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.6-1
- Update to 1.1.6

* Mon Feb  2 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.5-1
- Update to 1.1.5

* Wed Jan 28 2009 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-2
- ObexFTP write support

* Tue Jan 20 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.4-1
- Update to 1.1.4

* Tue Jan 13 2009 Adrian Reber <adrian@lisas.de> - 1.1.3-4
- Rebuild for libcdio-0.81

* Mon Jan 12 2009 Matthias Clasen  <mclasen@redhat.com> - 1.1.3-3
- Fix dav+sd.mount

* Fri Jan  9 2009 Matthias Clasen  <mclasen@redhat.com> - 1.1.3-2
- Support moving files in the burn backend

* Tue Jan  6 2009 Tomas Bzatek <tbzatek@redhat.com> - 1.1.3-1
- Update to 1.1.3

* Wed Dec 17 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.2-2
- Update the smb-browse auth patch

* Tue Dec 16 2008 Matthias Clasen  <mclasen@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Fri Dec 12 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-5
- FTP: Fix PASV connections

* Tue Dec  9 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-4
- Add support for .tar.lzma archives in archive mounter

* Fri Dec  5 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-3
- Added experimental smb-browse auth patch

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 1.1.1-2
- Update file lists to include the dav+sd backend

* Tue Dec  2 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Mon Dec  1 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Fri Nov  7 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-4
- SMB: timestamp setting support (#461505)

* Tue Nov  4 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-3
- Return an empty array on success when no content type
  matches (#468946)

* Fri Oct 24 2008 Alexander Larsson <alexl@redhat.com> - 1.0.2-2
- Don't return generic fallback icons for files,
  as this means custom mimetypes don't work (from svn)

* Mon Oct 20 2008 Tomas Bzatek <tbzatek@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Tue Oct  7 2008 Tomas Bzatek <tbzatek@redhat.com>  - 1.0.1-5
- Don't make warnings fatal (resolves #465693)

* Wed Oct  1 2008 David Zeuthen <davidz@redhat.com>  - 1.0.1-4
- Add patch for reverse mapping FUSE paths (bgo #530654)

* Mon Sep 29 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.1-3
- Fix mounting

* Mon Sep 29 2008 - Bastien Nocera <bnocera@redhat.com> - 1.0.1-2
- Update obexftp patch from upstream

* Wed Sep 24 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.1-1
- Update to 1.0.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com>  - 1.0.0-2
- Update to 1.0.0

* Fri Sep 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.8-6
- Update patch for missing file

* Fri Sep 19 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.8-5
- Updated patch, fixed deadlock whilst mounting

* Wed Sep 17 2008 Tomas Bzatek <tbzatek@redhat.com>  - 0.99.8-4
- Actually apply the kerberos patch

* Tue Sep 16 2008 Tomas Bzatek <tbzatek@redhat.com>  - 0.99.8-3
- SMB: Fix kerberos authentication

* Mon Sep 15 2008 Matthias Clasen <mclasen@redhat.com>  - 0.99.8-2
- Update to 0.99.8

* Mon Sep 15 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-4
- Update for BlueZ and obex-data-server D-Bus API changes

* Thu Sep 11 2008 Matthias Clasen <mclasen@redhat.com>  - 0.99.7.1-3
- Rebuild 

* Tue Sep 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-2
- Somebody made the build system be obnoxious and point out my
  errors in obvious ways

* Tue Sep 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.7.1-1
- Update to 0.99.7.1

* Tue Sep  2 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.6-1
- Update to 0.99.6

* Thu Aug 28 2008 Matthias Clasen <mclasen@redhat.com> - 0.99.5-3
- Add a comma

* Wed Aug 27 2008 - Bastien Nocera <bnocera@redhat.com> - 0.99.5-2
- Update some descriptions

* Wed Aug 20 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.5-1
- Update to 0.99.5

* Mon Aug  4 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.4-1
- Update to 0.99.4

* Sun Jul 27 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.3-2
- Use standard icon names

* Wed Jul 23 2008 Matthias Clasen  <mclasen@redhat.com> - 0.99.3-1
- Update to 0.99.3

* Tue Jul 22 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.2-1
- Update to 0.99.2
- Split out backends to separate packages

* Tue Jun 24 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.1-3
- gvfsd-trash: Skip autofs mounts

* Thu Jun 12 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.99.1-2
- Fix transfer of whole directories from FTP (#448560)

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.99.1-1
- Update to 0.99.1

* Tue May 27 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.4-1
- Update to 0.2.4

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-10
- Add application/zip to the supported mime types for the archive
  backend (launchpad #211697)

* Sun Apr 19 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-9
- Ensure archive mounts are read-only and turn on thumbnailing on them
- Update fuse threading patch

* Fri Apr 18 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-8
- Fix thread-safety issues in gvfs-fuse-daemon
- Prevent dbus from shutting us down unexpectedly

* Thu Apr 17 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-7
- Put X-Gnome-Vfs-System=gio into mount-archarive.desktop (See #442835)

* Wed Apr 16 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-6
- Reenable gphoto automounting 
- Support unmounting all mounts for a scheme

* Wed Apr 16 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-5
- Fix hangs when unmounting gphoto mounts

* Wed Apr 16 2008 David Zeuthen <davidz@redhat.com> - 0.2.3-4
- Only show mounts in /media and inside $HOME (#442189)

* Mon Apr 14 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-3
- Fix a bug that causes application crashes (#441084)

* Fri Apr 11 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-2
- Fix a crash of the fuse daemon on 64bit

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Fri Mar 28 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Tue Mar 25 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-4
- Moved fuse stuff to a dedicated package

* Thu Mar 20 2008 Alexander Larsson <alexl@redhat.com> - 0.2.1-3
- Add patch with simple archive backend UI integration

* Tue Mar 19 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-2
- Added libarchive dependency for archive backend
- Require new libsmbclient in order to get smb backend working again

* Tue Mar 18 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.2.1-1
- Update to 0.2.1 (archive backend temporarily disabled)

* Mon Mar 17 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.0.1-2
- Silence %%post

* Mon Mar 10 2008 Matthias Clasen  <mclasen@redhat.com> - 0.2.0.1-1
- Update to 0.2.0.1

* Thu Mar  6 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.11-2
- Add patch that fixes a deadlock when foreign volume is removed

* Tue Mar  4 2008 Matthias Clasen  <mclasen@redhat.com> - 0.1.11-1
- Update to 0.1.11

* Tue Mar 04 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.1.10-1
- Update to 0.1.10

* Mon Feb 25 2008 Alexander Larsson <alexl@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Thu Feb 14 2008 Alexander Larsson <alexl@redhat.com> - 0.1.7-3
- Add patch that fixes a smb bug that can cause short reads when copying files

* Tue Feb 12 2008 Alexander Larsson <alexl@redhat.com> - 0.1.7-2
- Fix double free in hal volume monitor
- Ensure gconf module is built by adding build dep

* Mon Feb 11 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Mon Jan 28 2008 Matthias Clasen <mclasen@redhat.com> - 0.1.5-1
- Update to 0.1.5
- Reenable http/dav 

* Mon Jan 21 2008 Alexander Larsson <alexl@redhat.com> - 0.1.4-2 
- Remove the http/dav stuff for now, as we don't have the latest libsoup

* Mon Jan 21 2008 Alexander Larsson <alexl@redhat.com> - 0.1.4-1
- Update to 0.1.4
- Send USR1 in post to reload config

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> 0.1.2-1
- Update to 0.1.2

* Tue Jan  8 2008 Matthias Clasen <mclasen@redhat.com> 0.1.1-1
- Update to 0.1.1

* Thu Dec 20 2007 Matthias Clasen <mclasen@redhat.com> 0.1.0-1
- Initial packaging
