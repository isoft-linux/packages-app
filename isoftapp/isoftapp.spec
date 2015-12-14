Name: isoftapp
Version: 1.0.1
Release: 1%{?dist}
Summary: iSOFT AppStore Skeleton

License: GPLv2 or GPLv3
URL: http://git.isoft.zhcn.cc/zhaixiang/isoftapp
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: pkgconfig
BuildRequires: glib2-devel
BuildRequires: librpm-devel
BuildRequires: popt-devel
BuildRequires: uriparser-devel
BuildRequires: libcurl-devel
BuildRequires: sqlite-devel


%description
iSOFT AppStore Skeleton.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%{_sysconfdir}/isoftapp/default.conf.example
%{_sysconfdir}/isoftapp/config.d/other.conf.example
%{_datadir}/isoftapp/pkgcache.db
%{_bindir}/isoft-genpkglist
%{_bindir}/isoft-gensrclist
%{_bindir}/isoft-genbasedir
%{_bindir}/isoftapp

%changelog
* Mon Dec 14 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Cleanup command info. 

* Fri Dec 11 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Full features support by fujiang.
- Fix upgrade issue.

* Thu Dec 10 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Add list-uninstalled and upgrade by fujiang.

* Wed Dec 09 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Rename gen* to isoft-gen* to avoid conflict with apt package.
- New configuration multi-repos support.
- Show detail error notice for configuration file.
- Add remove confirm.
- Add list-installed by fujiang.

* Tue Dec 08 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Release isoftapp v0.1.0 only support update, install, remove, check by fujiang.

