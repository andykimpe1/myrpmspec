# Regarding brew / rhpkg build:
# This is a noarch package, providing static data and cross platform scripts,
# intended for all platforms. However, it includes data in a Java compatible
# file format. The required "keytool" for building the Java compatible data
# is available on the i686 and x86_64 arches, only.
# As a result, it's necessary to use a compatible build host.
# Unfortunately, I haven't found a way to enforce the build host.
# ExcludeArch/ExclusiveArch doesn't work.
# You must repeat rhpkg build until the build gets randomly assigned to a 
# compatible build host.

%define pkidir %{_sysconfdir}/pki
%define catrustdir %{_sysconfdir}/pki/ca-trust
%define classic_tls_bundle ca-bundle.crt
%define trusted_all_bundle ca-bundle.trust.crt
%define legacy_default_bundle ca-bundle.legacy.default.crt
%define legacy_disable_bundle ca-bundle.legacy.disable.crt
%define neutral_bundle ca-bundle.neutral-trust.crt
%define bundle_supplement ca-bundle.supplement.p11-kit
%define java_bundle java/cacerts

Summary: The Mozilla CA root certificate bundle
Name: ca-certificates

# For the package version number, we use: year.{upstream version}
#
# The {upstream version} can be found as symbol
# NSS_BUILTINS_LIBRARY_VERSION in file nss/lib/ckfw/builtins/nssckbi.h
# which corresponds to the data in file nss/lib/ckfw/builtins/certdata.txt.
#
# The files should be taken from a released version of NSS, as published
# at https://ftp.mozilla.org/pub/mozilla.org/security/nss/releases/
#
# The versions that are used by the latest released version of 
# Mozilla Firefox should be available from:
# https://hg.mozilla.org/releases/mozilla-release/raw-file/default/security/nss/lib/ckfw/builtins/nssckbi.h
# https://hg.mozilla.org/releases/mozilla-release/raw-file/default/security/nss/lib/ckfw/builtins/certdata.txt
#
# The most recent development versions of the files can be found at
# http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/nssckbi.h
# http://hg.mozilla.org/projects/nss/raw-file/default/lib/ckfw/builtins/certdata.txt
# (but these files might have not yet been released).
#
# (until 2012.87 the version was based on the cvs revision ID of certdata.txt,
# but in 2013 the NSS projected was migrated to HG. Old version 2012.87 is 
# equivalent to new version 2012.1.93, which would break the requirement 
# to have increasing version numbers. However, the new scheme will work, 
# because all future versions will start with 2013 or larger.)

Version: 2020.2.41
# On RHEL 6.x, please keep the release version < 70
# When rebasing on Y-Stream (6.y), use 65.1, 65.2, 65.3, ...
# When rebasing on Z-Stream (6.y.z), use 65.0, 65.0.1, 65.0.2, ...
Release: 65.1%{?dist}
License: Public Domain

Group: System Environment/Base
URL: http://www.mozilla.org/

#Please always update both certdata.txt and nssckbi.h
Source0: certdata.txt
Source1: nssckbi.h
Source2: update-ca-trust
Source3: trust-fixes
Source4: certdata2pem.py
Source5: generate-cacerts.pl
Source6: ca-legacy.conf
Source7: ca-legacy
Source9: ca-legacy.8.txt
Source10: update-ca-trust.8.txt
Source11: README.usr
Source12: README.etc
Source13: README.extr
Source14: README.java
Source15: README.openssl
Source16: README.pem
Source17: README.src
Source18: README.ca-certificates

BuildArch: noarch

Requires: p11-kit >= 0.18.4-2
Requires: p11-kit-trust >= 0.18.4-2
Requires: coreutils
Requires(post): coreutils

BuildRequires: perl
BuildRequires: python
BuildRequires: openssl
BuildRequires: asciidoc
BuildRequires: libxslt

#for /usr/bin/keytool
BuildRequires: java-1.6.0-openjdk

