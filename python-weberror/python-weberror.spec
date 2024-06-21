%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-weberror
Version:        0.10.2
Release:        2%{?dist}
Summary:        Web Error handling and exception catching middleware

Group:          Development/Languages
# JQuery and its javascript plugins are licensed MIT or GPLv2
# weberror/collector.py has portions copyrighted as ZPLv2.0
# Everything else is licensed MIT
License: MIT and ZPLv2.0 and (MIT or GPLv2)
URL:            http://pypi.python.org/pypi/WebError
Source0:        http://pypi.python.org/packages/source/W/WebError/WebError-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose
BuildRequires:  python-webob
BuildRequires:  python-webtest
BuildRequires:  python-paste
BuildRequires:  python-pygments
BuildRequires:  python-tempita
BuildRequires:  python-simplejson

Requires:       python-webob
Requires:       python-tempita
Requires:       python-pygments
Requires:       python-simplejson

Patch0: bz746118-Fix-immediate-error-in-hash_identifier-in-case-of-FIPS.patch

%description
WebError is WSGI middleware that performs error handling and exception
catching.

%prep
%setup -q -n WebError-%{version}
%patch0 -p1 -b .bz746118
find . -type f -name ._\* -exec rm -f {} \;
%{__chmod} 0644 WebError.egg-info/*


%build
%{__python} setup.py build


%check
nosetests


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

 
%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENSE
%{python_sitelib}/weberror/
%{python_sitelib}/*.egg-info


%changelog
* Mon Aug 5 2013 Jan Pokorny <jpokorny@redhat.com> - 0.10.2-2
- Fix immediate error in hash_identifier in case of FIPS mode
Resolves: rhbz#746118
Related:  rhbz#956360

* Wed Jul 14 2010 David Malcolm <dmalcolm@redhat.com> - 0.10.2-1
- Update to 0.10.2
- Fix license tag
Resolves: rhbz#608729

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Ricky Zhou <ricky@fedoraproject.org> - 0.10.1-3
- Change define to global.
- Remove unnecessary BuildRequires on python-devel.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.10.1-1
- Update to 0.10.1
- Remove the wsgiref patch

* Wed Oct 22 2008 Luke Macken <lmacken@redhat.com> - 0.9-3
- Add python-{paste,pygments,tempita,simplejson} to the BuildRequires
- Add python-{tempita,pygments,simplejson} to the Requires

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 0.9-2
- Add a patch to remove the wsgiref requirement, as it is now in Python2.5

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 0.9-1
- Update to 0.9
- Add python-tempita to the BuildRequires

* Thu Jul 17 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.8-3
- Update Requires for python-webob rename.
- Add BuildRequires on python-webob and python-webtest.

* Mon Jul 07 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.8-2
- Add %%check section.

* Sat Jun 14 2008 Ricky Zhou <ricky@fedoraproject.org> - 0.8-1
- Initial RPM Package.
