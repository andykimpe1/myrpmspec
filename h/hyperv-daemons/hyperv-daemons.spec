# HyperV KVP daemon binary name
%global hv_kvp_daemon hypervkvpd
# HyperV VSS daemon binary name
%global hv_vss_daemon hypervvssd
# HyperV FCOPY daemon binary name
%global hv_fcopy_daemon hypervfcopyd
# snapshot version
%global snapver .20150108git
# use hardened build
%global _hardened_build 1

Name:     hyperv-daemons
Version:  0
Release:  0.17%{?snapver}%{?dist}
Summary:  HyperV daemons suite

Group:    System Environment/Daemons
License:  GPLv2
URL:      http://www.kernel.org

# Source files obtained from kernel upstream 3.19-rc3 (b1940cd21c0f4abdce101253e860feff547291b0)
# git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
# The daemon and scripts are located in "master branch - /tools/hv"
# COPYING -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/COPYING?id=b1940cd21c0f4abdce101253e860feff547291b
Source0:  COPYING

# HYPERV KVP DAEMON
# hv_kvp_daemon.c -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_kvp_daemon.c?id=b1940cd21c0f4abdce101253e860feff547291b0
Source1:  hv_kvp_daemon.c
# hv_get_dhcp_info.sh -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_get_dhcp_info.sh?id=b1940cd21c0f4abdce101253e860feff547291b0
Source2:  hv_get_dhcp_info.sh
# hv_get_dns_info.sh -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_get_dns_info.sh?id=b1940cd21c0f4abdce101253e860feff547291b0
Source3:  hv_get_dns_info.sh
# hv_set_ifconfig.sh -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_set_ifconfig.sh?id=b1940cd21c0f4abdce101253e860feff547291b0
Source4:  hv_set_ifconfig.sh
Source5:  hypervkvpd

# HYPERV VSS DAEMON
# hv_vss_daemon.c -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_vss_daemon.c?id=b1940cd21c0f4abdce101253e860feff547291b0
Source100:  hv_vss_daemon.c
Source101:  hypervvssd

# HYPERV FCOPY DAEMON
# hv_fcopy_daemon.c -> https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/plain/tools/hv/hv_fcopy_daemon.c?id=b1940cd21c0f4abdce101253e860feff547291b0
Source200:  hv_fcopy_daemon.c
Source201:  hypervfcopyd


# HYPERV KVP DAEMON
# Correct paths to external scripts ("/usr/libexec/hypervkvpd").
Patch0:   hypervkvpd-0-corrected_paths_to_external_scripts.patch
# use quoted include for linux/hyperv.h because we use gcc option
# -iquote for include PATH where it is located. This is because
# some headers in system include PATH are also in kernel-devel
# package.
Patch1:   hypervkvpd-0-include_fix.patch
# rhbz#872566
Patch2:   hypervkvpd-0-long_file_names_from_readdir.patch

# HYPERV VSS DAEMON
# use quoted include for linux/hyperv.h because we use gcc option
# -iquote for include PATH where it is located. This is because
# some headers in system include PATH are also in kernel-devel
# package.
Patch100:   hypervvssd-0-fix_includes.patch

# HYPERV FCOPY DAEMON
# use quoted include for linux/hyperv.h because we use gcc option
# -iquote for include PATH where it is located. This is because
# some headers in system include PATH are also in kernel-devel
# package.
Patch200:   hypervfcopyd-0-include_fix.patch


BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# HyperV is available only on x86 architectures
ExclusiveArch:  x86_64 i686
Requires:       hypervkvpd = %{version}-%{release}
Requires:       hypervvssd = %{version}-%{release}
Requires:       hypervfcopyd = %{version}-%{release}

%description
Suite of daemons that are needed when Linux guest
is running on Windows Host with HyperV.


%package -n hypervkvpd
Summary: HyperV key value pair (KVP) daemon
Group:   System Environment/Daemons
Requires: %{name}-license = %{version}-%{release}
BuildRequires:    kernel-devel >= 2.6.32-336
Requires(post):   chkconfig
Requires(preun):  chkconfig, initscripts
Requires(postun): initscripts

%description -n hypervkvpd
Hypervkvpd is an implementation of HyperV key value pair (KVP) 
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information 
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: HyperV VSS daemon
Group:   System Environment/Daemons
Requires: %{name}-license = %{version}-%{release}
BuildRequires:    kernel-devel >= 2.6.32-336
Requires(post):   chkconfig
Requires(preun):  chkconfig, initscripts
Requires(postun): initscripts

%description -n hypervvssd
Hypervvssd is an implementation of HyperV VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on HyperV hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions 
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.


%package -n hypervfcopyd
Summary: HyperV FCOPY daemon
Group:   System Environment/Daemons
Requires: %{name}-license = %{version}-%{release}
BuildRequires:  kernel-devel >= 2.6.32-490
Requires(post):   chkconfig
Requires(preun):  chkconfig, initscripts
Requires(postun): initscripts

%description -n hypervfcopyd
Hypervfcopyd is an implementation of file copy service functionality
for Linux Guest running on HyperV. The daemon enables host to copy
a file (over VMBUS) into the Linux Guest. The daemon first registers
with the kernel driver. After this is done it waits for instructions
from Windows Host.


%package license
Summary:    License of the HyperV daemons suite
Group:      Applications/System
BuildArch:  noarch

%description license
Contains license of the HyperV daemons suite.


%prep
%setup -Tc
cp -pvL %{SOURCE0} COPYING

