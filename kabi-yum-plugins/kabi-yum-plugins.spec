Name:		kabi-yum-plugins
Version:	1.0
Release:	2%{?dist}
Summary:	The CentOS Linux kernel ABI yum plugin

Group:		System Environment/Kernel
License:	GPLv2
URL:		http://www.redhat.com/
Source0:	kabi-yum-plugins-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python
Requires:	kabi-whitelists
Requires:	python
Requires:	yum >= 3.2.25-12

%description
The kABI yum plugins package contains a yum plugin that can be used in order
to enforce that only those third party kernel module packages meeting 
kernel ABI requirements are installed. The plugin requires that those drivers
be packaged in accordance with Red Hat Driver Update Program guidelines.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib/yum-plugins/kabi.*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/kabi.conf

%changelog
* Wed Jul  6 2011 Karanbir Singh <kbsingh@centos.org> - 1.0-2.el6.centos
- Remove text that might imply the user is not using CentOS
- Retain reference to the standard used for Driver handling

* Wed May 12 2010 Jon Masters <jcm@redhat.com> - 1.0-2
- Initial public build of kabi yum plugin package
- Resolves: #591463
