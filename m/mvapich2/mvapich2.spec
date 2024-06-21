# We only compile with gcc, but other people may want other compilers.
# Set the compiler here.
%define opt_cc gcc
# Optional CFLAGS to use with the specific compiler...gcc doesn't need any,
# so uncomment and define to use
#define opt_cflags
%define opt_cxx g++
#define opt_cxxflags
%define opt_f77 gfortran
#define opt_fflags
%define opt_fc gfortran
#define opt_fcflags

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

#define _cc_name_suffix -gcc

%define namearch %{name}-%{_arch}%{?_cc_name_suffix}
%define namepsmarch %{name}-psm-%{_arch}%{?_cc_name_suffix}



%define opt_cflags -O3 -fno-strict-aliasing
%define opt_cxxflags -O3
%ifarch i386
%define opt_cflags -m32 -O3 -fno-strict-aliasing
%define opt_cxxflags -m32 -O3
%define opt_fflags -m32
%define opt_fcflags -m32
%endif
%ifarch x86_64
%define opt_cflags -m64 -O3 -fno-strict-aliasing
%define opt_cxxflags -m64 -O3
%define opt_fflags -m64
%define opt_fcflags -m64
%endif



Summary: OSU MVAPICH2 MPI package
License: BSD/LGPLv2.1+
Group: Development/Libraries
Name: mvapich2
Version: 2.0rc1
Release: 1%{?dist}
# The -rh tarball is made by taking the upstream tarball and removing
# license-questionable, duplicated, and generated files, then editing
# the auto* files until it compiles.
# find * -name .codingcheck -delete
# find * -name .state-cache -delete
# rm .mailmap 
# rm osu_benchmarks/*
# # cat << EOF > osu_benchmarks/Makefile.in
# all:
# 	echo osu-benchmarks are in mpitests
# install:
# EOF
# rm src/mpi/romio/test/external32.c
# rm -r src/mpid/ch3/channels/mrail/src/hwloc/*
# rm src/mpid/ch3/channels/nemesis/netmod/scif/*.[ch]
# rm -fr src/mpid/pamid/{cross,include,src}
# rm -r src/pm/hydra/tools/topo/hwloc/hwloc/*
# cp /dev/null src/mpid/pamid/Makefile.mk
# cat << EOF > src/mpid/pamid/subconfigure.m4
# [#] start of __file__
# 
# dnl _PREREQ handles the former role of mpichprereq, setup_device, etc
# [#] expansion is: PAC_SUBCFG_PREREQ_[]PAC_SUBCFG_AUTO_SUFFIX
# AC_DEFUN([PAC_SUBCFG_PREREQ_]PAC_SUBCFG_AUTO_SUFFIX,[
# ])dnl end PREREQ
# AC_DEFUN([PAC_SUBCFG_BODY_]PAC_SUBCFG_AUTO_SUFFIX,[
# ])dnl end _BODY
# 
# [#] end of __file__
# EOF
# mkdir src/pm/hydra/tools/topo/hwloc/hwloc/config
# touch src/pm/hydra/tools/topo/hwloc/hwloc/config/{hwloc,hwloc_check_attributes,hwloc_check_visibility,hwloc_check_vendor,hwloc_components,hwloc_pkg}.m4
Source: %{name}-%{version}-rh.tgz
Source1: mvapich2.module.in
Source2: macros.mvapich2
Source3: macros.mvapich2-psm
Patch0: mvapich2-2.0rc1-build.patch
Patch1: mvapich2-2.0rc1-free.patch
URL: http://mvapich.cse.ohio-state.edu/
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc-gfortran
BuildRequires: libibumad-devel, libibverbs-devel >= 1.1.3, librdmacm-devel
BuildRequires: python, hwloc-devel, libibmad-devel
BuildRequires: bison, flex
Requires: environment-modules
Requires: %{name}-common = %{version}-%{release}
ExcludeArch: s390 s390x

%description
This is an MPI-2 implementation which includes all MPI-1 features.  It is
based on MPICH and MVICH.

%package	common
Summary:	Common files for mvapich2
Group:		Development/Libraries
BuildArch:	noarch

%description common
Contains files that are commen across installations of mvapich2
(Documentation, examples)

