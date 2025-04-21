# remirepo spec file for php74 SCL metapackage
#
# SPDX-FileCopyrightText:  Copyright 2018-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global scl_name_base    php
%global scl_name_version 74
%global scl              %{scl_name_base}%{scl_name_version}
%global macrosdir        %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_root_sysconfdir}/rpm; echo $d)
%global install_scl      1
%global rh_layout        1

%scl_package %scl

# do not produce empty debuginfo package
%global debug_package %{nil}

Summary:       Package that installs PHP 7.4
Name:          %scl_name
Version:       7.4.33
Release:       22%{?dist}
License:       GPL-2.0-or-later

Source0:       https://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@raw.githubusercontent.com/andykimpe1/myrpmspec/refs/heads/el7/php74/php74/macros-build
Source1:       https://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@raw.githubusercontent.com/andykimpe1/myrpmspec/refs/heads/el7/php74/php74/README
Source2:       https://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@raw.githubusercontent.com/andykimpe1/myrpmspec/refs/heads/el7/php74/php74/LICENSE

BuildRequires: scl-utils-build
BuildRequires: help2man
# Temporary work-around
BuildRequires: iso-codes
BuildRequires: environment-modules

Requires:      %{?scl_prefix}php-common%{?_isa}
Requires:      %{?scl_prefix}php-cli%{?_isa}
Requires:      %{?scl_name}-runtime%{?_isa}      = %{version}-%{release}

%description
This is the main package for %scl Software Collection,
that install PHP 7.4 language.


%package runtime
Summary:   Package that handles %scl Software Collection.
Requires:  scl-utils
Requires:  environment-modules
Requires(post): %{?_root_sbindir}/semanage
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11
Requires(post): %{_root_bindir}/selinuxenabled
%else
Requires(post): %{_root_sbindir}/selinuxenabled
%endif
Provides:  %{?scl_name}-runtime(%{scl_vendor})
Provides:  %{?scl_name}-runtime(%{scl_vendor})%{?_isa}

%description runtime
Package shipping essential scripts to work with %scl Software Collection.


%package build
Summary:   Package shipping basic build configuration
Requires:  scl-utils-build
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}

%description build
Package shipping essential configuration macros
to build %scl Software Collection.


%package scldevel
Summary:   Package shipping development files for %scl
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}

%description scldevel
Package shipping development files, especially usefull for development of
packages depending on %scl Software Collection.


%package syspaths
Summary:   System-wide wrappers for the %{name} package
Requires:  %{?scl_name}-runtime%{?_isa} = %{version}-%{release}
Requires:  %{?scl_name}-php-cli%{?_isa}
Requires:  %{?scl_name}-php-common%{?_isa}
Conflicts: php-common
Conflicts: php-cli
Conflicts: php54-syspaths
Conflicts: php55-syspaths
Conflicts: php56-syspaths
Conflicts: php70-syspaths
Conflicts: php71-syspaths
Conflicts: php72-syspaths
Conflicts: php73-syspaths

%description syspaths
System-wide wrappers for the %{name}-php-cli package.

Using the %{name}-syspaths package does not require running the
'scl enable' or 'module command. This package practically replaces the system
default php-cli package. It provides the php, phar and php-cgi commands.

Note that the php-cli and %{name}-syspaths packages conflict and cannot
be installed on one system.


%prep
%setup -c -T

cat <<EOF | tee enable
export PATH=%{_bindir}:%{_sbindir}\${PATH:+:\${PATH}}
export LD_LIBRARY_PATH=%{_libdir}\${LD_LIBRARY_PATH:+:\${LD_LIBRARY_PATH}}
export MANPATH=%{_mandir}:\${MANPATH}
EOF

# Broken: /usr/share/Modules/bin/createmodule.sh enable | tee envmod
# See https://bugzilla.redhat.com/show_bug.cgi?id=1197321
cat << EOF | tee envmod
#%%Module1.0
prepend-path    X_SCLS              %{scl}
prepend-path    PATH                %{_bindir}:%{_sbindir}
prepend-path    LD_LIBRARY_PATH     %{_libdir}
prepend-path    MANPATH             %{_mandir}
prepend-path    PKG_CONFIG_PATH     %{_libdir}/pkgconfig
EOF

# generate rpm macros file for depended collections
cat << EOF | tee scldev
%%scl_%{scl_name_base}         %{scl}
%%scl_prefix_%{scl_name_base}  %{scl_prefix}
EOF

# This section generates README file from a template and creates man page
# from that file, expanding RPM macros in the template file.
cat >README <<'EOF'
%{expand:%(cat %{SOURCE1})}
EOF

# copy the license file so %%files section sees it
cp %{SOURCE2} .

: prefix in %{_prefix}
: config in %{_sysconfdir}
: data in %{_localstatedir}


%build
# generate a helper script that will be used by help2man
cat >h2m_helper <<'EOF'
#!/bin/bash
[ "$1" == "--version" ] && echo "%{scl_name} Software Collection (PHP %{version})" || cat README
EOF
chmod a+x h2m_helper

# generate the man page
help2man -N --section 7 ./h2m_helper -o %{scl_name}.7


