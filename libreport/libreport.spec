%{!?python_site: %define python_site %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
# platform-dependent
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Generic library for reporting various problems
Name: libreport
Version: 2.0.9
Release: 34%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: https://fedorahosted.org/abrt/
Source: https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
Patch0: 0001-bugzilla-exclude-appending-package-name-for-kernel-o.patch
Patch1: 0002-debuginfo-downloader-minor-fix.patch
Patch2: 0003-make-descr-don-t-include-superfluous-FILENAME_REASON.patch
Patch3: 0004-plugin-kerneloops-change-the-kerneloops-url-to-repor.patch
Patch4: 0005-plugin-kerneloops-fix-the-libcurl-use-Expect-header.patch
Patch5: 0006-libreport.pc-rhbz-803736-pkg-config-cflags-libreport.patch
Patch6: 0007-added-notify-only-to-mailx-rhbz-803618.patch
Patch7: 0008-debuginfo.py-send-cpio-s-output-to-dev-null.patch
Patch8: 0009-wizard-replace-exitcodes-by-messages.patch
Patch9: 0010-Add-cgroup-information-filename.patch
Patch10: 0011-rhbz-795548-opt-kernel-out-of-showing-smolt-informat.patch
Patch11: 0012-debuginfo.py-fix-abort-handling.patch
Patch12: 0013-debuginfo-don-t-give-up-downloading-when-some-repo-c.patch
Patch13: 0014-trakc-480-use-macro-with-ISO-date-sample-instead-of-.patch
Patch14: 0015-pop_next_command-no-need-to-open-problem-directory-r.patch
Patch15: 0016-xmlrpc-rising-XMLRPC_XML_SIZE_LIMIT_DEFAULT-up-to-4-.patch
Patch16: 0017-trac-480-fixed-memory-leak-in-is_comment_dup-functio.patch
Patch17: 0018-ureport-ureport-introduction.patch
Patch18: 0019-build-add-inclusion-to-testsuite-to-see-abrt_curl.h.patch
Patch19: 0020-internal_libreport-add-FILENAME_-for-storing-package.patch
Patch20: 0021-Fix-abrt-build-breakage.patch
Patch21: 0022-Die-on-out-of-memory-in-JSON-generator-functions.patch
Patch22: 0023-fixed-build-errors.patch
Patch23: 0024-rhbz-820985-bz-4.2-doesn-t-have-bug_id-member-it-s-i.patch
Patch24: 0025-trac-526-add-check-for-locale.h-to-configure.ac-and-.patch
Patch25: 0026-prelink-fix-undefined-non-weak-symbols-rhbz-826745.patch
Patch26: 0027-iso_date_string-make-sure-year-is-between-0000-and-9.patch
Patch27: 0028-abrt-bodhi-after-Searching-for-updates-do-tell-its-r.patch
Patch28: 0029-strbuf-fix-conditional-jump-or-move-depends-on-unini.patch
Patch29: 0030-track-480-unused-pointer-value-in-bodhi_read_value.patch
Patch30: 0031-track-480-fixed-memory-leak-in-find_best_bt_rating_i.patch
Patch31: 0032-strbuf-strtrimch-memmove-reads-bytes-out-of-borders.patch
Patch32: 0033-don-t-leak-release-variable.patch
Patch33: 0034-Teach-dd_create_basic_files-to-save-an-additional-fi.patch
Patch34: 0035-track-542-track-544-teach-reporter-ureport-upload-ur.patch
Patch35: 0036-track-542-add-reporter-and-related_packages-fields-t.patch
Patch36: 0037-track-546-ureport-url-from-an-environment-variable.patch
Patch37: 0038-track-543-integration-of-reporter-ureport-in-librepo.patch
Patch38: 0040-track-552-reporter-ureport-allows-to-enable-disable-.patch
Patch39: 0041-use-retrace-instead-of-local-gdb-in-ureport-event.patch
Patch40: 0042-reporter-bugzilla-get-function-names-consistent-in-..patch
Patch41: 0043-track-557-remove-ureport-config-and-move-it-s-config.patch
Patch42: 0044-fixed-hyperlink-parsing-rhbz-831333.patch
Patch43: 0045-save-type-element-with-the-same-value-as-analyzer.patch
Patch44: 0046-reporter-bugzilla-do-not-require-problem-directory-w.patch
Patch45: 0047-reporter-rhtsupport-do-not-require-problem-directory.patch
Patch46: 0048-report-gtk-fix-report-gtk-NONEXISTENT_DIR-behaviour..patch
Patch47: 0049-Fix-bugs-uncovered-by-Coverity.-Closes-rhbz-809416.patch
Patch48: 0050-hide-mailx-from-UI.patch
Patch49: 0051-remove-json-bodhi-and-ureport.patch
Patch50: 0053-updated-translation.patch
Patch51: 0054-don-t-try-to-delete-dump-dir-which-doesn-t-exist-rhb.patch
Patch52: 0056-abrtd-make-it-ignore-non-problem-dirs-when-looking-f.patch
Patch53: 0057-rhbz-747410-bugzillas-are-created-according-to-rh-bz.patch
Patch54: 0058-rhbz-747410-skip-not-provided-bz-bug-description-tem.patch
Patch55: 0059-rhbz-747410-generate-koops-according-to-default-rhbz.patch
Patch56: 0060-rhbz-747410-reporter-bugzilla-do-not-attach-empty-fi.patch
Patch57: 0061-rhbz-747410-show-the-description-file-in-bugzilla-co.patch
Patch58: 0062-reporter-bugzilla-fix-adding-users-to-CC.-Partially-.patch
Patch59: 0063-don-t-show-the-credential-in-logs-rhbz-856960.patch
Patch60: 0065-updated-translation-rhbz-864025.patch
Patch61: 0067-added-relro-to-reportclient.so-and-_pyreport.so-rhbz.patch
Patch62: 0068-Make-get_dirsize_find_largest_dir-less-talkative.-re.patch
Patch63: 0069-fixed-the-relro-flags-rhbz-812283.patch
Patch64: 0070-never-follow-symlinks-rhbz-887866.patch
Patch65: 0071-Stop-reading-text-files-one-byte-at-a-time-realated-.patch
Patch66: 0072-dd-open-symlinks-on-request-related-895442.patch
Patch67: 0073-reporter-rhtsupport-retain-Beta-suffix-in-version.-C.patch
Patch68: 0074-don-t-suid-before-running-yum-related-to-rhbz-759443.patch
Patch69: 0076-fread_with_reporting-make-progress-indicator-less-no.patch
Patch70: 0077-RHTS-support-regularize-order-of-functions-and-comme.patch
Patch71: 0078-reporter-rhtsupport-factor-out-tarball-creation.patch
Patch72: 0079-reporter-rhtsupport-make-t-CASE_ID-work-without-FILE.patch
Patch73: 0080-reporter-rhtsupport-skip-hints-check-if-uploaded-dat.patch
Patch74: 0081-reporter-upload-factor-out-HTTP-PUT-upload.patch
Patch75: 0082-reporter-upload-move-file-upload-function-to-lib.patch
Patch76: 0083-reporter-rhtsupport-fix-double-free-error.patch
Patch77: 0084-reporter-rhtsupport-upload-file-to-BigFileURL-if-it-.patch
Patch78: 0085-reporter-rhtsupport-improve-logging.patch
Patch79: 0086-remove-new-line-from-ask-ask_password-responses.patch
Patch80: 0087-Change-default-conf-to-show-three-options-new-case-e.patch
Patch82: 0089-wizard-fix-unterminated-string-bug-in-ask-handling-r.patch
Patch83: 0090-reporter-rhtsupport-generate-archive-name-from-probl.patch
Patch84: 0091-reporter-upload-create-tarball-with-the-name-based-o.patch
Patch85: 0092-added-DD_DONT_WAIT_FOR_LOCK-and-int-dump_dir_accessi.patch
Patch86: 0093-includes-add-macro-for-last-occurrence-dump-dir-file.patch
Patch87: 0094-create-last_occurrence-at-the-time-of-the-first-cras.patch
Patch88: 0095-fixed-relro-flags-rhbz-812283.patch
Patch89: 0096-reporter-bz-make-binary-attachments-have-application.patch
Patch90: 0097-Fix-bugs-discoverent-by-Coverity.-rhbz-905051.patch
Patch91: 0098-report-python-export-DD_OPEN_READONLY-too.patch
Patch92: 0099-report-python-export-dd_delete_item-too.patch
Patch93: 0100-introduce-a-function-deleting-dd-s-element.patch
Patch94: 0103-updated-translation-rhbz-993626.patch
Patch95: 0104-rhbz-replace-obsolete-methods-by-their-substitutes.patch
Patch96: 0105-reporter-bugzilla-use-base64-XMLRPC-type-for-encoded.patch
Patch97: 0106-rhbz-get-id-of-duplicate-from-correct-field.patch
Patch98: 0107-updated-translation-rhbz-993626.patch
Patch99: 0108-do-not-leak-file-rhbz-997871.patch
Patch100: 0109-Include-hostname-in-mailx-notification.patch
Patch101: 0110-Bugzilla-pass-Bugzilla_token-in-all-XML-RPC-calls.patch
Patch102: 0111-mailx-improve-notification-e-mail-format.patch
# $ git format-patch 2.0.9-21.el6 -N --start-number 112 --topo-order -o /home/repos/rhel/libreport/
Patch112: 0112-Replace-btparser-with-satyr.patch
Patch113: 0113-reporter-ureport-from-upstream.patch
#Patch114: 0114-spec-add-plugin-ureport.patch
Patch115: 0115-refactorize-map_string_t-clean-up.patch
#Patch116: 0116-spec-install-libreport_types.h.patch
Patch117: 0117-create-augeas-lens-for-libreport.patch
Patch118: 0118-load-save-configuration-via-augeas.patch
Patch119: 0119-remove-file-options-not-matching-any-setting.patch
Patch120: 0120-remove-left-over-debug-stmts-from-conf-files-fns.patch
#Patch121: 0121-spec-add-augeas-devel-to-build-requires.patch
Patch122: 0122-testsuite-pack-conf-directory-in-the-dist-tarball.patch
Patch123: 0123-add-type-agnostic-functions-for-map_string_t.patch
Patch124: 0124-run_event_state-expose-children_count-in-python-wrap.patch
Patch125: 0125-make_description-add-an-option-for-URLs-from-reporte.patch
Patch126: 0126-URLs-in-description.patch
Patch127: 0127-map_string_t-fix-overflow-detection-in-to-int-conver.patch
Patch128: 0128-Ensure-long-long-unsigned-in-printf-format-args.patch
Patch129: 0129-Make-make_description-output-less-confusing.patch
Patch130: 0130-Export-the-return-codes-in-Python-modules.patch
Patch131: 0131-replace-all-Fedora-URLs-by-corresponding-values-for-.patch
Patch132: 0132-ureport-add-support-for-client-side-authentication.patch
Patch133: 0133-ureport.conf-turn-on-SSL-auth-with-RHSM-cert.patch
Patch134: 0134-lib-introduce-file-utils.patch
#Patch135: 0135-spec-installe-file-utils-headers.patch
Patch136: 0136-add-a-few-helpers-for-reading-files-as-one-malloced-.patch
Patch137: 0137-lib-add-function-converting-CSV-to-GList.patch
Patch138: 0138-ureport-enabled-inclusion-of-Authentication-data.patch
Patch139: 0139-lib-add-xstrdup_between-str-open-close.patch
Patch140: 0140-testsuite-add-test-for-xstrdup_between-src-open-clos.patch
Patch141: 0141-lib-add-wrapper-for-g_hash_table_size.patch
Patch142: 0142-lib-add-strremovech-str-ch.patch
Patch143: 0143-testsuite-add-test-for-strremovech-str-ch.patch
Patch144: 0144-ureport-use-additional-HTTP-headers-with-rhsm-entitl.patch
Patch145: 0145-ureport-publish-ureport.h-and-refactore-uReport-sour.patch
Patch146: 0146-ureport-aggressive-refactorization-of-uReport-source.patch
#Patch147: 0147-spec-install-ureport.h.patch
Patch148: 0148-ureport-support-HTTP-Basic-authentication.patch
Patch149: 0149-rhtsupport-submit-ureport-and-attach-case-ID-to-urep.patch
Patch150: 0150-rhtsupport-check-for-hints-only-when-creating-a-new-.patch
Patch151: 0151-ureport-provide-default-URLs.patch
Patch152: 0152-ureport-include-AuthDataItems-if-SSLClientAuth-is-co.patch
Patch153: 0153-report_RHTSupport-adapt-event-to-the-recent-changes.patch
Patch154: 0154-lib-fix-a-bug-in-ureport-response-parser.patch
Patch155: 0155-rhtsupport-re-prompt-for-credentials.patch
Patch156: 0156-rhtsupport-attach-the-contact-email-to-bthash.patch
Patch157: 0157-ureport-document-rhsm-entitlement-in-the-man-page.patch
Patch158: 0158-rhtsupport-send-ureport-before-creating-description.patch
Patch159: 0159-ureport-allow-multiple-cert-file-in-rhsm-entitlement.patch
Patch160: 0160-ureport-use-entit-certs-with-rhsm-and-drop-rhsm-enti.patch
Patch161: 0161-ureport-get-rhsm-entitlement-cert-dir-from-rhsm-conf.patch
Patch162: 0162-rhtsupport-never-use-uReport-URL-from-ureport.config.patch
Patch163: 0163-rhtsupport-do-not-leak-the-hints-results.patch
Patch164: 0164-ureport-fall-back-to-the-hardcoded-rhsm-cert-dir.patch
Patch165: 0165-ureport-fix-a-memory-leak-related-to-AuthDataItems.patch
Patch166: 0166-ureport-use-rhsm-ssl-client-auth-by-default.patch
Patch167: 0167-ureport-be-able-to-configure-ContactEmail-from-GUI.patch
Patch168: 0168-rhtsupport-be-able-to-turn-uReport-off-from-GUI.patch
Patch169: 0169-rhtsupport-move-RH-Portal-URL-c.-o.-to-Advanced-sect.patch
Patch170: 0170-testsuite-add-unittests-for-uReport-API.patch
Patch171: 0171-testsuite-changed-atlocal.in-to-work-with-last-commi.patch
Patch172: 0172-testsuite-do-not-expected-ureport-exiting-on-rhsm-ce.patch
#Patch173: 0173-spec-dump-the-log-files-of-failed-unit-tests.patch
Patch174: 0174-Client-API-introduce-non-iteractive-mode.patch
Patch175: 0175-ureport-introduce-HTTPAuth.patch
Patch176: 0176-Do-not-use-bool-in-OPT_BOOL-macro-it-expects-int.patch
Patch177: 0177-testsuite-adapt-ureport-test-to-rhel6.patch
Patch178: 0178-lib-add-functions-to-load-save-plugin-conf-files.patch
Patch179: 0179-lib-add-a-clone-function-for-map_string_t.patch
Patch180: 0180-problem_data-add-type-to-problem_data-in-add_basic.patch
Patch181: 0181-ureport-rename-its-event-to-submit_uReport.patch
#Patch182: 0182-spec-rename-the-ureport-event.patch
Patch183: 0183-RHTSupport-attach-reported_to-when-reporting-from-GU.patch
Patch184: 0184-file_obj-fix-a-null-pointer-derefference.patch
# $ git format-patch 2.0.9-22.el6 -N --start-number 185 --topo-order -o /home/repos/rhel/libreport/
Patch185: 0185-dd_sanitize-don-t-sanitize-symlinks.patch
Patch186: 0186-lib-introduce-a-new-function-copy_file_ext.patch
Patch187: 0187-dump_dir-allow-creating-of-a-new-dir-w-o-chowning-it.patch
Patch188: 0188-dump_dir-allow-hooks-to-create-dump-directory-withou.patch
Patch189: 0189-lib-add-a-function-checking-file-names.patch
Patch190: 0190-dd-harden-functions-against-directory-traversal-issu.patch
Patch191: 0191-lib-fix-races-in-dump-directory-handling-code.patch
Patch192: 0192-lib-add-alternative-dd-functions-accepting-fds.patch
# $ git format-patch 2.0.9-23.el6 -N --start-number 193 --topo-order -o /home/repos/rhel/libreport/
Patch193: 0193-dd-user-the-group-abrt-instead-of-the-user.patch
Patch194: 0194-dd-add-missing-return-statement.patch
# $ git format-patch 2.0.9-24.el6 -N --start-number 195 --topo-order -o /home/repos/rhel/libreport/
Patch195: 0195-wizard-fix-save-users-changes-after-reviewing-dump-d.patch
# $ git format-patch 2.0.9-25.el6_7 -N --start-number 196 --topo-order -o /home/repos/rhel/libreport/
Patch196: 0196-augeas-trim-spaces-arround.patch
# $ git format-patch 2.0.9-26.el6 -N --start-number 197 --topo-order -o /home/repos/rhel/libreport/
Patch197: 0197-curl-add-possibility-to-configure-SSH-keys.patch
Patch198: 0198-uploader-add-possibility-to-set-SSH-keyfiles.patch
#Patch199: 0199-spec-add-uploader-config-files-and-related-man-page.patch
# $ git format-patch 2.0.9-27.el6 -N --start-number 200 --topo-order -o /home/repos/rhel/libreport/
Patch200: 0200-dd-make-function-uid_in_group-public.patch
#Patch201: 0201-testsuite-add-test-for-uid_in_group.patch
Patch202: 0202-Bugzilla-private-bugs.patch
# $ git format-patch 2.0.9-28.el6 -N --start-number 203 --topo-order -o /home/repos/rhel/libreport/
Patch203: 0203-Add-uReport-reporter.patch
Patch204: 0204-report-gtk-Require-Reproducer-for-RHTSupport.patch
Patch205: 0205-Discourage-users-from-opening-one-shot-crashes.patch
Patch206: 0206-Discourage-users-from-reporting-problems-in-non-Red-.patch
Patch207: 0207-testsuite-add-problem-data-tests.patch
#Patch208: 0208-update-.gitignore.patch
#Patch209: 0209-spec-add-Problem-Format-API.patch
Patch210: 0210-lib-add-Problem-Format-API.patch
Patch211: 0211-rhtsupport-use-problem-report-API-to-create-descript.patch
Patch212: 0212-lib-problem-report-API-check-fseek-return-code.patch
# $ git format-patch 2.0.9-29.el6 -N --start-number 212 --topo-order -o /home/repos/rhel/libreport/
Patch213: 0213-ureport-attach-URL-of-uploaded-problem-data-to-uRepo.patch
Patch214: 0214-uploader-fix-compare-tmp-var-before-it-is-freed.patch
# $ git format-patch 2.0.9-30.el6 -N --start-number 215 --topo-order -o /home/repos/rhel/libreport/
Patch215: 0215-rhtsupport-add-pkg_vendor-reproducer-and-reproducibl.patch
Patch216: 0216-rhtsupport-attach-all-dump-dir-s-element-to-a-new-ca.patch
Patch217: 0217-configure-set-version-to-2.0.9.1.patch
# $ git format-patch 2.0.9-31.el6 -N --start-number 218 --topo-order -o /home/repos/rhel/libreport/
Patch218: 0218-dd-add-function-dd_get_env_variable.patch
#Patch219: 0219-testsuite-add-test-covering-of-dd_get_env_variable.patch
#Patch220: 0220-testsuite-add-a-forgotten-proc_helper.at-file.patch
# $ git format-patch 2.0.9-32.el6 -N --start-number 221 --topo-order -o /home/repos/rhel/libreport/
Patch221: 0221-workflow-Preventing-of-creating-a-customer-case-with.patch
Patch222: 0222-augeas-trim-spaces-before-key-value.patch
Patch223: 0223-reporter-mailx-rely-on-configured-email.patch
Patch224: 0224-problem_data-fix-segfault-if-last_occurrence-doesn-t.patch
Patch225: 0225-reporter-ureport-change-default-URL-to-FAF.patch
# $ git format-patch 2.0.9-33.el6 -N --start-number 226 --topo-order -o /home/repos/rhel/libreport/

#added by centos
Patch999: centos-disable-bugzilla.patch


# !!! Don't forget to add %%patch


BuildRequires: dbus-devel
BuildRequires: gtk2-devel
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: xmlrpc-c-devel
BuildRequires: python-devel
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: libtar-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: nss-devel
BuildRequires: texinfo
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: newt-devel
BuildRequires: libproxy-devel
BuildRequires: satyr-devel >= 0.16
BuildRequires: augeas-devel
BuildRequires: augeas
Requires: libreport-filesystem = %{version}-%{release}
# required for update from old report library, otherwise we obsolete report-gtk
# and all it's plugins, but don't provide the python bindings and the sealert
# end-up with: can't import report.GtkIO
# FIXME: can be removed when F15 will EOLed, needs to stay in rhel6!
Requires: libreport-python = %{version}-%{release}
# similarly, needed in order to update the system which has report-plugin-ftp/scp.
# FIXME: can be removed when F15 will EOLed, needs to stay in rhel6!
Requires: libreport-plugin-reportuploader = %{version}-%{release}
Requires: libreport-compat = %{version}-%{release}

# for rhel6
%if 0%{?rhel} == 6
BuildRequires: gnome-keyring-devel
%else
BuildRequires: libgnome-keyring-devel
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc...

%package filesystem
Summary: Filesystem layout for libreport
Group: Applications/File

%description filesystem
Filesystem layout for libreport

%package devel
Summary: Development libraries and headers for libreport
Group: Development/Libraries
Requires: libreport = %{version}-%{release}

%description devel
Development libraries and headers for libreport

%package python
Summary: Python bindings for report-libs
# Is group correct here? -
Group: System Environment/Libraries
Requires: libreport = %{version}-%{release}
Provides: report = 0.18-11
Obsoletes: report < 0.18-11
# in report the rhtsupport is in the main package, so we need to install it too
%if 0%{?rhel} >= 6
Requires: libreport-plugin-rhtsupport = %{version}-%{release}
%endif

%description python
Python bindings for report-libs.

%package cli
Summary: %{name}'s command line interface
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working
with problem dump reports

%package newt
Summary: %{name}'s newt interface
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: report-newt = 0.18-11
Obsoletes: report-newt < 0.18-11

%description newt
This package contains a simple newt application for reporting
bugs

%package gtk
Summary: GTK front-end for libreport
Group: User Interface/Desktops
Requires: libreport = %{version}-%{release}
Provides: report-gtk = 0.18-11
Obsoletes: report-gtk < 0.18-11

%description gtk
Applications for reporting bugs using libreport backend

%package gtk-devel
Summary: Development libraries and headers for libreport
Group: Development/Libraries
Requires: libreport-gtk = %{version}-%{release}

%description gtk-devel
Development libraries and headers for libreport-gtk

%package plugin-kerneloops
Summary: %{name}'s kerneloops reporter plugin
Group: System Environment/Libraries
Requires: curl
Requires: %{name} = %{version}-%{release}

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%package plugin-logger
Summary: %{name}'s logger reporter plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-logger < 2.0.4
Provides: report-plugin-localsave = 0.18-11
Obsoletes: report-plugin-localsave < 0.18-11
Provides: report-config-localsave = 0.18-11
Obsoletes: report-config-localsave < 0.18-11

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-mailx
Summary: %{name}'s mailx reporter plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: mailx
Obsoletes: abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%package plugin-bugzilla
Summary: %{name}'s bugzilla plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-bugzilla < 2.0.4
Provides: report-plugin-bugzilla = 0.18-11
Obsoletes: report-plugin-bugzilla < 0.18-11
Provides: report-config-bugzilla-redhat-com = 0.18-11
Obsoletes: report-config-bugzilla-redhat-com < 0.18-11

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%package plugin-rhtsupport
Summary: %{name}'s RHTSupport plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-rhtsupport < 2.0.4

%description plugin-rhtsupport
Plugin to report bugs into RH support system.

%package compat
Summary: %{name}'s compat layer for obsoleted 'report' package
Group: System Environment/Libraries
# bz should not be in the default configuration
#Requires: %%{name}-plugin-bugzilla = %%{version}-%%{release}
Requires: libreport = %{version}-%{release}
Requires: %{name}-plugin-rhtsupport = %{version}-%{release}

%description compat
Provides 'report' command-line tool.

%package plugin-reportuploader
Summary: %{name}'s reportuploader plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-reportuploader < 2.0.4
Provides: report-plugin-ftp = 0.18-11
Obsoletes: report-plugin-ftp < 0.18-11
Provides: report-config-ftp = 0.18-11
Obsoletes: report-config-ftp < 0.18-11
Provides: report-plugin-scp = 0.18-11
Obsoletes: report-plugin-scp < 0.18-11
Provides: report-config-scp = 0.18-11
Obsoletes: report-config-scp < 0.18-11

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%package plugin-ureport
Summary: %{name}'s micro report plugin
BuildRequires: json-c-devel
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description plugin-ureport
Uploads micro-report to abrt server

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch112 -p1
%patch113 -p1
#%patch114 -p1
%patch115 -p1
#%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
#%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
#%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
#%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
#%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
#%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
#%patch199 -p1
%patch200 -p1
#%patch201 -p1 0201-testsuite-add-test-for-uid_in_group.patch
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
#Patch208: 0208-update-.gitignore.patch
#Patch209: 0209-spec-add-Problem-Format-API.patch
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
#%patch219: 0219-testsuite-add-test-covering-of-dd_get_env_variable.patch
#%patch220: 0220-testsuite-add-a-forgotten-proc_helper.at-file.patch
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1

%patch999 -p1

%build
# rhbz#728190 remove pre-generated man pages, remove this line after rebase
rm -f src/plugins/*.1
mkdir -p m4
#rm libtool
rm ltmain.sh
test -r m4/aclocal.m4 || touch m4/aclocal.m4
aclocal
libtoolize
autoconf
automake --add-missing --force --copy
%configure --with-redhatbugzillacreateprivate=yes \
           --with-redhatbugzillaprivategroups=redhat
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
CFLAGS="-fno-strict-aliasing"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}
%find_lang %{name}

# remove all .la and .a files
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/events.d/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/events/

# After everything is installed, remove info dir
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post gtk
/sbin/ldconfig
# update icon cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%postun gtk
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gtk
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/plugins/
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/forbidden_words.conf
%{_libdir}/libreport.so.*
%{_libdir}/libabrt_dbus.so.*
%{_libdir}/libabrt_web.so.*
%exclude %{_libdir}/libabrt_web.so
%{_bindir}/report
%{_mandir}/man1/report.1.gz
%{_mandir}/man5/report_event.conf.5*
# filesystem package owns /usr/share/augeas/lenses directory
%{_datadir}/augeas/lenses/libreport.aug

%files filesystem
%defattr(-,root,root,-)
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/plugins/

%files devel
%defattr(-,root,root,-)
# Public api headers:
%{_includedir}/libreport/libreport_types.h
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/problem_report.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
%{_includedir}/libreport/file_obj.h
%{_includedir}/libreport/ureport.h
# Private api headers:
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%{_includedir}/libreport/global_configuration.h
%{_libdir}/libreport.so
%{_libdir}/libabrt_dbus.so
%{_libdir}/pkgconfig/libreport.pc
%dir %{_includedir}/libreport

%files python
%defattr(-,root,root,-)
%{python_sitearch}/report/*
%{python_sitearch}/reportclient/*

%files cli
%defattr(-,root,root,-)
%{_bindir}/report-cli
%{_mandir}/man1/report-cli.1.gz

%files newt
%defattr(-,root,root,-)
%{_bindir}/report-newt

%files gtk
%defattr(-,root,root,-)
%{_bindir}/report-gtk
%{_libdir}/libreport-gtk.so.*

%files gtk-devel
%defattr(-,root,root,-)
%{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc

%files plugin-kerneloops
%defattr(-,root,root,-)
%config %{_sysconfdir}/libreport/events/report_Kerneloops.xml
%{_mandir}/man*/reporter-kerneloops.*
%{_bindir}/reporter-kerneloops

%files plugin-logger
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/events/report_Logger.conf
%config %{_sysconfdir}/libreport/events/report_Logger.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%{_bindir}/reporter-print
%{_mandir}/man*/reporter-print.*

%files plugin-mailx
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/plugins/mailx.conf
%config %{_sysconfdir}/libreport/events/report_Mailx.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%{_mandir}/man*/reporter-mailx.*
%{_bindir}/reporter-mailx

%files plugin-bugzilla
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%config %{_sysconfdir}/libreport/events/report_Bugzilla.xml
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
# FIXME: remove with the old gui
%{_mandir}/man1/reporter-bugzilla.1.gz
%{_bindir}/reporter-bugzilla

%files plugin-rhtsupport
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/plugins/rhtsupport.conf
%config %{_sysconfdir}/libreport/events/report_RHTSupport.xml
%config %{_sysconfdir}/libreport/events/report_RHTSupportAttach.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
%{_mandir}/man1/reporter-rhtsupport.1.gz
%{_bindir}/reporter-rhtsupport

%files compat
%defattr(-,root,root,-)
%{_bindir}/report
%{_mandir}/man1/report.1.gz

%files plugin-reportuploader
%defattr(-,root,root,-)
%{_mandir}/man*/reporter-upload.*
%{_bindir}/reporter-upload
%config %{_sysconfdir}/libreport/events/report_Tarball.xml
%config %{_sysconfdir}/libreport/events/report_Uploader.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/tarball_event.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/upload.conf
%{_mandir}/man5/upload.conf.5.*
%config(noreplace) %{_sysconfdir}/libreport/events/report_Uploader.conf
%{_mandir}/man5/report_Uploader.conf.5.*


%files plugin-ureport
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/plugins/ureport.conf
%config %{_sysconfdir}/libreport/events/report_uReport.xml
%{_bindir}/reporter-ureport
%{_mandir}/man1/reporter-ureport.1.gz
%{_mandir}/man5/ureport.conf.5.gz

%changelog
* Tue Jun 19 2018 Johnny Hughes <johnny@centos.org> - 2.0.9-34
- disable the redhat.com bugzilla, set to example instead
- verify rht-support has no url path

* Tue Jan 23 2018 Martin Kutlak <mkutlak@redhat.com> - 2.0.9-34
- Correctly trim spaces before values with augeas
- Prevent creating of customer case without reproducing knowledge
- Rely on configurated email
- Change URL in config for bug-report server
- Fix segfaulting abrt-cli
- Related #1422030, #1328768, #1323625, #1463316, #1421754

* Wed Nov 02 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-33
- Avoid infinite crash loops
- Related: #1324586

* Thu Feb 25 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-32
- Rebuild because of failed rpmdiff
- Related: #1261398

* Wed Feb 24 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-31
- Add pkg_vendor, reproducer and reproducible to description
- Attach all dump dir's element to a new case
- Change libreport-version to 2.0.9.1
- Resolves: #1261398

* Fri Jan 29 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-30
- Attach URL of uploaded problem data to uReport
- Resolves: #1300777

* Fri Jan 22 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-29
- Change reporting workflow to enhance the quality of opened customer cases
- Limit the description section for ABRT reported cases
- Resolves: #1258474, #1261398

* Mon Jan 11 2016 Matej Habrnal <mhabrnal@redhat.com> - 2.0.9-28
- Make function uid_in_group() public
- Bugzilla private bugs
- Resolves: #1279454, #803769

* Tue Dec 8 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-27
- Enable configuration of SSH keys in report-upload
- Resolves: #1261120

* Thu Nov 19 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-26
- Correct augeas configuration parser
- Resolves: #1262246

* Sun Nov 15 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-25
- save all files changed by the reporter in the reporting GUI
- Fixes CVE-2015-5302
- Resolves: #1282144

* Fri May 22 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-24
- switch ownership of new directories from "abrt:user" to "user:abrt"
- fix a bug allowing libreport to read files outside dump directories
- Related: #1212095

* Fri May 15 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-23
- resolve symbolic and hard link vulnerabilities
- defend against directory traversal attack
- Resolves: #1212095

* Tue Feb 24 2015 Jakub Filak <jfilak@redhat.com> - 2.0.9-22
- Upstream uReport with Strata integration
- Resolves: #1152222

* Thu Jun 19 2014 Jakub Filak <jfilak@redhat.com> - 2.0.9-21
- Rebuild due to translation updates
- Resolves: #989530, #997871, #1090466, #1093375

* Thu Jun 19 2014 Jakub Filak <jfilak@redhat.com> - 2.0.9-20
- Bugzilla: pass Bugzilla_token in all XML RPC calls
- mailx: improve notification e-mail headers
- mailx: include hostane in notification e-mail
- Resolves: #989530, #997871, #1090466, #1093375

* Tue Aug 13 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-19
- updated transaltion (ko) rhbz#993626
- fixed bugzilla reporter to work with the new xmlrpc api rhbz#991088
- Resolves: #991088, #993626

* Wed Aug  7 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-18
- rebuild because of failed rpmdiff
- Related: #993626

* Tue Aug  6 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-17
- updated translation rhbz#993626
- fixed bugs doscovered by coverity rhbz#905051
- Resolves: #993626, #905051

* Fri Jun  7 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-16
- ABRT won't install debuginfos from rhn repository rhbz#759443
- Brewtap reports LibMissingRELRO rhbz#812283
- libreport attached sosreport into bugzilla with bad mimetype rhbz#885509
- reporter-rhtsupport on RHEL6.4 unable to open cases in RHT customer center rhbz#896090
- Change default set of reporters shown by CLI/GUI rhbz#948286
- [RFE] add the console notification to RHEL6 rhbz#961231
- Resolves: #885509, #812283, #961231, #961231, #961231, #948286, #759443, #896090, #875260

* Fri Jan 18 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-15
- rebuilding beacause of failed rpmdiff - no changes
- Related: #895443

* Fri Jan 18 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-14
- in same cases we have to follow symlinks
- Related: #895443

* Wed Jan 16 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-13
- don't follow symlinks
- Resolves: #895443

* Mon Jan  7 2013 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-12
- fixed relro flags
- removed confusing warning message
- added versioned requirements to silence rpmdiff
- Resolved: #847291, #812283, #857425

* Thu Oct 18 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-11
- removed reporter-bugzilla from config file re-added by mistake
- Related: #815339

* Thu Oct 18 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-10
- updated translation rhbz#864025
- fixed brewtap warnings rhbz#812283
- silence few rpmdiff warnings rhbz#857425
- Resolves: #864025, #812283, #857425

* Fri Sep 14 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-9
- don't show the user credentials in logs rhbz#856960
- Resolves: #856960

* Wed Aug 29 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-8
- use the default template for bz reports rhbz#747410
- fix adding users to CC in bugzilla rhbz#841338
- Resolves: #747410, #841338

* Thu Aug 23 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-7
- don't warn about daemon connection when deleting a problem rhbz#799909
- ignore non problem dirs when cleaning old problems rhbz#847291
- Resolves: #799909, #847291

* Thu Aug 09 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-6
- opt kernel out of showing smolt information in abrt bug reports. rhbz#795548
- ABRT mailx plugin on by default causes crashes being always labelled as reported rhbz#803618
- pkg-config --cflags libreport includs -fPIC rhbz#803736
- Coverity revealed memory leaks and possibly other issues rhbz#809416
- GLib warnings by report-gtk when crash dir does not exist rhbz#813283
- `report' tool requires current working directory to be a crash dir rhbz#817051
- Searching for duplicate anaconda bugs while reporting exception against partner-bugzilla during install fails rhbz#820985
- Undefined non-weak symbols rhbz#826745
- ABRT has wrong URL in dialog
Resolves: #809416,#813283,#817051,#826745,#820985,#795548,#803618,#803736

* Wed May 23 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-5
- rebuild due to rpmdiff
- Resolves: #823411

* Tue May 22 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-4
- fixed compatibility with bugzilla 4.2
- Resolves: #823411

* Fri Mar 16 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-3
- added notify-only option to mailx rhbz#803618
- Resolves: #803618

* Tue Mar 06 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-2
- minor fix in debuginfo downloader
- updated translations
- Related: #759377

* Wed Feb 15 2012 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.9-1
- new upstream release
- fixed typos in man
- fixed handling of anaconda-tb file
- generate valid xml file
- Resolves: #759377, #758366, #746727

* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-20
- fixed i18n initialization
- Resolves: #749148

* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-19
- rebuild, some translations were not propagated to xml files
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-18
- updated translations
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-17
- minor spec file fix
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-16
- minor fix to the search kbase
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-15
- fix the kbase searching rhbz#743198
- updated translation Related: #731037
- Resolves: #743198 #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com>
- fix the spec file changelog
- Resolves: #742474

* Fri Oct 21 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- abrt-cli uses wrong return codes
- Resolves: #742474

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-14
- reaply the man pages patch
- Resolves: #728190

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-13
- bumped release
- Resolves: #731037

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-12
- updated translation rhbz#731037
- search kbase before creating the ticket rhbz#743198
- Resolves: #731037 #743198

* Tue Oct 18 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- man pages contain suspicious version string
  Resolves: #728190

* Thu Oct 13 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-11
- disabled bugzilla rhbz#739936
- own /etc/libreport/plugins/ rhbz#744782
- removed unused patches to make rpmdiff happy
- updated translation
- Resolves: #739936 #744782

* Wed Sep 21 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-10
- make wizard page titles translatable
- updated transaltion
- Resolves: #734789 #731037

* Wed Aug 31 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-9
- fixed make check rhbz#729686
- fixed attaching anaconda-tb* rhbz#731389
- Resolves: #729686 #731389

* Fri Aug 26 2011 Nikola Pajkovsky <npajkovs@redhat.com> - 2.0.5-8
- Missing man pages of report and report.conf
  Resolves: #729957
- Update translations
  Resolves: #731037

* Thu Aug 25 2011 Denys Vlasenko <dvlasenk@redhat.com> - 2.0.5-7
- Fix report-cli crash if config files are missing.
  Resolves: #730942
- Pull in libreport-plugin-reportuploader on update
  (fixes a problem with "yum update" on RHEL system with old report package.
  Resolves: #732683

* Tue Aug 23 2011 Karel Klíč <kklic@redhat.com> - 2.0.5-6
- Added two patches (libreport-code-was-moved-to-abrt.git,
  libreport-fix-d-delete-option) from upstream making report-cli
  -d/--delete to remove DUMP_DIR after reporting. First patch also
  removes --list and --info and --full options, which were already
  moved to abrt-cli.
  Resolves: #726097
- Added fallback text editor for editing multiline fields in Anaconda
  Resolves: #728479

* Fri Aug 05 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-5
- added the report cmdline tool rhbz#725660
- fixed man pages version rhbz#728190
- fixed text wrapping rhbz#728132
- improved dump_dir detection rhbz#728166
- fixed reporting from Anaconda newt ui rhbz#729566
- added defualt config file for rhtsupport rhbz#729566
- make reporters use default conf when -c is not used rhbz#729986
- Resolves: #725660 #728190 #728132 #728166 #729566 #729986

* Tue Aug 02 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-4
- further improvement in Anaconda compatibility rhbz#727243
- warn silently when keyring is not available rhbz#725858
- Resolves: #727243 #725858

* Thu Jul 28 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-3
- improved compatibility with bugzilla
- enabled bugzilla for libreport reports (analyzer=libreport)
- Resolves: #725857

* Mon Jul 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-2
- removed mailx from possible reporter list (still enabled as post-create event)
- added python bindings to libreport client lib
- honor reporters minimal rating
- fixed (null) in bz summary
- Related: #714045

* Mon Jul 18 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-1
- move reporter plugins from abrt to libreport
- fixed provides/obsolete to properly obsolete report package
- wizard: make more fields editable
- Related: #697494

* Tue Jul 12 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-4
- added the python bindings -> obsoleting report

* Mon Jul 11 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-3
- bump release

* Mon Jun 27 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-2
- removed Provides/Obsoletes: report-gtk
- Resolves: #715373

* Mon Jun 20 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-1
- new upstream release
- cleaned some header files

* Thu Jun 16 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.3-1
- added report-cli
- updated translation

* Wed Jun 01 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.2-1
- initial packaging
