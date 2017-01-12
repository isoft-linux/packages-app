Name: isoft-boot-assistant
Version: 0.1.0
Release: 2
Summary: Boot assistant show the cost time of booting.

License: GPLv2 or GPLv3
URL: git@git.isoft.zhcn.cc:zhangjun/boot-qt.git
Source0: %{name}-%{version}.tar.gz

BuildRequires: qt5-qtbase-devel

Requires: qt5-qtbase

%description
show the cost time of booting.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
qmake ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
pushd %{_target_platform}
make install INSTALL_ROOT=%{buildroot}
popd

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/%{name}/*
%{_sysconfdir}/xdg/autostart/%{name}.desktop

%changelog
* Thu Jan 12 2017 x - 0.1.0-2
- Install desktopfile to /etc/xdg/autostart

* Mon Oct 31 2016 x <ming.wang@i-soft.com.cn> - 0.1.0-1
- Version 0.1.0-1.

