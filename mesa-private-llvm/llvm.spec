%if 0%{?rhel} == 6
%define rhel6 1
%endif

%define use_bundled_gcc         1
%define gcc_version             4.8.2-15
%define python_version          2.7.8

# llvm works on the 64-bit versions of these, but not the 32 versions.
# consequently we build swrast on them instead of llvmpipe.
ExcludeArch: ppc s390 %{?rhel6:s390x}

#global prerel rc3
%global downloadurl http://llvm.org/%{?prerel:pre-}releases/%{version}%{?prerel:/%{prerel}}

Name:           mesa-private-llvm
Version:        3.6.2
Release:        1%{?dist}
Summary:        llvm engine for Mesa

Group:		System Environment/Libraries
License:        NCSA
URL:            http://llvm.org/
Source0:        %{downloadurl}/llvm-%{version}%{?prerel:%{prerel}}.src.tar.xz
#Source0:	llvm-%{svndate}.tar.xz
Source1:	make-llvm-snapshot.sh
# multilib fixes
Source2:        llvm-Config-config.h
Source3:        llvm-Config-llvm-config.h
Source200:      https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
Source300:      gcc48-%{gcc_version}.el6.src.rpm

# Data files should be installed with timestamps preserved
Patch0:         llvm-2.6-timestamp.patch

# llvm Z13 backports (#1182150)
Patch1: llvm-z13-backports.patch

BuildRequires:  bison
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gcc-c++ >= 3.4
BuildRequires:  groff
BuildRequires:  libtool-ltdl-devel
BuildRequires:  zip
# for DejaGNU test suite
BuildRequires:  dejagnu tcl-devel python

# GCC 4.8 BuildRequires
# ==================================================================================
%if %{use_bundled_gcc}

%ifarch s390x
%global multilib_32_arch s390
%endif
%ifarch sparc64
%global multilib_32_arch sparcv9
%endif
%ifarch ppc64
%global multilib_32_arch ppc
%endif
%ifarch x86_64
%if 0%{?rhel} >= 6
%global multilib_32_arch i686
%else
%global multilib_32_arch i386
%endif
%endif

%global multilib_64_archs sparc64 ppc64 s390x x86_64

%if 0%{?rhel} >= 6
# Need binutils which support --build-id >= 2.17.50.0.17-3
# Need binutils which support %gnu_unique_object >= 2.19.51.0.14
# Need binutils which support .cfi_sections >= 2.19.51.0.14-33
BuildRequires: binutils >= 2.19.51.0.14-33
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
%else
# Don't have binutils which support --build-id >= 2.17.50.0.17-3
# Don't have binutils which support %gnu_unique_object >= 2.19.51.0.14
# Don't have binutils which  support .cfi_sections >= 2.19.51.0.14-33
BuildRequires: binutils >= 2.17.50.0.2-8
%endif
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, texinfo, sharutils
BuildRequires: /usr/bin/pod2man
%if 0%{?rhel} >= 7
BuildRequires: texinfo-tex
%endif
#BuildRequires: systemtap-sdt-devel >= 1.3
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
%if 0%{?rhel} >= 6
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%else
BuildRequires: elfutils-devel >= 0.72
%endif
%ifarch ppc ppc64 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
%ifarch %{multilib_64_archs} sparcv9 ppc
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif
%ifarch ia64
BuildRequires: libunwind >= 0.98
%endif
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
# On ppc64, need omit dot symbols support and --non-overlapping-opd
# Need binutils that owns /usr/bin/c++filt
# Need binutils that support .weakref
# Need binutils that supports --hash-style=gnu
# Need binutils that support mffgpr/mftgpr
#%if 0%{?rhel} >= 6
## Need binutils which support --build-id >= 2.17.50.0.17-3
## Need binutils which support %gnu_unique_object >= 2.19.51.0.14
## Need binutils which support .cfi_sections >= 2.19.51.0.14-33
#Requires: binutils >= 2.19.51.0.14-33
#%else
## Don't have binutils which support --build-id >= 2.17.50.0.17-3
## Don't have binutils which support %gnu_unique_object >= 2.19.51.0.14
## Don't have binutils which  support .cfi_sections >= 2.19.51.0.14-33
#Requires: binutils >= 2.17.50.0.2-8
#%endif
## Make sure gdb will understand DW_FORM_strp
#Conflicts: gdb < 5.1-2
#Requires: glibc-devel >= 2.2.90-12
#%ifarch ppc ppc64 s390 s390x sparc sparcv9 alpha
## Make sure glibc supports TFmode long double
#Requires: glibc >= 2.3.90-35
#%endif
#Requires: libgcc >= 4.1.2-43
#Requires: libgomp >= 4.4.4-13
#%if 0%{?rhel} == 6
#Requires: libstdc++ >= 4.4.4-13
#%else
#Requires: libstdc++ = 4.1.2
#%endif
##FIXME gcc version
#Requires: libstdc++-devel = %{version}-%{release}
BuildRequires: gmp-devel >= 4.1.2-8
%if 0%{?rhel} >= 6
BuildRequires: mpfr-devel >= 2.2.1
%endif
%if 0%{?rhel} >= 7
BuildRequires: libmpc-devel >= 0.8.1
%endif

