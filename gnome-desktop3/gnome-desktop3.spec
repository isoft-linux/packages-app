%define gtk3_version                      3.3.6
%define glib2_version                     2.35.0
%define gtk_doc_version                   1.9
%define gsettings_desktop_schemas_version 3.5.91
%define po_package                        gnome-desktop-3.0

Summary: Shared code among gnome-panel, gnome-session, nautilus, etc
Name: gnome-desktop3
Version: 3.18.2
Release: 2
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-desktop/3.13/gnome-desktop-%{version}.tar.xz
Patch0: 0001-default-input-sources-Switch-ja_JP-default-to-ibus-k.patch
Patch1: gnome-desktop-show-full-weekday.patch

License: GPLv2+ and LGPLv2+

# needed for GnomeWallClock
Requires: gsettings-desktop-schemas >= %{gsettings_desktop_schemas_version}

# Make sure that gnome-themes-standard gets pulled in for upgrades
Requires: gnome-themes-standard

BuildRequires: gtk3-devel >= %{gtk3_version}
BuildRequires: gobject-introspection-devel
BuildRequires: gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libxkbfile-devel
BuildRequires: gettext
BuildRequires: gtk-doc >= %{gtk_doc_version}
BuildRequires: automake autoconf libtool intltool
BuildRequires: itstool
BuildRequires: iso-codes-devel

# GnomeIdleMonitor API change breaks older gnome-shell versions
Conflicts: gnome-shell < 3.7.90

%description
The gnome-desktop package contains an internal library
(libgnomedesktop) used to implement some portions of the GNOME
desktop, and also some data files and other shared components of the
GNOME user environment.

%package devel
Summary: Libraries and headers for libgnome-desktop
License: LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for the GNOME-internal private library
libgnomedesktop.

%prep
%setup -q -n gnome-desktop-%{version}
%patch0 -p1
%patch1 -p1
%build
%configure --with-pnp-ids-path="/usr/share/hwdata/pnp.ids"
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# stuff we don't want
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{po_package} --all-name --with-gnome

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{po_package}.lang
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_datadir}/gnome/gnome-version.xml
%{_libexecdir}/gnome-rr-debug
# LGPL
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/GnomeDesktop-3.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/GnomeDesktop-3.0.gir
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gnome-desktop3/

%changelog
* Fri Nov 13 2015 Cjacker <cjacker@foxmail.com> - 3.18.2-2
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 3.18.1-2
- Rebuild for new 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.18.1

* Thu Sep 24 2015 Cjacker <cjacker@foxmail.com>
- update to gnome 3.18

