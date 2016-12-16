# we do not ship debug package of thunderbird.
%define debug_package %{nil}

Summary: Mozilla Thunderbird mail/newsgroup client
Name: thunderbird
Version: 38.3.0
Release: 19
URL: http://www.mozilla.org/projects/thunderbird/
License: MPL
Source0: thunderbird-%{version}.source.tar.bz2
Source1: thunderbird.desktop
Source4: thunderbird-mozconfig
Source10:  thunderbird-vendor.js
 
Source100: find-external-requires

Source200: thunderbird-kde.js

Patch0: thunderbird-install-dir.patch
Patch1: thunderbird-freetype26.patch

Patch10: thunderbird-mozilla-kde.patch
Patch11: thunderbird-firefox-kde.patch
Patch12: thunderbird-toolkit-download-folder.patch
Patch13: thunderbird-mozilla-nongnome-proxies.patch 

BuildRequires:  nss-devel 
BuildRequires:  nspr-devel
BuildRequires:  hunspell-devel 
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  libIDL-devel
BuildRequires:  gtk2-devel
BuildRequires:  krb5-devel
BuildRequires:  pango-devel
BuildRequires:  freetype-devel
BuildRequires:  libXt-devel
BuildRequires:  libXrender-devel
BuildRequires:  hunspell-devel
BuildRequires:  startup-notification-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libnotify-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libcurl-devel
BuildRequires:  libvpx-devel
BuildRequires:  autoconf213
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  sqlite-devel
BuildRequires:  libffi-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  zlib-devel, gzip, zip, unzip
BuildRequires:  yasm


Requires: nss
Requires: nspr
Requires: desktop-file-utils
Requires: hunspell

Obsoletes: MozillaThunderbird
Provides: MozillaThunderbird = %{version}

%define _use_internal_dependency_generator 0
%define __find_requires %{SOURCE100}

%description
Mozilla Thunderbird is a standalone mail and newsgroup client.

#===============================================================================

%prep
%setup -q -n comm-esr38
%patch0 -p1
%patch1 -p1

pushd mozilla
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
popd

cp -f %{SOURCE4} .mozconfig
echo "mk_add_options MOZ_MAKE_FLAGS='%{?_smp_mflags}'" >> .mozconfig

mkdir -p mozilla/js/src/.deps

#===============================================================================

%build
export MOZ_OPT_FLAGS=$(echo "$RPM_OPT_FLAGS -fpermissive" | \
                      %{__sed} -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')

export CFLAGS=$MOZ_OPT_FLAGS
export CXXFLAGS=$MOZ_OPT_FLAGS

make -f client.mk build MOZ_MAKE_FLAGS="%{?_smp_mflags}" 
#===============================================================================

%install
rm -rf %{buildroot}
%{__rm} -rf $RPM_BUILD_ROOT

make -f client.mk DESTDIR=$RPM_BUILD_ROOT install


for s in 16 22 24 32 48 256; do
    %{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps
    %{__cp} -p other-licenses/branding/%{name}/mailicon${s}.png \
               $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/thunderbird.png
done


install -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/thunderbird.desktop

#enable global plugins
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/thunderbird/defaults/preferences/
install -m 0644 %{SOURCE10} $RPM_BUILD_ROOT/%{_libdir}/thunderbird/defaults/preferences/vendor.js
install -m 0644 %{SOURCE200} $RPM_BUILD_ROOT/%{_libdir}/thunderbird/defaults/preferences/kde.js


#clean devel files
rm -rf $RPM_BUILD_ROOT/usr/{include,lib/thunderbird-devel-*,share/idl}

#===============================================================================

%post
touch --no-create %{_datadir}/icons/hicolor || :
update-desktop-database &> /dev/null || :

%posttrans
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    if [ -x %{_bindir}/gtk-update-icon-cache ]; then
      gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    fi
fi
update-desktop-database ||:

%files
%defattr(-,root,root,-)
%{_bindir}/thunderbird
%{_datadir}/*
%{_libdir}/thunderbird*

%changelog
* Fri Dec 16 2016 sulit - 38.3.0-19
- rebuild

* Sun Nov 01 2015 Cjacker <cjacker@foxmail.com> - 38.3.0-18
- Rebuild with icu 56.1

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 38.2.0-17
- Update to 38.3.0
- Rebuild for new 4.0 release

* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

