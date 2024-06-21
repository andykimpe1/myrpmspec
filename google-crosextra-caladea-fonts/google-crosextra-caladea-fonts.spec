%global fontname google-crosextra-caladea
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global archivename crosextrafonts-20130214

Name:           %{fontname}-fonts
Version:        1.002
Release:        0.3.20130214%{?dist}.1
Summary:        Serif font metric-compatible with Cambria font

Group:          User Interface/X
# License added in font as "otfinfo -i Caladea-Regular.ttf | grep License"
# also from http://code.google.com/p/chromium/issues/detail?id=280557
License:        ASL 2.0
URL:            http://code.google.com/p/chromium/issues/detail?id=168879
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        30-0-%{fontname}-fontconfig.conf
Source2:        62-%{fontname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Caladea is metric-compatible with Cambria font. This font is a serif
typeface family based on Lato.

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-fontconfig.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-fontconfig.conf

ln -s %{_fontconfig_templatedir}/%{fontconf30}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf30}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf62}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf62}-fontconfig.conf


%_font_pkg -f *-%{fontname}-fontconfig.conf *.ttf

%doc


%changelog
* Fri Apr 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.002-0.3.20130214.el6.1
- bump the release tag for EPEL6 to RHEL6 update

* Wed Jan 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.002-0.3.20130214
- Resolves:rh#1056029 - Fontconfig and summary required fixes

* Tue Oct 15 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.002-0.2.20130214
- Added license information in comments

* Thu Oct 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.002-0.1.20130214
- Initial Fedora release.