%package	devel
Group: Development/Libraries
Summary:	Development files for mvapich2
Requires: librdmacm-devel, libibverbs-devel, libibumad-devel
Requires:	%{name} = %{version}-%{release}, gcc-gfortran
Provides:	mpi-devel

%description devel
Contains development headers and libraries for mvapich2

%ifarch x86_64
%package	psm
Group: Development/Libraries
Summary:	OSU MVAPICH2 using infinipath package
Requires: librdmacm-devel, libibverbs-devel, libibumad-devel
BuildRequires: infinipath-psm-devel

%description psm
This is a version of mvapich2 that uses the QLogic Infinipath transport.

%package	psm-devel
Group: Development/Libraries
Summary:	Development files for mvapich2
Requires: librdmacm-devel, libibverbs-devel, libibumad-devel
Requires:	%{name}-psm = %{version}-%{release}, gcc-gfortran
Provides:	mpi-devel

%description psm-devel
Contains development headers and libraries for mvapich2 using Infinipath
%endif

%prep
rm -fr %{buildroot}
%setup -q -n %{name}-%{version}-rh
%patch0 -p1
%patch1 -p0
%ifarch x86_64
mkdir .psm
cp -pr * .psm
mkdir .non-psm
mv * .non-psm
mv .non-psm non-psm
mv .psm psm
%endif

%ifarch x86_64
cd psm
./configure \
    --prefix=%{_libdir}/%{name}-psm \
    --sbindir=%{_libdir}/%{name}-psm/bin \
    --mandir=%{_mandir}/%{namepsmarch} \
    --includedir=%{_includedir}/%{namepsmarch} \
    --sysconfdir=%{_sysconfdir}/%{namepsmarch} \
    --datarootdir=%{_datadir}/%{name} \
    --docdir=%{_datadir}/doc/%{name} \
    --enable-error-checking=runtime \
    --enable-timing=none \
    --enable-g=mem,dbg,meminit \
    --enable-mpe \
    --enable-shared \
    --enable-sharedlibs=gcc \
    --with-hwloc=yes --with-hwloc-prefix=system\
    --with-device=ch3:psm \
    CC=%{opt_cc}    CFLAGS="%{?opt_cflags} $RPM_OPT_FLAGS $XFLAGS" \
    CXX=%{opt_cxx}  CXXFLAGS="%{?opt_cxxflags} $RPM_OPT_FLAGS $XFLAGS" \
    FC=%{opt_fc}    FCFLAGS="%{?opt_fcflags} $RPM_OPT_FLAGS $XFLAGS" \
    F77=%{opt_f77}  FFLAGS="%{?opt_fflags} $RPM_OPT_FLAGS $XFLAGS"
cd ..
%endif

%ifarch x86_64
cd non-psm
%endif
./configure \
    --prefix=%{_libdir}/%{name} \
    --sbindir=%{_libdir}/%{name}/bin \
    --mandir=%{_mandir}/%{namearch} \
    --includedir=%{_includedir}/%{namearch} \
    --sysconfdir=%{_sysconfdir}/%{namearch} \
    --datarootdir=%{_datadir}/%{name} \
    --docdir=%{_datadir}/doc/%{name} \
    --enable-error-checking=runtime \
    --enable-timing=none \
    --enable-g=mem,dbg,meminit \
    --enable-mpe \
    --enable-shared \
    --enable-sharedlibs=gcc \
    --with-hwloc=yes --with-hwloc-prefix=system\
    --with-rdma=gen2 \
    CC=%{opt_cc}    CFLAGS="%{?opt_cflags} $RPM_OPT_FLAGS $XFLAGS" \
    CXX=%{opt_cxx}  CXXFLAGS="%{?opt_cxxflags} $RPM_OPT_FLAGS $XFLAGS" \
    FC=%{opt_fc}    FCFLAGS="%{?opt_fcflags} $RPM_OPT_FLAGS $XFLAGS" \
    F77=%{opt_f77}  FFLAGS="%{?opt_fflags} $RPM_OPT_FLAGS $XFLAGS"
%ifarch x86_64
cd ..
%endif

%build
export AR=ar
%ifarch x86_64
cd psm
make %{?_smp_mflags}
cd ..
%endif
%ifarch x86_64
cd non-psm
%endif
make %{?_smp_mflags}
%ifarch x86_64
cd ..
%endif

