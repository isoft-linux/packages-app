Summary:    Mac OS X icns icon thumbnail generator  
Name:	    icnsthumbs
Version: 5.0 
Release:	1
License:	GPL
Source0:	%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kio-devel
BuildRequires: qt5-qtbase-devel 
BuildRequires: libicns-devel

%description
Mac OS X icns icon thumbnail generator

%prep
%setup -q

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%clean
rm -rf %{buildroot}

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/kservices5/icnsthumbs.desktop ||:


%files
%{_qt5_plugindir}/icnsthumbs.so
%{_kf5_datadir}/kservices5/icnsthumbs.desktop

