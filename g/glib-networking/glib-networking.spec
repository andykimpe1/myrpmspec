%define glib2_version 2.28

Name:           glib-networking
Version:        2.28.6.1
Release:        2.4%{?dist}
Summary:        Networking support for GLib

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org
Source:         http://download.gnome.org/sources/glib-networking/2.28/%{name}-%{version}.tar.bz2
Requires:       ca-certificates

BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  libproxy-devel
BuildRequires:  gnutls-devel
BuildRequires:  intltool
BuildRequires:  ca-certificates

Patch0: rh1101418-no-gnome-proxy.patch
Patch1: rh1101418-libproxy-0.3.0.patch
Patch2: rh1176719-priority-string.patch
Patch3: rh1410438-handshake-crash.patch

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains a libproxy-based GProxyResolver
implementations and a gnutls-based GTlsConnection implementation.

%prep
%setup -q
%patch0 -p1 -b .no-gnome-proxy
%patch1 -p1 -b .libproxy-0.3.0
# Backport of https://git.gnome.org/browse/glib-networking/commit/?id=f474ec2
%patch2 -p1 -b .no-ssl3-client-version
%patch3 -p1 -b .handshake-crash


%build
%configure --with-libproxy --without-gnome-proxy

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/*.la

%find_lang %{name}

%post
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules

%postun
gio-querymodules-%{__isa_bits} %{_libdir}/gio/modules

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libdir}/gio/modules/libgiognutls.so
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service


%changelog
* Mon Jan  9 2017 Dan Winship <danw@redhat.com> - 2.28.6.1-2.4
- Fix a crash in gnome-panel (#1410438)

* Fri Oct 14 2016 Tomas Popela <tpopelaw@redhat.com> - 2.28.6.1-2.3
- gnutls: update default priority string and fallback rules
- Resolves: rhbz#1176719

* Mon Jul 14 2014 Dan Winship <danw@redhat.com> - 2.28.6.1-2.2
- Add minimum glib2 version to BuildRequires (#1119162)

* Mon Jun  9 2014 Dan Winship <danw@redhat.com> - 2.28.6.1-2.1
- Disable GNOME proxy support since RHEL6 doesn't have gsettings-desktop-schemas
- Allow building with libproxy 0.3.0

* Wed Apr 27 2011 Dan Winship <danw@redhat.com> - 2.28.6.1-2
- Require gsettings-desktop-schemas, for GNOME proxy support

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6.1-1
- Update to 2.28.6.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.6-1
- Update to 2.28.6

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.5-1
- Update to 2.28.5

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.4-1
- Update to 2.28.4

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Dan Winship <danw@redhat.com> - 2.27.90-1
- Update to 2.27.90, including TLS support

* Mon Nov  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.25.0-1
- Initial packaging
