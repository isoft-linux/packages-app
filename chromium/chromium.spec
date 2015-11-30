Name: chromium
Version: 46.0.2490.86
Release: 4%{?dist}
Summary: An open-source project that aims to build a safer, faster, and more stable browser

License: BSD and LGPLv2+
URL: https://www.chromium.org
Source0: https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz

# The following two source files are copied and modified from
# https://repos.fedorapeople.org/repos/spot/chromium/
Source1: chromium-browser.sh
Source2: chromium-browser.desktop

#svg icon
Source3: chromium-browser.svg

#unfortunately, nacl toolchain still need 32bit libbrary to run even under x86_64 bit environment.

#This is some 32bit runtime libraries to support nacl toolchain.
#it will not used in build process, but we should put it here.
#1, you have to untar this to / before build chromium
#2, also means chromium can not build in koji.
Source9: 32bit-runtime-library.tar.gz

#predownloaded nacl toolchain.
Source10: toolchain.tar.gz

# Enable window title frame under KDE
Patch0: chromium-enable-custom-window-title-frame.patch
# Patches to fix chromium issue under kf5
Patch3: chromium-kf5.patch
Patch4: chromium-fix-kf5-kioslaverc-dir.patch

#revert: https://codereview.chromium.org/1303313005
#This commit cause no border of chromium popup menu under KF5.
#Let's revert it.
Patch5: chromium-revert-issue-1303313005-patch.patch

#the way chromium support kdialog is via involking 'kdialog' command.
#It had a issue that:
#for gtk dialog, it's call via GTK api, then dialog file filter and filer index
#can be set and retreived. so, 'save page' can provide two way: only html and complete page.
#
#But involking 'kdialog' only return the filepath, there is no way to retreive file type index.
#chromium depend on the 'file type index' returned by filedialog to determine how to save a page.
#
#That's to say, even we passed two filter to kdialog, it still not work as our expected.
#refer to: https://code.google.com/p/chromium/issues/detail?id=109913
#So, here is a workaround, since most user need save page with picture etc.
#We force to save as complete page under kde and 'not forced to use gtk dialog'
Patch6: force-chromium-save-html-as-complete-page-when-use-kde-and-not-force-to-gtkdialog.patch

#https://code.google.com/p/chromium/issues/detail?id=505226
Patch100: 0001-Add-FPDFAPIJPEG_-prefix-to-more-libjpeg-functions.patch

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
%patch5 -p1
%patch6 -p1

%patch100 -p1 -d third_party/pdfium

tar zxf %{SOURCE10} -C native_client

# https://groups.google.com/a/chromium.org/d/topic/chromium-packagers/9JX1N2nf4PU/discussion
touch chrome/test/data/webui/i18n_process_css_test.html


%build
#prepare nacl toolchain
#download
#python2 build/download_nacl_toolchains.py  --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync
#extract
python2 build/download_nacl_toolchains.py  --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator extract

#we set this to use 32bit runtime library.
export LD_LIBRARY_PATH=/l32

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
    -Denable_nacl=1 \
    -Denable_pnacl=1 \
    -Ddisable_glibc=1 \
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

#nacl
install -m 755 out/Release/nacl_helper %{buildroot}%{chromiumdir}/
install -m 755 out/Release/nacl_helper_bootstrap %{buildroot}%{chromiumdir}/
cp out/Release/nacl_irt_*.nexe %{buildroot}%{chromiumdir}/
chmod 755  %{buildroot}%{chromiumdir}/*.nexe

for i in 22 24 48 64 128 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
    install -m 644 chrome/app/theme/chromium/product_logo_$i.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/chromium-browser.png
done

install -D -m0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/chromium-browser.svg

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
%dir %{chromiumdir}
%{chromiumdir}/chromium-browser
%{chromiumdir}/chrome-sandbox
%{chromiumdir}/chromedriver
%{chromiumdir}/nacl*
%{chromiumdir}/icudtl.dat
%{chromiumdir}/natives_blob.bin
%{chromiumdir}/snapshot_blob.bin
%{chromiumdir}/*.pak
%dir %{chromiumdir}/locales
%{chromiumdir}/locales/*.pak



%changelog
* Sat Nov 28 2015 Cjacker <cjacker@foxmail.com> - 46.0.2490.86-4
- Enable nacl

* Thu Nov 19 2015 Cjacker <cjacker@foxmail.com> - 46.0.2490.86-3
- Enable save complete html under kde if use kdialog

* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 46.0.2490.86-2
- Update, revert issue 1303313005 commit
- add svg icon

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
