
# When bootstrapping an arch, omit the -demos subpackage.

%define dri_drivers --with-dri-drivers=savage,unichrome,mga,r128

%define _default_patch_fuzz 2

Summary: Mesa graphics libraries
Name: mesa-dri1-drivers
Version: 7.11
Release: 8%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.mesa3d.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExcludeArch: s390 s390x

Source0: ftp://ftp.freedesktop.org/pub/mesa/%{version}%{?snapshot}/MesaLib-%{version}%{?snapshot}.tar.bz2
#Source0: http://www.mesa3d.org/beta/MesaLib-%{version}%{?snapshot}.tar.bz2
#Source0: %{name}-%{gitdate}.tar.bz2

Patch3: mesa-no-mach64.patch

# 7.11 branch backport
Patch60: mesa-7.11-b9c7773e.patch

BuildRequires: pkgconfig autoconf automake libtool
BuildRequires: kernel-headers >= 2.6.27-0.305.rc5.git6
BuildRequires: libdrm-devel >= 2.4.24-1
BuildRequires: libXxf86vm-devel
BuildRequires: expat-devel >= 2.0
BuildRequires: xorg-x11-proto-devel >= 7.1-10
BuildRequires: makedepend
BuildRequires: libselinux-devel
BuildRequires: libXext-devel
BuildRequires: freeglut-devel
BuildRequires: libXfixes-devel
BuildRequires: libXdamage-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: elfutils
BuildRequires: python
BuildRequires: libxml2-python
BuildRequires: libtalloc-devel
BuildRequires: bison flex

Requires: mesa-libGL
Requires: mesa-dri-filesystem%{?_isa}

%description
Mesa DRI1 drivers


%prep
%setup -q -n Mesa-%{version}%{?snapshot}
%patch3 -p1 -b .no-mach64

# don't -b this one, it breaks the glsl build.  sigh sigh sigh.
%patch60 -p1

%build

autoreconf --install  

export CFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden"
export CXXFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden"
%ifarch %{ix86}
# i do not have words for how much the assembly dispatch code infuriates me
%define common_flags --enable-selinux --enable-pic --disable-asm
%else
%define common_flags --enable-selinux --enable-pic
%endif

# XXX should get visibility working again post-dricore.
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

# now build the rest of mesa
%configure %{common_flags} \
    --disable-glw \
    --disable-glut \
    --disable-egl \
    --disable-glu \
    --disable-gl-osmesa \
    --with-driver=dri \
    --with-dri-driverdir=%{_libdir}/dri \
    --disable-gallium-egl \
    --disable-gallium \
    --with-gallium-drivers="" \
    %{?dri_drivers}

make #{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

# core libs and headers, but not drivers.
make install DESTDIR=$RPM_BUILD_ROOT DRI_DIRS=

# just the DRI drivers that are sane
install -d $RPM_BUILD_ROOT%{_libdir}/dri
for f in mga r128 savage unichrome; do
    so=%{_lib}/${f}_dri.so
    test -e $so && echo $so
done | xargs install -m 0755 -t $RPM_BUILD_ROOT%{_libdir}/dri >& /dev/null || :

# strip out undesirable headers
pushd $RPM_BUILD_ROOT%{_includedir}
rm -rf GL
popd

pushd $RPM_BUILD_ROOT%{_libdir}
rm -f libEGL* libGL*
rm -rf pkgconfig
popd

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.

%clean
rm -rf $RPM_BUILD_ROOT

%check

%files
%defattr(-,root,root,-)
%{_libdir}/dri/*_dri.so

%changelog
* Tue Oct 02 2012 Dave Airlie <airlied@redhat.com> 7.11-8
- drop the directory from this rpm the filesystem one owns it

* Tue Oct 02 2012 Dave Airlie <airlied@redhat.com> 7.11-7
- fix mesa-dri-filesystem requires

* Wed Aug 22 2012 Dave Airlie <airlied@redhat.com> 7.11-6
- initial fork from 7.11 mesa packages


