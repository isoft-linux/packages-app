Name:		kf5-kmozillahelper
Version:	0.6.4
Release:	4.git
Summary:    Mozilla kde integration	

License:    GPL	
#https://github.com/cruiseliu/kmozillahelper-frameworks.git
Source0:    kmozillahelper-frameworks.tar.gz
Patch0:     kmozillahelper-frameworks-fix-build.patch
Patch1:     kmozillahelper-add-filter-support.patch
 
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-knotifications-devel


%description
%{summary}

%prep
%setup -q -n kmozillahelper-frameworks
%patch0 -p1
%patch1 -p1

%build
mkdir -p build
pushd build
%{cmake_kf5} ..
make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd

#remove notifyrc.
rm -rf %{buildroot}%{_datadir}/kmozillahelper

%files
%{_libdir}/mozilla/kmozillahelper

%changelog
* Thu Nov 19 2015 Cjacker <cjacker@foxmail.com> - 0.6.4-4.git
- Remove notifyrc

* Thu Nov 19 2015 Cjacker <cjacker@foxmail.com> - 0.6.4-3.git
- Add filters support

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.6.4-2.git
- Rebuild for new 4.0 release

* Sun Jul 19 2015 Cjacker <cjacker@foxmail.com>
- add patch1 to fix build
