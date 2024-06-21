Summary: Convert filename encodings
Name: convmv
Version: 1.15
Release: 2%{?dist}

License: GPLv2 or GPLv3
URL: http://j3e.de/linux/convmv
Source0: http://j3e.de/linux/convmv/convmv-%{version}.tar.gz
BuildArch: noarch

%description
This package contains the tool convmv with which you can convert the encodings
of filenames, e.g. from Latin1 to UTF-8.

%prep
%setup -q
tar -xf testsuite.tar
# This is needed to preserve the timestamp of convmv file
sed -i 's/install/install -p/g' Makefile

%build
make %{_smp_mflags}

%check
make test

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install

%files
%doc CREDITS Changes GPL2 TODO
%{_bindir}/convmv
%{_mandir}/man*/*

%changelog
* Wed May 28 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.15-2
- Follow the recent packaging guideline changes

* Wed Sep 11 2013 Nils Philippsen <nils@redhat.com> - 1.15-1
- version 1.15
- reenable testsuite
- fix bogus dates in changelog

* Tue Mar 03 2009 Nils Philippsen <nils@redhat.com> - 1.14-1
- version 1.14
- temporarily disable "make test" to work around problems in koji

* Mon Feb 25 2008 Nils Philippsen <nphilipp@redhat.com> - 1.12-1
- version 1.12
- remove obsolete tests patch
- don't run md5sum against MD5sums as it lists a non-existing .MD5sums file
  which causes md5sum to error out
- change license tag to "GPLv2 or GPLv3"

* Thu Sep 27 2007 Nils Philippsen <nphilipp@redhat.com> - 1.10-3
- don't expect find output to be sorted, move "make test" to %%check (#237687,
  patch by Giuseppe Bonacci)
- change license tag to "GPLv2"

* Mon Aug 28 2006 Nils Philippsen <nphilipp@redhat.com> - 1.10-2
- FC6 mass rebuild

* Wed Aug 16 2006 Nils Philippsen <nphilipp@redhat.com> - 1.10-1
- version 1.10
- use dist tag

* Fri Mar 10 2006 Nils Philippsen <nphilipp@redhat.com>
- version 1.09

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jan 14 2005 Warren Togami <wtogami@redhat.com>
- remove testsuite.tar from doc

* Fri Jan 14 2005 Nils Philippsen <nphilipp@redhat.com>
- version 1.08

* Sat Feb 07 2004 Nils Philippsen <nphilipp@redhat.com>
- version 1.07
- initial build
