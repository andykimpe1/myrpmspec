# If you have trouble building locally ('make local') try adding
#   %libguestfs_buildnet 1
# to your ~/.rpmmacros file.

# Enable to run tests during check
# Default is enabled
%if %{defined libguestfs_runtests}
%global runtests %{libguestfs_runtests}
%else
%global runtests 1
%endif

Summary:       Access and modify virtual machine disk images
Name:          libguestfs
Epoch:         1
Version:       1.20.11
Release:       20%{?dist}
License:       LGPLv2+
Group:         Development/Libraries
URL:           http://libguestfs.org/
Source0:       http://libguestfs.org/download/1.20-stable/%{name}-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
ExclusiveArch: x86_64

# The RHEL patch repo is in the upstream libguestfs git repository in
# a branch called 'rhel-6.x' (ie. 'rhel-6.6' for RHEL 6.6).  Note this
# is a non-fast-forward branch.
#
# https://github.com/libguestfs/libguestfs/branches
#
# Use 'copy-patches.sh' to copy the patches from the git repo to the
# current directory.
#
# These patches are documented in each individual patch file.

# Feature and backport patches.
Patch0001:     0001-Add-support-for-getting-and-setting-GPT-partition-ty.patch
Patch0002:     0002-daemon-Make-gdisk-into-an-optional-dependency-and-op.patch
Patch0003:     0003-utils-Add-utility-functions-guestfs___concat_strings.patch
Patch0004:     0004-Augeas-1.0.0-is-now-required.patch
Patch0005:     0005-inspection-Fix-hostname-inspection-because-of-faulty.patch
Patch0006:     0006-tests-Add-a-regression-test-for-iface-launch-hangs-R.patch
Patch0007:     0007-sysprep-New-operation-to-remove-RPM-database-files.patch
Patch0008:     0008-sysprep-rhn_systemid-delete-osad-auth.conf-file-in-R.patch
Patch0009:     0009-launch-direct-Specify-cpu-host-kvmclock.patch
Patch0010:     0010-launch-direct-Don-t-use-cpu-host-on-TCG.patch
Patch0011:     0011-daemon-tar-Use-a-temporary-file-to-pass-excludes-to-.patch
Patch0012:     0012-Add-a-regression-test-of-tar-out-excludes-option-RHB.patch
Patch0013:     0013-rsync-Document-use-of-glob-rsync-out-in-guestfish-RH.patch
Patch0014:     0014-mke2fs-Document-that-too-small-blockscount-will-resu.patch
Patch0015:     0015-fish-Use-UNIX_PATH_MAX-instead-of-hard-coded-value-f.patch
Patch0016:     0016-fish-CVE-2013-4419-Fix-insecure-temporary-directory-.patch
Patch0017:     0017-ruby-Fix-.new-method-RHBZ-1046509.patch
Patch0018:     0018-run-Use-timeout-foreground-option.patch
Patch0019:     0019-run-Actually-use-timeout-foreground-option-RHBZ-1025.patch
Patch0020:     0020-tar-in-Fix-places-where-we-didn-t-cancel-the-receive.patch
Patch0021:     0021-Add-a-regression-test-for-RHBZ-1091803.patch
Patch0022:     0022-rhbz1091803.sh-manually-create-the-image-instead-of-.patch
Patch0023:     0023-fuse-In-mount-local-run-test-if-root-filesystem-has-.patch
Patch0024:     0024-fuse-use-fusermount-instead-of-guestunmount-in-error.patch
Patch0025:     0025-listfs-If-LDM-not-available-don-t-inhibit-partition-.patch
Patch0026:     0026-blockdev-Deprecate-blockdev_setbsz-and-make-it-do-no.patch
Patch0027:     0027-Backport-virt-sysprep-from-libguestfs-1.24.patch
Patch0028:     0028-sysprep-add-feature-of-deleting-specified-paths.patch
Patch0029:     0029-builder-sysprep-Describe-password-root-password-opti.patch
Patch0030:     0030-builder-sysprep-Allow-random-as-a-password-selector.patch
Patch0031:     0031-builder-sysprep-Allow-accounts-to-be-locked-RHBZ-102.patch
Patch0032:     0032-sysprep-Add-a-test-suite-for-the-password-option.patch
Patch0033:     0033-sysprep-adapt-test-virt-sysprep-passwords.sh-to-libg.patch
Patch0034:     0034-sysprep-allow-to-specify-globbing-for-delete.patch
Patch0035:     0035-sysprep-mention-globbing-in-help-for-delete.patch
Patch0036:     0036-firstboot-Send-the-output-to-the-console-as-well-as-.patch
Patch0037:     0037-builder-Move-is_block_device-function-into-common-ut.patch
Patch0038:     0038-sparsify-Prevent-overwriting-block-or-char-output-de.patch
Patch0039:     0039-Fix-some-spelling-mistakes-and-typos-in-documentatio.patch
Patch0040:     0040-fuse-UID-0-should-override-all-permissions-checks-RH.patch
Patch0041:     0041-sparsify-Get-free-space-on-TMPDIR-and-give-a-warning.patch
Patch0042:     0042-sparsify-use-Filename.temp_dir_name-instead-of-get_t.patch
Patch0043:     0043-sparsify-Advertize-in-machine-readable-that-we-suppo.patch
Patch0044:     0044-sparsify-Fix-incorrect-reference-to-documentation-fr.patch
Patch0045:     0045-appliance-Increase-udev-timeout-to-6000s-RHBZ-109657.patch
Patch0046:     0046-launch-Close-file-descriptors-after-fork-RHBZ-112300.patch
Patch0047:     0047-mllib-Create-a-common-utility-function-is_directory.patch
Patch0048:     0048-sparsify-Add-tmp-option-to-allow-specifying-temp-dir.patch
Patch0049:     0049-sparsify-Add-tmp-prebuilt-file-option.patch
Patch0050:     0050-sparsify-update-documentation.patch
Patch0051:     0051-customize-fix-locking-accounts-with-passwords.patch
Patch0052:     0052-daemon-add-add_sprintf.patch
Patch0053:     0053-daemon-move-AUGEAS_ERROR-to-the-common-header.patch
Patch0054:     0054-daemon-lvm-filter-use-augeas-for-setting-the-filter.patch
Patch0055:     0055-daemon-Check-return-value-of-end_stringsbuf.patch
Patch0056:     0056-java-run-Add-java-.libs-to-LD_LIBRARY_PATH-so-JVM-fi.patch
Patch0057:     0057-java-Fix-bogus-construction-of-all-RStructList-retur.patch
Patch0058:     0058-java-Split-long-lines-in-generated-output-and-add-ot.patch
Patch0059:     0059-java-Factor-out-common-field-code-in-RStructList.patch
Patch0060:     0060-java-Use-correct-Set-Field-JNI-accessors-to-set-fiel.patch
Patch0061:     0061-bindtests-Fill-in-all-fields-in-dummy-lvm_pv-struct.patch
Patch0062:     0062-java-Add-regression-test-for-RStruct-RStructList-RHB.patch
Patch0063:     0063-daemon-add-sysroot_realpath.patch
Patch0064:     0064-daemon-scrub-file-resolve-the-path-before-calling-sc.patch
Patch0065:     0065-fish-list-also-aliases-in-the-guestfish-help-RHBZ-11.patch
Patch0066:     0066-edit-fix-format-documentation-RHBZ-1151738.patch
Patch0067:     0067-ls-in-CSV-mode-always-have-a-checksum-field-RHBZ-115.patch
Patch0068:     0068-cat-diff-avoid-double-slashes-in-paths-RHBZ-1151910.patch
Patch0069:     0069-lib-fix-newline-in-error-output-RHBZ-923355.patch
Patch0070:     0070-customize-firstboot-make-sure-to-run-Linux-scripts-o.patch
Patch0071:     0071-customize-firstboot-fix-Linux-log-output.patch
Patch0072:     0072-Fix-description-of-set_append-and-get_append-APIs-RH.patch
Patch0073:     0073-fish-fix-dir-completion-on-filesystems-w-o-dirent.d_.patch
Patch0074:     0074-fish-complete-symlink-properly.patch
Patch0075:     0075-add_drive-Introduce-cachemode-parameter-to-control-d.patch
Patch0076:     0076-sparsify-Use-cachemode-unsafe-for-the-overlay-disk.patch
Patch0077:     0077-rescue-Use-cachemode-unsafe-for-the-virt-rescue-scra.patch
Patch0078:     0078-generator-Generate-guestfs_user_cancel.patch
Patch0079:     0079-sysprep-user-account-mark-changed-file-if-users-were.patch
Patch0080:     0080-sysprep-recommend-use-of-selinux-relabel.patch
Patch0081:     0081-sparsify-Relax-requirement-that-output-device-cannot.patch
Patch0082:     0082-drives-Remove-check-for-in-filename-RHBZ-1128942.patch
Patch0083:     0083-mllib-add-simple-qemu-filename-sanitizing-function.patch
Patch0084:     0084-sparsify-handle-output-filenames-with.patch
Patch0085:     0085-sparsify-remove-checks-for-in-filenames.patch
Patch0086:     0086-inspection-Get-icons-from-RHEL-and-CentOS-7-RHBZ-116.patch
Patch0087:     0087-inspection-Allow-etc-favicon.png-to-be-a-symbolic-li.patch
Patch0088:     0088-inspection-Support-Fedora-17-in-old-inspection-code-.patch
Patch0089:     0089-inspection-recognize-xfs-as-Linux-filesystem-RHBZ-12.patch
Patch0090:     0090-inspection-read-UUID-and-label-for-xfs-RHBZ-1216305.patch
Patch0091:     0091-mllib-add-an-optional-filter-for-rm_rf_only_files.patch
Patch0092:     0092-mllib-add-and-use-last_part_of.patch
Patch0093:     0093-sysprep-rework-and-fix-cron-spool-operation-RHBZ-122.patch
Patch0094:     0094-sparsify-read-all-qemu-img-help-output-RHBZ-1218934.patch
Patch0095:     0095-daemon-use-btrfs-1-to-get-btrfs-labels.patch
Patch0096:     0096-daemon-use-ntfslabel-1-to-get-ntfs-labels.patch
Patch0097:     0097-actions-fix-documented-limit-for-btrfs-labels.patch
Patch0098:     0098-daemon-Fix-ext2-labels-error-message-RHBZ-1294956.patch
Patch0099:     0099-daemon-resolve-paths-for-ll-and-llz.patch
Patch0100:     0100-fish-edit-write-to-the-real-file-name.patch
Patch0101:     0101-inspect-improve-UsrMove-detection-RHBZ-1186935.patch