%install
install -D -m 644 enable %{buildroot}%{_scl_scripts}/enable
install -D -m 644 envmod %{buildroot}%{_root_datadir}/Modules/modulefiles/%{scl_name}
install -D -m 644 scldev %{buildroot}%{macrosdir}/macros.%{scl_name_base}-scldevel
install -D -m 644 %{scl_name}.7 %{buildroot}%{_root_mandir}/man7/%{scl_name}.7

install -d -m 755 %{buildroot}%{_datadir}/licenses
install -d -m 755 %{buildroot}%{_datadir}/doc/pecl
install -d -m 755 %{buildroot}%{_datadir}/tests/pecl
install -d -m 755 %{buildroot}%{_localstatedir}/lib/pear/pkgxml

%scl_install

cat %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config

# Add the scl_package_override macro
sed -e 's/@SCL@/%{scl}/g;s:@PREFIX@:/opt/%{scl_vendor}:;s/@VENDOR@/%{scl_vendor}/' %{SOURCE0} \
  | tee -a %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config

# Move in correct location, if needed
if [ "%{_root_sysconfdir}/rpm" != "%{macrosdir}" ]; then
  mv  %{buildroot}%{_root_sysconfdir}/rpm/macros.%{scl}-config \
      %{buildroot}%{macrosdir}/macros.%{scl}-config
fi

# syspaths
mkdir -p %{buildroot}%{_root_sysconfdir}
ln -s %{_sysconfdir}/php.ini %{buildroot}%{_root_sysconfdir}/php.ini
ln -s %{_sysconfdir}/php.d   %{buildroot}%{_root_sysconfdir}/php.d
mkdir -p %{buildroot}%{_root_bindir}
ln -s %{_bindir}/php     %{buildroot}%{_root_bindir}/php
ln -s %{_bindir}/phar    %{buildroot}%{_root_bindir}/phar
ln -s %{_bindir}/php-cgi %{buildroot}%{_root_bindir}/php-cgi
mkdir -p %{buildroot}%{_root_mandir}/man1
ln -s %{_mandir}/man1/php.1.gz     %{buildroot}%{_root_mandir}/man1/php.1.gz
ln -s %{_mandir}/man1/phar.1.gz    %{buildroot}%{_root_mandir}/man1/phar.1.gz
ln -s %{_mandir}/man1/php-cgi.1.gz %{buildroot}%{_root_mandir}/man1/php-cgi.1.gz


%post runtime
# Simple copy of context from system root to SCL root.
semanage fcontext -a -e /                      %{?_scl_root}     &>/dev/null || :
semanage fcontext -a -e %{_root_sysconfdir}    %{_sysconfdir}    &>/dev/null || :
semanage fcontext -a -e %{_root_localstatedir} %{_localstatedir} &>/dev/null || :
selinuxenabled && load_policy || :
restorecon -R %{?_scl_root}     &>/dev/null || :
restorecon -R %{_sysconfdir}    &>/dev/null || :
restorecon -R %{_localstatedir} &>/dev/null || :


%{!?_licensedir:%global license %%doc}

%files


%files runtime -f filesystem
%license LICENSE
%doc README
%scl_files
%{_root_mandir}/man7/%{scl_name}.*
%{?_licensedir:%{_datadir}/licenses}
%{_datadir}/tests
%{_root_datadir}/Modules/modulefiles/%{scl_name}


%files build
%{macrosdir}/macros.%{scl}-config


%files scldevel
%{macrosdir}/macros.%{scl_name_base}-scldevel


%files syspaths
%{_root_sysconfdir}/php.ini
%{_root_sysconfdir}/php.d
%{_root_bindir}/php
%{_root_bindir}/phar
%{_root_bindir}/php-cgi
%{_root_mandir}/man1/php.1.gz
%{_root_mandir}/man1/phar.1.gz
%{_root_mandir}/man1/php-cgi.1.gz


%changelog
* Fri Feb 14 2025 Remi Collet <remi@remirepo.net> 7.4-5
- F42: fix dependencies
- re-license spec file to CECILL-2.1

* Tue Aug 22 2023 Remi Collet <remi@remirepo.net> 7.4-4
- F39 build

* Wed Apr 26 2023 Remi Collet <remi@remirepo.net> 7.4-3
- redefine %%__phpize and %%__phpconfig

* Thu Mar  9 2023 Remi Collet <remi@remirepo.net> 7.4-2
- define %%scl_vendor and %%_scl_prefix in macros.php74-config
- move man page out of scl tree
- improve the man page

* Tue Nov  9 2021 Remi Collet <remi@remirepo.net> 7.4-1
- EL-9 build

* Thu Apr  9 2020 Remi Collet <remi@remirepo.net> 1.0-3
- add conflict between php73-syspaths and php74-syspaths

* Thu Aug 22 2019 Remi Collet <remi@remirepo.net> 1.0-2
- fix error: Macro %%undefine is a built-in
  see https://bugzilla.redhat.com/1744583

* Mon May 20 2019 Remi Collet <remi@remirepo.net> 1.0-1
- initial package for 7.4

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> 2.0-1
- add syspaths sub package providing system-wide wrappers

* Thu Jan 17 2019 Remi Collet <remi@remirepo.net> 1.0-2
- cleanup for EL-8

* Thu Aug 23 2018 Remi Collet <remi@remirepo.net> 1.0-1
- scl-utils 2.0.2 drop modules support

* Thu Jun  7 2018 Remi Collet <remi@remirepo.net> 1.0-0.1
- initial packaging
