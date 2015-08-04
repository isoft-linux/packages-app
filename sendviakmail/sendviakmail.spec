Name:		sendviakmail
Version:	0.1
Release:	1
Summary:	Dolphin servicemenu and kmail2thunderbird wrapper.

License:    GPL	
Source0:    %{name}.tar.gz	

BuildRequires:	kdelibs-devel, kdepimlibs-devel
Requires:	kde-baseapps, thunderbird

%description
%{summary}

%prep
%setup -q -n %{name}

%build
make

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/kmail
%{_datadir}/kservices5/ServiceMenus/*

%changelog