# RHEL 6 specific patches.
Patch0102:     0102-RHEL-6-Emphasize-libguestfs-winsupport-package-RHBZ-.patch
Patch0103:     0103-RHEL-6-Require-external-hex-editor-set-with-HEXEDITO.patch
Patch0104:     0104-RHEL-6-Directly-include-String-ShellQuote.patch
Patch0105:     0105-RHEL-6-Modify-blkid-test-so-it-is-successful-on-RHEL.patch
Patch0106:     0106-RHEL-6-Remove-libguestfs-live-RHBZ-798980.patch
Patch0107:     0107-RHEL-6-Exclude-iptables-from-the-appliance-RHBZ-8586.patch
Patch0108:     0108-RHEL-6-In-mount-local-docs-change-refs-to-libguestfs.patch
Patch0109:     0109-RHEL-6-Ignore-etc-release-if-etc-redhat-release-exis.patch
Patch0110:     0110-RHEL-6-Modify-ruby-Rakefile.in-to-work-with-older-Ru.patch
Patch0111:     0111-RHEL-6-Remove-check-for-qemu-1.patch
Patch0112:     0112-RHEL-6-Revert-Use-pkg-config-for-Python.patch
Patch0113:     0113-RHEL-6-tests-regressions-rhbz895904.sh-Use-instead-o.patch
Patch0114:     0114-RHEL-6-Add-back-some-state-test-commands-to-guestfis.patch
Patch0115:     0115-RHEL-6-Pipe-yes-into-ntfsresize-RHBZ-971326.patch
Patch0116:     0116-RHEL-6-Remove-9p-APIs-from-RHEL-RHBZ-997884.patch
Patch0117:     0117-RHEL-6-disable-fstrim-API-RHBZ-982979.patch
Patch0118:     0118-RHEL-6-sysprep-remove-etc-shadow-note.patch

# Basic build requirements:
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Man)
BuildRequires: /usr/bin/pod2text
BuildRequires: febootstrap >= 3.21-4
BuildRequires: hivex-devel >= 1.2.7-7
BuildRequires: perl(Win::Hivex)
BuildRequires: perl(Win::Hivex::Regedit)
BuildRequires: augeas-devel
BuildRequires: readline-devel
BuildRequires: genisoimage
BuildRequires: libxml2-devel
BuildRequires: qemu-kvm >= 2:0.12.1.0
BuildRequires: createrepo
BuildRequires: glibc-static
BuildRequires: libselinux-utils
BuildRequires: libselinux-devel
BuildRequires: fuse-devel
BuildRequires: pcre-devel
BuildRequires: file-devel
BuildRequires: libvirt-devel
#BuildRequires: po4a
BuildRequires: gperf
BuildRequires: db4-utils
BuildRequires: cpio
BuildRequires: libconfig-devel
# Fix buffer overflow and information leak CVE-2015-8869
BuildRequires: ocaml >= 3.11.2-3.el6
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-gettext-devel
BuildRequires: netpbm-progs
#BuildRequires: icoutils
BuildRequires: perl(XML::XPath)
BuildRequires: perl(XML::XPath::XMLParser)
#BuildRequires: libvirt-daemon-qemu
#BuildRequires: perl(Expect)
#BuildRequires: lua
#BuildRequires: lua-devel
BuildRequires: libacl-devel
BuildRequires: libcap-devel
#BuildRequires: libldm-devel
BuildRequires: yajl-devel
BuildRequires: /bin/ping
BuildRequires: /usr/bin/wget

# krb5 moved all the libraries around to different locations.  Force
# the version of this library with the new locations.
BuildRequires: krb5-libs >= 1.10.3-5.el6

# openldap removed libldif, see RHBZ#1099105
BuildRequires: openldap >= 2.4.39-8.el6

# Build requirements for the appliance.
# sed 's/^ *//' < appliance/packagelist | sort
BuildRequires: acl
BuildRequires: attr
BuildRequires: augeas-libs >= 1.0.0-8.el6
BuildRequires: bash
BuildRequires: binutils
BuildRequires: btrfs-progs
BuildRequires: bzip2
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: cryptsetup
BuildRequires: diffutils
BuildRequires: dosfstools
BuildRequires: e2fsprogs
BuildRequires: file
BuildRequires: findutils
BuildRequires: gawk
BuildRequires: gdisk
#BuildRequires: gfs2-utils
#BuildRequires: gfs-utils
BuildRequires: grep
#%ifarch %{ix86} x86_64
BuildRequires: grub
#%endif
BuildRequires: gzip
%ifnarch %{arm}
#BuildRequires: hfsplus-tools
%endif
BuildRequires: iproute
BuildRequires: iputils
#BuildRequires: jfsutils
BuildRequires: kernel
#BuildRequires: kmod
BuildRequires: libcap
#BuildRequires: libldm
BuildRequires: libselinux
BuildRequires: libxml2
BuildRequires: lsof
#BuildRequires: lsscsi
BuildRequires: lvm2
BuildRequires: lzop
BuildRequires: mdadm
#BuildRequires: nilfs-utils
#BuildRequires: ntfs-3g
%ifarch %{ix86} x86_64
#BuildRequires: ntfsprogs
%endif
BuildRequires: openssh-clients
BuildRequires: parted
BuildRequires: procps
BuildRequires: psmisc
#BuildRequires: reiserfs-utils
BuildRequires: rsync
BuildRequires: scrub
BuildRequires: strace
#BuildRequires: systemd
BuildRequires: tar
BuildRequires: udev
BuildRequires: upstart
BuildRequires: util-linux
BuildRequires: vim-minimal
#BuildRequires: xfsprogs
BuildRequires: xz
BuildRequires: yajl
#BuildRequires: zerofree
# Not supported on ARM http://zfs-fuse.net/issues/94
%ifnarch %{arm}
#BuildRequires: zfs-fuse
%endif

# Must match the above set of BuildRequires exactly!
Requires:      acl
Requires:      attr
Requires:      augeas-libs >= 1.0.0-8.el6
Requires:      bash
Requires:      binutils
Requires:      btrfs-progs
Requires:      bzip2
Requires:      coreutils
Requires:      cpio
Requires:      cryptsetup
Requires:      diffutils
Requires:      dosfstools
Requires:      e2fsprogs
Requires:      file
Requires:      findutils
Requires:      gawk
Requires:      gdisk
#Requires:      gfs2-utils
#Requires:      gfs-utils
Requires:      grep
#%ifarch %{ix86} x86_64
Requires:      grub
#%endif
Requires:      gzip
%ifnarch %{arm}
#Requires:      hfsplus-tools
%endif
Requires:      iproute
Requires:      iputils
#Requires:      jfsutils
Requires:      kernel
#Requires:      kmod
Requires:      libcap
#Requires:      libldm
Requires:      libselinux
Requires:      libxml2
Requires:      lsof
#Requires:      lsscsi
Requires:      lvm2
Requires:      lzop
Requires:      mdadm
#Requires:      nilfs-utils
#Requires:      ntfs-3g
%ifarch %{ix86} x86_64
#Requires:      ntfsprogs
%endif
Requires:      openssh-clients
Requires:      parted
Requires:      procps
Requires:      psmisc
#Requires:      reiserfs-utils
Requires:      rsync
Requires:      scrub
Requires:      strace
#Requires:      systemd
Requires:      tar
Requires:      udev
Requires:      upstart
Requires:      util-linux
Requires:      vim-minimal
#Requires:      xfsprogs
Requires:      xz
Requires:      yajl
#Requires:      zerofree
# Not supported on ARM http://zfs-fuse.net/issues/94
%ifnarch %{arm}
#Requires:      zfs-fuse
%endif

# Although libguestfs will build against older versions of augeas, we require
# the latest available version during the build so that the supermin appliance
# will pick up all available lenses.
BuildRequires: augeas-devel >= 1.0.0-8.el6

# These are only required if you want to build the bindings for
# different languages:
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.00
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(String::ShellQuote)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: python-devel
BuildRequires: ruby-devel
BuildRequires: rubygem-rake
#BuildRequires: rubygem(minitest)
BuildRequires: ruby-irb
BuildRequires: java-1.7.0-openjdk
BuildRequires: java-1.7.0-openjdk-devel
BuildRequires: jpackage-utils
#BuildRequires: php-devel
#BuildRequires: erlang-erts
#BuildRequires: erlang-erl_interface
#BuildRequires: glib2-devel
#BuildRequires: gobject-introspection-devel
#BuildRequires: gjs

# For libguestfs-tools:
BuildRequires: perl(Sys::Virt)
BuildRequires: /usr/bin/qemu-img

# Use git for patch management.
BuildRequires: git

# In RHEL 5 we used to include autotools changes in the patches, but
# in RHEL 6 we now re-run autotools after applying the patches, hence
# we need to depend on these:
BuildRequires: automake, autoconf, libtool, gettext, gettext-devel

# Runtime requires:
Requires:      qemu-kvm >= 2:0.12.1.0

# For building the appliance.
Requires:      febootstrap-supermin-helper >= 3.21-4

# For core inspection API.
Requires:      db4-utils
Requires:      netpbm-progs
#Requires:      icoutils
#Requires:      libosinfo

# krb5 moved all the libraries around to different locations.  Force
# the version of this library with the new locations.
Requires:      krb5-libs >= 1.10.3-5.el6

# For core mount-local (FUSE) API.
Requires:      fuse

# Provide our own custom requires for the supermin appliance.
Source1:       libguestfs-find-requires.sh
%global _use_internal_dependency_generator 0
%global __find_provides %{_rpmconfigdir}/find-provides
%global __find_requires %{SOURCE1} %{_rpmconfigdir}/find-requires

# Replacement README file for Fedora users.
Source4:       README-replacement.in

