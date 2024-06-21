Name:           libmnl
Version:        1.0.2
Release:        3%{?dist}
Summary:        A minimalistic Netlink library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://netfilter.org/projects/libmnl
Source0:        http://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
libmnl is a minimalistic user-space library oriented to Netlink developers.
There are a lot of common tasks in parsing, validating, constructing of both
the Netlink header and TLVs that are repetitive and easy to get wrong.
This library aims to provide simple helpers that allows you to re-use code and
to avoid re-inventing the wheel.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so


%changelog
* Wed Feb 15 2012 Thomas Woerner <twoerner@redhat.com> 1.0.2-3
- dropped examples from devel sub package to make build multilib clean.

* Fri Feb 10 2012 Thomas Woerner <twoerner@redhat.com> 1.0.2-2
- adapted for RHEL-6: added clean tag, BuildRoot, defattrs

* Sat Feb 04 2012 Hushan Jia <hushan.jia@gmail.com> 1.0.2-1
- Update to 1.0.2.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 24 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-4
- fix require of devel package
- add example source files to docs

* Wed Aug 24 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-3
- remove unnecessary buildroot and defattr tags
- remove unnecessary build requires

* Sat Aug 20 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-2
- use upstream released source tarball

* Sat Aug 20 2011 Hushan Jia <hushan.jia@gmail.com> 1.0.1-1
- initial packaging

