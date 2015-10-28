Name:		kio-afc
Version:    0.1	
Release:	2
Summary:	kio slave implementation wrapping the AFC protocol

License:    GPL	
Source0:    kio_afc.tar.gz


BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  libimobiledevice-devel

%description
%{summary}

%prep
%setup -q -n kio_afc

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%{_kf5_plugindir}/kio/*.so
%{_kf5_datadir}/kservices5/*.protocol
%{_datadir}/remoteview/afc-network.desktop
%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.1-2
- Rebuild for new 4.0 release


