%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_ver: %define python_ver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name: python-linux-procfs
Version: 0.4.9
Release: 5%{?dist}
License: GPLv2
Summary: Linux /proc abstraction classes
Group: System Environment/Libraries
Source: http://userweb.kernel.org/~acme/python-linux-procfs/%{name}-%{version}.tar.bz2
URL: http://userweb.kernel.org/~acme/python-linux-procfs
BuildArch: noarch
BuildRequires: python-devel
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Patch1: pidstats-fix-documentation-indentation.patch
Patch2: fix-parse_affinity-for-CPU-numbers-greater-than-31.patch

%description
Abstractions to extract information from the Linux kernel /proc files.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -p -m755 pflags-cmd.py %{buildroot}%{_bindir}/pflags

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/pflags
%{python_sitelib}/procfs/
%defattr(0644,root,root,0755)
%if "%{python_ver}" >= "2.5"
%{python_sitelib}/*.egg-info
%endif
%doc COPYING

%changelog
* Mon Sep 12 2016 John Kacur <jkacur@gmail.com> - 0.4.9-5
- fix parse_affinity for CPU numbers greater than 31
Resolves: rhbz#1374804

* Fri Mar 11 2016 John Kacur <jkacur@gmail.com> - 0.4.9-4
- Add specfile changes to install pflags (utility to print processor flags)
Resolves: rhbz#1255725

* Wed Nov 11 2015 John Kacur <jkacur@redhat.com> - 0.4.9-3
- pidstats-fix-documentation-indentation
Resolves: rhbz#1065076

* Fri Nov 06 2015 John Kacur <jkacur@redhat.com> - 0.4.9-2
- Update to upstream version 0.4.9
Resolves: rhbz#1255725

* Thu Oct  8 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.9-1
- Adds documentations to classes, more work to do on methods
- Fixes parsing of users in /proc/interrupts users field
- Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=1245677

* Tue Jun 23 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.8-1
- Support spaces in COMM names
- Fixes: https://bugzilla.redhat.com/show_bug.cgi?id=1232394

* Thu Jun 11 2015 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.7-1
- Fix pidstat.process_flag()
- Introduce pflags utility
- Parse IRQ affinities for !root
- Add PF_NO_SETAFFINITY const

* Tue Sep 2 2014 John Kacur <jkacur@redhat.com> - 0.4.6-3
- Rebased to python-linux-procfs-0.4.6
- Resolves: rhbz#1133700

* Wed Jun  5 2013 Jiri Kastner <jkastner@redhat.com> - 0.4.6-1
- support for parsing cgroups
- support for parsing environ variables

* Mon Oct 1 2012 John Kacur <jkacur@redhat.com> - 0.4.5-2
- Rebuilt for rhel6.4
- Resolves: rhbz#858814

* Mon May 10 2010 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.5-1
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=577365

* Tue Feb 10 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.4-1
- Even more fixes due to the fedora review process

* Mon Feb  9 2009 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.3-1
- Fixups due to the fedora review process

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4.2-1
- interrupts: Add find_by_user_regex
- process: Always set the "cmdline" array, even if empty
- pidstats: Remove dead processes in find_by_name()
- pidstats: Add process class to catch dict references for late parsing
- pidstats: Move the /proc/PID/{stat,status} parsing to classes
- pidstats: Introduce process_flags method

* Tue Aug 12 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.4-1
- Per process flags needed by tuna

* Fri Jun 13 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.3-1
- Support CPU hotplug

* Mon Feb 25 2008 Arnaldo Carvalho de Melo <acme@redhat.com> - 0.1-1
- package created
