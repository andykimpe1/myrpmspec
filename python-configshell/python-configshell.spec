# Copyright 2011, Red Hat

%global oname configshell-fb

Name:           python-configshell
License:        AGPLv3
Group:          System Environment/Libraries
Summary:        A framework to implement simple but nice CLIs
Epoch:          1
Version:        1.1.fb4
Release:        1%{?dist}
URL:            https://github.com/agrover/configshell-fb
Source:         https://github.com/agrover/%{oname}/tarball/v%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel epydoc python-simpleparse python-urwid
Requires: python-simpleparse python-urwid

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup -q -n agrover-%{oname}-0deef22

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}
%doc COPYING README

%changelog
* Tue Jan 10 2012 Andy Grover <agrover@redhat.com> - 1:1.1.fb4-1
- New upstream release

* Tue Dec 14 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb3-1
- New upstream release

* Tue Dec 13 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb2-1
- New upstream release

* Tue Dec 6 2011 Andy Grover <agrover@redhat.com> - 1:1.1.fb1-1
- New upstream source and release
- Remove patches:
  * python-configshell-remove-epydoc-dep.patch
  * python-configshell-git-version.patch

* Mon Nov 21 2011 Andy Grover <agrover@redhat.com> - 1:1.1-2
- Properly update changelog
- Sync version with upstream, Epoch used
- Change Source URL to intermediate github repo

* Fri Sep 23 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-5
* Rebuild

* Thu Aug 25 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-4
- Add patch
  - python-configshell-remove-epydoc-dep.patch

* Wed Aug 17 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-3
- Address comments from spec review
  - drop examples/myshell from doc, it hasn't been updated for API change
  - Fully document procedure to generate source .tar.gz
  - Remove "." from summary
  - Remove commented-out spec todos and other cruft

* Mon Aug 1 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-2
- Update to latest git version
- Add urwid builddep

* Tue May 10 2011 Andy Grover <agrover@redhat.com> - 1.99.1.git987b63b-1
- Initial packaging
