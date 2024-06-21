%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define __libtoolize :

Summary: A utility for determining file types
Name: file
Version: 5.04
Release: 30%{?dist}
License: BSD
Group: Applications/File
Source0: ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
URL: http://www.darwinsys.com/file/
Patch0: file-4.21-pybuild.patch
Patch1: file-5.00-devdrv.patch
Patch2: file-5.00-mdmp.patch
Patch3: file-5.04-separ.patch
Patch4: file-5.04-filesystem.patch
Patch5: file-5.04-ruby-modules.patch
Patch6: file-5.04-squashfs.patch
Patch7: file-5.04-ulaw-segfault.patch
Patch8: file-5.04-core-trim.patch
Patch9: file-5.04-html-regression.patch
Patch10: file-5.04-differentiate-gfs1-gfs2.patch
Patch11: file-5.04-zip64.patch
Patch12: file-5.04-volume_key.patch
Patch13: file-5.04-text-string.patch
Patch14: file-5.04-python-diff-magic.patch
Patch15: file-5.04-man-return-code.patch
Patch16: file-5.04-webm.patch
Patch17: file-5.04-rpm.patch
Patch18: file-5.04-s390-kernel.patch
Patch19: file-5.04-core-prpsinfo.patch
Patch20: file-5.04-python-regex.patch
Patch21: file-5.04-man-page.patch
Patch22: file-5.04-latex-improve.patch
Patch23: file-5.04-text-fix.patch
Patch24: file-5.04-elf-header-size.patch
Patch25: file-4.17-i64-swap.patch
Patch26: file-4.17-rpm-name.patch
Patch27: file-5.04-bios.patch
Patch28: file-5.04-generic-msdos.patch
Patch29: file-5.04-lzma.patch
Patch30: file-5.04-python-func.patch
Patch31: file-localmagic.patch
Patch32: file-qed-vdi-image.patch
Patch33: file-5.11-compress.patch
Patch34: file-5.11-magicmgc-home.patch
Patch35: file-5.11-dump-twice.patch
Patch36: file-5.04-minix.patch
Patch37: file-5.04-netpbm.patch
Patch38: file-5.04-biorad.patch
Patch39: file-5.11-qcow3.patch
Patch40: file-5.11-rrdtool.patch
Patch41: file-5.04-CVE-2014-3479.patch
Patch43: file-5.04-CVE-2014-3480.patch
Patch44: file-5.04-CVE-2014-0237.patch
Patch45: file-5.04-CVE-2014-0238.patch
Patch46: file-5.04-CVE-2014-2270.patch
Patch47: file-5.04-CVE-2014-1943.patch
Patch48: file-5.04-CVE-2012-1571.patch
Patch49: file-5.04-trim.patch
Patch50: file-5.04-ppc32core.patch
Patch51: file-5.04-java1718.patch
Patch52: file-5.04-pascal.patch
Patch53: file-5.04-epub.patch
Patch54: file-5.04-zipmime.patch
Patch55: file-5.04-xml.patch
Patch56: file-5.04-auxv.patch
Patch57: file-5.04-newpython.patch
Patch58: file-5.04-msooxml.patch
Patch59: file-5.04-CVE-2014-3587.patch
Patch60: file-5.04-CVE-2014-3710.patch
Patch61: file-5.04-CVE-2014-8116.patch
Patch62: file-5.04-CVE-2014-8117.patch
Patch63: file-5.04-CVE-2014-9620.patch
Patch64: file-5.04-CVE-2014-9653.patch
Patch65: file-5.04-CVE-2014-3538.patch

Requires: file-libs = %{version}-%{release}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: zlib-devel

%description
The file command is used to identify a particular file according to the
type of data contained by the file.  File can identify many different
file types, including ELF binaries, system libraries, RPM packages, and
different graphics formats.

%package libs
Summary: Libraries for applications using libmagic
Group:   Applications/File

%description libs

Libraries for applications using libmagic.

%package devel
Summary:  Libraries and header files for file development
Group:    Applications/File
Requires: %{name} = %{version}-%{release}

%description devel
The file-devel package contains the header files and libmagic library
necessary for developing programs using libmagic.

%package static
Summary: Static library for file development
Group:    Applications/File
Requires: %{name} = %{version}-%{release}

