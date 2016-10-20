Name: knetshare
Version: 0.4.0
Release: 12
Summary: netshare for KF5

License: GPLv2 or GPLv3
URL: http://git.isoft.zhcn.cc/zhaixiang/knetshare
Source0: %{name}-%{version}.tar.bz2

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kdelibs4support-devel

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

%find_lang knetshare

%files -f knetshare.lang
# %{_kf5_qtplugindir}/sambausershareplugin.so
# %{_kf5_datadir}/kservices5/sambausershareplugin.desktop

# plugin of dolphin
%{_kf5_qtplugindir}/phodavsharedplugin.so
%{_datadir}/kservices5/fileshared.desktop

# %{_datadir}/dbus-1/interfaces/org.webdav.server.configuration.xml

# kcm plugin and desktop
%{_kf5_qtplugindir}/kcm_knetshare.so
%{_datadir}/kservices5/kcm_knetshare.desktop

# configuration is on dbus
%{_libexecdir}/isoft-netshare-configuration
%{_datadir}/dbus-1/services/org.isoft.netshare.service

# auto start executable
%{_bindir}/chezdavd
%{_datadir}/apps/knetshare/chezdavd.desktop

# translation
%{_datadir}/locale/zh_CN/LC_MESSAGES/knetshare.mo

%changelog
* Thu Oct 20 2016 x <ming.wang@i-soft.com.cn> - 0.4.0-12
- Integrate account manager in dolphin and KConfig Module.

* Thu Jun 02 2016 WangMing <ming.wang@i-soft.com.cn> - 0.4.0-10
- Add dependencies to po target.

* Thu Jun 02 2016 WangMing <ming.wang@i-soft.com.cn> 0.4.0-8
- restart when readonly option changed.

* Thu Jun 02 2016 WangMing <ming.wang@i-soft.com.cn> 0.4.0-6
- Validate port range and manage shared directory.

* Wed May 11 2016 WangMing <ming.wang@i-soft.com.cn> 0.4.0-4
- Fixed plugin can not shown.

* Wed May 11 2016 WangMing <ming.wang@i-soft.com.cn> - 0.4.0-2
- Add file shared service base on phodav.

* Thu Nov 26 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix rename share issue.
- Add special characters denied.

* Fri Nov 20 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Fix zh_CN po issue.

* Fri Oct 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Migrated to KF5