cp -pvL %{SOURCE1} hv_kvp_daemon.c
cp -pvL %{SOURCE2} hv_get_dhcp_info.sh
cp -pvL %{SOURCE3} hv_get_dns_info.sh
cp -pvL %{SOURCE4} hv_set_ifconfig.sh
cp -pvL %{SOURCE5} hypervkvpd

cp -pvL %{SOURCE100} hv_vss_daemon.c
cp -pvL %{SOURCE101} hypervvssd

cp -pvL %{SOURCE200} hv_fcopy_daemon.c
cp -pvL %{SOURCE201} hypervfcopyd

%patch0 -p1 -b .external_scripts
%patch1 -p1 -b .include
%patch2 -p1 -b .long_names

%patch100 -p1 -b .include

%patch200 -p1 -b .include

%build
# kernel-devel version
%{!?kversion: %global kversion `ls %{_usrsrc}/kernels | sort -dr | head -n 1`}

# HYPERV KVP DAEMON
gcc \
    $RPM_OPT_FLAGS \
    -iquote %{_usrsrc}/kernels/%{kversion}/include \
    -c hv_kvp_daemon.c

gcc \
    $RPM_LD_FLAGS \
    hv_kvp_daemon.o \
    -o hv_kvp_daemon

# HYPERV VSS DAEMON
gcc \
    $RPM_OPT_FLAGS \
    -iquote %{_usrsrc}/kernels/%{kversion}/include \
    -c hv_vss_daemon.c

gcc \
    $RPM_LD_FLAGS \
    hv_vss_daemon.o \
    -o hv_vss_daemon

# HYPERV FCOPY DAEMON
gcc \
    $RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 \
    -iquote %{_usrsrc}/kernels/%{kversion}/include \
    -c hv_fcopy_daemon.c

gcc \
    $RPM_LD_FLAGS \
    hv_fcopy_daemon.o \
    -o hv_fcopy_daemon


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
install -p -m 0755 hv_kvp_daemon %{buildroot}%{_sbindir}
install -p -m 0755 hv_vss_daemon %{buildroot}%{_sbindir}
install -p -m 0755 hv_fcopy_daemon %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_initrddir}
# initscripts
install -p -m 0755 %{SOURCE5} %{buildroot}%{_initrddir}
install -p -m 0755 %{SOURCE101} %{buildroot}%{_initrddir}
install -p -m 0755 %{SOURCE201} %{buildroot}%{_initrddir}
# Shell scripts for the KVP daemon
mkdir -p %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}
install -p -m 0755 hv_get_dhcp_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dhcp_info
install -p -m 0755 hv_get_dns_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dns_info
install -p -m 0755 hv_set_ifconfig.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_set_ifconfig
# Directory for pool files
mkdir -p %{buildroot}%{_sharedstatedir}/hyperv


%post -n hypervkvpd
/sbin/chkconfig --add hypervkvpd

%preun -n hypervkvpd
if [ "$1" -eq "0" ] ; then
    /sbin/service hypervkvpd stop >/dev/null 2>&1
    /sbin/chkconfig --del hypervkvpd
fi

%postun -n hypervkvpd
# hypervkvpd daemon does NOT support restarting (driver, neither)
# If removing the package, delete %%{_sharedstatedir}/hyperv directory
if [ "$1" -eq "0" ] ; then
    rm -rf %{_sharedstatedir}/hyperv || :
fi


%post -n hypervvssd
/sbin/chkconfig --add hypervvssd

%preun -n hypervvssd
if [ "$1" -eq "0" ] ; then
    /sbin/service hypervvssd stop >/dev/null 2>&1
    /sbin/chkconfig --del hypervvssd
fi

%postun -n hypervvssd
# hypervvssd daemon does NOT support restarting (driver, neither)


%post -n hypervfcopyd
/sbin/chkconfig --add hypervfcopyd

%preun -n hypervfcopyd
if [ "$1" -eq "0" ] ; then
    /sbin/service hypervfcopyd stop >/dev/null 2>&1
    /sbin/chkconfig --del hypervfcopyd
fi

%postun -n hypervfcopyd
# hypervfcopyd daemon does NOT support restarting (driver, neither)


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
# the base package does not contain any files.

%files -n hypervkvpd
%defattr(-,root,root,-)
%{_sbindir}/hv_kvp_daemon
%{_initrddir}/hypervkvpd
%dir %{_libexecdir}/%{hv_kvp_daemon}
%{_libexecdir}/%{hv_kvp_daemon}/*
%dir %{_sharedstatedir}/hyperv

%files -n hypervvssd
%defattr(-,root,root,-)
%{_sbindir}/hv_vss_daemon
%{_initrddir}/hypervvssd

%files -n hypervfcopyd
%{_sbindir}/hv_fcopy_daemon
%{_initrddir}/hypervfcopyd

%files license
%defattr(-,root,root,-)
%doc COPYING

%changelog
* Wed May 13 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.17.20150108git
- Change CFLAGS to support large (>3GB) files on i686 (#1221097)

* Fri Jan 09 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.16.20150108git
- Rebase to 3.19-rc3 (20150108 git snapshot)
- Skip all readonly-mounted filesystemd (#1161368)

* Mon Jul 14 2014 Tomas Hozza <thozza@redhat.com> - 0-0.15.20130826git
- Package new File copy daemon (#1107559)

* Fri Jul 04 2014 Tomas Hozza <thozza@redhat.com> - 0-0.14.20130826git
- Fix the status command in hypervvssd init script (#1116337)

* Thu Apr 24 2014 Tomas Hozza <thozza@redhat.com> - 0-0.13.20130826git
- Initial package
