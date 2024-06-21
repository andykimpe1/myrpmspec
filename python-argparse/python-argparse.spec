%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global oname  argparse

Summary:       Optparse inspired command line parser for Python
Name:          python-argparse
Version:       1.2.1
Release:       2.1%{?dist}
License:       Python
Group:         Development/Languages
URL:           http://code.google.com/p/argparse/
Source0:       http://argparse.googlecode.com/files/argparse-%{version}.tar.gz
BuildRequires: python-setuptools
BuildRequires: dos2unix
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

The argparse module is an optparse-inspired command line parser that
improves on optparse by:
 * handling both optional and positional arguments
 * supporting parsers that dispatch to sub-parsers
 * producing more informative usage messages
 * supporting actions that consume any number of command-line args
 * allowing types and actions to be specified with simple callables 
    instead of hacking class attributes like STORE_ACTIONS or CHECK_METHODS 

as well as including a number of other more minor improvements on the
optparse API.

%prep
%setup -q -n %{oname}-%{version}
dos2unix -k README.txt NEWS.txt
%{__rm} -rf doc/source

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%check
pushd test
PYTHONPATH=../ %{__python} test_%{oname}.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc README.txt LICENSE.txt NEWS.txt doc/*
%{python_sitelib}/*

%changelog
* Tue Sep 11 2012 Alan Pevec <apevec@redhat.com> 1.2.1-2.1
- Import to RHEL 6.4 (rhbz#851798)

* Wed Jun 29 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-2
- Include LICENSE.txt file

* Wed Jun 29 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.1-1
- New compatble upstream with some bugfixes and a GPL2 vompatible license
- Enable test suite

* Wed Feb 10 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-1.1
- First build for EL-5
- Small change to %%files section so lack of egg-info on EL-5 is okay.

* Sun Dec 06 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1
- Ship more docs
- Project has moved
- Disable test for now
- Change license to Apache 2.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-2
- fixes from review, thanks Jussi!

* Sat Jan 17 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.8.0-1
- initial build