%description static
The file-static package contains the static version of
the libmagic library.

%package -n python-magic
Summary: Python bindings for the libmagic API
Group:   Development/Libraries
BuildRequires: python-devel
Requires: %{name} = %{version}-%{release}

%description -n python-magic
This package contains the Python bindings to allow access to the
libmagic API. The libmagic library is also used by the familiar
file(1) command.

%prep
# Don't use -b -- it will lead to poblems when compiling magic file
%setup -q
%patch0 -p1
#fixes #463809
%patch1 -p1
#fixes #485835
%patch2 -p1
#fixes #575178
%patch3 -p1
#fixes #570785
%patch4 -p1
#fixes #562840
%patch5 -p1
#fixes #550212
%patch6 -p1
#fixes #533245
%patch7 -p1
#fixes #580490
%patch8 -p1
#fixes #594605,#594624,#594636
%patch9 -p1
#fixes #670125
%patch10 -p1
#fixes #637782
%patch11 -p1
#fixes #643046
%patch12 -p1
#fixes #594083
%patch13 -p1
#fixes #594083
%patch14 -p1
#fixes #608686
%patch15 -p1
#fixes #610795
%patch16 -p1
#fixes #676045, #712992
%patch17 -p1
#fixes #688700
%patch18 -p1
#fixes #692098
%patch19 -p1
#fixes #712988
%patch20 -p1
#fixes #690801
%patch21 -p1
#fixes #675691
%patch22 -p1
#fixes #716665
%patch23 -p1
#fixes #730336
%patch24 -p1
#fixes #758109
%patch25 -p1
#fixes #760083
%patch26 -p1
#fixes #709846
%patch27 -p1
#fixes #688136
%patch28 -p1
#fixes #747999
%patch29 -p1
#fixes #733229
%patch30 -p1
#fixes #719583
%patch31 -p1
#fixes #795761, #795425
%patch32 -p1
#fixes #801711
%patch33 -p1
#fixes #797784
%patch34 -p1
#fixes #859834
%patch35 -p1
#fixes #873997
%patch36 -p1
#fixes #884396
%patch37 -p1
#fixes #980941
%patch38 -p1
#fixes #1067771
%patch39 -p1
#fixes #1064463
%patch40 -p1
#fixes CVE-2014-3479
%patch41 -p1
#fixes CVE-2014-3480
%patch43 -p1
#fixes CVE-2014-0237
%patch44 -p1
#fixes CVE-2014-0238
%patch45 -p1
#fixes CVE-2014-2270
%patch46 -p1
#fixes CVE-2014-1943
%patch47 -p1
#fixes CVE-2012-1571
%patch48 -p1
#fixes #664513
%patch49 -p1
#fixes #1037279
%patch50 -p1
#fixes #1169509
%patch51 -p1
#fixes #1243650
%patch52 -p1
#fixes #1161058
%patch53 -p1
#fixes #1154802
%patch54 -p1
#fixes #1246073
%patch55 -p1
#fixes #1263987
%patch56 -p1
#fixes #809898
%patch57 -p1
#fixes #966953
%patch58 -p1
#fixes CVE-2014-3587
%patch59 -p1
#fixes CVE-2014-3710
%patch60 -p1
#fixes CVE-2014-8116
%patch61 -p1
#fixes CVE-2014-8117
%patch62 -p1
#fixes CVE-2014-9620
%patch63 -p1
#fixes CVE-2014-9653
%patch64 -p1
#fixes CVE-2014-3538
%patch65 -p1


