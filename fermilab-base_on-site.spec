Name:		fermilab-base_on-site
Version:	1.0
Release:	6%{?dist}
Summary:	Pull in the packages required on the FNAL network

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-base_on-site

BuildArch:	noarch
Requires:	krb5-workstation

Requires:	fermilab-conf_doe-banner-console
Requires:	fermilab-conf_doe-banner-login-screen
Requires:	fermilab-conf_install-updates
Requires:	fermilab-conf_kerberos
Requires:	fermilab-conf_login-screen-no-user-list
Requires:	fermilab-conf_ocsinventory
Requires:	fermilab-conf_screenlock
Requires:	fermilab-conf_ssh-server
Requires:	fermilab-conf_system-logger

%if 0%{?rhel} >= 8 || 0%{?fedora} >= 27
# Recommends are installed by default with DNF
#  but can be removed without issue
Recommends:	fermilab-conf_email-gateway
Recommends:	fermilab-conf_firewall
Recommends:	fermilab-conf_ssh-client
Recommends:	fermilab-conf_sssd
Recommends:	fermilab-conf_timesync

# Suggests are not installed by default with DNF
#  and can be removed without issue
Suggests:	fermilab-conf_ca-certs
Suggests:	fermilab-util_makehostkeys
Suggests:	fermilab-util_kcron
%endif

%description
Using the network on site at Fermilab requires a some specific config
settings and applications.  This package provides one way to ensure
your system meets these requirements.


%prep


%build


%install


%files
%doc


%changelog
* Tue Mar 1 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-6
- Initial Build for EL9
- Use rich deps to match yum group defs (minus yum repo)

* Mon Feb 3 2020 Pat Riehecky <riehecky@fnal.gov> 1.0-5
- Hard requirement on Kerberos bits

* Wed Jan 29 2020 Pat Riehecky <riehecky@fnal.gov> 1.0-4
- Initial Build for EL8

* Mon Feb 29 2016 Pat Riehecky <riehecky@fnal.gov> 1.0-3
- build as noarch

* Tue Feb 9 2016 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- build as noarch

* Fri Aug 7 2015 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build for EL7
