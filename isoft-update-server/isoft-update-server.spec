Name: isoft-update-server 
Version: 1.0
Release: 1
Summary: iSoft update utility(Server side)
Vendor:  iSoft

License: GPL
#URL:  
Source0: %{name}-%{version}.tar.gz

BuildRequires:  libxml2-devel >= 2.9
BuildRequires:  libtar-devel >= 1.2
BuildRequires:  xz-devel >= 5.2

Requires: libxml2 libtar xz-libs

%description
iSoft update utility for server side. support upt package generation/vailidation/merging etc.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
#sign, we need to rename it.
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/isoft_update_server %{buildroot}%{_bindir}/%{name}

#?
mkdir -p %{buildroot}%{_datadir}/%{name}
cp %{_builddir}/%{name}-%{version}/doc/update.xsd %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/isoft-update-server
%dir %{_datadir}/isoft-update-server
%{_datadir}/isoft-update-server/update.xsd

%changelog

