%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-repoze-who
Version:        1.0.18
Release:        1%{?dist}
Summary:        An identification and authentication framework for WSGI

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/pypi/repoze.who
Source0:        http://pypi.python.org/packages/source/r/repoze.who/repoze.who-%{version}.tar.gz
Patch0:         %{name}-setup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel python-setuptools-devel

# Needed for test suite:
BuildRequires:  python-nose
BuildRequires:  python-paste
BuildRequires:  python-zope-interface

Requires:       python-paste
Requires:       python-setuptools
Requires:       python-zope-interface

%description
repoze.who is an identification and authentication framework for arbitrary WSGI
applications.  It acts as WSGI middleware.

repoze.who is inspired by Zope 2's Pluggable Authentication Service (PAS) (but
repoze.who is not dependent on Zope in any way; it is useful for any WSGI
application).  It provides no facility for authorization (ensuring whether a
user can or cannot perform the operation implied by the request).  This is
considered to be the domain of the WSGI application.


%prep
%setup -q -n repoze.who-%{version}
%patch0 -b .setup


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%check
nosetests -v

%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt
%{python_sitelib}/*


%changelog
* Wed Mar 28 2012 David Malcolm <dmalcolm@redhat.com> - 1.0.18-1
- rebase to 1.0.18
Resolves: rhbz#639075
- add a %%check phase, running the upstream test suite

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Luke Macken <lmacken@redhat.com> - 1.0.13-1
- Update to the latest upstream release.

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 1.0.7-1
- Initial package
