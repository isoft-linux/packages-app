Name:		sendviakmail
Version:	0.1
Release:	2
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
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.1-2
- Rebuild for new 4.0 release