# Patches can generate *.orig files, which can't stay in the magic dir,
# otherwise there will be problems when compiling magic file!
rm -fv magic/Magdir/*.orig

iconv -f iso-8859-1 -t utf-8 < doc/libmagic.man > doc/libmagic.man_
touch -r doc/libmagic.man doc/libmagic.man_
mv doc/libmagic.man_ doc/libmagic.man

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE" \
%configure --enable-fsect-man5 --disable-rpath
# remove hardcoded library paths from local libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
export LD_LIBRARY_PATH=%{_builddir}/%{name}-%{version}/src/.libs
make
cd python
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man5
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/misc
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/file

make DESTDIR=${RPM_BUILD_ROOT} install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.la

# local magic in /etc/magic
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
cp -a ./magic/magic.local ${RPM_BUILD_ROOT}%{_sysconfdir}/magic

cat magic/Magdir/* > ${RPM_BUILD_ROOT}%{_datadir}/misc/magic
ln -s misc/magic ${RPM_BUILD_ROOT}%{_datadir}/magic
#ln -s file/magic.mime ${RPM_BUILD_ROOT}%{_datadir}/magic.mime
ln -s ../magic ${RPM_BUILD_ROOT}%{_datadir}/file/magic

cd python
%{__python} setup.py install -O1 --skip-build --root ${RPM_BUILD_ROOT}
%{__install} -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}
%{__install} -D example.py ${RPM_BUILD_ROOT}/%{_docdir}/python-magic-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README
%{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/magic

%files libs
%defattr(-,root,root,-)
%{_libdir}/*so.*
%{_datadir}/magic*
%{_mandir}/man5/*
%{_datadir}/file
%{_datadir}/misc/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/magic.h
%{_mandir}/man3/*

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files -n python-magic
%defattr(-, root, root, -)
%doc python/README COPYING python/example.py
%{python_sitearch}/magic.so
%if 0%{?fedora} >= 9 || 0%{?rhel} >= 6
%{python_sitearch}/*egg-info
%endif

%changelog
* Tue Feb 16 2016 Jan Kaluza <jkaluza@redhat.com> 5.04-30
- fix CVE-2014-3538 (unrestricted regular expression matching)

* Tue Jan 05 2016 Jan Kaluza <jkaluza@redhat.com> 5.04-29
- fix #1284826 - try to read ELF header to detect corrupted one

* Wed Dec 16 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-28
- fix #1263987 - fix bugs found by coverity in the patch

* Thu Nov 26 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-27
- fix CVE-2014-3587 (incomplete fix for CVE-2012-1571)
- fix CVE-2014-3710 (out-of-bounds read in elf note headers)
- fix CVE-2014-8116 (multiple DoS issues (resource consumption))
- fix CVE-2014-8117 (denial of service issue (resource consumption))
- fix CVE-2014-9620 (limit the number of ELF notes processed)
- fix CVE-2014-9653 (malformed elf file causes access to uninitialized memory)

* Tue Nov 24 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-26
- fix #809898 - add support for detection of Python 2.7 byte-compiled files

* Tue Nov 24 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-25
- fix #1263987 - fix coredump execfn detection on ppc64 and s390

* Fri Nov 13 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-24
- fix #966953 - include msooxml file in magic.mgc generation

* Fri Nov 13 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-23
- fix #966953 - increate the strength of MSOOXML magic patterns

* Thu Nov 05 2015 Jan Kaluza <jkaluza@redhat.com> 5.04-22
- fix #1169509 - add support for Java 1.7 and 1.8
- fix #1243650 - comment out too-sensitive Pascal magic
- fix #1080453 - remove .orig files from magic directory
- fix #1161058 - add support for EPUB
- fix #1162149 - remove parts of patches patching .orig files
- fix #1154802 - fix detection of zip files containing file named "mime"
- fix #1246073 - fix detection UTF8 and UTF16 encoded XML files
- fix #1263987 - add new "execfn" to coredump output to show the real name of
  executable which generated the coredump
- fix #809898 - add support for detection of Python 3.2-3.5 byte-compiled files
- fix #966953 - backport support for MSOOXML

* Mon Aug 04 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-21
- fix typographical error in changelog

* Fri Jul 18 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-20
- fix #1037279 - better patch for the bug from previous release

* Fri Jul 18 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-19
- fix #1037279 - display "from" field on 32bit ppc core

* Thu Jul 10 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-18
- fix #664513 - trim white-spaces during ISO9660 detection

* Mon Jun 30 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-17
- fix CVE-2014-3479 (cdf_check_stream_offset boundary check)
- fix CVE-2014-3480 (cdf_count_chain insufficient boundary check)
- fix CVE-2014-0237 (cdf_unpack_summary_info() excessive looping DoS)
- fix CVE-2014-0238 (CDF property info parsing nelements infinite loop)
- fix CVE-2014-2270 (out-of-bounds access in search rules with offsets)
- fix CVE-2014-1943 (unrestricted recursion in handling of indirect type rules)
- fix CVE-2012-1571 (out of bounds read in CDF parser)

* Thu Apr 24 2014 Jan Kaluza <jkaluza@redhat.com> 5.04-16
- fix #873997 - improve Minix detection pattern to fix false positives
- fix #884396 - improve PBM pattern to fix misdetection with x86 boot sector
- fix #980941 - improve Bio-Rad pattern to fix false positives
- fix #849621 - tweak strength of XML, Latex and Python patterns to execute
  them in the proper order
- fix #1067771 - detect qcow version 3 images
- fix #1064463 - treat RRDTool files as binary files

* Tue Sep 25 2012 Jan Kaluza <jkaluza@redhat.com> 5.04-15
- fix #859834 - removed duplicated patterns for backups generated by "dump" tool

* Tue Aug 14 2012 Jan Kaluza <jkaluza@redhat.com> 5.04-14
- fix #795425 - detect vdi images
- fix #795761 - detect qed images
- fix #801711 - uncompress bzip2 archives using -z parameter
- fix #797784 - read patterns from ~/.magic.mgc

* Tue Feb 14 2012 Jan Kaluza <jkaluza@redhat.com> 5.04-13
- fix #688136 - fixed the patch from previous commit
- fix #719583 - support for local magic file in /etc/magic

* Wed Feb 08 2012 Jan Kaluza <jkaluza@redhat.com> 5.04-12
- fix #758109 - detect ia64 swap
- fix #760083 - print RPM packages names
- fix #709846 - detect BIOS headers
- fix #688136 - remove weak msdos patterns
- fix #747999 - improve lzma detection
- fix #733229 - magic pattern for python function detection

* Mon Sep 05 2011 Jan Kaluza <jkaluza@redhat.com> 5.04-11
- fix #730336 - updated patch from upstream

* Wed Aug 17 2011 Jan Kaluza <jkaluza@redhat.com> 5.04-10
- fix #730336 - parse all ELF headers

* Wed Jun 29 2011 Jan Kaluza <jkaluza@redhat.com> 5.04-9
- fix #716665 - detect MP3 files properly

* Wed Jun 22 2011 Jan Kaluza <jkaluza@redhat.com> 5.04-8
- fix #676045 - detect all RPM architectures
- fix #712992 - detect noarch RPM packages
- fix #688700 - detect s390 kernel
- fix #692098 - do not try to get coredump informations from normal binary
- fix #712988 - do not handle Python scripts as binary files
- fix #690801 - fixed grammar mistakes in man page
- fix #675691 - improve TeX recognition

* Wed Jan 26 2011 Jan Kaluza <jkaluza@redhat.com> 5.04-6
- fix #637782 - identify the zip64 format correctly
- fix #643046 - recognize volume_key escrow packets
- fix #594083 - improve Python recognition
- fix #608686 - mention return code in manpage
- fix #610795 - recognize webm content
- fix #670125 - don't identify GFS2 filesystems as GFS1 filesystems

* Fri Jun 11 2010 Jan Kaluza <jkaluza@redhat.com> 5.04-5
- removed excessive HTML/SGML "magic patterns"
  (#594605,#594624,#594636)

* Thu Apr 08 2010 Daniel Novotny <dnovotny@redhat.com> 5.04-4
- fix #580490 - "file" may trim too much of command line from core file

* Thu Mar 25 2010 Daniel Novotny <dnovotny@redhat.com> 5.04-3
- fix #576804 - pull "file" changes from Rawhide to Rhel6

* Wed Mar 24 2010 Daniel Novotny <dnovotny@redhat.com> 5.04-2
- fix #575178 - file command does not print separator 
  when --print0 option is used

* Wed Mar 10 2010 Daniel Novotny <dnovotny@redhat.com> 5.04-1
- rebase to 5.04 (#572155)

* Wed Feb 24 2010 Daniel Novotny <dnovotny@redhat.com> 5.03-14
- static library moved to new "-static" subpackage

* Fri Jan 22 2010 Daniel Novotny <dnovotny@redhat.com> 5.03-13
- fix #557608 -  RFE: add detection of Python 3 bytecode

* Mon Nov 30 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-12
- fix the patch for multilib (#515767) in Makefile.in

* Tue Nov 24 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-11
- BuildRequires automake because of the Makefile.am patch

* Fri Nov 13 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-10
- fix #537324 -  update spec conditional for rhel

* Tue Aug 25 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-9
- fix #515767 -  multilib: file /usr/share/misc/magic.mgc conflicts

* Thu Aug 06 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-8
- rebuild for #515767 -  multilib: file /usr/share/misc/magic.mgc conflicts

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-6
- fix #510429 -  file is confused by string "/* (if any) */" 
       in C header and claims it "Lisp/Scheme program text"

