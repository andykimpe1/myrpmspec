Summary: A program that ejects removable media using software control
Name: eject
Version: 2.1.5
Release: 17%{?dist}
License: GPLv2+
Group: System Environment/Base

# source URL is no longer valid
Source: %{name}-%{version}.tar.gz

Source1: eject.pam
Patch1: eject-2.1.1-verbose.patch
Patch2: eject-timeout.patch
Patch3: eject-2.1.5-opendevice.patch
Patch4: eject-2.1.5-spaces.patch
Patch5: eject-2.1.5-lock.patch
Patch6: eject-2.1.5-umount.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
URL: http://www.pobox.com/~tranter
ExcludeArch: s390 s390x
BuildRequires: gettext
BuildRequires: libtool

%description
The eject program allows the user to eject removable media (typically
CD-ROMs, floppy disks or Iomega Jaz or Zip disks) using software
control. Eject can also control some multi-disk CD changers and even
some devices' auto-eject features.

Install eject if you'd like to eject removable media using software
control.

%prep
%setup -q -n %{name}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%configure

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make DESTDIR=%{buildroot} install

# pam stuff
install -m 755 -d %{buildroot}/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/pam.d/%{name}

install -m 755 -d %{buildroot}/%{_sysconfdir}/security/console.apps/
echo "FALLBACK=true" > %{buildroot}/%{_sysconfdir}/security/console.apps/%{name}

install -m 755 -d %{buildroot}/%{_sbindir}
pushd %{buildroot}/%{_bindir}
mv eject ../sbin
ln -s consolehelper eject
popd

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO COPYING ChangeLog
%attr(644,root,root) %{_sysconfdir}/security/console.apps/*
%attr(644,root,root) %{_sysconfdir}/pam.d/*
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*

%changelog
* Fri Apr 09 2010 Kamil Dudka <kdudka@redhat.com> 2.1.5-17
- mention the option -i in eject(1) man page (#580895)

* Tue Dec 15 2009 Kamil Dudka <kdudka@redhat.com> 2.1.5-16
- honor merge review comments (#225720)
- remove invalid URL of source tarball

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.1.5-15.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-14
- Fixed space replacing in mount points (#492524)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1.5-12
- fix license tag

* Wed Apr 02 2008 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-11
- Added check if device is hotpluggable
- Resolves #438610

* Thu Mar 20 2008 Jesse Keating <jkeating@redhat.com> - 2.1.5-10
- Fix the patch again now that sysfs makes things in /sys/block symlinks.

* Mon Mar 17 2008 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-9
- Rewriten patch for removable flag
- Resolves #437362

* Wed Mar 12 2008 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-8.1
- Added dist tag

* Wed Mar 12 2008 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-8
- Added check for a removable flag
- Resolves: #432187

* Thu Feb 28 2008 Zdenek Prikryl <zprikryl@redhat.com> 2.1.5-7
- Added lock functionality, patch from upstream.
- Resolves: #145843

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1.5-6
- Autorebuild for GCC 4.3

* Mon Oct 30 2006 Than Ngo <than@redhat.com> 2.1.5-5
- apply upstream patch to fix #212467

* Mon Aug 28 2006 Than Ngo <than@redhat.com> 2.1.5-4
- fix #204222, Password error window popuped by calling "eject" command from remote

* Tue Aug 22 2006 Than Ngo <than@redhat.com> 2.1.5-3
- made eject use pam 

* Mon Aug 07 2006 Than Ngo <than@redhat.com> 2.1.5-2
- apply patch to fix timeout issue

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.1.5-1.1
- rebuild

* Sat Jun 10 2006 Than Ngo <than@redhat.com> 2.1.5-1
- 2.1.5 

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1.2-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1.2-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Aug 25 2005 Than Ngo <than@redhat.com> 2.1.2-1
- update to 2.1.2
- drop several patches, which included in new upstream


* Wed Aug 24 2005 Than Ngo <than@redhat.com> 2.1.1-1
- update to 2.1.1
- remove eject-2.0.13-scsi.patch, which included in new upstream

* Thu May 12 2005 Than Ngo <than@redhat.com> 2.0.13-15
- add better translation for zh_TW #157519,
  thanks to Wei-Lun Chao

* Thu Mar 03 2005 Than Ngo <than@redhat.com> 2.0.13-14
- rebuilt 

* Wed Dec 01 2004 Than Ngo <than@redhat.com> 2.0.13-13
- add patch to remove deprecated SCSI ioctl

* Tue Nov 02 2004 Than Ngo <than@redhat.com> 2.0.13-12
- rebuilt

* Tue Nov 02 2004 Than Ngo <than@redhat.com> 2.0.13-11
- fix Invalid argument error, bug #131959

* Tue Sep 07 2004 Than Ngo <than@redhat.com> 2.0.13-10
- Added patch to find name in /media

* Sun Aug  8 2004 Alan Cox <alan@redhat.com>
- Fix build dependancies (#125317) - Steve Grubb

* Thu Jun 24 2004 Alan Cox <alan@redhat.com>
- Added Chris Woods patches as requested by Al Viro to handle modern
  namespace mounting and unmount by mount point not device

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Than Ngo <than@redhat.com> 2.0.13-5
- don't use kernel headers directly, #116613

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 20 2002 Than Ngo <than@redhat.com> 2.0.13-1
- update to 2.0.13

* Fri Nov  8 2002 Than Ngo <than@redhat.com> 2.0.12-8
- Added missing mo files

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Apr 28 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not build on mainframe

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 2.0.12-4
- rebuild in new enviroment

* Tue Feb 05 2002 Than Ngo <than@redhat.com> 2.0.12-3
- fix autoclose bug (stssppnn@yahoo.com, #59326)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Nov 14 2001 Than Ngo <than@redhat.com> 2.0.12-1
- update to 2.0.12

* Thu Sep 20 2001 Than Ngo <than@redhat.com> 2.0.11-1
- update to 2.0.11 (bug #53828)

* Mon May 21 2001 Than Ngo <than@redhat.com>
- update to 2.0.8
- remove eject-2.0.4-ignorecomments.patch, 2.0.8 has it

* Mon May 14 2001 Than Ngo <than@redhat.com>
- update to 2.0.6, fixed buffer overrun

* Tue May 01 2001 Than Ngo <than@redhat.com>
- update to 2.0.4

* Tue Apr 24 2001 Than Ngo <than@redhat.com>
- update to 2.0.3, supports devfs available in 2.4.x kernels and fixes
  a number of small problems

* Tue Apr  3 2001 Preston Brown <pbrown@redhat.com>
- ignore commented out entries in /etc/fstab (#33734)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- gzip man page.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 16 1999 Preston Brown <pbrown@redhat.com>
- solved a lot of problems by finding eject 2.0.2. :)

* Tue Feb 09 1999 Preston Brown <pbrown@redhat.com>
- patch to improve symlink handling folded into linux-2.2 patch

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jul 15 1998 Donnie Barnes <djb@redhat.com>
- added small patch to 1.5 for longer device names

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 1.5
- various spec file clean ups
- eject rocks!

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
