Summary: Utilities for performing block layer IO tracing in the linux kernel
Name: blktrace
Version: 1.0.1
Release: 7%{?dist}
License: GPLv2+
Group: Development/System
Source:  http://brick.kernel.dk/snaps/blktrace-%{version}.tar.bz2
Url: http://brick.kernel.dk/snaps

Requires: python
BuildRequires: libaio-devel python texlive-latex dvipdfm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch0:  blktrace-1.0.1-avoid-device-duplication.patch
Patch1:  blktrace-1.0.1-blktrace-print-correct-usage.patch
Patch2:  blktrace-1.0.1-blktrace-add-back-devname-conversion.patch
Patch3:  blktrace-1.0.1-option-k-doesnt-kill.patch
Patch4:  blktrace-1.0.1-blkiomon-update-documentation.patch
Patch5:  blktrace-1.0.1-exit-with-zero-status.patch
Patch6:  blktrace-1.0.1-blktrace-unblock-tracers-if-unsuccess.patch
Patch7:  blktrace-1.0.1-btrecord-man-page-inconsistencies.patch
Patch8:  blktrace-1.0.1-blkiomon-undocumented-options.patch
Patch9:  blktrace-1.0.1-blkparce-undocumented-options.patch
Patch10: blktrace-1.0.1-blktrace-undocumented-options.patch
Patch11: blktrace-1.0.1-btreplay-undocumented-options.patch
Patch12: blktrace-1.0.1-btt-undocumented-options.patch
Patch13: blktrace-1.0.1-pc-write-completion.patch
Patch14: blktrace-1.0.1-flush-fua.patch
Patch15: blktrace-1.0.1-fix-for-realloc-bug.patch
Patch16: blktrace-1.0.1-blktrace-high-cpu-count.patch

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations to user space.  This package
includes both blktrace, a utility which gathers event traces from the kernel;
and blkparse, a utility which formats trace data collected by blktrace.

You should install the blktrace package if you need to gather detailed
information about IO patterns.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
make CFLAGS="%{optflags}" all
make CFLAGS="%{optflags}" docs

%install
rm -rf %{buildroot}
make dest=%{buildroot} prefix=%{buildroot}/%{_prefix} mandir=%{buildroot}/usr/share/man install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING
%doc btt/doc/btt.pdf btreplay/doc/btreplay.pdf doc/blktrace.pdf
%{_bindir}/*
%attr(0644,root,root) /usr/share/man/man1/*
%attr(0644,root,root) /usr/share/man/man8/*

%changelog
* Thu Nov 12 2015 Eric Sandeen <sandeen@redhat.com> - 1.0.1-7
- Fix realloc memory corruption (#1168101)
- cpu scalability patches (#1252894)

* Wed Sep 07 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.1-6
- Add FLUSH/FUA support (#736399)

* Fri Jul 22 2011 Eric Sandeen <sandeen@redhat.com> - 1.0.1-5
- fix up incorrect pc write completion count (#705128)

* Thu Nov 05 2010 Edward Shishkin <edward@redhat.com> - 1.0.1-4
- blktrace doesn't run when device name is duplicated (#583615)
- blktrace prints incorrect usage when running w/o parameters (#619201)
- btreplay cannot work for /dev/cciss/c0d0 device (#650229)
- option -k doesn't kill running trace (#583624)
- blkiomon prints nothing when blktrace works with logical volume (#650243)
- blkparese exit with non-zero status when tracefile doesn't exist (#583695)
- run time went but blktrace is still running (#595356)
- inconsistencies in btrecord man page (#595413)
- undocumented options in blkiomon (#595419)
- undocumented options in blkparce (#595615)
- undocumented options in blktrace (#595620)
- undocumented options in btreplay (#595623)
- undocumented options in btt (#595628)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.1-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-2
- Upstream respun the release tarball to re-include top-level dir
- drop exclude of bno_plot.py[co], not getting built now?

* Mon May 11 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.1-1
- New upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Eric Sandeen <sandeen@redhat.com> - 1.0.0-2
- Build PDF documentation after all

* Sun Nov 02 2008 Eric Sandeen <sandeen@redhat.com> - 1.0.0-1
- New upstream version (now with actual versioning!)

* Fri Feb 08 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.9.20080103162505git
- gcc-4.3 rebuild

* Sat Jan 26 2008 Eric Sandeen <sandeen@redhat.com> - 0.0-0.8.20080103162505git
- New upstream version

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.6.20071010202719git
- Add libaio-devel to BuildRequires

* Wed Oct 24 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.5.20071010202719git
- New upstream version

* Wed Aug 15 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.4.20070730162628git
- Fix up btt/Makefile to accept rpm's CFLAGS

* Tue Aug 14 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.3.20070730162628git
- Just drop the pdf build, bloats the buildroot for such a simple tool

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.2.20070730162628git
- Add ghostscript to BuildRequires, use attr macro for man pages

* Wed Aug 01 2007 Eric Sandeen <sandeen@redhat.com> - 0.0-0.1.20070730162628git
- New package, initial build.
