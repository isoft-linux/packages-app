Name:       bomi
Summary:    A multimedia player
License:    GPLv2
Version:    0.9.11
Release:    5%{?dist}
Url:        http://bomi.github.io/
Source0:    https://github.com/xylosper/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch0: bomi-customized.patch
Patch1: bomi-add-zh-trans.patch
Patch2: bomi-always-use-utf8-to-load-playlist.patch

BuildRequires:  ffmpeg-devel
BuildRequires:  bzip2-devel
BuildRequires:  libvdpau-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qtbase-devel >= 5.1.1
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquickcontrols
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  gcc >= 4.8
BuildRequires:  glib2-devel
BuildRequires:  libass-devel
BuildRequires:  libbluray-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libchardet-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libmpg123-devel
BuildRequires:  libva-devel
BuildRequires:  python
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
Requires: qt5-qtquickcontrols

%description
bomi is a Qt-based multimedia player utilizing the MPV video back-end.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
./configure --prefix=/usr \
    --disable-jack \
    --disable-samba \
    --enable-pulseaudio \
    --enable-vdpau \
    --enable-vaapi \
    --enable-cdda \
    --mandir=%{_mandir}
make %{?_smp_mflags}

%install
make DEST_DIR=%{buildroot} install

#bug skin
rm -rf %{buildroot}%{_datadir}/bomi/skins/Freya

#move solid actions from kde4 location to kf5
mkdir -p %{buildroot}%{_datadir}/solid/actions
mv %{buildroot}%{_datadir}/apps/solid/actions/bomi-opendvd.desktop %{buildroot}%{_datadir}/solid/actions
rm -rf %{buildroot}%{_datadir}/apps

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%files
%doc COPYING.txt CHANGES.txt GPL.txt ICON-AUTHORS.txt ICON-COPYING.txt MPL.txt README.md
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/solid/actions/*
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/bash-completion/completions/bomi
%{_mandir}/man1/bomi.1.gz

%changelog
* Sat Nov 21 2015 Cjacker <cjacker@foxmail.com> - 0.9.11-5
- disable mpris2 option by default

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.9.11-4
- Rebuild for new 4.0 release

* Thu Oct 15 2015 Cjacker <cjacker@foxmail.com> - 0.9.11-2
- set up default theme, window size and other settings.
- enable Bar visulization when play audio.

* Sun Jul 19 2015 Cjacker <cjacker@foxmail.com> - 0.9.11-1
- initial build.
