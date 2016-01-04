Name:           kcm-useraccount
Version:        5.4.2
Release:        2
Summary:        User accounts manager for plasma workspace 

License:        GPLv3+
Source0:        kuseraccount-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  libpwquality-devel
BuildRequires:  polkit-qt5-1-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kwallet-devel
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
* Mon Jan 04 2016 fujiang <fujiang.zhu@i-soft.com.cn> - 5.4.2-2
- change password rule

* Tue Nov 24 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix polkit sync API blocking issue.

* Mon Nov 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix kcm_useraccount.desktop Name and Comment issue.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 5.4.0-5
- Rebuild for new 4.0 release

* Wed Aug 26 2015 Cjacker <cjacker@foxmail.com>
- update to 5.4.0