# Old virt-inspector (new virt-inspector is shipped as 'virt-inspector2').
Source10:      virt-inspector
Source11:      virt-inspector.rng
Source12:      example1.xml
Source13:      example2.xml
Source14:      example3.xml
Source15:      example4.xml

# LD_PRELOAD library used as a workaround for RHBZ#563103 & RHBZ#968905.
Source20:      brew-kernel.c

Source99:      copy-patches.sh

# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:      bundled(gnulib)


%description
Libguestfs is a library for accessing and modifying guest disk images.
Amongst the things this is good for: making batch configuration
changes to guests, getting disk used/free statistics (see also:
virt-df), migrating between virtualization systems (see also:
virt-p2v), performing partial backups, performing partial guest
clones, cloning guests and changing registry/UUID/hostname info, and
much else besides.

Libguestfs uses Linux kernel and qemu code, and can access any type of
guest filesystem that Linux and qemu can, including but not limited
to: ext2/3/4, btrfs, FAT and NTFS, LVM, many different disk partition
schemes, qcow, qcow2, vmdk.

Libguestfs provides ways to enumerate guest storage (eg. partitions,
LVs, what filesystem is in each LV, etc.).  It can also run commands
in the context of the guest.

Libguestfs is a library that can be linked with C and C++ management
programs.

For high level virt tools, guestfish (shell scripting and command line
access), and guestmount (mount guest filesystems using FUSE), install
'%{name}-tools'.

For shell scripting and command line access, install 'guestfish'.

To mount guest filesystems on the host using FUSE, install
'%{name}-mount'.

For Java bindings, install 'libguestfs-java-devel'.

For OCaml bindings, install 'ocaml-libguestfs-devel'.

For Perl bindings, install 'perl-Sys-Guestfs'.

For Python bindings, install 'python-libguestfs'.

For Ruby bindings, install 'ruby-libguestfs'.


%package devel
Summary:       Development tools and libraries for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      pkgconfig

# For libguestfs-make-fixed-appliance.
Requires:      xz
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}


%description devel
%{name}-devel contains development tools and libraries
for %{name}.


%package tools-c
Summary:       System administration tools for virtual machines
Group:         Development/Tools
License:       GPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

# for guestfish:
#Requires:      /usr/bin/emacs #theoretically, but too large
#Requires:      /usr/bin/hexedit #compiled out in RHEL 6
Requires:      /usr/bin/less
Requires:      /usr/bin/man
Requires:      /bin/vi

# for virt-sparsify:
Requires:      /usr/bin/qemu-img

# Obsolete and replace earlier packages.
Provides:      guestfish = %{epoch}:%{version}-%{release}
Obsoletes:     guestfish < %{epoch}:%{version}-%{release}
Provides:      libguestfs-mount = %{epoch}:%{version}-%{release}
Obsoletes:     libguestfs-mount < %{epoch}:%{version}-%{release}