%endif # bundled gcc BuildRequires

%description
This package contains the LLVM-based runtime support for Mesa.  It is not a
fully-featured build of LLVM, and use by any package other than Mesa is not
supported.

%package devel
Summary:        Libraries and header files for Mesa's llvm engine
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel >= 3.4

%description devel
This package contains library and header files needed to build the LLVM
support in Mesa.

%prep
%setup -q -n llvm-%{version}.src
rm -r -f tools/clang

# llvm patches
%patch0 -p1 -b .timestamp
%patch1 -p1 -b .z13

# fix ld search path
sed -i 's|/lib /usr/lib $lt_ld_extra|%{_libdir} $lt_ld_extra|' \
    ./configure

# mangle the library name
sed -i 's|^LLVM_VERSION_SUFFIX=|&-mesa|' ./configure

%ifnarch s390x
%define r600 ,r600
%endif
# Prepare Python 2.7 sources
tar xf %{SOURCE200} 

%build
%if %{use_bundled_gcc}
GCC_FILE="gcc48-%{gcc_version}*.rpm"
GCC_PATH="%{_rpmdir}"

rpmbuild --nodeps --rebuild %{SOURCE300}
cd %{_rpmdir}
if [ ! -f $GCC_PATH/$GCC_FILE ]; then
    GCC_PATH="$GCC_PATH/%{_arch}"
fi
rpm2cpio $GCC_PATH/$GCC_FILE | cpio -iduv
# Clean gcc48 rpms to avoid including them to package
rm -f gcc48-*.rpm
cd -
PATH=%{_rpmdir}/usr/bin:$PATH
export PATH
export CXX=g++
%endif  # bundled gcc

# Build Python 2.7 and set environment
BUILD_DIR=`pwd`/python_build
cd Python-%{python_version}
./configure --prefix=$BUILD_DIR --exec-prefix=$BUILD_DIR
make
make install
cd -

PATH=$BUILD_DIR/bin:$PATH
export PATH

%configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --includedir=%{_includedir}/mesa-private \
  --with-extra-ld-options=-Wl,-Bsymbolic,--default-symver \
  --enable-targets=host%{?r600} \
  --enable-bindings=none \
  --enable-debug-runtime \
  --enable-jit \
  --enable-shared \
  --enable-optimized \
  --disable-clang-arcmt \
  --disable-clang-static-analyzer \
  --disable-clang-rewriter \
  --disable-assertions \
  --disable-docs \
  --disable-libffi \
  --disable-terminfo \
  --disable-timestamps \
%ifarch armv7hl armv7l
  --with-cpu=cortex-a8 \
  --with-tune=cortex-a8 \
  --with-arch=armv7-a \
  --with-float=hard \
  --with-fpu=vfpv3-d16 \
  --with-abi=aapcs-linux \
%endif
  %{nil}

# FIXME file this
# configure does not properly specify libdir or includedir
sed -i 's|(PROJ_prefix)/lib|(PROJ_prefix)/%{_lib}|g' Makefile.config
sed -i 's|(PROJ_prefix)/include|&/mesa-private|g' Makefile.config

