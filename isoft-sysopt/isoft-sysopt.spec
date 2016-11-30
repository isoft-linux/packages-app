Name: isoft-sysopt
Version: 1.0.0
Release: 1
Summary: viewing internet speed and memory use on your system.

License: GPLv2 or GPLv3
URL: git@git.isoft.zhcn.cc:wangxiaomei/isoftsysopt.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtquick1-devel
BuildRequires: qt5-qtquickcontrols-devel
BuildRequires: libpcap-devel
BuildRequires: ncurses-devel
BuildRequires: glibc-devel
BuildRequires: procps-ng-devel

Requires: python2

%description
Viewing internet speed and memory use on your system.

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
%{_libdir}/python2.7/dist-packages/isoft-assistant-daemon/*

%changelog
* Mon Oct 31 2016 x <ming.wang@i-soft.com.cn> - 0.1.0-1
- Version 1.0.0-1.

