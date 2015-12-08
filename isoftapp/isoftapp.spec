Name: isoftapp
Version: 0.1.0
Release: 1%{?dist}
Summary: iSOFT App

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
iSOFT App.


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
%{_sysconfdir}/isoftapp/sources.list
%{_datadir}/isoftapp/pkgcache.db
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_bindir}/genbasedir
%{_bindir}/isoftapp

%changelog
* Tue Dec 08 2015 Leslie Zhai <xiang.zhai@i-soft.com.cn>
- Release isoftapp v0.1.0 only support update, install, remove, check by fujiang.

