Name: btparser
Version: 0.17
Release: 2%{?dist}
Summary: Parser and analyzer for backtraces produced by GDB
Group: Development/Libraries
License: GPLv2+
URL: http://fedorahosted.org/btparser
Source0: https://fedorahosted.org/released/btparser/btparser-%{version}.tar.xz
Patch0: btparser-rhbz#811147.patch
Patch1: btparser-rhbz#803774.patch
Patch2: btparser-rhbz#903140.patch
Patch3: btparser-rhbz#905854.patch
BuildRequires: python-devel
# Autoconf is required by btparser-rhbz#811147.patch
BuildRequires: autoconf

%description
Btparser is a backtrace parser and analyzer, which works with
backtraces produced by the GNU Project Debugger. It can parse a text
file with a backtrace to a tree of C structures, allowing to analyze
the threads and frames of the backtrace and work with them.

Btparser also contains some backtrace manipulation and extraction
routines:
- it can find a frame in the crash-time backtrace where the program
  most likely crashed (a chance is that the function described in that
  frame is buggy)
- it can produce a duplication hash of the backtrace, which helps to
  discover that two crash-time backtraces are duplicates, triggered by
  the same flaw of the code
- it can "rate" the backtrace quality, which depends on the number of
  frames with and without the function name known (missing function
  name is caused by missing debugging symbols)

%package devel
Summary: Development libraries for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%package python
Summary: Python bindings for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python
Python bindings for %{name}.

%prep
%setup -q
%patch0 -p1 -b.811147
%patch1 -p1 -b.803774
%patch2 -p1 -b.903140
%patch3 -p1 -b.905854

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -regex ".*\.la$" | xargs rm -f --

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README NEWS COPYING TODO ChangeLog
%{_bindir}/btparser
%{_mandir}/man1/%{name}.1.gz
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files python
%dir %{python_sitearch}/%{name}
%{python_sitearch}/%{name}/*

%changelog
* Mon Jun 10 2013 Martin Milata <mmilata@redhat.com> - 0.17-2
- Backport commit ec1bf395 that fixes several memory leaks
- Backport abf036d5 that fixes a NULL dereference
- Backport 6e0f49a3 that adds version to the manual page
- Resolves: #803774, #903140, #905854

* Wed Aug 08 2012 Jiri Moskovcak <jmoskovc@redhat.com> - 0.17-1
- New upstream release
- Resolves: #846667

* Mon May  7 2012 Karel Klíč <kklic@redhat.com> - 0.16-3
- Report correct crash_function in the crash sumary
  Resolves: rhbz#811147

* Wed Feb  8 2012 Karel Klíč <kklic@redhat.com> - 0.16-1
- New upstream release
  Resolves: #768377

* Mon May 16 2011 Karel Klíč <kklic@redhat.com> - 0.13-1
- Initial packaging
