Name: freshplayerplugin 
Version: 0.3.4
Release: 1.git
Summary: PPAPI-host NPAPI-plugin adapter.

License: MIT
URL: https://github.com/i-rinat/freshplayerplugin
Source0: freshplayerplugin.tar.gz

BuildRequires: cmake 
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: ragel 
BuildRequires: alsa-lib-devel 
BuildRequires: openssl-devel
BuildRequires: glib2-devel 
BuildRequires: pango-devel 
BuildRequires: mesa-libGL-devel 
BuildRequires: libevent-devel 
BuildRequires: gtk2-devel
BuildRequires: libXrandr-devel 
BuildRequires: libXrender-devel 
BuildRequires: libXcursor-devel 
BuildRequires: libv4l-devel
BuildRequires: mesa-libGLES-devel  
BuildRequires: ffmpeg-devel 
BuildRequires: libva-devel 
BuildRequires: libvdpau-devel 
BuildRequires: libdrm-devel
BuildRequires: pulseaudio-libs-devel

%description
freshplayerplugin help firefox to use the latest flashplugin from Google Chrome.

%prep
%setup -q -n %{name}

%build
mkdir build
pushd build
%cmake ..
popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd


%files
%doc data/freshwrapper.conf.example
%{_libdir}/mozilla/plugins/libfreshwrapper-flashplayer.so

%changelog
* Mon Oct 12 2015 Cjacker <cjacker@foxmail.com>
- initial build
