Name: isoft-package-installer
Version: 0.4.0
Release: 1%{?dist}
Summary: iSOFT Package Installer

License: GPLv2 or GPLv3
URL: http://git.isoft.zhcn.cc/zhaixiang/isoft-package-installer
Source0: %{name}-%{version}.tar.bz2

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: systemd-units
BuildRequires: systemd-devel
BuildRequires: xz-devel
BuildRequires: librpm-devel
BuildRequires: popt-devel
BuildRequires: libtar-devel
BuildRequires: zlib-devel
BuildRequires: dpkg-devel
BuildRequires: bzip2-devel
BuildRequires: libelfutils-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-ki18n-devel

Requires: kf5-filesystem
Requires: systemd 
Requires: os-release
Requires: os-update

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
iSOFT Package Installer.


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

%find_lang isoftpackageinstaller

%post
%systemd_post isoft-install-daemon.service

%preun
%systemd_preun isoft-install-daemon.service

%postun
%systemd_postun isoft-install-daemon.service


%files -f isoftpackageinstaller.lang
%{_sysconfdir}/dbus-1/system.d/org.isoftlinux.Install.conf
%{_datadir}/dbus-1/interfaces/org.isoftlinux.Install.xml
%{_datadir}/dbus-1/system-services/org.isoftlinux.Install.service
%{_unitdir}/isoft-install-daemon.service
%{_bindir}/isoft-install-daemon
# greeter
%{_kf5_bindir}/isoft-package-installer
%{_kf5_datadir}/applications/isoft-package-installer.desktop

%changelog
* Tue Nov 24 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use yetist deb2rpm mkapp.

* Mon Nov 23 2015 dingkai - 0.3.0-3
- install deb file update the file of po

* Fri Nov 20 2015 dingkai - 0.2.0-2
- change po

* Wed Nov 18 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix install deb file issue.
- Update UI by dingkai.

* Tue Nov 17 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Release 0.1.0
