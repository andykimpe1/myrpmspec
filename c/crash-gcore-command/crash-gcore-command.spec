#
# crash core analysis suite
#
Summary: Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.0
Release: 5%{?dist}
License: GPLv2
Group: Development/Debuggers
Source: %{name}-%{version}.tar.gz
URL: http://people.redhat.com/anderson/extensions/%{name}-%{version}.tar.gz
# Vendor: FUJITSU LIMITED
# Packager: HATAYAMA Daisuke <d.hatayama@jp.fujitsu.com>
ExclusiveOS: Linux
ExclusiveArch: x86_64 %{ix86} arm
Buildroot: %{_tmppath}/%{name}-root
BuildRequires: crash-devel >= 5.1.5, zlib-devel lzo-devel
Requires: crash >= 5.1.5
Patch0: use_RPM_OPT_FLAGS.patch
Patch1: VDSO_and_vsyscall_pages.patch

%description
Command for creating a core dump file of a user-space task that was
running in a kernel dumpfile.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b use_RPM_OPT_FLAGS.patch
%patch1 -p1 -b VDSO_and_vsyscall_pages.patch

%build
make -f gcore.mk

%install
rm -Rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_libdir}/crash/extensions/
cp %{_builddir}/%{name}-%{version}/gcore.so %{buildroot}%{_libdir}/crash/extensions/

%clean
rm -rf %{buildroot}
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/gcore.so
%doc COPYING

%changelog
* Tue Aug 20 2013 Dave Anderson <anderson@redhat.com> - 1.0-5
  Fix to be able to build VDSO/vsyscall patch with crash-6.1.0-2.el6
  Resolves: rbhz#890232

* Wed May 29 2013 Dave Anderson <anderson@redhat.com> - 1.0-4
  Fixes for missing VDSO and vsyscall pages in core dump. 
  Resolves: rbhz#890232

* Tue Jan 31 2012 Dave Anderson <anderson@redhat.com> - 1.0-3
  Address Pkgwrangler/rpmlint issues.
  Resolves: rbhz#692799

* Wed Jan 25 2012 Dave Anderson <anderson@redhat.com> - 1.0-2
  Compile with RPM_OPT_FLAGS and fix warnings generated from using it. 
  Resolves: rbhz#692799

* Thu Apr 13 2011 HATAYAMA Daisuke <d.hatayama@jp.fujitsu.com> - 1.0-1
- Remove inclusion of kvmdump.h and unwind_x86_64.h due to non-supporting issue
  on crash-devel package. Instead, use a new interface for them.
- Remove ppc64, ia64, s390 and s390x from ExclusiveArch, leave x86_64
  and %%{ix86} there.
- Add descriptions in BuildRequires and Requires about crash and crash-devel.

* Wed Apr 6 2011 HATAYAMA Daisuke <d.hatayama@jp.fujitsu.com> - 1.0-0
- Initial crash-gcore-command package

