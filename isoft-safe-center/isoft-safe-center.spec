Name: isoft-safe-center
Version: 1.0.0
Release: 1
Summary: Clean temporary files, optimize & speed up your computer.

License: GPLv2 or GPLv3
URL: git@git.isoft.zhcn.cc:wangxiaomei/isoftsysopt.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: polkit-qt5-1-devel
BuildRequires: polkit-qt5-1
BuildRequires: qt5-qtmultimedia-devel

Requires: qt5-qtbase
Requires: polkit-qt5-1
Requires: ph_sensor
Requires: libhddtemp
Requires: qt5-qtmultimedia
Requires: python2

%description
Clean temporary files, optimize & speed up your computer.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
qmake .. QMAKE_INSTALL_ROOT=%{buildroot}
make %{?_smp_mflags}
popd

%install
pushd %{_target_platform}
make install INSTALL_ROOT=%{buildroot}
popd

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_libdir}/python2.7/dist-packages/isoft-safe-daemon
%{_datadir}/dbus-1/system-services/*
%{_datadir}/polkit-1/actions/*
%{_datadir}/dbus-1/services/*
%{_sysconfdir}/dbus-1/system.d/*

%changelog
* Mon Oct 31 2016 x <ming.wang@i-soft.com.cn> - 0.1.0-1
- Version 1.0.0-1.

