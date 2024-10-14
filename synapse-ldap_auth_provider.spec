Name:		synapse-ldap_auth_provider
Version:	0.3.0
Release:	1
Source0:	https://github.com/matrix-org/matrix-synapse-ldap3/archive/refs/tags/v%{version}.tar.gz
Summary:	LDAP authentication support for the Synapse Matrix server
URL:		https://github.com/matrix-org/matrix-synapse-ldap3
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch
Requires:	synapse

%description
Allows synapse to use LDAP as a password provider.

This allows users to log in to synapse with their
username and password from an LDAP server.

%prep
%autosetup -p1 -n matrix-synapse-ldap3-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/ldap_auth_provider.py
%{py_sitedir}/__pycache__/*
%{py_sitedir}/matrix_synapse_ldap3-%{version}.dist-info
