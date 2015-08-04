Name:       bomi
Summary:    A multimedia player
License:    GPLv2
Group:      Applications/Multimedia
Version:    0.9.11
Release:    1%{?dist}
Url:        http://bomi.github.io/
Source0:    https://github.com/xylosper/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

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

%post
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%postun
/usr/bin/update-desktop-database -q
xdg-icon-resource forceupdate --theme hicolor &> /dev/null

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/apps/solid/actions/*
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_mandir}/man1/bomi.1.gz

%doc COPYING.txt CHANGES.txt GPL.txt ICON-AUTHORS.txt ICON-COPYING.txt MPL.txt README.md

%changelog
* Sun Jul 19 2015 Cjacker <cjacker@foxmail.com> - 0.9.11-1
- first build.

* Tue Sep 30 2014 Ben R <thebenj88@gmail.com> - 0.8.16-1
- Upstream release

* Fri Jun 13 2014 Ben R <thebenj88@gmail.com> - 0.8.14-1
- Upstream release

* Fri Mar 21 2014 Ben R <thebenj88@gmail.com> - 0.8.13-1
- Upstream release
- Added libbluray-devel build dependency

* Sat Mar 08 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.12-1
- Upstream release

* Wed Feb 12 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.11-1
- Upstream release

* Sun Feb 09 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.10-1
- Upstream release
- Openal dependency removed; upstream has dropped openal support

* Mon Feb 03 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.9-1
- Upstream release

* Sun Feb 02 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.8-1
- Upstream release

* Sat Feb 01 2014 Ben Reedy <thebenj88@gmail.com> - 0.8.7-1
- Upstream release

* Thu Dec 12 2013 Ben Reedy <thebenj88@gmail.com> - 0.8.6-2
- Updated dependencies

* Sun Dec 01 2013 Ben Reedy <thebenj88@gmail.com> - 0.8.6-1
- Updated build instructions for OpenSUSE users.
- Updated build dependencies for OpenSUSE users.

* Sat Nov 30 2013 xylosper <darklin20@gmail.com> - 0.8.6-1
- Upstream Release
- New: new option 'Apply in fullscreen mode only' for 'Hide mouse cursor'
- Fix: hiding mouse cursor with Qt 5.2.0 didn't work (#22)
- Fix: crash when linked with Qt 5.2.0
- Fix: open file dialog will open in the folder where last played is located
- Fix: urlencoded URLs doesn't open when passed as a parameter (issue #18)
- Fix: volume normalizer is broken(issue #17)