%install
%ifarch x86_64
cd non-psm
%endif
make DESTDIR=%{buildroot} install
# find %{buildroot}%{_mandir}/%{namearch} -type f | xargs gzip -9
mkdir %{buildroot}%{_mandir}/%{namearch}/man{2,4,5,6,7,8,9,n}

# Make the environment-modules file
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles/mpi
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#'%{_libdir}/%{name}'#g;s#@ETCDIR@#'%{_sysconfdir}/%{namearch}'#g;s#@FMODDIR@#'%{_fmoddir}/%{namearch}'#g;s#@INCDIR@#'%{_includedir}/%{namearch}'#g;s#@MANDIR@#'%{_mandir}/%{namearch}'#g;s#@PYSITEARCH@#'%{python_sitearch}/%{name}'#g;s#@COMPILER@#%{name}-'%{_arch}%{?_cc_name_suffix}'#g;s#@SUFFIX@#'%{?_cc_name_suffix}'_%{name}#g' < %SOURCE1 > %{buildroot}%{_sysconfdir}/modulefiles/%{namearch}
# make the rpm config file
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cp %SOURCE2 %{buildroot}%{_sysconfdir}/rpm/macros.%{namearch}
mkdir -p %{buildroot}%{_fmoddir}/%{namearch}
mkdir -p %{buildroot}%{python_sitearch}/%{name}%{?_cc_name_suffix}
%ifarch x86_64
cd ..
%endif

%ifarch x86_64
cd psm
make DESTDIR=%{buildroot} install
# find %{buildroot}%{_mandir}/%{namepsmarch} -type f | xargs gzip -9
mkdir %{buildroot}%{_mandir}/%{namepsmarch}/man{2,4,5,6,7,8,9,n}

# Make the environment-modules file
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#'%{_libdir}/%{name}-psm'#g;s#@ETCDIR@#'%{_sysconfdir}/%{namepsmarch}'#g;s#@FMODDIR@#'%{_fmoddir}/%{namepsmarch}'#g;s#@INCDIR@#'%{_includedir}/%{namepsmarch}'#g;s#@MANDIR@#'%{_mandir}/%{namepsmarch}'#g;s#@PYSITEARCH@#'%{python_sitearch}/%{name}-psm'#g;s#@COMPILER@#%{name}-psm-'%{_arch}%{?_cc_name_suffix}'#g;s#@SUFFIX@#'%{?_cc_name_suffix}'_%{name}-psm#g' < %SOURCE1 > %{buildroot}%{_sysconfdir}/modulefiles/%{namepsmarch}
# make the rpm config file
cp %SOURCE3 %{buildroot}%{_sysconfdir}/rpm/macros.%{namepsmarch}
mkdir -p %{buildroot}%{_fmoddir}/%{namepsmarch}
mkdir -p %{buildroot}%{python_sitearch}/%{name}-psm%{?_cc_name_suffix}
cd ..
%endif

rm -f %{buildroot}%{_libdir}/%{name}*/lib/*.la
rm -rf %{buildroot}%{_libdir}/%{name}*/lib/trace_rlog

# Ensure the osu files get blown away.
rm -rf %{buildroot}%{_libdir}/%{name}-psm/libexec
rm -rf %{buildroot}%{_libdir}/%{name}/libexec

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/lib
%dir %{_mandir}/%{namearch}
%dir %{_mandir}/%{namearch}/man*
%dir %{_fmoddir}/%{namearch}
%dir %{python_sitearch}/%{name}

