Summary: Mozilla Thunderbird mail/newsgroup client
Name: thunderbird
Version: 38.2.0
Release: 16 
URL: http://www.mozilla.org/projects/thunderbird/
License: MPL
Group:  Applications/Internet
Source0: thunderbird-%{version}.source.tar.bz2
Source1: thunderbird.desktop
Source4: thunderbird-mozconfig
Source10:  thunderbird-vendor.js
 
Source100: find-external-requires

Patch0: thunderbird-install-dir.patch
Patch1: thunderbird-freetype26.patch

Source200: thunderbird-kde.js
Patch10: thunderbird-mozilla-kde.patch
Patch11: thunderbird-firefox-kde.patch
Patch12: thunderbird-toolkit-download-folder.patch
Patch13: thunderbird-mozilla-nongnome-proxies.patch 

BuildRequires: libpng-devel, libjpeg-devel, gtk2-devel
BuildRequires: zlib-devel, gzip, zip, unzip
BuildRequires: freetype-devel
BuildRequires:  nss-devel 
BuildRequires:  nspr-devel
BuildRequires:  hunspell-devel 
Requires: nss
Requires: nspr
Obsoletes: MozillaThunderbird
Provides: MozillaThunderbird = %{epoch}:%{version}

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
rpmclean

%clean

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

#===============================================================================

%postun
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%{_bindir}/thunderbird
%{_datadir}/*
%{_libdir}/thunderbird*

%changelog
* Tue Dec 10 2013 Cjacker <cjacker@gmail.com>
- first build, prepare for the new release.

