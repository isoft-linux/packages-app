Name: kdenetwork-filesharing
Version: 15.08.1
Release: 1%{?dist}
Summary: netshare for KF5

License: GPLv2 or GPLv3
URL: https://projects.kde.org/projects/kde/kdenetwork/kdenetwork-filesharing
Source0: %{name}-%{version}.tar.xz

# Migrated to KF5
Patch1: 0001-migrated-to-kf5.patch

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kwidgetsaddons-devel


Requires: kf5-filesystem


%description
netshare for KF5.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_kf5_qtplugindir}/sambausershareplugin.so
%{_kf5_datadir}/kservices5/sambausershareplugin.desktop


%changelog
* Fri Oct 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Migrated to KF5
