Name:    kamera
Summary: Digital camera support for KDE 
Version: 15.04.3
Release: 2%{?dist}

License: GPLv2
URL:     https://projects.kde.org/projects/kde/kdegraphics/kamera
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: ftp://ftp.kde.org/pub/kde/%{stable}/%{version}/src/%{name}-%{version}.tar.xz

Patch0: kamera-port-to-kf5.patch
Patch1: kamera-15.04.3-port-to-kf5-2.patch

BuildRequires: kdelibs4-devel >= 4.14
BuildRequires: pkgconfig(libgphoto2)

%{?kde_runtime_requires}

# when split occurred
Conflicts: kdegraphics < 7:4.6.95-10

%description
%{summary}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%files
%doc AUTHORS README
%{_kf5_plugindir}/kio/kamera.so
%{_kf5_qtplugindir}/*.so
%{_kf5_datadir}/solid/actions/solid_camera.desktop
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_docdir}/HTML/en/kcontrol/%{name}/


%changelog
