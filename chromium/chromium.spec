Name:       chromium
Version:    46.0.2490.80
Release:    4%{?dist}
Summary:    An open-source project that aims to build a safer, faster, and more stable browser

License:    BSD and LGPLv2+
URL:        https://www.chromium.org
Source0:    https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz

# The following two source files are copied and modified from
# https://repos.fedorapeople.org/repos/spot/chromium/
Source1:    chromium-browser.sh
Source2:    chromium-browser.desktop

# Enable window title frame under KDE
Patch0: chromium-enable-custom-window-title-frame.patch
# Patches to fix chromium issue under kf5
Patch3: chromium-kf5.patch
Patch4: chromium-fix-kf5-kioslaverc-dir.patch
 
# I don't have time to test whether it work on other architectures
ExclusiveArch: x86_64

# Make sure we don't encounter GCC 5.1 bug
BuildRequires: gcc >= 5.1.1-2
# Basic tools and libraries
BuildRequires: ninja-build, bison, gperf
BuildRequires: python
BuildRequires: libcap-devel, cups-devel, minizip-devel, alsa-lib-devel
BuildRequires: pkgconfig(gtk+-2.0), pkgconfig(libexif), pkgconfig(nss)
BuildRequires: pkgconfig(xtst), pkgconfig(xscrnsaver)
BuildRequires: pkgconfig(dbus-1), pkgconfig(libudev)
BuildRequires: pkgconfig(gnome-keyring-1)
# use_system_*
BuildRequires: expat-devel
BuildRequires: flac-devel
BuildRequires: harfbuzz-devel
# Chromium requires icu 55
# BuildRequires: libicu-devel
BuildRequires: jsoncpp-devel
BuildRequires: libevent-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
# Chromium requires libvpx 1.4.0
# BuildRequires: libvpx-devel
BuildRequires: libwebp-devel
BuildRequires: openssl-devel
BuildRequires: opus-devel
BuildRequires: snappy-devel
BuildRequires: speex-devel
BuildRequires: zlib-devel
# linux_link_*
BuildRequires: pciutils-devel
BuildRequires: pulseaudio-libs-devel
# install desktop files
BuildRequires: desktop-file-utils
Requires:   desktop-file-utils
Requires:   hicolor-icon-theme


%description
%{summary}

%prep
%setup -q
%patch0 -p1
%patch3 -p1
%patch4 -p1

# https://groups.google.com/a/chromium.org/d/topic/chromium-packagers/9JX1N2nf4PU/discussion
touch chrome/test/data/webui/i18n_process_css_test.html

%build
./build/linux/unbundle/replace_gyp_files.py \
    -Duse_system_expat=1 \
    -Duse_system_flac=1 \
    -Duse_system_harfbuzz=1 \
    -Duse_system_icu=0 \
    -Duse_system_jsoncpp=1 \
    -Duse_system_libevent=1 \
    -Duse_system_libjpeg=1 \
    -Duse_system_libpng=1 \
    -Duse_system_libvpx=0 \
    -Duse_system_libwebp=1 \
    -Duse_system_opus=1 \
    -Duse_system_snappy=1 \
    -Duse_system_speex=1 \
    -Duse_system_zlib=1

# find third_party/icu -type f '!' -regex '.*\.\(gyp\|gypi\|isolate\)' -delete

GYP_GENERATORS=ninja ./build/gyp_chromium --depth=. \
    -Duse_system_expat=1 \
    -Duse_system_flac=1 \
    -Duse_system_harfbuzz=1 \
    -Duse_system_icu=0 \
    -Duse_system_jsoncpp=1 \
    -Duse_system_libevent=1 \
    -Duse_system_libjpeg=1 \
    -Duse_system_libpng=1 \
    -Duse_system_libvpx=0 \
    -Duse_system_libwebp=1 \
    -Duse_system_opus=1 \
    -Duse_system_snappy=1 \
    -Duse_system_speex=1 \
    -Duse_system_zlib=1 \
    -Duse_gconf=0 \
    -Dlinux_use_bundled_gold=0 \
    -Dlinux_use_bundled_binutils=0 \
    -Dlinux_link_gsettings=1 \
    -Dlinux_link_kerberos=1 \
    -Dlinux_link_libbrlapi=0 \
    -Dlinux_link_libgps=0 \
    -Dlinux_link_libpci=1 \
    -Dlinux_link_libspeechd=0 \
    -Dlinux_link_pulseaudio=1 \
    -Dicu_use_data_file_flag=1 \
    -Dclang=0 \
    -Dwerror= \
    -Ddisable_fatal_linker_warnings=1 \
    -Denable_hotwording=0 \
    -Ddisable_nacl=1 \
    -Dgoogle_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM \
    -Dgoogle_default_client_id=413772536636.apps.googleusercontent.com \
    -Dgoogle_default_client_secret=0ZChLK6AxeA3Isu96MkwqDR4 \

#./build/download_nacl_toolchains.py --packages \
#    nacl_x86_glibc,nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract

ninja-build -C out/Release chrome chrome_sandbox chromedriver


%install
rm -rf %{buildroot}
%define chromiumdir %{_libdir}/chromium-browser
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{chromiumdir}/locales
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/applications
sed -e "s|@@CHROMIUMDIR@@|%{chromiumdir}|" -e "s|@@BUILDTARGET@@|iSoft Enterprise Desktop|" \
    %{SOURCE1} > chromium-browser.sh
install -m 755 chromium-browser.sh %{buildroot}%{_bindir}/chromium-browser
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
install -m 644 out/Release/chrome.1 %{buildroot}%{_mandir}/man1/chromium-browser.1
install -m 755 out/Release/chrome %{buildroot}%{chromiumdir}/chromium-browser
install -m 4755 out/Release/chrome_sandbox %{buildroot}%{chromiumdir}/chrome-sandbox
install -m 755 out/Release/chromedriver %{buildroot}%{chromiumdir}/
install -m 644 out/Release/icudtl.dat %{buildroot}%{chromiumdir}/
install -m 644 out/Release/natives_blob.bin %{buildroot}%{chromiumdir}/
install -m 644 out/Release/snapshot_blob.bin %{buildroot}%{chromiumdir}/
install -m 644 out/Release/*.pak %{buildroot}%{chromiumdir}/
install -m 644 out/Release/locales/*.pak %{buildroot}%{chromiumdir}/locales/
for i in 22 24 48 64 128 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/chromium/product_logo_$i.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/chromium-browser.png
done


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%{_bindir}/chromium-browser
%{_datadir}/applications/chromium-browser.desktop
%{_datadir}/icons/hicolor/*/apps/chromium-browser.*
%{_mandir}/man1/chromium-browser.1.gz
%{chromiumdir}/chromium-browser
%{chromiumdir}/chrome-sandbox
%{chromiumdir}/chromedriver
%{chromiumdir}/icudtl.dat
%{chromiumdir}/natives_blob.bin
%{chromiumdir}/snapshot_blob.bin
%{chromiumdir}/*.pak
%{chromiumdir}/locales/*.pak



%changelog
* Sat Oct 31 2015 Cjacker <cjacker@foxmail.com> - 46.0.2490.80-4
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 46.0.2490.71-3
- Rebuild for new 4.0 release

* Wed Oct 14 2015 Cjacker <cjacker@foxmail.com>
- update to 46.0.2490.71

* Tue Sep 22 2015 Cjacker <cjacker@foxmail.com>
- update to 45.0.2454.99
- add patch2 to fix 3030 bug.

* Sat Sep 19 2015 Cjacker <cjacker@foxmail.com>
- initial build.
- Add patch1 to enable custom frame under kwin.
