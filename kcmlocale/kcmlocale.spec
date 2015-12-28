Name: kcmlocale
Version: 1.0
Release: 3
Summary: Locale setting tool for plasma desktop

License: GPLv3+
Source0: kcmlocale-%{version}.tar.gz
Patch0: remove-flags.patch

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: plasma-systemsettings-devel

Requires: kf5-kdelibs4support

Requires: kf5-ki18n

%description
Locale setting tool for the Plasma workspace.

%prep
%setup -q -n kcmlocale-%{version}
%patch0 -p1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kcmlocale

%files -f kcmlocale.lang
%{_kf5_qtplugindir}/kcm*.so
%{_kf5_datadir}/kservices5/*.desktop

%changelog
* Mon Dec 28 2015 xiaotian.wu@i-soft.com.cn - 1.0-3
- add patch to disable flags.

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 1.0-2
- Rebuild for new 4.0 release

* Fri Oct 16 2015 Cjacker <cjacker@foxmail.com>
- initial created.

