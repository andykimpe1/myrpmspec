%global fontname google-crosextra-carlito
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global archivename crosextrafonts-carlito-20130920

Name:           %{fontname}-fonts
Version:        1.103
Release:        0.1.20130920%{?dist}.1
Summary:        Sans-serif font metric-compatible with Calibri font

Group:          User Interface/X
License:        OFL
URL:            http://code.google.com/p/chromium/issues/detail?id=280557
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        30-0-%{fontname}-fontconfig.conf
Source2:        62-%{fontname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Carlito is metric-compatible with Calibri font. Carlito comes in regular, bold,
italic, and bold italic. The family covers Latin-Greek-Cyrillic (not a 
complete set, though) with about 2,000 glyphs. It has the same character 
coverage as Calibri. This font is sans-serif typeface family based on Lato.

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

%doc LICENSE


%changelog
* Fri Apr 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.103-0.1.20130920.el6.1
- bump the release tag for EPEL6 to RHEL6 update

* Thu Oct 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.103-0.1.20130920
- Initial Fedora release.

