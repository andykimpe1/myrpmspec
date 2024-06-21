Summary: User-space access to Linux Kernel SCTP
Name: lksctp-tools
Version: 1.0.10
Release: 7%{?dist}
# src/apps/bindx_test.C is GPLv2, I've asked upstream for clarification
License: GPLv2 and GPLv2+ and LGPLv2 and BSD
Group: System Environment/Libraries
URL: http://lksctp.sourceforge.net
Source0: %{name}-%{version}.tar.gz
Patch0: lksctp-tools-1.0.6-libdir.patch
Patch1: lksctp-tools-1.0.10-test-crash.patch
Patch2: 0001-api-Update-the-sctp.h-header-to-match-the-kernel.patch
Patch3: 0002-lib-fix-make-distcheck-for-lksctp-tools.patch
Patch4: 0003-tools-fix-parallel-build-warning.patch
Patch5: 0004-apps-Fix-compiler-warnings-in-sctp_darn.patch
Patch6: 0005-lib-Fix-compiler-warning-for-connectx.c.patch
Patch7: 0006-func_test-fix-compiler-warnings-in-functional-tests.patch
Patch8: 0008-lib-Support-non-blocking-sctp_connectx-calls.patch
Patch9: 0009-lib-Fix-the-new-connectx-api-to-prefent-SEGFAULTS.patch
Patch10: 0010-API-Add-SCTP_SACK_IMMEDIATELY-defintion.patch
Patch11: 0011-api-SCTP_DELAYED_SACK-typo-fix.patch
Patch12: 0012-api-Remove-the-old-obsolete-getaddrs-interfaces.patch
Patch13: 0013-api-Remove-the-sctp-option-enumerator.patch
Patch14: 0014-sctp_darn-add-inter-command-heartbeat-for-user-initi.patch
Patch15: 0015-sctp_test-add-B-option-and-C-option-for-specifying-a.patch
Patch16: 0016-sctp_test-add-O-option-for-specifying-live-time-of-m.patch
Patch17: 0017-Implement-SCTP_GET_ASSOC_STATS.patch
Patch18: 0018-sctp_send-fix-msg_control-data-corruption.patch
Patch19: 0019-lksctp-tools-Update-sctp.h-with-info-for-DTLS.patch
Patch20: 0022-test_fragments-increase-message-size-since-it-succee.patch
Patch21: 0023-sctp_xconnect-memory-leak-when-malloc-big-buffer.patch
Patch22: 0024-docs-update-current-maintainers-of-lksctp-tools.patch
Patch23: 0025-apps-fix-format-string-warnings-due-to-size_t-usage.patch
Patch24: 0026-apps-nagle-remove-unused-af_family-variable.patch
Patch25: 0027-sctp_darn-remove-never-read-peer_prim_len-variable.patch
Patch26: 0028-func_tests-drop-more-af_family-occurences.patch
Patch27: 0029-test_1_to_1_sendmsg-remove-set-only-iov-variable-wit.patch
Patch28: 0030-test_1_to_1_threads-fixup-pthread-init-and-exit.patch
Patch29: 0031-test_1_to_1_addrs-remove-unused-socket-iov-and-mallo.patch
Patch30: 0032-test_1_to_1_nonblock-remove-unused-iov-and-malloced-.patch
Patch31: 0033-test_1_to_1_recv-minor-fix-compiler-warning.patch
Patch32: 0035-test_autoclose-remove-unneeded-variable.patch
Patch33: 0036-nagle_snd-remove-variable-with-assignment-only.patch
Patch34: 0037-apps-peel-no-reason-to-keep-unused-assigned-only-var.patch
Patch35: 0038-test_1_to_1_sockopt-fix-deprecated-SO_RCVBUF-SO_SNDB.patch
Patch36: 0039-apps-sctp_darn-fix-format-string-warning-on-some-arc.patch
Patch37: 0040-apps-func_tests-adapt-cflags-for-older-architectures.patch
Patch38: 0041-sctp_darn-fix-__u64-format-string-issues-on-ppc64-x8.patch
Patch39: 0047-test_1_to_1_threads-fixup-pthread-hung-by-giving-an-.patch
Patch40: 0048-test_1_to_1_threads-remove-unused-variable-for-t_rec.patch
Patch41: 0050-sctp-Add-new-spinfo-state-values-to-enumeration.patch
Patch42: 0053-sctp_status-fix-printstatus-output.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtool, automake, autoconf, git
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Conflicts: kernel < 2.6.10

%description
This is the lksctp-tools package for Linux Kernel SCTP (Stream Control
Transmission Protocol) Reference Implementation.

This package is intended to supplement the Linux Kernel SCTP Reference
Implementation now available in the Linux kernel source tree in
versions 2.5.36 and following.  For more information on LKSCTP see the
package documentation README file, section titled "LKSCTP - Linux
Kernel SCTP."

This package contains the base run-time library and command-line tools.

