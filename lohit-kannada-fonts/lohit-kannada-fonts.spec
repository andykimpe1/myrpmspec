%global fontname lohit-kannada
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.5
Release:        6%{?dist}
Summary:        Free Kannada font

Group:          User Interface/X
License:        GPLv2 with exceptions
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Patch1: bug-578032.patch
Patch2: bug-577127.patch
Patch3: bug-577127-1.patch
Patch4: bug-691289.patch
Patch5: bug-603415.patch
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Kannada truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fix-font-conf
%patch2 -p1 -b .2-increase-kerning
%patch3 -p1 -b .3-handline-zwj
%patch4 -p1 -b .4-added-rupee-symbol
%patch5 -p1 -b .5-resolved-character-cut

%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Tue Jan 24 2012 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- Resolves: bug 603415

* Tue Jul 05 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- Resolves: bug 691289

* Thu Jan 20 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- Resolves: bug 577127
- will work when, zwj processing will be fixed in pango

* Mon Oct 18 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- fixed bug 577127

* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- Resolves: bug 586857

* Tue Mar 30 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- Resolves: bug 577128
- Resolves: bug 577127

* Mon Dec 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- fixed bug 548686, license field
- Resolves: bug 550991

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.4-2.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