%{_libdir}/%{name}/bin/hydra_nameserver
%{_libdir}/%{name}/bin/hydra_persist
%{_libdir}/%{name}/bin/hydra_pmi_proxy
%{_libdir}/%{name}/bin/mpichversion
%{_libdir}/%{name}/bin/mpiexec
%{_libdir}/%{name}/bin/mpiexec.hydra
%{_libdir}/%{name}/bin/mpiexec.mpirun_rsh
%{_libdir}/%{name}/bin/mpiname
%{_libdir}/%{name}/bin/mpirun
%{_libdir}/%{name}/bin/mpirun_rsh
%{_libdir}/%{name}/bin/mpispawn
%{_libdir}/%{name}/bin/mpivars
%{_libdir}/%{name}/bin/parkill
%{_libdir}/%{name}/lib/*.so.*
%{_mandir}/%{namearch}/man1/*
%{_sysconfdir}/modulefiles/%{namearch}


%files devel
%defattr(-,root,root,-)
# % dir %{_sysconfdir}/%{namearch}
%dir %{_includedir}/%{namearch}
%{_sysconfdir}/rpm/macros.%{namearch}
# % config(noreplace) %{_sysconfdir}/%{namearch}/*
%{_includedir}/%{namearch}/*
%{_mandir}/%{namearch}/man3/*
%{_libdir}/%{name}/bin/mpic++
%{_libdir}/%{name}/bin/mpicc
%{_libdir}/%{name}/bin/mpicxx
%{_libdir}/%{name}/bin/mpif77
%{_libdir}/%{name}/bin/mpif90
%{_libdir}/%{name}/lib/pkgconfig
%{_libdir}/%{name}/lib/*.a
%{_libdir}/%{name}/lib/*.so

%files common
%defattr(-,root,root,-)
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/*

%ifarch x86_64
%files psm
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}-psm
%dir %{_libdir}/%{name}-psm/bin
%dir %{_libdir}/%{name}-psm/lib
%dir %{_mandir}/%{namepsmarch}
%dir %{_mandir}/%{namepsmarch}/man*
%dir %{_fmoddir}/%{namepsmarch}
%dir %{python_sitearch}/%{name}-psm

%{_libdir}/%{name}-psm/bin/hydra_nameserver
%{_libdir}/%{name}-psm/bin/hydra_persist
%{_libdir}/%{name}-psm/bin/hydra_pmi_proxy
%{_libdir}/%{name}-psm/bin/mpichversion
%{_libdir}/%{name}-psm/bin/mpiexec
%{_libdir}/%{name}-psm/bin/mpiexec.hydra
%{_libdir}/%{name}-psm/bin/mpiexec.mpirun_rsh
%{_libdir}/%{name}-psm/bin/mpiname
%{_libdir}/%{name}-psm/bin/mpirun
%{_libdir}/%{name}-psm/bin/mpirun_rsh
%{_libdir}/%{name}-psm/bin/mpispawn
%{_libdir}/%{name}-psm/bin/mpivars
%{_libdir}/%{name}-psm/bin/parkill
%{_libdir}/%{name}-psm/lib/*.so.*
%{_mandir}/%{namepsmarch}/man1/*
%{_sysconfdir}/modulefiles/%{namepsmarch}


%files psm-devel
%defattr(-,root,root,-)
# % dir %{_sysconfdir}/%{namepsmarch}
%dir %{_includedir}/%{namepsmarch}
%{_sysconfdir}/rpm/macros.%{namepsmarch}
# % config(noreplace) %{_sysconfdir}/%{namepsmarch}/*
%{_includedir}/%{namepsmarch}/*
%{_libdir}/%{name}-psm/bin/mpic++
%{_libdir}/%{name}-psm/bin/mpicc
%{_libdir}/%{name}-psm/bin/mpicxx
%{_libdir}/%{name}-psm/bin/mpif77
%{_libdir}/%{name}-psm/bin/mpif90
%{_mandir}/%{namepsmarch}/man3/*
%{_libdir}/%{name}-psm/lib/pkgconfig
%{_libdir}/%{name}-psm/lib/*.a
%{_libdir}/%{name}-psm/lib/*.so
%endif

%changelog
* Mon Jun 2 2014 Jay Fenlason <fenlason@redhat.com> 2.0rc1-1
- Upgrade to upstream 2.0rc1
- Backport from RHEL-7 to RHEL-6
- Include the -free patch (written by me) to prevent errors caused
  by calling the free macro rather than the free() function.
- Fix the build process to work on RHEL-6, with its ancient
  auto*, libtool, etc.  This requires not rerunning autogen.sh
- Resolves: rhbz1093454


* Mon Sep 16 2013 Jay Fenlason <fenlason@redhat.com> 2.0a-1
- Add Build Requires on autoconf, automake, libtool,
  perl-Digest-MD5, hwloc-devel, and libibmad-devel.
- remove build requires on java
- New upstream version, edited so it can pass a license audit.
  (RHEL7) R e s o l v e s: r h b z 1001718

* Mon Aug 19 2013 Jay Fenlason <fenlason@redhat.com> 1.8-3
- Move the module files to the (correct for RHEL-7) mpi/ directory.
- Add MANPATH to the module files.

* Wed May 30 2012 Jay Fenlason <fenlason@redhat.com> 1.8-2
- Add BuildRequires on flex and bison
- Add "export AR=ar" to allow builds on RHEL-7 to work.
  Resolves: rhbz822527

* Tue Feb 14 2012 Jay Fenlason <fenlason@redhat.com> 1.8-1
- New upstream version, with man pages again.
  This fixes the following bugs:
  Related: rhbz739138
  Resolves: rhbz613696
  Resolves: rhbz625620
  Resolves: rhbz735954
  Resolves: rhbz782263
* Fri Aug 19 2011 Jay Fenlason <fenlason@redhat.com> 1.6-3.el6
- Change the requires on mvapich2-psm-devel to mvapich2-psm from mvapich2
  so that mpitests will build
- clean up the build to not use .{non-}psm directories.
  Related: rhbz725016

* Wed Aug 17 2011 Jay Fenlason <fenlason@redhat.com> 1.6-2.el6
- Fix the psm RPM macros so that we can build a -psm variant of
  mpitests
- remove the osu-micro-benchmarks, which are being installed with a
  bogus rpath, and which are included in mpitests
  Related: rhbz725016

* Mon Aug 15 2011 Jay Fenlason <fenlason@redhat.com> 1.6-1.el6
- New upstream release, with different build process, and without
  man pages, because we don't have the sowing package, and its
  licensing status is unclear (no licence description of any kind in
  the tarball).
  Related: rhbz725016

* Mon Jun 7 2010 Jay Fenlason <fenlason@redhat.com> 1.4-5.el6
- Forgot the BuildRequires
  Related: rhbz570274

* Mon Jun 7 2010 Jay Fenlason <fenlason@redhat.com>
- Add support for -psm subpackages on x86_64.
  Related: rhbz570274

* Tue Mar 2 2010 Jay Fenlason <fenlason@redhat.com> 1.4-4.el6
- Move -devel requires to the -devel subpackage.
  Resolves: bz568450
- Add defattr as required by packaging guidelines
  Related: bz555835

* Fri Jan 15 2010 Doug Ledford <dledford@redhat.com> - 1.4-3.el6
- Fix an issue with usage of _cc_name_suffix that caused a broken define in
  our module file
  Related: bz543948

* Fri Jan 15 2010 Jay Fenlason <fenlason@redhat.com> 1.4-2.el6
- Add BuildRequires: python
- Add BuildRequires: java
- Remove the pkgconfig file entirely
  Related: bz543948

* Thu Jan 14 2010 Jay Fenlason <fenlason@redhat.com>
- Add Group: to -devel
- Split into subpackages as required by packaging guidelines
- cleanup BuildRequires
- attempt to build on ppc
- cleanup spec file
- cleanup mvapich2.pc, still not correct, but closer
  Related: bz543948

* Thu Jan 14 2010 Jay Fenlason <fenlason@redhat.com>
- New EnvironmentModules version for RHEL-6
  Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Update to latest upstream version
- Related: bz518218

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 1.2-0.p1.3.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 1.2-0.p1.2.el5
- Compile against non-XRC libibverbs
- Related: bz506258

* Wed Apr 22 2009 Doug Ledford <dledford@redhat.com> - 1.2-0.p1.1
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Thu Oct 16 2008 Doug Ledford <dledford@redhat.com> - 1.0.3-3
- Make sure MPD_BIN is set in the mpivars files
- Related: bz466390

* Fri Oct 03 2008 Doug Ledford <dledford@redhat.com> - 1.0.3-2
- Make scriptlets match mvapich
- Include a Requires(post) and Requires(preun) so installs work properly
- Resolves: bz465448

* Thu Sep 18 2008 Doug Ledford <dledford@redhat.com> - 1.0.3-1
- Initial rhel5 package
- Resolves: bz451477

* Sun May 04 2008 Jonathan Perkins <perkinjo@cse.ohio-state.edu>
- Created initial MVAPICH2 1.0.3 SRPM with IB and iWARP support.

