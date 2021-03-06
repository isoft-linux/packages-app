Name: firstboot-qt
Version: 1.0
Release: 13
Summary: First boot setup wizard

License: GPLv2
Source0: %{name}-%{version}.tar.gz
Patch1: firstboot-not-run.patch
BuildRequires: git cmake qt5-qtbase-devel qt5-qttools-devel gnome-desktop3-devel
BuildRequires: kf5-ki18n-devel
Requires: qt5-qtbase

%description
The setup wizard after system installed and first booting.

%prep
%setup -n %{name}
%patch1 -p1

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
* Thu Dec 08 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0-13
- rebuilt:get os version from file.

* Fri Jan 29 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0-12
- modify run-firstboot to fix bug 13171.

* Fri Jan 08 2016 xiaotian.wu@i-soft.com.cn - 1.0-11
- fixed bug 13171.

* Fri Jan 08 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0-10
- set lc=utf8 when config grub 

* Mon Jan 04 2016 fj <fujiang.zhu@i-soft.com.cn> - 1.0-9
- modify grub;change pwd; 

* Fri Dec 18 2015 fujiang <fujiang.zhu@i-soft.com.cn> - 1.0-8
- update autologin

* Mon Dec 07 2015 fujiang <fujiang.zhu@isoft.com.cn> - 1.0-7
- update language

* Tue Dec 01 2015 fujiang <fujiang.zhu@isoft.com.cn> - 1.0-6
- update

* Thu Nov 19 2015 fujiang <fujiang.zhu@isoft.com.cn> - 1.0-5
- add background pictures;update root pwd;

* Wed Nov 04 2015 fujiang <fujiang.zhu@isoft.com.cn> - 1.0-4
- update:set keylayout

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.0-3
- Rebuild for new 4.0 release

