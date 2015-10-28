Summary: Harddisk Partition Editor
Name: gparted
Version: 0.22.0
Release: 3 
License: GPLv2+
URL: http://www.gparted.org
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

Source10: libsigc++-2.3.1.tar.xz
Source11: glibmm-2.40.0.tar.xz
Source12: atkmm-2.22.7.tar.xz
Source13: cairomm-1.11.2.tar.gz
Source14: pangomm-2.34.0.tar.xz
Source15: gtkmm-2.24.4.tar.xz

#for kf5 systemsettings
Source20: kcm_gparted.desktop

BuildRequires:	parted-devel 
BuildRequires:	libuuid-devel gettext perl(XML::Parser) 
BuildRequires:	desktop-file-utils intltool
BuildRequires:  pkgconfig
BuildRequires:  ntfs-3g-devel

%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep
%setup -q -a10 -a11 -a12 -a13 -a14 -a15

%build
#static build gtkmm
export PKG_CONFIG_PATH=`pwd`/interbin/lib/pkgconfig

pushd libsigc++-2.3.1
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

pushd glibmm-2.40.0
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

pushd atkmm-2.22.7
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

pushd cairomm-1.11.2
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

pushd pangomm-2.34.0
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

pushd gtkmm-2.24.4
CFLAGS="-fPIC" ./configure --prefix=`pwd`/../interbin --disable-shared --enable-static --disable-documentation
make %{?_smp_mflags}
make install
popd

rm -rf `pwd`/interbin/lib/*.so*


%configure \
    --enable-libparted-dmraid \
    --disable-doc \
    CFLAGS="-I`pwd`/interbin/include" \
    CXXFLAGS="-I`pwd`/interbin/include" \
    LDFLAGS="-I`pwd`/interbin/lib" \
    LIBS="-lpthread"

make %{?_smp_mflags} 

%install
make DESTDIR=%{buildroot} install

sed -i 's#_X-GNOME-FullName#X-GNOME-FullName#' %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original			\
        --dir %{buildroot}%{_datadir}/applications	\
	    --mode 0644					\
        %{buildroot}%{_datadir}/applications/%{name}.desktop

echo "X-KDE-SubstituteUID=true" >> %{buildroot}%{_datadir}/applications/%{name}.desktop
echo "NotShowIn=KDE;" >> %{buildroot}%{_datadir}/applications/%{name}.desktop

#for kf5 systemsettings
mkdir -p %{buildroot}%{_datadir}/kservices5/
install -m 0644 %{SOURCE20} %{buildroot}%{_datadir}/kservices5/


%find_lang %{name}

%post
touch --no-create %{_datadir}/icons/hicolor || :
update-desktop-database ||:
%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database ||:

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%{_sbindir}/gparted
%{_sbindir}/gpartedbin
%{_datadir}/applications/gparted.desktop
%{_datadir}/icons/hicolor/*/apps/gparted.*
%{_datadir}/appdata/gparted.appdata.xml
#%{_datadir}/gnome/help/gparted/
#%{_datadir}/omf/gparted/
%{_datadir}/kservices5/*.desktop

%{_mandir}/man8/gparted.*

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 0.22.0-3
- Rebuild for new 4.0 release

* Sun Oct 18 2015 Cjacker <cjacker@foxmail.com>
- add systemsettings entry for kf5.
