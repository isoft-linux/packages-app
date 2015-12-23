Name: kcm-pointing-devices
Version: 0.1 
Release: 5
Summary: Pointing devices configuration utility for KF5

License: GPLv3+
#https://quickgit.kde.org/?p=scratch%2Falexandermezin%2Fpointing-devices-kcm.git
Source0: pointing-devices-kcm.tar.gz

#script to extract pot file
Source1: Messages.sh

Source2: kcm_pointingdevices-zh_CN.po

Patch0: pointing-devices-desktop-i18n.patch
#the window size of 'kcmshell5 kcm_pointingdevices' is not correct.
Patch1: pointing-devices-kcm-fix-prefer-size.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel qt5-qtdeclarative-devel qt5-qttools-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kpackage-devel
BuildRequires:  pkgconfig(xcb) pkgconfig(xcb-event)

%description
%{summary}

%prep
%autosetup -n pointing-devices-kcm -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

mkdir -p %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES
msgfmt %{SOURCE2} -o %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm_pointingdevices.mo

%find_lang kcm_pointingdevices

%files -f kcm_pointingdevices.lang
%{_kf5_libdir}/libpointingdevices.so
%{_kf5_qtplugindir}/kcms/kcm_pointingdevices.so
%{_kf5_qtplugindir}/kf5/kded/pointingdevices.so
%{_kf5_qtplugindir}/libpointingdevices_x11.so
%{_kf5_datadir}/kservices5/kcm_pointingdevices.desktop
%{_kf5_datadir}/kpackage/kcms/kcm_pointingdevices

%changelog
* Tue Dec 22 2015 Cjacker <cjacker@foxmail.com> - 0.1-5
- Fix kcmshell5 kcm_pointingdevice window size

* Sat Dec 19 2015 Cjacker <cjacker@foxmail.com> - 0.1-4
- Add zh_CN po

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.1-3
- Rebuild for new 4.0 release

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

