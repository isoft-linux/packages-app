Name:           kcm-pointing-devices
Version:        0.1 
Release:        3
Summary:        User accounts manager for plasma workspace 

License:        GPLv3+
#https://quickgit.kde.org/?p=scratch%2Falexandermezin%2Fpointing-devices-kcm.git
Source0:        pointing-devices-kcm.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-rpm-macros


%description

%prep
%setup -q -n pointing-devices-kcm

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%{_kf5_libdir}/libpointingdevices.so
%{_kf5_qtplugindir}/kcms/kcm_pointingdevices.so
%{_kf5_qtplugindir}/kf5/kded/pointingdevices.so
%{_kf5_qtplugindir}/libpointingdevices_x11.so
%{_kf5_datadir}/kservices5/kcm_pointingdevices.desktop
%{_kf5_datadir}/kpackage/kcms/kcm_pointingdevices

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.1-3
- Rebuild for new 4.0 release

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

