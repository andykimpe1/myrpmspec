%global pypi_name jsonpatch
%global github_name python-json-patch
%global commit f6f3cd235337209fc96b71316215a40d1cd3026c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        1.2
Release:        4%{?dist}
Summary:        Applying JSON Patches in Python

License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
#Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# pypi tarball does not contain README.md and tests.py
Source0:        https://github.com/stefankoegl/%{github_name}/archive/%{commit}/%{github_name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-jsonpointer
Requires:       python-jsonpointer

%description
Library to apply JSON Patches according to RFC 6902.

%prep
%setup -qn %{github_name}-%{commit}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} tests.py

%files
%doc README.md COPYING
%{python_sitelib}/%{pypi_name}.py*
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Feb 20 2017 Tomas Orsava <torsava@redhat.com> - 1.2-4
- Bumping release so this RHEL-6 package obsoletes the one in epel6

* Tue Oct 15 2013 Alan Pevec <apevec@gmail.com> - 1.2-2
- add runtime dep on jsonpointer

* Fri Oct 11 2013 Alan Pevec <apevec@gmail.com> - 1.2-1
- Update to 1.2

* Fri Sep 13 2013 Alan Pevec <apevec@gmail.com> - 1.1-2
- review feedback: move %%check section, add missing build requirements

* Mon Jul 01 2013 Alan Pevec <apevec@gmail.com> - 1.1-1
- Initial package.