%package devel
Summary: Development files for lksctp-tools
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for lksctp-tools which include man pages, header files,
static libraries, symlinks to dynamic libraries and some tutorial source code.

%package doc
Summary: Documents pertaining to SCTP
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description doc
Documents pertaining to LKSCTP & SCTP in general (IETF RFC's & Internet
Drafts).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Create a git repo within the expanded tarball and let git do all the dirty work.
git init
git config user.email "dborkman@redhat.com"
git config user.name "Daniel Borkmann"
git add .
git commit -a -q -m "%{version} baseline."
# Apply all the patches on top of the release + patch0+1.
git am -s `echo %{patches} | cut -d' ' -f3-`

%build
[ ! -x ./configure ] && sh bootstrap
%configure --disable-static
# remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
rm -f doc/rfc2960.txt doc/states.txt
make install DESTDIR="$RPM_BUILD_ROOT"

find $RPM_BUILD_ROOT/%{_libdir}/ -name "*.la"  | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING* README
%{_bindir}/*
%{_libdir}/libsctp.so.*
%dir %{_libdir}/lksctp-tools/
%{_libdir}/lksctp-tools/libwithsctp.so.*
%{_mandir}/man7/*

%files devel
%defattr(-,root,root,0755)
%{_includedir}/*
%{_libdir}/libsctp.so
%dir %{_libdir}/lksctp-tools/
%{_libdir}/lksctp-tools/libwithsctp.so
%{_datadir}/lksctp-tools/
%{_mandir}/man3/*

%files doc
%defattr(0644,root,root,0755)
%doc doc/*.txt

%changelog
* Fri Jul 26 2013 Daniel Borkmann - 1.0.10-7
- Fix build for Git rework

* Fri Jul 26 2013 Daniel Borkmann - 1.0.10-6
- Move spec system to apply patches via git-am(1), which makes it more
  convienient for future backports
- Backport SCTP_GET_ASSOC_STATS support (#908390) and import its dependencies
- Fix bugs (#855379), (#953383), (#912557) and import its dependencies

* Mon Feb 22 2010 Jan Safranek <jsafrane@redhat.com> - 1.0.10-5
- Fixed the License of the package, it's BSD license, not MIT

* Tue Feb  9 2010 Jan Safranek <jsafrane@redhat.com> - 1.0.10-4
- Fixed the test suite (#528463)

* Tue Dec  1 2009 Jan Safranek <jsafrane@redhat.com> - 1.0.10-3
- Remove static libraries
- Remove rpath from binaries

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Zdenek Prikryl <zprikryl@redhat.com> 1.0.10-1
- added release tag to Requires of devel and doc packages (#492531)
- Update to 1.0.10

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 06 2008 Zdenek Prikryl <zprikryl@redhat.com> 1.0.9-1
- Update to 1.0.9

* Wed Jul 16 2008 Zdenek Prikryl <zprikryl@redhat.com> 1.0.8-1
- Update to 1.0.8

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.7-3
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Karsten Hopp <karsten@redhat.com> 1.0.7-2
- rebuild for buildid

* Wed Aug 08 2007 Karsten Hopp <karsten@redhat.com> 1.0.7-1
- update to 1.0.7
- update license tag

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 1.0.6-3
- add post/postun requirements
- review fixes

* Tue Sep 19 2006 Karsten Hopp <karsten@redhat.de> 1.0.6-2
- fix fileconflict (#205225)

* Tue Jul 25 2006 Karsten Hopp <karsten@redhat.de> 1.0.6-1
- update to 1.0.6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.fc5.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.fc5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.fc5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 24 2006 Warren Togami <wtogami@redhat.com> 1.0.5-1
- 1.0.5

* Fri Nov 11 2005 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.
- Update syntax patch.
- Execute bootstrap if no configure script is found.
- Don't own entire man? directories.
- Own data and lib lksctp-tools directories.
- Move devel libs in _libdir/lksctp-tools/ to devel package.
- Exclude .la files.
- Minor spec file cleanups.

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.0.2-5
- build with gcc-4

* Mon Feb 07 2005 Karsten Hopp <karsten@redhat.de> 1.0.2-4
- initialize variable before use
- fix subscript out of range bug (#147286)

* Mon Jan 24 2005 Karsten Hopp <karsten@redhat.de> 1.0.2-3
- build for FC

* Mon Jan 24 2005 Karsten Hopp <karsten@redhat.de> 1.0.2-2.40E.1
- initial RH version based on sourceforge rpm

* Thu Dec 30 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.2-1
- 1.0.2 Release

* Tue May 11 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.1-1
- 1.0.1 Release

* Thu Feb 26 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.0-1
- 1.0.0 Release

* Fri Feb  6 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.9.0-1
- package only .txt doc files

* Wed Feb  4 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.7.5-1
- badly placed & undelivered files
- simplified delivery list

* Tue Jan 27 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.7.5-1
- Integrate comment from project team

* Sat Jan 10 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 2.6.0_test7_0.7.4-1
- Creation
