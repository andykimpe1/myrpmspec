Summary: Browser default start page for CentOS
Name: centos-indexhtml
Version: 6
Release: 2%{?dist}
Source: %{name}-%{version}.tar.gz
License: Distributable
Group: Documentation
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1
Provides: redhat-indexhtml

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed CentOS Linux

%prep
%setup -q -n HTML

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Fri Oct 24 2014 Johnny Hughes <johnny@centos.org> - 6-2.el6.centos
- Updated Branding

* Wed Jun 29 2011 Karanbir Singh <kbsingh@centos.org> 6-1.el6.centos
- Roll in CentOS Branding
