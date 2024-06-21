%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define srcname Markdown

Name:           python-markdown
Version:        2.0.1
Release:        4%{?dist}
Summary:        Markdown implementation in Python
Group:          Development/Languages
License:        BSD
URL:            http://www.freewisdom.org/projects/python-markdown/
Source0:        http://pypi.python.org/packages/source/M/%{srcname}/%{srcname}-%{version}.tar.gz
# Fix issues with angle brackets recognition in HTML parser
# First with only one angle bracket '<' - https://github.com/waylan/Python-Markdown/commit/de949d2af47b9a094ace82ed64f810aaff7d3ac7
# Second with empty angle brackets '<>' - https://github.com/waylan/Python-Markdown/commit/07bc7a4c8f2e834e0f8150de004c1f8fd98a3d60
# Resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1020170
Patch0:         fix-raw-html-recongition.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-devel
%if 0%{?rhel} && 0%{?rhel} < 6
BuildRequires:  python-elementtree
Requires:       python-elementtree
%endif


%description
This is a Python implementation of John Gruber's Markdown. It is
almost completely compliant with the reference implementation, though
there are a few known issues.


%prep
%setup -q -n %{srcname}-%{version}

%patch0 -p0

# remove shebangs
find markdown -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc docs/*
%{python_sitelib}/*
%{_bindir}/markdown


%changelog
* Wed Nov 02 2016 Lumír Balhar <lbalhar@redhat.com> - 2.0.1-4
- Added patch to fix recognition of empty angle brackets as raw html
Resolves: rhbz#1020170

* Tue Dec  1 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.1-3.1
- Fix conditional for RHEL

* Thu Aug 27 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-3
- Add requirement on python-elementtree, which was a separate package
  before Python 2.5.
- Re-add changelog entries accidentally removed earlier.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-1
- Update to 2.0.1.
- Upstream stripped .py of the cmdline script.

* Sat Apr 25 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-1
- Update to 2.0.
- Adjusted source URL.
- License changed to BSD only.
- Upstream now provides a script to run markdown from the cmdline.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.7-2
- Rebuild for Python 2.6

* Mon Aug  4 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.7-1
- New package.
