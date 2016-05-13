Name: isoft-update-client
Version: 1.0.5
Release: 1%{?dist}
Summary: iSOFT Update Client

License: GPLv2 or GPLv3
URL: http://git.isoft.zhcn.cc/zhaixiang/isoft-update-client
Source0: %{name}-%{version}.tar.bz2

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: pkgconfig
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires: systemd-units
BuildRequires: systemd-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: xz-devel
BuildRequires: librpm-devel
BuildRequires: popt-devel
BuildRequires: libtar-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquickcontrols-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-plasma-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: plasma-workspace-devel
BuildRequires: NetworkManager-glib-devel

Requires: kf5-filesystem
Requires: systemd 
Requires: os-release
Requires: os-update

Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description
iSOFT Update Client.


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

%find_lang plasma_applet_org.kde.plasma.isoftupdate

%post
%systemd_post isoft-update-daemon.service

%preun
%systemd_preun isoft-update-daemon.service

%postun
%systemd_postun isoft-update-daemon.service


%files -f plasma_applet_org.kde.plasma.isoftupdate.lang
%{_sysconfdir}/isoft-update.conf
%{_sysconfdir}/dbus-1/system.d/org.isoftlinux.Update.conf
%{_datadir}/dbus-1/interfaces/org.isoftlinux.Update.xml
%{_datadir}/dbus-1/system-services/org.isoftlinux.Update.service
%{_unitdir}/isoft-update-daemon.service
%{_bindir}/isoft-update-daemon
%{_bindir}/isoft-update-console
# kcm
%{_kf5_qtplugindir}/kcm_isoftupdate.so
%{_kf5_datadir}/kservices5/kcm_isoftupdate.desktop
%{_kf5_qtplugindir}/kcm_isoftupdate_viewer.so
%{_kf5_datadir}/kservices5/kcm_isoftupdate_viewer.desktop
# plasmoid
%{_qt5_prefix}/qml/org/kde/plasma/isoftupdate/libplasma_applet_isoftupdate.so
%{_qt5_prefix}/qml/org/kde/plasma/isoftupdate/qmldir
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.isoftupdate/
%{_datadir}/plasma/plasmoids/org.kde.plasma.isoftupdate/contents
%{_datadir}/plasma/plasmoids/org.kde.plasma.isoftupdate/metadata.desktop
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.isoftupdate.desktop


%changelog
* Fri May 13 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0.5-1
- set lc_all for grub.cfg

* Thu Jan 28 2016 fj <fujiang.zhu@i-soft.com.cn>
- Update qml,add i18n

* Fri Jan 22 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Release v1.0.3 for fujiang.

* Tue Jan 19 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0.2-2
- Update qml

* Fri Jan 15 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix daemon update duplicate upt packages by fujiang.

* Thu Jan 14 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix update xml file exsist issue.

* Fri Dec 11 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Changed the name of the enum to HiddenStatus.

* Thu Dec 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- HideMyselfStatus implemented.

* Mon Nov 30 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Use g_spawn_command_line_sync instead of system.
- Use KWorkSpace::requestShutDown instead of system.

* Fri Nov 27 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Disable default button.

* Tue Nov 24 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Remove plasma noizzzy network and other error.

* Mon Nov 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add HTTP header 404 check.

* Tue Nov 03 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- fujiang fix rpm-helper install rpm list issue.
- fujiang update kcm and plasmoid UI.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.2.0-4
- Rebuild for new 4.0 release

* Tue Oct 20 2015 Cjacker <cjacker@foxmail.com>
- add requires to os-release/os-update

* Fri Oct 16 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- updates.xml provided by other package.

* Wed Oct 14 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix daemon issue.
- Update plasmoid UI.