# FIXME upstream need to fix this
# llvm-config.cpp hardcodes lib in it
sed -i 's|ActiveLibDir = ActivePrefix + "/lib"|ActiveLibDir = ActivePrefix + "/%{_lib}"|g' tools/llvm-config/llvm-config.cpp
sed -i 's|ActiveIncludeDir = ActivePrefix + "/include|&/mesa-private|g' tools/llvm-config/llvm-config.cpp

make %{_smp_mflags} VERBOSE=1 OPTIMIZE_OPTION="%{optflags}"

%install
make install DESTDIR=%{buildroot}

# rename the few binaries we're keeping
mv %{buildroot}%{_bindir}/llvm-config %{buildroot}%{_bindir}/%{name}-config-%{__isa_bits}

pushd %{buildroot}%{_includedir}/mesa-private/llvm/Config
mv config.h config-%{__isa_bits}.h
cp -p %{SOURCE2} config.h
mv llvm-config.h llvm-config-%{__isa_bits}.h
cp -p %{SOURCE3} llvm-config.h
popd

file %{buildroot}/%{_bindir}/* %{buildroot}/%{bindir}/*.so | \
    awk -F: '$2~/ELF/{print $1}' | \
    xargs -r chrpath -d

# FIXME file this bug
sed -i 's,ABS_RUN_DIR/lib",ABS_RUN_DIR/%{_lib}/%{name}",' \
  %{buildroot}%{_bindir}/%{name}-config-%{__isa_bits}

rm -f %{buildroot}%{_libdir}/*.a

rm -f %{buildroot}%{_libdir}/libLLVM-%{version}.so

# remove documentation makefiles:
# they require the build directory to work
find examples -name 'Makefile' | xargs -0r rm -f

# RHEL: strip out most binaries, most libs, and man pages
ls %{buildroot}%{_bindir}/* | grep -v bin/mesa-private | xargs rm -f
ls %{buildroot}%{_libdir}/* | grep -v libLLVM | xargs rm -f
rm -rf %{buildroot}%{_mandir}/man1

# RHEL: Strip out some headers Mesa doesn't need
rm -rf %{buildroot}%{_includedir}/mesa-private/llvm/{Analysis,Assembly}
rm -rf %{buildroot}%{_includedir}/mesa-private/llvm/{DebugInfo,Option}
rm -rf %{buildroot}%{_includedir}/mesa-private/llvm/TableGen

# RHEL: Strip out cmake build foo
rm -rf %{buildroot}%{_datadir}/llvm/cmake

%check
# the Koji build server does not seem to have enough RAM
# for the default 16 threads

# just log the results, don't fail the build
make check LIT_ARGS="-v -j4" | tee llvm-testlog-%{_arch}.txt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE.TXT
%{_libdir}/libLLVM-3.6-mesa.so

%files devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config-%{__isa_bits}
%{_includedir}/mesa-private/llvm
%{_includedir}/mesa-private/llvm-c

%changelog
* Wed Nov 18 2015 Dave Airlie <airlied@redhat.com> 3.6.2-1
- m-p-l 3.6.2 + gcc 4.8 + python 2.7.8

* Mon Apr 28 2014 Adam Jackson <ajax@redhat.com> 3.4-3
- Fix specfile so %%postun isn't interpreted as a shell script

* Mon Apr 21 2014 Adam Jackson <ajax@redhat.com> 3.4-1
- m-p-l 3.4 plus radeonsi backport

* Tue Jun 18 2013 Adam Jackson <ajax@redhat.com> 3.3-0.3.rc3
- Port to RHEL6
- Don't bother building R600 on s390x

* Tue Jun 11 2013 Adam Jackson <ajax@redhat.com> 3.3-0.2.rc3
- 3.3 rc3
- Drop tblgen
- Strip out some headers

* Tue May 14 2013 Adam Jackson <ajax@redhat.com> 3.3-0.1.rc1
- Update to 3.3 rc1
- Move library to %%{_libdir} to avoid rpath headaches
- Link with -Bsymbolic and --default-symver
- --disable-libffi
- Misc spec cleanup

* Wed Dec 05 2012 Adam Jackson <ajax@redhat.com> 3.1-13
- Forked spec for RHEL7 Mesa's private use
  - no ocaml support
  - no doxygen build
  - no clang support
  - no static archives
  - no libraries, binaries, or manpages not needed by Mesa