%post tools-c
# RHBZ#843068
chmod 0600 /root/.guestfish /home/*/.guestfish >/dev/null 2>&1 ||:


%description tools-c
This package contains miscellaneous system administrator command line
tools for virtual machines.

Note that you should install %{name}-tools (which pulls in
this package).  This package is only used directly when you want
to avoid dependencies on Perl.


%package tools
Summary:       System administration tools for virtual machines
Group:         Development/Tools
License:       GPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}

# NB: Only list deps here which are not picked up automatically.
Requires:      perl(Sys::Virt)
#Requires:      perl(String::ShellQuote)
Requires:      perl(XML::Writer)
Requires:      perl(Win::Hivex) >= 1.2.7

# for virt-make-fs:
Requires:      /usr/bin/qemu-img


%description tools
This package contains miscellaneous system administrator command line
tools for virtual machines.

Guestfish is the Filesystem Interactive SHell, for accessing and
modifying virtual machine disk images from the command line and shell
scripts.

The guestmount command lets you mount guest filesystems on the host
using FUSE and %{name}.

Virt-alignment-scan scans virtual machines looking for partition
alignment problems.

Virt-cat is a command line tool to display the contents of a file in a
virtual machine.

Virt-copy-in and virt-copy-out are command line tools for uploading
and downloading files and directories to and from virtual machines.

Virt-df is a command line tool to display free space on virtual
machine filesystems.  Unlike other tools, it doesn’t just display the
amount of space allocated to a virtual machine, but can look inside
the virtual machine to see how much space is really being used.  It is
like the df(1) command, but for virtual machines, except that it also
works for Windows virtual machines.

Virt-edit is a command line tool to edit the contents of a file in a
virtual machine.

Virt-filesystems is a command line tool to display the filesystems,
partitions, block devices, LVs, VGs and PVs found in a disk image
or virtual machine.  It replaces the deprecated programs
virt-list-filesystems and virt-list-partitions with a much more
capable tool.

Virt-format is a command line tool to erase and make blank disks.

Virt-inspector examines a virtual machine and tries to determine the
version of the OS, the kernel version, what drivers are installed,
whether the virtual machine is fully virtualized (FV) or
para-virtualized (PV), what applications are installed and more.

Virt-ls is a command line tool to list out files in a virtual machine.

Virt-make-fs is a command line tool to build a filesystem out of
a collection of files or a tarball.

Virt-rescue provides a rescue shell for making interactive,
unstructured fixes to virtual machines.

Virt-resize can resize existing virtual machine disk images.

Virt-sparsify makes virtual machine disk images sparse (thin-provisioned).

Virt-sysprep lets you reset or unconfigure virtual machines in
preparation for cloning them.

Virt-tar-in and virt-tar-out are archive, backup and upload tools
for virtual machines.  These replace the deprecated program virt-tar.

Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.


%package -n ocaml-%{name}
Summary:       OCaml bindings for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}
ocaml-%{name} contains OCaml bindings for %{name}.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %{name} you will also need ocaml-%{name}-devel.


%package -n ocaml-%{name}-devel
Summary:       OCaml bindings for %{name}
Group:         Development/Libraries
Requires:      ocaml-%{name} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}-devel
ocaml-%{name}-devel contains development libraries
required to use the OCaml bindings for %{name}.


%package -n perl-Sys-Guestfs
Summary:       Perl bindings for %{name} (Sys::Guestfs)
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# RHBZ#523547
Requires:      perl(XML::XPath)
# RHBZ#652587 - for backwards compat with the old name
Provides:      perl-%{name} = %{epoch}:%{version}-%{release}
Obsoletes:     perl-%{name} < %{epoch}:%{version}-%{release}


%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %{name} (Sys::Guestfs).


%package -n python-%{name}
Summary:       Python bindings for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%description -n python-%{name}
python-%{name} contains Python bindings for %{name}.


%package -n ruby-%{name}
Summary:       Ruby bindings for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      ruby(abi) = 1.8
Requires:      ruby
Provides:      ruby(guestfs) = %{version}

%{!?ruby_vendorlibdir: %global ruby_vendorlibdir %(ruby -rrbconfig -e "puts Config::CONFIG['vendorlibdir']")}
%{!?ruby_vendorarchdir: %global ruby_vendorarchdir %(ruby -rrbconfig -e "puts Config::CONFIG['vendorarchdir']")}

%description -n ruby-%{name}
ruby-%{name} contains Ruby bindings for %{name}.


%package java
Summary:       Java bindings for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      java >= 1.7.0
Requires:      jpackage-utils

%description java
%{name}-java contains Java bindings for %{name}.

If you want to develop software in Java which uses %{name}, then
you will also need %{name}-java-devel.


%package java-devel
Summary:       Java development package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-java = %{epoch}:%{version}-%{release}

%description java-devel
%{name}-java-devel contains the tools for developing Java software
using %{name}.

See also %{name}-javadoc.


%package javadoc
Summary:       Java documentation for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-java = %{epoch}:%{version}-%{release}
Requires:      jpackage-utils

%description javadoc
%{name}-javadoc contains the Java documentation for %{name}.


%prep
%setup -q

# Use git to manage patches.
# http://rwmj.wordpress.com/2011/08/09/nice-rpm-git-patch-management-trick/
git init
git config user.email "libguestfs@redhat.com"
git config user.name "libguestfs"
git add .
git commit -a -q -m "%{version} baseline"
git am %{patches}

# Patches affect Makefile.am and configure.ac, so rerun autotools.
autoreconf
autoconf

mkdir -p daemon/m4

# Replace developer-centric README that ships with libguestfs, with
# our replacement file.
mv README README.orig
sed 's/@VERSION@/%{version}/g' < %{SOURCE4} > README


%build
# Test if network is available.
if ping -c 3 -w 20 8.8.8.8 && wget http://libguestfs.org -O /dev/null; then
  extra=
else
  mkdir repo
  # -n 1 because of RHBZ#980502.
  find /var/cache/yum -type f -name '*.rpm' -print0 | xargs -0 -n 1 cp -t repo
  createrepo repo
  cat > yum.conf <<EOF
[main]
cachedir=/var/cache/yum
debuglevel=1
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
reposdir=/dev/null

[local]
name=local
baseurl=file://$(pwd)/repo
failovermethod=priority
enabled=1
gpgcheck=0
EOF
  extra=--with-febootstrap-yum-config=$(pwd)/yum.conf
fi

# Using febootstrap 3.
export SUPERMIN=febootstrap3

%{configure} \
  --with-extra="rhel=%{rhel},release=%{release}" \
  --with-qemu="qemu-kvm qemu-system-%{_build_arch} qemu" \
  --disable-php \
  --disable-haskell \
  --disable-erlang \
  --disable-lua \
  --disable-gobject \
  --disable-install-daemon \
  $extra

# Workaround #883463 (in yum).
# /usr/lib/python2.6/site-packages/yum/rpmsack.py:
# class RPMDBAdditionalData method __init__ tries to create
# "/var/lib/yum/yumdb", and fails since it's not running as root.
cat > rhbz883463.c <<'EOF'
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
int
mkdir(const char *pathname, mode_t mode)
{
  if (strcmp (pathname, "/var/lib/yum/yumdb") != 0)
    return mkdirat (AT_FDCWD, pathname, mode);
  else
    return 0;
}
EOF
gcc -fPIC -c rhbz883463.c
gcc -shared -Wl,-soname,rhbz883463.so.1 rhbz883463.o -o rhbz883463.so
LD_PRELOAD=$(pwd)/rhbz883463.so
export LD_PRELOAD

# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
make V=1 INSTALLDIRS=vendor %{?_smp_mflags}


%check
# Enable debugging - very useful if a test does fail, although
# it produces masses of output in the build.log.
export LIBGUESTFS_DEBUG=1

# Enable trace.  Since libguestfs 1.9.7 this produces 'greppable'
# output even when combined with trace (see RHBZ#673477).
export LIBGUESTFS_TRACE=1

# This test fails because we build the ISO after encoding the checksum
# of the ISO in the test itself.  Need to fix the test to work out the
# checksum at runtime.
export SKIP_TEST_CHECKSUM_DEVICE=1

# Disable all btrfs tests (RHBZ#863978).
export SKIP_TEST_BTRFS_FSCK=1
export SKIP_TEST_BTRFS_SET_SEEDING=1
export SKIP_TEST_BTRFS_FILESYSTEM_SYNC=1
export SKIP_TEST_BTRFS_SUBVOLUME_DELETE=1
export SKIP_TEST_BTRFS_SUBVOLUME_SNAPSHOT=1
export SKIP_TEST_MKFS_BTRFS=1
export SKIP_TEST_BTRFS_DEVICES_SH=1
export SKIP_TEST_BTRFS_SUBVOLUME_DEFAULT_PL=1
export SKIP_TEST_CHARSET_FIDELITY=1
export SKIP_TEST_VIRT_MAKE_FS_BTRFS=1

# Skip test/md/test-mdadm.sh, see RHBZ#865503.
export SKIP_TEST_MDADM_SH=1

# Skip ACL tests which use APIs not supported on RHEL 6.
export SKIP_TEST_ACL_SET_FILE=1
export SKIP_TEST_ACL_DELETE_DEF_FILE=1

# 9p test uses -fsdev option (for the test) which doesn't
# work on RHEL 6 qemu.
export SKIP_TEST_9P_SH=1

# Workaround RHBZ#563103 and RHBZ#968905
cp %{SOURCE20} brew-kernel.c
gcc -fPIC -c brew-kernel.c
gcc -shared -Wl,-soname,brew-kernel.so.1 brew-kernel.o -o brew-kernel.so -ldl
LD_PRELOAD=$(pwd)/brew-kernel.so
export LD_PRELOAD

%if %{runtests}
make check -k
%endif


%install
rm -rf $RPM_BUILD_ROOT

# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
make DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor install

# Delete static libraries, libtool files.
rm $RPM_BUILD_ROOT%{_libdir}/libguestfs.a
rm $RPM_BUILD_ROOT%{_libdir}/libguestfs.la

find $RPM_BUILD_ROOT -name perllocal.pod -delete
find $RPM_BUILD_ROOT -name .packlist -delete
find $RPM_BUILD_ROOT -name '*.bs' -delete
find $RPM_BUILD_ROOT -name 'bindtests.pl' -delete

rm $RPM_BUILD_ROOT%{python_sitearch}/libguestfsmod.la

if [ "$RPM_BUILD_ROOT%{python_sitearch}" != "$RPM_BUILD_ROOT%{python_sitelib}" ]; then
   mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
   mv $RPM_BUILD_ROOT%{python_sitearch}/guestfs.py* \
     $RPM_BUILD_ROOT%{python_sitelib}/
fi

# Remove static-linked Java bindings.
rm $RPM_BUILD_ROOT%{_libdir}/libguestfs_jni.la

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv $RPM_BUILD_ROOT%{_docdir}/libguestfs installed-docs

# Remove Japanese manpages, since these are not translated fully at
# the moment.  When these are translated properly we intend to add
# them back.
rm -rf $RPM_BUILD_ROOT%{_mandir}/ja/man{1,3}/

# Rename virt-inspector (new) to virt-inspector2.
mv $RPM_BUILD_ROOT%{_bindir}/virt-inspector \
   $RPM_BUILD_ROOT%{_bindir}/virt-inspector2
# Rewrite the virt-inspector2 manual page.  Bit of a hack.
sed 's/[Vv]irt.\?-inspector/&2/g' \
  < $RPM_BUILD_ROOT%{_mandir}/man1/virt-inspector.1 | \
  sed '/^\.SH .OLD VERSIONS OF VIRT-INSPECTOR/,/^\.Ve/d' \
  > $RPM_BUILD_ROOT%{_mandir}/man1/virt-inspector2.1
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-inspector.1
mkdir installed-docs/virt-inspector2
mv installed-docs/virt-inspector.rng installed-docs/virt-inspector2/virt-inspector2.rng
mv installed-docs/example-*.xml installed-docs/virt-inspector2/

# Install (old) virt-inspector.
install -m 0755 %{SOURCE10} $RPM_BUILD_ROOT%{_bindir}/
pod2man --stderr -u \
  --section 1 \
  -c "Virtualization Support" \
  --name virt-inspector \
  --release "%{name}-%{version}" \
  < %{SOURCE10} > $RPM_BUILD_ROOT%{_mandir}/man1/virt-inspector.1
mkdir installed-docs/virt-inspector
install -m 0644 %{SOURCE11} installed-docs/virt-inspector/
install -m 0644 %{SOURCE12} installed-docs/virt-inspector/
install -m 0644 %{SOURCE13} installed-docs/virt-inspector/
install -m 0644 %{SOURCE14} installed-docs/virt-inspector/
install -m 0644 %{SOURCE15} installed-docs/virt-inspector/

# Find locale files.
%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/libguestfs-test-tool
%{_libdir}/guestfs/
%{_libdir}/libguestfs.so.*
%{_mandir}/man1/guestfs-faq.1*
%{_mandir}/man1/guestfs-performance.1*
%{_mandir}/man1/guestfs-recipes.1*
%{_mandir}/man1/guestfs-release-notes.1*
%{_mandir}/man1/guestfs-testing.1*
%{_mandir}/man1/libguestfs-test-tool.1*


%files devel
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog HACKING TODO README ROADMAP
%doc examples/*.c
%doc installed-docs/*
%{_libdir}/libguestfs.so
%{_sbindir}/libguestfs-make-fixed-appliance
%{_mandir}/man1/libguestfs-make-fixed-appliance.1*
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*
%{_includedir}/guestfs.h
%{_libdir}/pkgconfig/libguestfs.pc


%files tools-c
%defattr(-,root,root,-)
%doc README
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/guestfish-bash-completion.sh
%{_bindir}/guestfish
%{_mandir}/man1/guestfish.1*
%{_bindir}/guestmount
%{_mandir}/man1/guestmount.1*
%{_bindir}/virt-alignment-scan
%{_mandir}/man1/virt-alignment-scan.1*
%{_bindir}/virt-cat
%{_mandir}/man1/virt-cat.1*
%{_bindir}/virt-copy-in
%{_mandir}/man1/virt-copy-in.1*
%{_bindir}/virt-copy-out
%{_mandir}/man1/virt-copy-out.1*
%{_bindir}/virt-df
%{_mandir}/man1/virt-df.1*
%{_bindir}/virt-edit
%{_mandir}/man1/virt-edit.1*
%{_bindir}/virt-filesystems
%{_mandir}/man1/virt-filesystems.1*
%{_bindir}/virt-format
%{_mandir}/man1/virt-format.1*
%{_bindir}/virt-inspector2
%{_mandir}/man1/virt-inspector2.1*
%{_bindir}/virt-ls
%{_mandir}/man1/virt-ls.1*
%{_bindir}/virt-rescue
%{_mandir}/man1/virt-rescue.1*
%{_bindir}/virt-resize
%{_mandir}/man1/virt-resize.1*
%{_bindir}/virt-sparsify
%{_mandir}/man1/virt-sparsify.1*
%{_bindir}/virt-sysprep
%{_mandir}/man1/virt-sysprep.1*
%{_bindir}/virt-tar-in
%{_mandir}/man1/virt-tar-in.1*
%{_bindir}/virt-tar-out
%{_mandir}/man1/virt-tar-out.1*


%files tools
%defattr(-,root,root,-)
%doc README
%{_bindir}/virt-inspector
%{_mandir}/man1/virt-inspector.1*
%{_bindir}/virt-list-filesystems
%{_mandir}/man1/virt-list-filesystems.1*
%{_bindir}/virt-list-partitions
%{_mandir}/man1/virt-list-partitions.1*
%{_bindir}/virt-make-fs
%{_mandir}/man1/virt-make-fs.1*
%{_bindir}/virt-tar
%{_mandir}/man1/virt-tar.1*
%{_bindir}/virt-win-reg
%{_mandir}/man1/virt-win-reg.1*


%files -n ocaml-%{name}
%defattr(-,root,root,-)
%{_libdir}/ocaml/guestfs
%exclude %{_libdir}/ocaml/guestfs/*.a
%exclude %{_libdir}/ocaml/guestfs/*.cmxa
%exclude %{_libdir}/ocaml/guestfs/*.cmx
%exclude %{_libdir}/ocaml/guestfs/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files -n ocaml-%{name}-devel
%defattr(-,root,root,-)
%doc ocaml/examples/*.ml
%{_libdir}/ocaml/guestfs/*.a
%{_libdir}/ocaml/guestfs/*.cmxa
%{_libdir}/ocaml/guestfs/*.cmx
%{_libdir}/ocaml/guestfs/*.mli
%{_mandir}/man3/guestfs-ocaml.3*


%files -n perl-Sys-Guestfs
%defattr(-,root,root,-)
%doc perl/examples/*.pl
%{perl_vendorarch}/*
%{_mandir}/man3/Sys::Guestfs.3pm*
%{_mandir}/man3/Sys::Guestfs::Lib.3pm*
%{_mandir}/man3/guestfs-perl.3*


%files -n python-%{name}
%defattr(-,root,root,-)
%doc python/examples/*.py
%{python_sitearch}/*
%{python_sitelib}/*.py
%{python_sitelib}/*.pyc
%{python_sitelib}/*.pyo
%{_mandir}/man3/guestfs-python.3*


%files -n ruby-%{name}
%defattr(-,root,root,-)
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%{ruby_vendorlibdir}/guestfs.rb
%{ruby_vendorarchdir}/_guestfs.so
%{_mandir}/man3/guestfs-ruby.3*


%files java
%defattr(-,root,root,-)
%doc java/examples/*.java
%{_libdir}/libguestfs_jni*.so.*
%{_datadir}/java/*.jar


%files java-devel
%defattr(-,root,root,-)
%{_libdir}/libguestfs_jni*.so
%{_mandir}/man3/guestfs-java.3*


%files javadoc
%defattr(-,root,root,-)
%{_datadir}/javadoc/%{name}-java-%{version}


%changelog
* Wed Oct 26 2016 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-20
- inspection: fix detection of /usr in separate partition
  resolves: rhbz#1388407

* Mon Sep 12 2016 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-19
- libguestfs-java: bump the java Require to >= 1.7.0, matching the
  Build-Require, and the generated bytecode
  resolves: rhbz#1319086

* Thu Jun 09 2016 Richard W.M. Jones <rjones@redhat.com> - 1:1.20.11-18
- Fix buffer overflow and information leak CVE-2015-8869
  resolves: rhbz#1343103

* Tue Jan 19 2016 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-17
- Mention ext2/3/4 in set-label error messages for ext labels.
  resolves: rhbz#1294956
- Fix handling of symlinks in ll and llz, and when editing files in guestfish
  and virt-edit.
  resolves: rhbz#1293276

* Tue Nov 10 2015 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-16
- Fix the old inspection code to handle some features of RHEL 7 images:
  handle /bin as symlink to /usr/bin, grub2 in boot partition, and
  recognize xfs as filesystem (reading UUID and label for it).
  resolves: rhbz#1216305
- Fix reading of icon in RHEL 7 guests.
  resolves: rhbz#1216298
- virt-sysprep: don't delete /var/spool/at/.SEQ
  resolves: rhbz#1229305
- virt-sparsify: read all the output of `qemu-img --help`
  resolves: rhbz#1218934
- Fix getting long labels for NTFS and btrfs filesystems; also correct the
  documented maximum length of btrfs labels.
  resolves: rhbz#1164729

* Mon Jan 19 2015 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-14
- Raise augeas (Build)Requires to >= 1.0.0-8.el6, which fixes
  rhbz#1160261, so virt-sysprep can remove users from /etc/shadow;
  also remove note about that lack.
  resolves: rhbz#1138630
- Make sure that libguesfs (the library itself), and virt-sparsify in
  particular, can handle filenames with ':'.
  resolves: rhbz#1128942

* Tue Dec 16 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-13
- guestfish: fix Tab completion with some filesystems (e.g. xfs).
  resolves: rhbz#1153846
- Improve drive caching by selecting the caching mode.
  resolves: rhbz#1038977
- Generate user-cancel automatically, so there is also documentation for it.
  resolves: rhbz#1100533
- virt-sysprep: make sure to trigger autorelabel by default when removing
  users.
  resolves: rhbz#1153855
- virt-sysprep: recommend usage of --selinux-relabel with SELinux guests.
  related: rhbz#1153855
- virt-sparsify: allow block devices as output.
  resolves: rhbz#1122557

* Tue Dec 02 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-12
- Fix lvm-set-filter to work with newer lvm2 versions.
  resolves: rhbz#1168751
- Fix handling of structs in the Java bindings.
  resolves: rhbz#1074005
- Fix scrub-file so it can work on symlinks.
  resolves: rhbz#1091859
- Show also aliases in the output of `guestfish -h`.
  resolves: rhbz#1100530
- Fix typo in the man page of virt-edit.
  resolves: rhbz#1151739
- virt-ls: always output the checksum field in CSV mode.
  resolves: rhbz#1151901
- virt-ls: avoid double slashes in directory output.
  resolves: rhbz#1151911
- Fix newline character in error output.
  resolves: rhbz#1153974
- Fix virt-sysprep firstboot scripts to not be run more than once.
  resolves: rhbz#1159651
- Fix logging of virt-sysprep firstboot scripts.
  resolves: rhbz#1160203
- Fix description of 'set_append' and 'get_append' APIs.
  resolves: rhbz#1164734

* Mon Sep 08 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.20.11-11
- virt-sysprep: Fix locking accounts with passwords.
  resolves: rhbz#1037166
- Update copy-patches script to RHEL 6.6.

* Tue Aug 05 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-10
- virt-sparsify: allow specifying temporary file or block device
  resolves: rhbz#1117540

* Mon Aug 04 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-9
- Close all the file descriptors before launching qemu
  resolves: rhbz#1123794

* Mon Jun 23 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-8
- Raise timeout for udev in the appliance to 6000s
  resolves: rhbz#1096579

* Fri Jun 20 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-7
- FUSE: fix access as root to files and directories not owned by root
  resolves: rhbz#1106548
- virt-sparsify: check for available space before starting
  resolves: rhbz#1097359
- Enable gdisk support to make part-get-gpt-type and part-set-gpt-type work
  resolves: rhbz#965495

* Wed Jun 18 2014 Richard W.M. Jones <rjones@redhat.com> - 1:1.20.11-6
- Rebuild against openldap >= 2.4.39 (RHBZ#1099105).

* Thu May 29 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-5
- Exclude fstrim from perl documentation coverage as well
  related: rhbz#982979

* Wed May 28 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-4
- Don't inhibit partition detection if LDM not available
  resolves: rhbz#1079182
- Deprecate blockdev_setbsz and make it do nothing
  resolves: rhbz#624335
- Disable fstrim API
  resolves: rhbz#982979
- Backport virt-sysprep from libguestfs 1.24, with few backports from
  greater versions too
  resolves: rhbz#1037166
- virt-sparsify: don't overwrite block or char devices if used as output files
  resolves: rhbz#1056558
- fix few typos in the documentation
  resolves: rhbz#1099332

* Tue May  6 2014 Pino Toscano <ptoscano@redhat.com> - 1:1.20.11-3
- Fix .new method in Ruby bindings.
  resolves: rhbz#1072062
- Properly use timeout --foreground when running tests
  resolves: rhbz#1025269
- Fix cancellation on errors in tar-in
  resolves: rhbz#1091805
- Check whether something has been mounted to / when using mount-local* APIs
  resolves: rhbz#1057510

* Wed Oct 16 2013 Richard W.M. Jones <rjones@redhat.com> - 1:1.20.11-2
- Fix CVE-2013-4419: insecure temporary directory handling for
  guestfish's network socket
  resolves: rhbz#1019737

* Thu Aug 29 2013 Richard W.M. Jones <rjones@redhat.com> - 1:1.20.11-1
- Rebase to libguestfs 1.20.11.
  resolves: rhbz#958183
- Remove buildnet: builds now detect network automatically.
- The rhel-6.x branches containing the patches used in RHEL are
  now stored on a public git repository
  (https://github.com/libguestfs/libguestfs/branches).
- Compare spec file to Fedora 18 and fix where necessary.
- Backport new APIs part-get-gpt-type and part-set-gpt-type
  resolves: rhbz#965495
- Fix DoS (abort) due to a double free flaw when inspecting certain guest
  files / images (CVE-2013-2124)
  resolves: rhbz#968337
- libguestfs-devel should depend on an explicit version of
  libguestfs-tools-c, in order that the latest package is pulled in.
- Rebuild against Augeas >= 1.0.0-5
  resolves: rhbz#971207
- Backport Windows inspection changes
  resolves: rhbz#971090
- Add back state test commands to guestfish
  resolves: rhbz#971664
- Work around problem with ntfsresize command in RHEL 6
  resolves: rhbz#971326
- Fix txz-out API
  resolves: rhbz#972413
- Move virt-sysprep to the libguestfs-tools-c package since it's no longer
  a shell script
  resolves: rhbz#975572
- Fix hostname inspection because of faulty Augeas path expression
  resolves: rhbz#975377
- Calculate appliance root correctly when iface drives are added
  resolves: rhbz#975760
- Add notes about resizing Windows disk images to virt-resize documentation
  resolves: rhbz#975753
- Remove dependency on lsscsi, not available in 6Client
  resolves: rhbz#973425
- Fix yum cache copy so it works if there are multiple repos
  resolves: rhbz#980502
- Fix hivex-commit API to fail with relative paths
  resolves: rhbz#980372
- Better documentation for filesystem-available API
  resolves: rhbz#980358
- Fix double free when kernel link fails during launch
  resolves: rhbz#983690
- Fix virt-sysprep --firstboot option
  resolves: rhbz#988863
- Fix cap-get-file so it returns empty string instead of error on no cap
  resolves: rhbz#989352
- Better documentation for acl-set-file
  resolves: rhbz#985269
- Fix bogus waitpid error when using guestfish --remote
  resolves: rhbz#996825
- Disable 9p support
  resolves: rhbz#997884
- Document that guestfish --remote doesn't work with certain other arguments
  resolves: rhbz#996039
- Enable kvmclock in the appliance to reduce clock instability
  resolves: rhbz#998108
- Fix 'sh' command before mount causes daemon to segfault
  resolves: rhbz#1000122
- Various fixes to tar-out 'excludes' (RHBZ#1001875)
- Document use of glob + rsync-out (RHBZ#1001876)
- Document mke2fs blockscount (RHBZ#1002032)

* Thu Dec  6 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.34-2
- Bump and rebuild to fix RHBZ#883559.

* Tue Dec  4 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.34-1
- Rebase to latest stable-1.16 branch version libguestfs 1.16.34.
- Include missing patch which adds <locale.h> to fuse/guestmount.c
  resolves: rhbz#883338
- Fix link to engineering git repo.
- Add workaround for bug in yum: RHBZ#883463.

* Fri Nov 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.32-4
- Fix: virt-df with two -a options displays incorrect disk image name
  resolves: rhbz#880805

* Mon Nov  5 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.32-3
- Set permissions of .guestfish files in home directories to 0600
  resolves: rhbz#843068
- Ignore /etc/release if /etc/redhat-release exists
  resolves: rhbz#872454

* Thu Oct 11 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.32-2
- Rebase to libguestfs 1.16.32 which includes a fix for inspection
  of Windows guests.
  resolves: rhbz#858126
- Skip test-mdadm.sh.

* Fri Sep 28 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.31-4
- Fix inspection of Windows guests (RHBZ#858126).
- Fix list-devices when different drive interfaces are used (RHBZ#858128).

* Thu Sep 27 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.31-3
- Add dependency on fuse.
  resolves: rhbz#836501
- Clarify the error message from resize2fs-M.
  resolves: rhbz#801640
- Increase limit on size of Windows registry for inspection (RHBZ#852396).
- Change virt-sparsify to work with old 'file' command (RHBZ#853763).
- Enable tests by adding an LD_PRELOAD workaround for RHBZ#563103.
- Tidy up comments in the check section.

* Thu Sep 27 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.31-1
- Rebase to libguestfs 1.16.31.
- Backport mount-local feature.
  resolves: rhbz#830135
- Include copy-patches.sh shell script.
- Simplify .gitignore.

* Tue Sep 25 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.30-4
- Forgot to apply the patch.
  resolves: rhbz#858648

* Thu Sep 20 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.30-3
- Force krb5 version that contains new build layout.
- Add non-upstream patch to exclude iptables from the appliance.
  resolves: rhbz#858648

* Thu Sep 13 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.30-1
- Rebase to libguestfs 1.16.30
  resolves: rhbz#837691, rhbz#822626, rhbz#830369, rhbz#838609, rhbz#843068, rhbz#816839, rhbz#836573
- Rebuild for new location of krb5 library.
- Remove workaround for test-getlogin_r test.  This is fixed by a
  change in libguestfs (commit 6e1b5f0feac50a4) instead.

* Wed Apr 18 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.19-1
- Rebase to libguestfs 1.16.19
  resolves: rhbz#719879
- Rebuild against augeas 0.9.0-3.el6
  related: rhbz#808662
- Fix: Don't abort inspection if mdadm.conf ARRAY doesn't have a uuid.
- Switch back to git for patch management.

* Fri Apr 13 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.18-2
- Rebase to libguestfs 1.16.18
  resolves: rhbz#719879
- Fix: guestfs_last_error not set when qemu fails early during launch
  resolves: rhbz#811673
- Fix: RFE: virt-sysprep: hostname can not be changed on rhel system
  (RHBZ#811112)
- Fix: RFE: virt-sysprep: net-hwaddr not removed from "ifcfg-*" files on
  rhel (RHBZ#811117)
- Fix: inspection fails on ubuntu 10.04 guest with encrypted swap (RHBZ#811872)
- Fix: cannot open disk images which are symlinks to files that
  contain ':' (colon) character (RHBZ#812092)
- BR gettext-devel so we can rerun autoconf.

* Tue Apr  3 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.15-1
- Rebase to libguestfs 1.16.15
  resolves: rhbz#719879
- Fix: inspection doesn't recognize Fedora 17+ (RHBZ#809401)

* Mon Apr  2 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.14-1
- Rebase to libguestfs 1.16.14
  resolves: rhbz#719879
- virt-sysprep should use virt-inspector2
  resolves: rhbz#807557
- Fix: mkfs blocksize option breaks when creating btrfs
  resolves: rhbz#807905

* Fri Mar 23 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.12-1
- Rebase to libguestfs 1.16.12
  resolves: rhbz#719879
- Fix: could not locate HKLM\SYSTEM\MountedDevices
  resolves: rhbz#803699

* Tue Mar 13 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.10-1
- Rebase to libguestfs 1.16.10
  resolves: rhbz#719879
- Fix: libguestfs holds open file descriptors when handle is launched
  resolves: rhbz#801788
- Fix: Document for set-pgroup need to be updated
  resolves: rhbz#801273
- Fix: Possible null dereference and resource leaks
  resolves: rhbz#801298

* Mon Mar  5 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.8-1
- Rebase to libguestfs 1.16.8
  resolves: rhbz#719879
- Fix set_autosync function so it is not 'ConfigOnly'
  resolves: rhbz#796520
- Fix header compilation for C++
  resolves: rhbz#799695

* Thu Mar  1 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.6-1
- Rebase to libguesfs 1.16.6
  resolves: rhbz#798197, rhbz#797760,rhbz#790958,rhbz#798980,rhbz#795322,rhbz#796520
- Fix virt-inspector2 man page.

* Mon Feb 13 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.5-1
- Rebase to libguestfs 1.16.5
  resolves: rhbz#679737, rhbz#789960

* Fri Feb 10 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.4-1
- Rebase to libguestfs 1.16.4
  resolves: rhbz#788642

* Thu Feb  9 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.3-1
- Rebase to libguestfs 1.16.3
  resolves: rhbz#679737, rhbz#769359, rhbz#785305

* Tue Jan 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.2-1
- Rebase to libguestfs 1.16.2
  resolves: rhbz#719879

* Wed Jan 25 2012 Richard W.M. Jones <rjones@redhat.com> - 1:1.16.1-1
- Rebase to libguestfs 1.16.1
- Disable tests (probably because we are hitting
  https://lists.gnu.org/archive/html/qemu-devel/2010-02/threads.html#00823 )
  resolves: rhbz#719879

* Wed Dec 21 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.14.7-4
- Continue with rebase to libguestfs 1.14.7
  resolves: rhbz#719879

* Tue Dec 20 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.14.7-1
- Rebase to libguestfs 1.14.7
  resolves: rhbz#719879

* Fri Aug 12 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-26
- Document that remote run in cmd substitution context hangs.
  resolves: rhbz#730248
- Note that additional memory may be required to typecheck Augeas lenses.
  resolves: rhbz#729887

* Thu Aug 11 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-25
- Fix 'unknown filesystem' warnings in old inspection code
  resolves: rhbz#678231
  resolves: rhbz#666578

* Wed Aug 10 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-24
- inspect: Detect 32 bit applications running on WOW64 emulator
  resolves: rhbz#692394
- perl: Binding and test for guestfs_last_errno
  resolves: rhbz#672491
- New API: list-dm-devices
  fish: Show device mapper device in tab completion
  resolves: rhbz#688062
- Document that fullvirt query only works for Linux guests
  resolves: rhbz#690358

* Tue Aug  9 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-23
- Use git to manage patches.
- Include all minor bugfixes from upstream stable-1.8 branch up to
  libguestfs 1.8.11.

* Mon Jul  4 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-19
- virt-make-fs: Round disk size to integer, fix for qemu-img 0.14.
  resolves: rhbz#695881

* Mon Jul  4 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-18
- python: Convert any iterable argument to a list.
  resolves: rhbz#693306
- Renumber the RHEL 6.1-specific patches from 0500+.

* Mon Apr 11 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-17
- Remove dependency on gfs2-utils.
  resolves: rhbz#695138

* Tue Mar 29 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-16
- Canonicalize /dev/vd* paths in virt-inspector code.
  resolves: rhbz#691724

* Mon Mar  7 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-15
- Fix trace segfault for non-daemon functions.
  resolves: rhbz#676788

* Tue Feb 22 2011 Matthew Booth <mbooth@redhat.com> - 1:1.7.17-14
- Add explicit BuildRequires for latest augeas. (RHBZ#677616)

* Tue Feb 15 2011 Matthew Booth <mbooth@redhat.com> - 1:1.7.17-13
- Rebuild to pick up new augeas lens (RHBZ#677616)

* Mon Jan 31 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-12
- Fix typo in virt-make-fs manual page.
  resolves: rhbz#673721
- Add a grep-friendly string to LIBGUESTFS_TRACE output.
  resolves: rhbz#673477

* Mon Jan 17 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-11
- Only runtime require febootstrap-supermin-helper (not whole of
  febootstrap) (RHBZ#669840).

* Fri Jan 14 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-10
- Remove external hexedit script and make guestfish users set $HEXEDITOR.
  This is because requiring emacs pulls in all of X (RHBZ#641494).

* Tue Jan 11 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-9
- Fix: guestfish fails when guest fstab entry does not exist (RHBZ#668611).

* Mon Jan 10 2011 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-8
- Backport patches up to upstream 1.8.1. (RHBZ#613593)
- Fixes:
   * guestfish: fails to tilde expand '~' when $HOME unset (RHBZ#617440)
   * libguestfs: unknown filesystem /dev/fd0 (RHBZ#666577)
   * libguestfs: unknown filesystem label SWAP-sda2 (RHBZ#666578)
   * libguestfs: unknown filesystem /dev/hd{x} (cdrom) (RHBZ#666579)
   * virt-filesystems fails on guest with corrupt filesystem label (RHBZ#668115)
   * emphasize "libguestfs-winsupport" in error output (RHBZ#627468)

* Mon Dec 20 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-4
- Backport patches up to upstream 1.8.0 _except_ for:
   * changes which require febootstrap 3.x
   * changes which were only relevant for other distros

* Tue Nov 30 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.7.17-3
- New upstream version 1.7.17, rebase for RHEL 6.1 (RHBZ#613593).
- Require febootstrap >= 2.11.
- Split out new libguestfs-tools-c package from libguestfs-tools.
  . This is so that the -tools-c package can be pulled in by people
    wanting to avoid a dependency on Perl, while -tools pulls in everything
    as before.
  . The C tools currently are: cat, df, filesystems, fish, inspector, ls,
    mount, rescue.
  . libguestfs-tools no longer pulls in guestfish.
- guestfish no longer requires pod2text, hence no longer requires perl.
- guestfish also depends on: less, man, vi, emacs.
- Add BR db4-utils (although since RPM needs it, it not really necessary).
- Runtime requires on db4-utils should be on core lib, not tools package.
- Change all "Requires: perl-Foo" to "Requires: perl(Foo)".
- New manual pages containing example code.
- Ship examples for C, OCaml, Ruby, Python.
- Don't ship HTML versions of man pages.
- Rebase no-fuse-test patch to latest version.
- New tool: virt-filesystems.
- Rename perl-libguestfs as perl-Sys-Guestfs (RHBZ#652587).
- Remove guestfs-actions.h and guestfs-structs.h.  Libguestfs now
  only exports a single <guestfs.h> header file.
- Add AUTHORS file from tarball.

* Thu Nov 18 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.6.2-4
- New upstream stable version 1.6.2, rebase for RHEL 6.1 (RHBZ#613593).
- Remove previous patches which are now all upstream and in this new version.
- BR febootstrap 2.10 (RHBZ#628849).
- BR cryptsetup-luks for new LUKS encryption support.
- ocaml-xml-light{,-devel} is no longer required to build.
- guestfish is no longer dependent on virt-inspector.
- Require the ruby package.
- Disable PHP and Haskell bindings in configure (they wouldn't build anyway,
  but this will help people building from source).
- Set sysconfdir in configure.
- --enable-debug-command is no longer required by configure script.
- New command 'virt-make-fs'.
- Include virt-inspector2, upstream replacement for virt-inspector.
- Provide hexedit replacement script for guestfish.
- BR autotools, and rerun after applying patches.

* Tue Sep  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.24
- Remove runtime requires xfsprogs and /lib64/libhandle.so.1 (RHBZ#630986).
  Note that we have removed support completely from the appliance.  Even
  installing xfsprogs separately will not provide support in this
  build of libguestfs.

* Wed Aug  4 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.23
- Backport new API is_lv from upstream development branch (RHBZ#619826).

* Fri Jul 30 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.22
- Include generated code in patch for RHBZ#617165.

* Mon Jul 26 2010 Matthew Booth <mbooth@redhat.com> - 1:1.2.7-1.21
- Rely on upstream augeas lens for modules.conf (RHBZ#616753)
- Use link-local addresses for host<->guest communication (RHBZ#613562)

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.20
- Mount operations on unclean filesystems fail when drives are added
  readonly (RHBZ#617165).

* Tue Jul 20 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.18
- Missing Requires binutils (RHBZ#616438).

* Mon Jul 19 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.17
- Fix libguestfs-find-requires.sh for new location of hostfiles (RHBZ#615870).

* Thu Jul  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.16
- Don't allow this RPM to be mixed with qemu-kvm RPM from 6.1 (RHBZ#612309).

* Wed Jul  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.11
- For RHBZ#600148:
  * In guestfs_mkfs_b, map block size to cluster size for VFAT and NTFS
  * Remove power-of-2 test from API tests.  Not supported by backported
    code.

* Wed Jul  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.9
- Fix 'add-cdrom' command in RHEL 6 (RHBZ#598807).

* Wed Jul  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.8
- Don't fail if both -m and --listen flags given to guestfish (RHBZ#609990).

* Wed Jul  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.7
- Don't add extra chars after dist tag (RHBZ#604552).

* Wed Jul  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.el6.6
- Backport guestfish help command error status patch from stable branch
  (RHBZ#598771).

* Tue May 18 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1.el6.5
- Backport ignore utempter patch from upstream.
- Work around buggy getlogin_r test in gnulib.
- Explicitly depend on e2fsprogs (no longer pulled in implicitly).

* Mon May 17 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.7-1
- Pull in latest release of upstream stable branch.
- Remove NTFS support from this package.
- Backport supermin unification patch from upstream development branch.

* Wed Apr 21 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.5-1.el6.5
- Branch from Fedora 13 and compile for RHEL-6.
- Include NTFS support in the appliance for V2V and other virtualization
  operations on Windows guests.
- Backport aug_clear API from upstream development branch.

* Tue Apr 20 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.3-1
- New upstream stable branch version 1.2.3.
- Fixes: 582548, 583554, 582948, 582901, 582929, 582899, 582953,
  578407.

* Thu Apr  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.2-1
- New upstream stable branch version 1.2.2.
- Fixes RHBZ#580016.
- Fixes several important bugs in virt-resize.

* Thu Apr  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.2.1-1
- New upstream stable branch version 1.2.1.
- Includes the new tools virt-list-partitions, virt-resize, and
  updated virt-rescue and virt-win-reg (with regedit support).
- Reenable tests.
- Fixes bugs: 580650, 579155, 580246, 579664, 578123, 509597,
  505329, 576876, 576688, 576689, 569757, 567567, 570181.

* Fri Mar 12 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-2.4
- Backport upstream patch to remove dependency on /lib/libntfs-3g.so.N.
- The above depends on the bash quoting patch, so apply that first.

* Mon Mar 08 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-2.3
- Rebuild against latest plymouth in F-13 updates-testing.

* Mon Mar 08 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-2.2
- Bump and rebuild.

* Fri Mar 05 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-2.1
- Bump and rebuild.

* Wed Mar 03 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-2
- Bump and rebuild.

* Mon Mar  1 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.85-1
- New upstream version 1.0.85.
- Remove hivex, now a separate upstream project and package.
- Remove supermin quoting patch, now upstream.

* Mon Mar  1 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.84-6
- Fix quoting in supermin-split script (RHBZ#566511).
- Don't include bogus './builddir' entries in supermin hostfiles
  (RHBZ#566512).

* Mon Feb 22 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.84-4
- Don't include generator.ml in rpm.  It's 400K and almost no one will need it.
- Add comments to spec file about how repo building works.
- Whitespace changes in the spec file.

* Mon Feb 22 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.84-3
- Bump and rebuild.

* Tue Feb 16 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.84-2
- Bump and rebuild.

* Fri Feb 12 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.84-1
- New upstream version 1.0.84.

* Fri Feb 12 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.83-8
- Bump and rebuild.

* Thu Feb 11 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.83-7
- Disable tests.  These fail in Koji (on RHEL 5 kernel) because of a
  bug in preadv/pwritev emulation in glibc (RHBZ#563103).

* Tue Feb  9 2010 Matthew Booth <mbooth@redhat.com> - 1.0.83-6
- Change buildnonet to buildnet
- Allow buildnet, mirror, updates, virtio and runtests to be configured by user
  macros.

* Mon Feb  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.83-5
- libguestfs-tools should require perl-XML-Writer (RHBZ#562858).

* Mon Feb  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.83-4
- Use virtio for block device access (RHBZ#509383 is fixed).

* Fri Feb  5 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.83-3
- Rebuild: possible timing-related build problem in Koji.

* Fri Feb  5 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.83-2
- New upstream release 1.0.83.
- This release fixes:
  Add Marathi translations (RHBZ#561671).
  Polish translations (RHBZ#502533).
  Add Gujarti translations (Sweta Kothari) (RHBZ#560918).
  Update Oriya translations (thanks Manoj Kumar Giri) (RHBZ#559498).
  Set locale in C programs so l10n works (RHBZ#559962).
  Add Tamil translation (RHBZ#559877) (thanks to I.Felix)
  Update Punjabi translation (RHBZ#559480) (thanks Jaswinder Singh)
- There are significant fixes to hive file handling.
- Add hivexsh and manual page.
- Remove two patches, now upstream.

* Sun Jan 31 2010 Richard W.M. Jones <rjones@redhat.com> - 1:1.0.82-7
- Bump and rebuild.

* Fri Jan 29 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.82-6
- Backport a better fix for RHBZ557655 test from upstream.
- Backport fix for unreadable yum.log from upstream.

* Thu Jan 28 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.82-3
- Backport RHBZ557655 test fix from upstream.

* Thu Jan 28 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.82-1
- New upstream version 1.0.82.  This includes the two patches
  we were carrying, so those are now removed.
- This release fixes:
  RHBZ#559498 (Oriya translation).
  RHBZ#559480 (Punjabi translation).
  RHBZ#558593 (Should prevent corruption by multilib).
  RHBZ#559237 (Telugu translation).
  RHBZ#557655 (Use xstrtol/xstrtoll to parse integers in guestfish).
  RHBZ#557195 (Missing crc kernel modules for recent Linux).
- In addition this contains numerous fixes to the hivex library
  for parsing Windows Registry files, making hivex* and virt-win-reg
  more robust.
- New API call 'filesize'.

* Thu Jan 28 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-8
- Backport special handling of libgcc_s.so.
- Backport unreadable files patch from RHEL 6 / upstream.

* Fri Jan 22 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-5
- Require febootstrap >= 2.6 (RHBZ#557262).

* Thu Jan 21 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-4
- Rebuild for unannounced soname bump (libntfs-3g.so).

* Fri Jan 15 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-3
- Rebuild for unannounced soname bump (libplybootsplash.so).

* Thu Jan 14 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-2
- Rebuild for broken dependency (iptables soname bump).

* Wed Jan 13 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.81-1
- New upstream version 1.0.81.
- Remove two upstream patches.
- virt-inspector: Make RPM application data more specific (RHBZ#552718).

* Tue Jan 12 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-14
- Reenable tests because RHBZ#553689 is fixed.

* Tue Jan 12 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-13
- Rebuild because of libparted soname bump (1.9 -> 2.1).

* Fri Jan  8 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-12
- qemu in Rawhide is totally broken (RHBZ#553689).  Disable tests.

* Thu Jan  7 2010 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-11
- Remove gfs-utils (deprecated and removed from Fedora 13 by the
  upstream Cluster Suite developers).
- Include patch to fix regression in qemu -serial stdio option.

* Tue Dec 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-10
- Remove some debugging statements which were left in the requires
  script by accident.

* Mon Dec 21 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-9
- Generate additional requires for supermin (RHBZ#547496).

* Fri Dec 18 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-3
- Work around udevsettle command problem (RHBZ#548121).
- Enable tests.

* Wed Dec 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-2
- Disable tests because of RHBZ#548121.

* Wed Dec 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.80-1
- New upstream release 1.0.80.
- New Polish translations (RHBZ#502533).
- Give a meaningful error if no usable kernels are found (RHBZ#539746).
- New tool: virt-list-filesystems

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1:1.0.79-3
- rebuild against perl 5.10.1

* Wed Nov 18 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.79-2
- New upstream release 1.0.79.
- Adds FUSE test script and multiple fixes for FUSE (RHBZ#538069).
- Fix virt-df in Xen (RHBZ#538041).
- Improve speed of supermin appliance.
- Disable FUSE-related tests because Koji doesn't currently allow them.
  fuse: device not found, try 'modprobe fuse' first

* Tue Nov 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.78-2
- New upstream release 1.0.78.
- Many more filesystem types supported by this release - add them
  as dependencies.

* Tue Nov  3 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.77-1
- New upstream release 1.0.77.
- Support for mounting guest in host using FUSE (guestmount command).
- hivex*(1) man pages should be in main package, not -devel, since
  they are user commands.
- libguestfs-tools: Fix "self-obsoletion" issue raised by rpmlint.
- perl: Remove bogus script Sys/bindtests.pl.

* Thu Oct 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.75-2
- New upstream release 1.0.75.
- New library: libhivex.
- New tools: virt-win-reg, hivexml, hivexget.
- Don't require chntpw.
- Add BR libxml2-devel, accidentally omitted before.

* Tue Oct 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.74-1
- New upstream release 1.0.74.
- New API call: guestfs_find0.
- New tools: virt-ls, virt-tar.

* Wed Oct 14 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.73-1
- New upstream release 1.0.73.
- OCaml library now depends on xml-light.
- Deal with installed documentation.

* Tue Sep 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.72-2
- Force rebuild.

* Wed Sep 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.72-1
- New upstream release 1.0.72.
- New tools: virt-edit, virt-rescue.
- Combine virt-cat, virt-df, virt-edit, virt-inspector and virt-rescue
  into a single package called libguestfs-tools.

* Tue Sep 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.71-2
- New upstream release 1.0.71.

* Fri Sep 18 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.70-2
- Perl bindings require perl-XML-XPath (fixed RHBZ#523547).

* Tue Sep 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.70-1
- New upstream release 1.0.70.
- Fixes build problem related to old version of GNU gettext.

* Tue Sep 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.69-1
- New upstream release 1.0.69.
- Reenable the tests (because RHBZ#516543 is supposed to be fixed).
- New main loop code should fix RHBZ#501888, RHBZ#504418.
- Add waitpid along guestfs_close path (fixes RHBZ#518747).

* Wed Aug 19 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.68-2
- New upstream release 1.0.68.
- BR genisoimage.

* Thu Aug 13 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.67-2
- New upstream release 1.0.67.

* Fri Aug  7 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.66-5
- Set network interface to ne2k_pci (workaround for RHBZ#516022).
- Rerun autoconf because patch touches configure script.

* Thu Aug  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.66-1
- New upstream release 1.0.66.

* Wed Jul 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.65-1
- New upstream release 1.0.65.
- Add Obsoletes for virt-df2 (RHBZ#514309).
- Disable tests because of ongoing TCG problems with newest qemu in Rawhide.

* Thu Jul 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.64-3
- RHBZ#513249 bug in qemu is now fixed, so try to rebuild and run tests.
- However RHBZ#503236 still prevents us from testing on i386.

* Thu Jul 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.64-1
- New upstream release 1.0.64.
- New tool 'libguestfs-test-tool'.

* Wed Jul 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.61-1
- New upstream release 1.0.61.
- New tool / subpackage 'virt-cat'.
- New BR perl-libintl.

* Wed Jul 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.60-2
- Fix runtime Requires so they use epoch correctly.

* Tue Jul 14 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.60-1
- New upstream release 1.0.60.

* Fri Jul 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.58-2
- New upstream release 1.0.58.

* Fri Jul 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.57-1
- New upstream release 1.0.57.
- New tool virt-df (obsoletes existing package with this name).
- RHBZ#507066 may be fixed, so reenable tests.

* Tue Jul  7 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.56-2
- New upstream release 1.0.56.
- Don't rerun generator.

* Thu Jul  2 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.55-1
- New upstream release 1.0.55.
- New manual page libguestfs(3).

* Mon Jun 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.54-2
- New upstream release 1.0.54.
- +BR perl-XML-Writer.

* Wed Jun 24 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.53-1
- New upstream release 1.0.53.
- Disable all tests (because of RHBZ#507066).

* Wed Jun 24 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.52-1
- New upstream release 1.0.52.

* Mon Jun 22 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.51-1
- New upstream release 1.0.51.
- Removed patches which are now upstream.

* Sat Jun 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.49-5
- Remove workaround for RHBZ#507007, since bug is now fixed.
- Pull in upstream patch to fix pclose checking
  (testing as possible fix for RHBZ#507066).
- Pull in upstream patch to check waitpid return values
  (testing as possible fix for RHBZ#507066).

* Fri Jun 19 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.49-2
- New upstream release 1.0.49.
- Add workaround for RHBZ#507007.

* Tue Jun 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.48-2
- Accidentally omitted the supermin image from previous version.

* Tue Jun 16 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.48-1
- New upstream release 1.0.48.
- Should fix all the brokenness from 1.0.47.
- Requires febootstrap >= 2.3.

* Mon Jun 15 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.47-2
- New upstream release 1.0.47.
- Enable experimental supermin appliance build.
- Fix path to appliance.

* Fri Jun 12 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.45-2
- New upstream release 1.0.45.

* Wed Jun 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.44-2
- Disable ppc/ppc64 tests again because of RHBZ#505109.

* Wed Jun 10 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.44-1
- New upstream version 1.0.44.
- Try enabling tests on ppc & ppc64 since it looks like the bug(s?)
  in qemu which might have caused them to fail have been fixed.

* Tue Jun  9 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.43-1
- New upstream version 1.0.43.
- New upstream URL.
- Requires chntpw program.

* Sat Jun  6 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.42-1
- New upstream version 1.0.42.

* Thu Jun  4 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.41-1
- New upstream version 1.0.41.
- Fixes a number of regressions in RHBZ#503169.

* Thu Jun  4 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.40-1
- New upstream version 1.0.40.

* Thu Jun  4 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.39-1
- New upstream version 1.0.39.
- Fixes:
  . libguestfs /dev is too sparse for kernel installation/upgrade (RHBZ#503169)
  . OCaml bindings build failure (RHBZ#502309)

* Tue Jun  2 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.38-2
- Disable tests on ix86 because of RHBZ#503236.

* Tue Jun  2 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.38-1
- New upstream version 1.0.38.

* Fri May 29 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.37-1
- New upstream version 1.0.37.
- Fixes:
  . "mkdir-p" should not throw errors on preexisting directories (RHBZ#503133)
  . cramfs and squashfs modules should be available in libguestfs appliances
      (RHBZ#503135)

* Thu May 28 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.36-2
- New upstream version 1.0.36.
- Rerun the generator in prep section.

* Thu May 28 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.35-1
- New upstream version 1.0.35.
- Fixes multiple bugs in bindings parameters (RHBZ#501892).

* Wed May 27 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.34-1
- New upstream version 1.0.34.

* Wed May 27 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.33-1
- New upstream version 1.0.33.
- --with-java-home option is no longer required.
- Upstream contains potential fixes for:
    501878 built-in commands like 'alloc' and 'help' don't autocomplete
    501883 javadoc messed up in libguestfs java documentation
    501885 Doesn't detect missing Java, --with-java-home=no should not be needed
    502533 Polish translation of libguestfs
    n/a    Allow more ext filesystem kmods (Charles Duffy)

* Tue May 26 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.32-2
- New upstream version 1.0.32.
- Use %%find_lang macro.

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 1.0.31-1
- Rebuild for OCaml 3.11.1.
- New upstream version 1.0.31.

* Thu May 21 2009 Richard Jones <rjones@redhat.com> - 1.0.30-1
- New upstream version 1.0.30.  Now includes test-bootbootboot.sh script.

* Thu May 21 2009 Richard Jones <rjones@redhat.com> - 1.0.29-3
- New upstream version 1.0.29 (fixes RHBZ#502007 RHBZ#502018).
- This should allow us to enable tests for i386 and x86-64.
- Added test-bootbootboot.sh script which was missed from 1.0.29 tarball.
- Pass kernel noapic flag to workaround RHBZ#502058.

* Thu May 21 2009 Richard Jones <rjones@redhat.com> - 1.0.28-1
- New upstream version 1.0.28.  Nothing has visibly changed, but
  the source has been gettextized and we want to check that doesn't
  break anything.

* Thu May 21 2009 Richard Jones <rjones@redhat.com> - 1.0.27-3
- Change requirement from qemu -> qemu-kvm (RHBZ#501761).

* Tue May 19 2009 Richard Jones <rjones@redhat.com> - 1.0.27-2
- New upstream version 1.0.27.

* Mon May 18 2009 Richard Jones <rjones@redhat.com> - 1.0.26-6
- Experimentally try to reenable ppc and ppc64 builds.
- Note BZ numbers which are causing tests to fail.

* Mon May 18 2009 Richard Jones <rjones@redhat.com> - 1.0.26-1
- New upstream version 1.0.26.

* Tue May 12 2009 Richard Jones <rjones@redhat.com> - 1.0.25-4
- New upstream version 1.0.25.
- Enable debugging when running the tests.
- Disable tests - don't work correctly in Koji.

* Tue May 12 2009 Richard Jones <rjones@redhat.com> - 1.0.24-1
- New upstream version 1.0.24.
- BRs glibc-static for the new command tests.
- Enable tests.

* Mon May 11 2009 Richard Jones <rjones@redhat.com> - 1.0.23-2
- New upstream version 1.0.23.
- Don't try to use updates during build.

* Fri May  8 2009 Richard Jones <rjones@redhat.com> - 1.0.21-3
- New upstream version 1.0.21.

* Thu May  7 2009 Richard Jones <rjones@redhat.com> - 1.0.20-2
- New upstream version 1.0.20.

* Thu May  7 2009 Richard Jones <rjones@redhat.com> - 1.0.19-1
- New upstream version 1.0.19.

* Tue Apr 28 2009 Richard Jones <rjones@redhat.com> - 1.0.15-1
- New upstream version 1.0.15.

* Fri Apr 24 2009 Richard Jones <rjones@redhat.com> - 1.0.12-1
- New upstream version 1.0.12.

* Wed Apr 22 2009 Richard Jones <rjones@redhat.com> - 1.0.6-1
- New upstream version 1.0.6.

* Mon Apr 20 2009 Richard Jones <rjones@redhat.com> - 1.0.2-1
- New upstream version 1.0.2.

* Thu Apr 16 2009 Richard Jones <rjones@redhat.com> - 0.9.9-12
- Multiple fixes to get it to scratch build in Koji.

* Sat Apr  4 2009 Richard Jones <rjones@redhat.com> - 0.9.9-1
- Initial build.
