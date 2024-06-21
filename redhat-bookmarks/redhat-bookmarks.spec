Name:           redhat-bookmarks
Version:        6
Release:        1%{?dist}
Summary:        CentOS Linux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.centos.org
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for CentOS Linux

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Wed Jun 29 2011 Karanbir Singh <kbsingh@centos.org> 6-1.el6.centos
- Roll in CentOS branding (#4589, fpee)

* Tue Aug  3 2010 Christopher Aillon <caillon@redhat.com> 6-1
- Update for RHEL 6

* Fri Jan 29 2010 Christopher Aillon <caillon@redhat.com> 6-0
- Initial SRPM

