Name:           kcm-useraccount
Version:        5.4.0
Release:        4 
Summary:        User accounts manager for plasma workspace 

License:        GPLv3+
Source0:        kuseraccount-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  boost-devel
# we need the unified libsystemd.so, which was introduced in systemd 209
BuildRequires:  systemd-devel >= 209
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-rpm-macros
BuildRequires: qt5-qtaccountsservice-devel >= 0.6.0
Requires: qt5-qtaccountsservice >= 0.6.0


%description
User accounts manager for the Plasma workspace.
A System Settings module for managing users on your system.

%prep
%setup -q -n kuseraccount-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ../
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kuseraccount
%files -f kuseraccount.lang
%{_kf5_qtplugindir}/kcm_useraccount.so
%{_kf5_datadir}/kdm/pics/users
%{_kf5_datadir}/kservices5/kcm_useraccount.desktop

%changelog
* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