* Wed Jul 22 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-5
- #513079 -  RFE: file - recognize xfs metadump images

* Fri Jul 10 2009 Adam Jackson <ajax@redhat.com> 5.03-4
- Clean up %%description.

* Tue Jun 16 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-4
- one more PostScript font magic added (#505762),
  updated font patch

* Tue Jun 16 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-3
- added magic for three font issues (PostScript fonts)
  (#505758, #505759, #505765)

* Thu May 14 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-2
- fix #500739 - Disorganized magic* file locations in file-libs

* Mon May 11 2009 Daniel Novotny <dnovotny@redhat.com> 5.03-1
- new upstream version

* Tue May 05 2009 Daniel Novotny <dnovotny@redhat.com> 5.02-1
- new upstream version; drop upstreamed patches; this fixes #497913

* Wed Apr 29 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-8
- fix #498036 - Elang JAM file definition breaks detection of postscript-files

* Mon Apr 20 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-7
- fix previous patch:
  the name of the format is a bit different (MDUMP -> MDMP)

* Fri Apr 17 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-6
- fix #485835 (MDUMP files)

* Mon Mar 23 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-5
- added two font definitions (#491594, #491595)
  and a fix for file descriptor leak when MAGIC_COMPRESS used (#491596)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-3
- fix #486105 -  file-5.00-2.fc11 fails to recognise a file 
  (and makes rpmbuild fail)

* Mon Feb 16 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-2
- fix #485141 -  rpm failed while checking a French Word file

* Mon Feb 09 2009 Daniel Novotny <dnovotny@redhat.com> 5.00-1
- upgrade to 5.00
- drop upstreamed patches, rebase remaining patch

* Wed Jan 14 2009 Daniel Novotny <dnovotny@redhat.com> 4.26-9
- fix #476655 detect JPEG-2000 Code Stream Bitmap

* Mon Jan 12 2009 Daniel Novotny <dnovotny@redhat.com> 4.26-8
- fix #479300 - add btrfs filesystem magic

* Mon Dec 15 2008 Daniel Novotny <dnovotny@redhat.com> 4.26-7
- fix the LaTex issue in bz#474156

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.26-6
- Rebuild for Python 2.6

* Thu Dec 04 2008 Daniel Novotny <dnovotny@redhat.com> - 4.26-5
- fix #470811 - Spurious perl auto-requires

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.26-4
- Rebuild for Python 2.6

* Thu Oct 16 2008 Daniel Novotny <dnovotny@redhat.com> 4.26-3
- fix #465994 file --mime-encoding seems broken

* Tue Oct 07 2008 Daniel Novotny <dnovotny@redhat.com> 4.26-2
- fix #463809: rpmbuild rpmfcClassify: Assertion fails on some binary files
  (false positive test on "DOS device driver" crashed file(1)
   and rpmbuild(8) failed)  

* Mon Sep 15 2008 Daniel Novotny <dnovotny@redhat.com> 4.26-1
- new upstream version: fixes #462064

* Mon Jul 21 2008 Tomas Smetana <tsmetana@redhat.com> - 4.25-1
- new upstream version; drop upstreamed patches

* Fri Jun 06 2008 Tomas Smetana <tsmetana@redhat.com> - 4.24-4
- add GFS2 filesystem magic; thanks to Eric Sandeen
- add LVM snapshots magic (#449755); thanks to Jason Farrell

* Wed Jun 04 2008 Tomas Smetana <tsmetana@redhat.com> - 4.24-3
- drop patches that do nothing in recent build system
- create the text magic file during installation

* Tue Jun 03 2008 Tomas Smetana <tsmetana@redhat.com> - 4.24-2
- rebuild because of egg-info

* Tue Jun 03 2008 Tomas Smetana <tsmetana@redhat.com> - 4.24-1
- new upstream version

* Tue Mar 11 2008 Tomas Smetana <tsmetana@redhat.com> - 4.23-5
- fix EFI detection patch

* Fri Feb 01 2008 Tomas Smetana <tsmetana@redhat.com> - 4.23-4
- fix mismatching gzip files and text files as animations

* Fri Feb 01 2008 Tomas Smetana <tsmetana@redhat.com> - 4.23-3
- fix #430927 - detect ext4 filesystems

* Thu Jan 31 2008 Tomas Smetana <tsmetana@redhat.com> - 4.23-2
- fix #430952 - wrong handling of ELF binaries

* Tue Jan 29 2008 Tomas Smetana <tsmetana@redhat.com> - 4.23-1
- new upstream version; update patches; drop unused patches

* Thu Jan 24 2008 Tomas Smetana <tsmetana@redhat.com> - 4.21-5
- build a separate python-magic package; thanks to Terje Rosten

* Thu Dec 06 2007 Tomas Smetana <tsmetana@redhat.com> - 4.21-4
- add PE32/PE32+ magic

* Wed Aug 15 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.21-3
- resolves: #172015: no longer reports filename of crashed app when run on core files.
- resolves: #249578: Weird output from "file -i"
- resolves: #234817: file reports wrong filetype for microsoft word file

* Wed Jul  4 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.21-2
- resolves: #246700: RPM description isn't related to product
- resolves: #238789: file-devel depends on %%{version}
  but not on %%{version}-%%{release}
- resolves: #235267: for core files, file doesn't display the executable name

* Tue May 29 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.21-1
- upgrade to new upstream 4.21
- resolves: #241034: CVE-2007-2799 file integer overflow

* Wed Mar  7 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.20-1
- upgrade to new upstream 4.20

* Tue Feb 20 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.19-4
- rpath in file removal

* Mon Feb 19 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.19-3
- Resolves: #225750 - Merge Review: file

* Thu Jan 25 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.19-2
- Resolves: #223297 - file does not recognize OpenOffice "native" formats
- Resolves: #224344 - Magic rules should be in file-libs

* Tue Jan  9 2007 Martin Bacovsky <mbacovsk@redhat.com> - 4.19-1
- Resolves: #208880 - Pointless file(1) error message while detecting ELF 64-bit file
    thanks to <jakub@redhat.com> for patch
- Resolves: #214992 - file-devel should own %%_includedir/* %%_libdir/lib*.so
- Resolves: #203548 - a -devel package should be split out for libmagic
- upgrade to new upstream 4.19
- patch revision and cleaning
- split package to file, file-devel and file-libs

* Wed Aug 23 2006 Martin Bacovsky <mbacovsky@redhat.com> - 4.17-8
- fix recognition of perl script with embed awk (#203610) 

* Fri Aug 18 2006 Martin Bacovsky <mbacovsk@redhat.com> - 4.17-7
- fix recognition of bash script with embed awk (#202185)

* Thu Aug 03 2006 Martin Bacovsky <mbacovsk@redhat.com> - 4.17-6
- fix gziped empty file (#72986)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.17-5.1
- rebuild

* Mon Jul 10 2006 Radek Vokal <rvokal@redhat.com> 4.17-5
- fix powerpoint mine (#190373) <vonsch@gmail.com>

* Wed May 24 2006 Radek Vokal <rvokal@redhat.com> 4.17-4
- /usr/share/file is owned by package (#192858)
- fix magic for Clamav files (#192406)

* Fri Apr 21 2006 Radek Vokal <rvokal@redhat.com> 4.17-3
- add support for OCFS or ASM (#189017)

* Tue Mar 14 2006 Radek Vokal <rvokal@redhat.com> 4.17-2
- fix segfault when compiling magic
- add check for wctype.h
- fix for flac and mp3 files

* Mon Mar 13 2006 Radek Vokal <rvokal@redhat.com> 4.17-1
- upgrade to file-4.17, patch clean-up

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.16-6.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.16-6.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb 04 2006 Radek Vokal <rvokal@redhat.com> 4.16-6
- xen patch, recognizes Xen saved domain

* Fri Jan 13 2006 Radek Vokal <rvokal@redhat.com> 4.16-5
- fix for 64bit arrays

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 29 2005 Radek Vokal <rvokal@redhat.com> - 4.16-4
- printf utf8 filenames and don't use isprint() (#174348)

* Tue Nov 08 2005 Radek Vokal <rvokal@redhat.com> - 4.16-3
- remove .la files (#172633)

* Mon Oct 31 2005 Radek Vokal <rvokal@redhat.com> - 4.16-2
- fix core files output, show "from" (#172015)

* Tue Oct 18 2005 Radek Vokal <rvokal@redhat.com> - 4.16-1
- upgrade to upstream

* Mon Oct 03 2005 Radek Vokal <rvokal@redhat.com> - 4.15-4
- file output for Berkeley DB gains Cracklib (#168917)

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> - 4.15-3
- small fix in previously added patch, now it works for multiple params

* Mon Sep 19 2005 Radek Vokal <rvokal@redhat.com> - 4.15-2
- print xxx-style only once (#168617)

* Thu Aug 09 2005 Radek Vokal <rvokal@redhat.com> - 4.15-1
- upgrade to upstream 

* Tue Aug 09 2005 Radek Vokal <rvokal@redhat.com> - 4.14-4
- mime for mpeg and aac files fixed (#165323)

* Fri Aug 05 2005 Radek Vokal <rvokal@redhat.com> - 4.14-3
- mime for 3ds files removed, conflicts with text files (#165165)

* Fri Jul 22 2005 Radek Vokal <rvokal@redhat.com> - 4.14-2
- fixed mime types recognition (#163866) <mandriva.org>

* Thu Jul 14 2005 Radek Vokal <rvokal@redhat.com> - 4.14-1
- sync with upstream, patch clean-up

* Mon Jul 04 2005 Radek Vokal <rvokal@redhat.com> - 4.13-5
- fixed reiserfs check (#162378)

* Mon Apr 11 2005 Radek Vokal <rvokal@redhat.com> - 4.13-4
- check Cyrus files before Apple Quicktime movies (#154342) 

* Mon Mar 07 2005 Radek Vokal <rvokal@redhat.com> - 4.13-3
- check for shared libs before fs dump files (#149868)

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> - 4.13-2
- gcc4 rebuilt

* Tue Feb 15 2005 Radek Vokal <rvokal@redhat.com> - 4.13-1
- new version, fixing few bugs, patch clean-up
- consistent output for bzip files (#147440)

* Mon Jan 24 2005 Radek Vokal <rvokal@redhat.com> - 4.12-3
- core64 patch fixing output on core files (#145354) <kzak@redhat.com>
- minor change in magic patch

* Mon Jan 03 2005 Radek Vokal <rvokal@redhat.com> - 4.12-2
- fixed crashes in threaded environment (#143871) <arjanv@redhat.com>

* Thu Dec 02 2004 Radek Vokal <rvokal@redhat.com> - 4.12-1
- upgrade to file-4.12
- removed Tim's patch, tuned magic patch

* Sat Nov 20 2004 Miloslav Trmac <mitr@redhat.com> - 4.10-4
- Convert libmagic.3 to UTF-8

* Thu Nov 18 2004 Radek Vokal <rvokal@redhat.com> 4.10-3
- set of patches from debian.org
- new magic types (#128763)
- zlib added to BuildReq (#125294)

* Tue Oct 12 2004 Tim Waugh <twaugh@redhat.com> 4.10-2
- Fixed occasional segfault (bug #131892).

* Wed Aug 11 2004 Radek Vokal <rvokal@redhat.com>
- zlib patch deleted, note patch deleted, rh patch updated, debian patch updated
- upgrade to file-4.10

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 10 2004 Jakub Jelinek <jakub@redhat.com>
- fix ELF note handling (#109495)

* Tue Mar 23 2004 Karsten Hopp <karsten@redhat.de> 4.07-3 
- add docs (#115966)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Jan 18 2004 Jeff Johnson <jbj@jbj.org> 4.07-1
- upgrade to 4.07.
- deal gracefully with unreadable files (#113207).
- detect PO files (from Debian).

* Tue Dec 16 2003 Jeff Johnson <jbj@jbj.org> 4.06-1
- upgrade to file-4.06.

* Mon Nov 10 2003 Tim Waugh <twaugh@redhat.com> 4.02-4
- Minimal fix for busy loop problem (bug #109495).

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 4.05-1
- upgrade to 4.05.

* Thu Oct  9 2003 Jeff Johnson <jbj@jbj.org> 4.02-3
- use zlib rather than exec'ing gzip.

-* Thu Aug 28 2003 Dan Walsh <dwalsh@redhat.com>
-- Add Selinux support.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat May 24 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add ldconfig to post/postun

* Mon Apr 21 2003 Jeff Johnson <jbj@redhat.com> 4.02-1
- upgrade to file-4.02.

* Thu Feb 27 2003 Jeff Johnson <jbj@redhat.com> 3.39-9
- check size read from elf header (#85297).

* Tue Feb 18 2003 Matt Wilson <msw@redhat.com> 3.39-8
- add FHS compatibility symlink from /usr/share/misc/magic -> ../magic
  (#84509)

* Fri Feb 14 2003 Jeff Johnson <jbj@redhat.com> 3.39-7
- the "real" fix to the vorbis/ogg magic details (#82810).

* Mon Jan 27 2003 Jeff Johnson <jbj@redhat.com> 3.39-6
- avoid vorbis/ogg magic details (#82810).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 3.39-5
- rebuilt

* Sun Jan 12 2003 Nalin Dahyabhai <nalin@redhat.com> 3.39-4
- PT_NOTE, take 3

* Fri Jan 10 2003 Nalin Dahyabhai <nalin@redhat.com> 3.39-3
- don't barf in ELF headers with align = 0

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 3.39-2
- don't get lost when looking at PT_NOTE sections

* Sat Oct 26 2002 Jeff Johnson <jbj@redhat.com> 3.39-1
- update to 3.39.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May  6 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.37-6
- Don't use an old magic.mime 
- Add mng detection (#64229)

* Tue Feb 26 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.37-5
- Rebuild

* Mon Jan 14 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.37-4
- Fix missing include of <stdint.h> (#58209)

* Tue Dec 11 2001 Trond Eivind Glomsrød <teg@redhat.com> 3.37-2
- Add CFLAGS to handle large files (#53576)

* Mon Dec 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 3.37-1
- 3.37
- s/Copyright/License/
- build with --enable-fsect-man5, drop patch
- disable two old patches

* Fri Jul 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- revert a patch to Magdir/elf, which breaks many libtool scripts
  in several rpm packages

* Mon Jun 25 2001 Crutcher Dunnavant <crutcher@redhat.com>
- iterate to 3.35

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Sun Nov 26 2000 Jeff Johnson <jbj@redhat.com>
- update to 3.33.

* Mon Aug 14 2000 Preston Brown <pbrown@redhat.com>
- Bill made the patch but didn't apply it. :)

* Mon Aug 14 2000 Bill Nottingham <notting@redhat.com>
- 'ASCII text', not 'ASCII test' (#16168)

* Mon Jul 31 2000 Jeff Johnson <jbj@redhat.com>
- fix off-by-1 error when creating filename for use with -i.
- include a copy of GNOME /etc/mime-types in %%{_datadir}/magic.mime (#14741).

* Sat Jul 22 2000 Jeff Johnson <jbj@redhat.com>
- install magic as man5/magic.5 with other formats (#11172).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Wed Jun 14 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue Apr 14 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 3.30

* Wed Feb 16 2000 Cristian Gafton <gafton@redhat.com>
- add ia64 patch from rth

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages
- update to 3.28

* Mon Aug 23 1999 Jeff Johnson <jbj@redhat.com>
- identify ELF stripped files correctly (#4665).
- use SPARC (not sparc) consistently throughout (#4665).
- add entries for MS Office files (#4665).

* Thu Aug 12 1999 Jeff Johnson <jbj@redhat.com>
- diddle magic so that *.tfm files are identified correctly.

* Tue Jul  6 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.27.

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- experimental support for realmedia files added

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binary.

* Fri Nov 27 1998 Jakub Jelinek <jj@ultra.linux.cz>
- add SPARC V9 magic.

* Tue Nov 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.26.

* Mon Aug 24 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.25.
- detect gimp XCF versions.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.24
- buildrooted

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 31 1997 Erik Troan <ewt@redhat.com>
- Fixed problems caused by 64 bit time_t.

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Improved recognition of Linux kernel images.