%description
This package contains the set of CA certificates chosen by the
Mozilla Foundation for use with the Internet PKI.

%prep
rm -rf %{name}
mkdir %{name}
mkdir %{name}/certs
mkdir %{name}/certs/legacy-default
mkdir %{name}/certs/legacy-disable
mkdir %{name}/java

%build
pushd %{name}/certs
 pwd
 cp %{SOURCE0} .
 python %{SOURCE4} >c2p.log 2>c2p.err
popd

pushd %{name}
 (
   cat <<EOF
# This is a bundle of X.509 certificates of public Certificate
# Authorities.  It was generated from the Mozilla root CA list.
#
# Source: nss/lib/ckfw/builtins/certdata.txt
# Source: nss/lib/ckfw/builtins/nssckbi.h
#
# Generated from:
EOF
   cat %{SOURCE1}  |grep -w NSS_BUILTINS_LIBRARY_VERSION | awk '{print "# " $2 " " $3}';
   echo '#';
 ) > %{classic_tls_bundle}

 (
   cat <<EOF
# This is a bundle of X.509 certificates of public Certificate
# Authorities.  It was generated from the Mozilla root CA list.
# These certificates are in the OpenSSL "TRUSTED CERTIFICATE"
# format and have trust bits set accordingly.
# An exception are auxiliary certificates, without positive or negative
# trust, but are used to assist in finding a preferred trust path.
# Those neutral certificates use the plain BEGIN CERTIFICATE format.
#
# Source: nss/lib/ckfw/builtins/certdata.txt
# Source: nss/lib/ckfw/builtins/nssckbi.h
#
# Generated from:
EOF
   cat %{SOURCE1}  |grep -w NSS_BUILTINS_LIBRARY_VERSION | awk '{print "# " $2 " " $3}';
   echo '#';
 ) > %{trusted_all_bundle}
 touch %{neutral_bundle}
 for f in certs/*.crt; do 
   echo "processing $f"
   tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
   distbits=`sed -n '/^# openssl-distrust/{s/^.*=//;p;}' $f`
   alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
   case $tbits in
     *serverAuth*) openssl x509 -text -in "$f" >> %{classic_tls_bundle} ;;
   esac
   targs=""
   if [ -n "$tbits" ]; then
      for t in $tbits; do
         targs="${targs} -addtrust $t"
      done
   fi
   if [ -n "$distbits" ]; then
      for t in $distbits; do
         targs="${targs} -addreject $t"
      done
   fi
   if [ -n "$targs" ]; then
      echo "trust flags $targs for $f" >> info.trust
      openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{trusted_all_bundle}
   else
      echo "no trust flags for $f" >> info.notrust
      # p11-kit-trust defines empty trust lists as "rejected for all purposes".
      # That's why we use the simple file format
      #   (BEGIN CERTIFICATE, no trust information)
      # because p11-kit-trust will treat it as a certificate with neutral trust.
      # This means we cannot use the -setalias feature for neutral trust certs.
      openssl x509 -text -in "$f" >> %{neutral_bundle}
   fi
 done

 touch %{legacy_default_bundle}
 NUM_LEGACY_DEFAULT=`find certs/legacy-default -type f | wc -l`
 if [ $NUM_LEGACY_DEFAULT -ne 0 ]; then
     for f in certs/legacy-default/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       case $tbits in
         *serverAuth*) openssl x509 -text -in "$f" >> %{classic_tls_bundle} ;;
       esac
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy default flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_default_bundle}
       fi
     done
 fi

 touch %{legacy_disable_bundle}
 NUM_LEGACY_DISABLE=`find certs/legacy-disable -type f | wc -l`
 if [ $NUM_LEGACY_DISABLE -ne 0 ]; then
     for f in certs/legacy-disable/*.crt; do 
       echo "processing $f"
       tbits=`sed -n '/^# openssl-trust/{s/^.*=//;p;}' $f`
       alias=`sed -n '/^# alias=/{s/^.*=//;p;q;}' $f | sed "s/'//g" | sed 's/"//g'`
       targs=""
       if [ -n "$tbits" ]; then
          for t in $tbits; do
             targs="${targs} -addtrust $t"
          done
       fi
       if [ -n "$targs" ]; then
          echo "legacy disable flags $targs for $f" >> info.trust
          openssl x509 -text -in "$f" -trustout $targs -setalias "$alias" >> %{legacy_disable_bundle}
       fi
     done
 fi

 P11FILES=`find certs -name *.p11-kit | wc -l`
 if [ $P11FILES -ne 0 ]; then
   for p in certs/*.p11-kit; do 
     cat "$p" >> %{bundle_supplement}
   done
 fi
 # Append our trust fixes
 cat %{SOURCE3} >> %{bundle_supplement}
popd

pushd %{name}/java
 test -s ../%{classic_tls_bundle} || exit 1
 %{__perl} %{SOURCE5} %{_bindir}/keytool ../%{classic_tls_bundle}
 touch -r %{SOURCE0} cacerts
popd

#manpage
cp %{SOURCE10} %{name}/update-ca-trust.8.txt
asciidoc.py -v -d manpage -b docbook %{name}/update-ca-trust.8.txt
xsltproc --nonet -o %{name}/update-ca-trust.8 /usr/share/asciidoc/docbook-xsl/manpage.xsl %{name}/update-ca-trust.8.xml

cp %{SOURCE9} %{name}/ca-legacy.8.txt
asciidoc.py -v -d manpage -b docbook %{name}/ca-legacy.8.txt
xsltproc --nonet -o %{name}/ca-legacy.8 /usr/share/asciidoc/docbook-xsl/manpage.xsl %{name}/ca-legacy.8.xml


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
install -p -m 644 %{name}/update-ca-trust.8 ${RPM_BUILD_ROOT}%{_mandir}/man8
install -p -m 644 %{name}/ca-legacy.8 $RPM_BUILD_ROOT%{_mandir}/man8

#### traditional, old-style
mkdir -p $RPM_BUILD_ROOT%{pkidir}/tls/certs
install -p -m 644 %{name}/%{classic_tls_bundle} $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{classic_tls_bundle}
install -p -m 644 %{name}/%{trusted_all_bundle} $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{trusted_all_bundle}

ln -s certs/%{classic_tls_bundle} $RPM_BUILD_ROOT%{pkidir}/tls/cert.pem
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{classic_tls_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{pkidir}/tls/certs/%{trusted_all_bundle}

# Install Java cacerts file.
mkdir -p -m 755 $RPM_BUILD_ROOT%{pkidir}/java
install -p -m 644 %{name}/%{java_bundle} $RPM_BUILD_ROOT%{pkidir}/java/

# /etc/ssl/certs symlink for 3rd-party tools
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/ssl
ln -s ../pki/tls/certs $RPM_BUILD_ROOT%{_sysconfdir}/ssl/certs

#### extracted, new-style
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/source/blacklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/pem
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl
mkdir -p -m 755 $RPM_BUILD_ROOT%{catrustdir}/extracted/java
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/anchors
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/blacklist
mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy

install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/README
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{catrustdir}/README
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{catrustdir}/extracted/README
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{catrustdir}/extracted/java/README
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl/README
install -p -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/README
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{catrustdir}/source/README

mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/README

install -p -m 644 %{name}/%{trusted_all_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{trusted_all_bundle}
install -p -m 644 %{name}/%{neutral_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{neutral_bundle}
install -p -m 644 %{name}/%{bundle_supplement} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{bundle_supplement}

install -p -m 644 %{name}/%{legacy_default_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
install -p -m 644 %{name}/%{legacy_disable_bundle} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}

ln -s %{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle} $RPM_BUILD_ROOT%{catrustdir}/source/ca-bundle.legacy.crt

install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{catrustdir}/ca-legacy.conf

touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{trusted_all_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{neutral_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-source/%{bundle_supplement}

touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}

install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update-ca-trust

install -p -m 755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/ca-legacy

# touch ghosted files that will be extracted dynamically
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/tls-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/email-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/pem/objsign-ca-bundle.pem
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/openssl/%{trusted_all_bundle}
touch $RPM_BUILD_ROOT%{catrustdir}/extracted/%{java_bundle}


%clean
rm -rf $RPM_BUILD_ROOT


%post
if test -e %{_bindir}/ca-legacy ; then
    %{_bindir}/ca-legacy install
fi
if test -e %{_bindir}/update-ca-trust ; then
	%{_bindir}/update-ca-trust
fi

%postun
# While the following is strictly discouraged, we cannot prevent it from happening:
# An admin could potentially use "update-ca-trust enable", thereby installing
# symbolic links for the legacy filename, and afterwards, the admin could 
# downgrade the ca-certificates package to an older version, which doesn't
# provide the new system of extracted files.
# If that happened, the symbolic links will become dangling links,
# and the old bundle files will get installed as .rpmnew files.
# That's a broken configuration.
# 
# Let's attempt to prevent admins from shooting themselves in the foot,
# by handling that scenario in a sane way.
#
if [ $1 -gt 0 ] ; then
	# This isn't a complete removal of the package.
	# There is still a ca-certificates package installed.
	# Because we are noarch, this cannot be a multilib situation.
	# Therefore it's clear the package that belongs to this script 
	# has been replaced by a newer or an older package.
	#
	# Detect if the legacy filenames are symbolic links.
	# If they aren't symbolic links, we're good, the legacy support was disabled,
	#     we assume the upgrade or downgrade has succeeded,
	#     and we don't take any action.
	# If they are symbolic links, then we must check if the link resolves to a file.
	# If it resolves, we're good. It was an upgrade or a downgrade to package version
	#     that provides the target files. No action necessary.
	# However, if we detect broken (dangling) links, then the new package version
	#     doesn't provide the new target files. We assume it's a downgrade
	#     and we must repair the dangling links. We'll replace them with ordinary
	#     files, either taking the files from our backup, or if no backup is
	#     available (unexpectedly) we'll use the .rpmnew file that just got installed.
    #
    # The above logic will restore the backup files that got saved at the time
    # the "enable" command had been executed.
    # If one of the backed up files was a file that had been modified by the admin
    # (prior to the backup), then that modified file will be restored
    # (because rpm kept the config(noreplace) file.
    # However, if the admin didn't change the files, then rpm has installed
    # more recent versions of the bundle files, and that more recent file will
    # be backed up.
    # In the latter scenario, as a result, our recovery logic will recover
    # using the more recent bundle file from the more recent package,
    # despite an older package being installed.
    # This side effect, which keeps slightly more recent unmodified bundles 
    # despite a package downgrade, should be an acceptable side effect, because
    # restoring the manually modified bundle files is much more important.
    
    backuppath=/etc/pki/backup-traditional-recent-config/
    already_warned=0
    for legacy in "cacerts" "ca-bundle.crt" "ca-bundle.trust.crt"; do
		lpath=
		if [ $legacy = "cacerts" ]; then
			lpath="/etc/pki/java/"
		fi
		if [ $legacy = "ca-bundle.crt" ]; then
			lpath="/etc/pki/tls/certs/"
		fi
		if [ $legacy = "ca-bundle.trust.crt" ]; then
			lpath="/etc/pki/tls/certs/"
		fi
		
		if ! test -z "$lpath"; then
			# sanity check succeded, lpath not empty
			if test -L ${lpath}${legacy}; then
				# is link
				if test -e ${lpath}${legacy}; then
					echo "Please ignore warnings about ${lpath}${legacy}.rpmnew, they are expected as the new consolidated configuration feature is enabled" >&2
				else
					# link target doesnt exist
					
					if [ $already_warned -eq 0 ] ; then 
						echo "Detected a downgrade of ca-certificates.rpm to an older package," >&2
						echo "  which doesn't support the new consolidated configuration feature." >&2
						echo "However, at the time of dowgrading, the new consolidated feature was enabled." >&2
						echo "This was an unsupported action, but this script will try its best to recover." >&2
						already_warned=1
					fi
					
					rm -f ${lpath}${legacy}
					echo "Removing symbolic link ${lpath}${legacy}" >&2
					echo "  because the new configuration feature has been removed" >&2
					
					if test -e ${backuppath}${legacy}; then
						# backup file exists
						echo "Backup file found at ${backuppath}${legacy}," >&2
						echo "    restoring it as ${lpath}${legacy}" >&2
						cp --dereference --preserve --force \
							${backuppath}${legacy} ${lpath}${legacy}
					else
						echo "No backup file found."
						if test -e ${lpath}${legacy}.rpmnew; then
							# .rpmnew file found
							echo "Using file ${lpath}${legacy}.rpmnew " >&2
							echo "  and installing it at ${lpath}${legacy}" >&2
							cp --dereference --preserve --force \
								${lpath}${legacy}.rpmnew ${lpath}${legacy}
						# else
							# there's nothing we can do
							echo "Sorry, no files found to provide ${lpath}${legacy}" >&2
						fi
					fi
				fi
			fi
		fi
	done
fi


%files
%defattr(-,root,root,-)
%{_mandir}/man8/update-ca-trust.8.gz
%{_mandir}/man8/ca-legacy.8.gz
%dir %{pkidir}/java
%config(noreplace) %{pkidir}/java/cacerts
%dir %{pkidir}/tls
%dir %{pkidir}/tls/certs
%config(noreplace) %{pkidir}/tls/certs/ca-bundle.*crt
%{pkidir}/tls/cert.pem
%dir %{_sysconfdir}/ssl
%{_sysconfdir}/ssl/certs

%dir %{catrustdir}
%dir %{catrustdir}/source
%dir %{catrustdir}/source/anchors
%dir %{catrustdir}/source/blacklist
%dir %{catrustdir}/extracted
%dir %{catrustdir}/extracted/pem
%dir %{catrustdir}/extracted/openssl
%dir %{catrustdir}/extracted/java
%dir %{_datadir}/pki
%dir %{_datadir}/pki/ca-trust-source
%dir %{_datadir}/pki/ca-trust-source/anchors
%dir %{_datadir}/pki/ca-trust-source/blacklist
%dir %{_datadir}/pki/ca-trust-legacy

%config(noreplace) %{catrustdir}/ca-legacy.conf

%{_datadir}/pki/ca-trust-source/README
%{catrustdir}/README
%{catrustdir}/extracted/README
%{catrustdir}/extracted/java/README
%{catrustdir}/extracted/openssl/README
%{catrustdir}/extracted/pem/README
%{catrustdir}/source/README
%{_datadir}/doc/%{name}-%{version}/README

# master bundle file with trust
%{_datadir}/pki/ca-trust-source/%{trusted_all_bundle}
%{_datadir}/pki/ca-trust-source/%{neutral_bundle}
%{_datadir}/pki/ca-trust-source/%{bundle_supplement}
%{_datadir}/pki/ca-trust-legacy/%{legacy_default_bundle}
%{_datadir}/pki/ca-trust-legacy/%{legacy_disable_bundle}
# update/extract tool
%{_bindir}/update-ca-trust
%{_bindir}/ca-legacy
%ghost %{catrustdir}/source/ca-bundle.legacy.crt
# extracted files
%ghost %{catrustdir}/extracted/pem/tls-ca-bundle.pem
%ghost %{catrustdir}/extracted/pem/email-ca-bundle.pem
%ghost %{catrustdir}/extracted/pem/objsign-ca-bundle.pem
%ghost %{catrustdir}/extracted/openssl/%{trusted_all_bundle}
%ghost %{catrustdir}/extracted/%{java_bundle}


%changelog
* Wed Jul 22 2020 Bob Relyea <rrelyea@redhat.com> - 2020.2.41-65.1
- remove DISTRUST_AFTER attributes.

*Tue Jun 09 2020 Bob Relyea <rrelyea@redhat.com> - 2020.2.41-60.0
- Update to CKBI 2.41 from NSS 3.53.0
-    Removing:
-     # Certificate "AddTrust Low-Value Services Root"
-     # Certificate "AddTrust External Root"
-     # Certificate "UTN USERFirst Email Root CA"
-     # Certificate "Certplus Class 2 Primary CA"
-     # Certificate "Deutsche Telekom Root CA 2"
-     # Certificate "Staat der Nederlanden Root CA - G2"
-     # Certificate "Swisscom Root CA 2"
-     # Certificate "Certinomis - Root CA"
-    Adding:
-     # Certificate "Entrust Root Certification Authority - G4"

*Thu Oct 03 2019 Bob Relyea <rrelyea@redhat.com> - 2019.2.32-65.1
- Remove expired 1024 bit roots
-    Removing:
-     # Certificate "GTE CyberTrust Global Root"
-     # Certificate "Equifax Secure CA"
-     # Certificate "ValiCert Class 1 VA"
-     # Certificate "ValiCert Class 2 VA"
-     # Certificate "RSA Root Certificate 1"
-     # Certificate "Entrust.net Secure Server CA"
-     # Certificate "NetLock Business (Class B) Root"
-     # Certificate "NetLock Express (Class C) Root"

*Fri Jun 21 2019 Bob Relyea <rrelyea@redhat.com> - 2019.2.32-60.0
-Update to CKBI 2.32 from NSS 3.44
-   Removing:
-    # Certificate "Visa eCommerce Root"
-    # Certificate "AC Raiz Certicamara S.A."
-    # Certificate "TC TrustCenter Class 3 CA II"
-    # Certificate "ComSign CA"
-    # Certificate "S-TRUST Universal Root CA"
-    # Certificate "TÜRKTRUST Elektronik Sertifika Hizmet Sağlayıcısı H5"
-    # Certificate "Certplus Root CA G1"
-    # Certificate "Certplus Root CA G2"
-    # Certificate "OpenTrust Root CA G1"
-    # Certificate "OpenTrust Root CA G2"
-    # Certificate "OpenTrust Root CA G3"
-   Adding:
-    # Certificate "GlobalSign Root CA - R6"
-    # Certificate "OISTE WISeKey Global Root GC CA"
-    # Certificate "GTS Root R1"
-    # Certificate "GTS Root R2"
-    # Certificate "GTS Root R3"
-    # Certificate "GTS Root R4"
-    # Certificate "UCA Global G2 Root"
-    # Certificate "UCA Extended Validation Root"
-    # Certificate "Certigna Root CA"
-    # Certificate "emSign Root CA - G1"
-    # Certificate "emSign ECC Root CA - G3"
-    # Certificate "emSign Root CA - C1"
-    # Certificate "emSign ECC Root CA - C3"
-    # Certificate "Hongkong Post Root CA 3"

* Wed Feb 28 2018 Kai Engert <kaie@redhat.com> - 2018.2.22-65.1
- Update to CKBI 2.22 from NSS 3.35 with legacy modifications.

* Mon Dec 18 2017 Kai Engert <kaie@redhat.com> - 2017.2.20-65.1
- Update to CKBI 2.20 from NSS 3.34.1 with legacy modifications.
  In the original upstream release, Mozilla.org removed all trust for
  the code signing usage. As part of the default legacy configuration,
  this package retains code signing trust for all CAs that are still
  trusted for the server authentication usage.
  The ca-legacy disable configuration disables all code signing trust.

* Fri Apr 28 2017 Kai Engert <kaie@redhat.com> - 2017.2.14-65.1
- Update to CKBI 2.14 from NSS 3.28.5 with legacy modifications.

* Thu Feb 23 2017 Kai Engert <kaie@redhat.com> - 2017.2.11-65.1
- Update to CKBI 2.11 from NSS 3.28.1 with legacy modifications.

* Tue Nov 01 2016 Kai Engert <kaie@redhat.com> - 2016.2.10-65.4
- fix a typo in the manual page

* Wed Oct 26 2016 Kai Engert <kaie@redhat.com> - 2016.2.10-65.3
- Update to CKBI 2.10 from NSS 3.27 with legacy modifications.

* Mon Jan 18 2016 Kai Engert <kaie@redhat.com> - 2015.2.6-65.1
- Update to CKBI 2.6 from NSS 3.21 with legacy modifications.

* Thu Apr 23 2015 Kai Engert <kaie@redhat.com> - 2015.2.4-65.1
- Update to CKBI 2.4 from NSS 3.18.1 with legacy modifications.

* Tue Apr 14 2015 Kai Engert <kaie@redhat.com> - 2015.2.3-65.3
- Fix a typo in the ca-legacy manual page (rhbz#1208850)

* Wed Apr 01 2015 Kai Engert <kaie@redhat.com> - 2015.2.3-65.2
- Include the legacy CA certificates in the classic TLS bundle, too.

* Tue Mar 31 2015 Kai Engert <kaie@redhat.com> - 2015.2.3-65.1
- Update to CKBI 2.3 from NSS 3.18 with legacy modifications.
- Add a patch to the source RPM that documents the changes from the
  upstream version.
- Introduce the ca-legacy utility, a manual page, and the ca-legacy.conf
  configuration file.
- The new scriptlets require the coreutils package.
- Remove the obsolete blacklist.txt file.

* Thu Dec 04 2014 Kai Engert <kaie@redhat.com> - 2014.1.98-65.2
- Add an alternative version of the "Thawte Premium Server CA" root,
  which carries a SHA1-RSA signature, to allow OpenJDK to verify applets
  which contain that version of the root certificate (rhbz#1138230).
  This change doesn't add trust for another key, because both versions
  of the certificate use the same public key.

* Mon Jul 14 2014 Kai Engert <kaie@redhat.com> - 2014.1.98-65.1
- Rebuild, ensure y-stream uses larger release number than z-stream.

* Thu May 29 2014 Kai Engert <kaie@redhat.com> - 2014.1.98-65.0
- Update to CKBI 1.98 from NSS 3.16.1

* Tue Dec 17 2013 Kai Engert <kaie@redhat.com> - 2013.1.95-65.1
- Bump release number for consistency across branches

* Tue Dec 17 2013 Kai Engert <kaie@redhat.com> - 2013.1.95-65.0
- Update to CKBI 1.95 from NSS 3.15.3.1

* Tue Sep 03 2013 Kai Engert <kaie@redhat.com> - 2013.1.94-65.0
- Update to CKBI 1.94 from NSS 3.15

* Thu Jul 18 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.9
- fix manpage format

* Wed Jul 17 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.8
- improve manpage

* Thu Jul 11 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.7
- ExcludeArch/ExclusiveArch doesn't work to enforce a build host
- Added comment that explains the special build requirements.
- Added a comment suggesting to keep the release number below the 
  ones used on RHEL 7.
- Fixed permissions of /etc/pki/java (thanks to stefw)

* Mon Jul 08 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.6
- set a certificate alias in trusted bundle (thanks to Ludwig Nussel)

* Mon Jul 08 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.5
- update required p11-kit version

* Wed Jul 03 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.4
- attempt to handle unsupported downgrades, where the admin has enabled
  legacy support, but downgrades to an old package that is incompatible
  provide the new feature.
- move manual page to the man8 section (system administration commands)
- simplify the README files now that we have a manual page

* Fri Jun 14 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.3
- added a manual page and related build requirements
- updated copyright sections in scripts
- enhance update-ca-trust script

* Fri Jun 14 2013 Stef Walter <stefw@redhat.com> - 2012.87-65.2
- update-ca-trust: Print warnings to stderr

* Fri Jun 14 2013 Stef Walter <stefw@redhat.com> - 2012.87-65.1
- update-ca-trust: Update p11-kit script path
- update-ca-trust: script uses bash not sh

* Fri Jun 14 2013 Kai Engert <kaie@redhat.com> - 2012.87-65.0
- Major rework introducing the SharedSystemCertificates feature, 
  disabled by default.
- Require the p11-kit package that contains tools to automatically create
  other file format bundles.
- Added a update-ca-trust script which can be used to enable the
  new system and to regenerate the merged trust output.
- Refer to the various README files that have been added for more detailed
  explanation of the new system.
- No longer require rsc for building. Remove use of rcs/ident.
- Update source URLs and comments, add source file for version information.
- Add explanation for the future version numbering scheme,
  because the old numbering scheme assumed upstream using cvs,
  which is no longer true, and therefore can no longer be used.

* Thu Mar  1 2012 Joe Orton <jorton@redhat.com> - 2010.63-4
- fix inclusion of code-signing-only certs in .trust.crt
- exclude blacklisted root from java keystore too
- remove trust from DigiNotar root (#734678)

* Wed Apr  7 2010 Joe Orton <jorton@redhat.com> - 2010.63-3
- package /etc/ssl/certs symlink for third-party apps (#572725)

* Wed Apr  7 2010 Joe Orton <jorton@redhat.com> - 2010.63-2
- rebuild

* Wed Apr  7 2010 Joe Orton <jorton@redhat.com> - 2010.63-1
- update to certdata.txt r1.63
- use upstream RCS version in Version

* Fri Mar 19 2010 Joe Orton <jorton@redhat.com> - 2010-4
- fix ca-bundle.crt (#575111)

* Thu Mar 18 2010 Joe Orton <jorton@redhat.com> - 2010-3
- update to certdata.txt r1.58
- add /etc/pki/tls/certs/ca-bundle.trust.crt using 'TRUSTED CERTICATE' format
- exclude ECC certs from the Java cacerts database
- catch keytool failures
- fail parsing certdata.txt on finding untrusted but not blacklisted cert

* Fri Jan 15 2010 Joe Orton <jorton@redhat.com> - 2010-2
- fix Java cacert database generation: use Subject rather than Issuer
  for alias name; add diagnostics; fix some alias names.

* Mon Jan 11 2010 Joe Orton <jorton@redhat.com> - 2010-1
- adopt Python certdata.txt parsing script from Debian

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Joe Orton <jorton@redhat.com> 2009-1
- update to certdata.txt r1.53

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 14 2008 Joe Orton <jorton@redhat.com> 2008-7
- update to certdata.txt r1.49

* Wed Jun 25 2008 Thomas Fitzsimmons <fitzsim@redhat.com> - 2008-6
- Change generate-cacerts.pl to produce pretty aliases.

* Mon Jun  2 2008 Joe Orton <jorton@redhat.com> 2008-5
- include /etc/pki/tls/cert.pem symlink to ca-bundle.crt

* Tue May 27 2008 Joe Orton <jorton@redhat.com> 2008-4
- use package name for temp dir, recreate it in prep

* Tue May 27 2008 Joe Orton <jorton@redhat.com> 2008-3
- fix source script perms
- mark packaged files as config(noreplace)

* Tue May 27 2008 Joe Orton <jorton@redhat.com> 2008-2
- add (but don't use) mkcabundle.pl
- tweak description
- use /usr/bin/keytool directly; BR java-openjdk

* Tue May 27 2008 Joe Orton <jorton@redhat.com> 2008-1
- Initial build (#448497)
#off
