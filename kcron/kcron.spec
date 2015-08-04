Name:    kcron
Summary: Cron KDE configuration module
Version: 15.04.3
Release: 2%{?dist}

License: GPLv2+
URL:     https://projects.kde.org/projects/kde/kdeadmin/kcron
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
#BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kitemviews-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: pkgconfig(Qt5Widgets) pkgconfig(Qt5PrintSupport)
#BuildRequires: libappstream-glib

Conflicts:      kdeadmin < 4.10.80
Obsoletes:      kdeadmin < 4.10.80

%description
Systemsettings module for the cron task scheduler.

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


%check
#appstream-util validate-relax --nonet %{buildroot}%{_kf5_datadir}/appdata/%{name}.appdata.xml ||:
#desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.%{name}.desktop ||:


%files
%doc COPYING*
%doc README
#{_kf5_bindir}/%{name}
#{_kf5_libdir}/libkdeinit5_%{name}.so
#{_sysconfdir}/xdg/%{name}.knsrc
#{_kf5_datadir}/applications/org.kde.%{name}.desktop
#{_datadir}/appdata/%{name}.appdata.xml
#{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
#{_kf5_datadir}/%{name}/
%{_kf5_docdir}/HTML/en/%{name}/
#{_kf5_datadir}/kconf_update/%{name}*
#{_kf5_datadir}/kxmlgui5/%{name}/
#{_kf5_datadir}/sounds/%{name}/
#{_kf5_datadir}/config.kcfg/%{name}.kcfg
%{_kf5_qtplugindir}/kcm_cron.so
%{_kf5_datadir}/kservices5/kcm_cron.desktop


%changelog
