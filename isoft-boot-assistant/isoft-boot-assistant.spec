Name: isoft-boot-assistant
Version: 0.1.0
Release: 1
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
%{_datadir}/autostart/%{name}.desktop

%changelog
* Mon Oct 31 2016 x <ming.wang@i-soft.com.cn> - 0.1.0-1
- Version 0.1.0-1.

