Name: firstboot-qt
Version: 1.0
Release: 3 
Summary: First boot setup wizard

License: GPLv2
Source0: %{name}-%{version}.tar.gz
BuildRequires: git cmake qt5-qtbase-devel qt5-qttools-devel gnome-desktop3-devel
Requires: qt5-qtbase

%description
The setup wizard after system installed and first booting.

%prep
%setup -n %{name}

%build
mkdir -p build 
pushd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
make GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 DESTDIR=%{buildroot} install -C build

%find_lang firstboot-qt

%files -f firstboot-qt.lang
%defattr(-,root,root,-)
%{_bindir}/firstboot-qt
%{_bindir}/run-firstboot
%{_unitdir}/firstboot.service
%dir %{_datadir}/apps/firstboot
%{_datadir}/apps/firstboot/*

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.0-3
- Rebuild for new 4.0 release

