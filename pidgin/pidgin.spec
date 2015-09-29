Summary: Multiprotocol IM client
Name:pidgin
Version: 2.10.11
Release: 4 
License:GPL
URL:    http://pidgin.im/
Source:%{name}-%{version}.tar.bz2
BuildRequires: NetworkManager-devel
BuildRequires: libidn-devel
BuildRequires: ncurses-devel
BuildRequires: glib2-devel dbus-devel
BuildRequires: python-devel
BuildRequires: libxml2-devel
BuildRequires: nss-devel nspr-devel
BuildRequires: dbus-glib-devel
BuildRequires: libX11-devel libSM-devel libXScrnSaver-devel libICE-devel libXext-devel gtk2-devel fontconfig-devel freetype-devel pango-devel
BuildRequires: glibc-devel
 
Requires: libpurple
%description
Multiprotocol IM client

%package devel
Summary: Development headers for pidgin plugin development. 
Requires: libpurple-devel = %{version}

%description devel
%{summary}

%package -n libpurple-tools
Summary: Demo tools from libpurple library.
Requires: libpurple = %{version}
%description -n libpurple-tools
%{summary}

%package -n libpurple 
Summary: Runtime libraries for Pidgin IM client.

%description -n libpurple 
%{summary}

%package -n libpurple-devel
Summary: Headers and libraries for IM client development.  
Requires: libpurple = %{version}

%description -n libpurple-devel
%{summary}

%package -n finch 
Summary: console frontend to libpurple
Requires: libgnt = %{version}

%description -n finch
%{summary}

%package -n finch-devel
Summary: Headers to console frontend IM client plugin development
Requires: libgnt-devel = %{version}

%description -n finch-devel
%{summary}


%package -n libgnt 
Summary: Runtime library for console frontend of libpurple
Requires: libpurple = %{version}

%description -n libgnt 
%{summary}

%package -n libgnt-devel
Summary: Headers and libraries for Console IM client development.  
Requires: libpurple-devel = %{version}

%description -n libgnt-devel
%{summary}



%prep
%setup -q
%build
%configure  \
    --enable-nss=yes \
    --disable-gevolution \
    --enable-gnutls=no  \
    --disable-meanwhile \
    --disable-vv \
    --disable-avahi \
    --disable-tcl \
    --disable-perl \
    --disable-gtkspell \
    --disable-gstreamer 
#new ld will not add dependency automatically
sed -i -e "s/LDFLAGS =/LDFLAGS=-lm/g" pidgin/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%find_lang pidgin
rpmclean


%post
gtk-update-icon-cache /usr/share/icons/hicolor ||:
%postun 
gtk-update-icon-cache /usr/share/icons/hicolor ||:

%post -n libpurple
/sbin/ldconfig
%postun -n libpurple
/sbin/ldconfig

%post -n libgnt
/sbin/ldconfig
%postun -n libgnt
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pidgin.lang
%defattr(-,root,root,-)
%{_bindir}/pidgin
%{_mandir}/man1/pidgin*
%dir %{_datadir}/pixmaps/pidgin
%{_datadir}/pixmaps/pidgin/*
%{_datadir}/icons/hicolor/*/apps/pidgin.*
%{_datadir}/applications/pidgin.desktop
%dir %{_libdir}/pidgin
%{_libdir}/pidgin/*
%{_datadir}/appdata/pidgin.appdata.xml

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pidgin
%{_includedir}/pidgin/*
%{_libdir}/pkgconfig/pidgin.pc

%files -n finch
%defattr(-,root,root,-)
%{_bindir}/finch
%{_mandir}/man1/finch*
%dir %{_libdir}/finch
%{_libdir}/finch/*

%files -n finch-devel
%{_libdir}/pkgconfig/finch.pc
%dir %{_includedir}/finch
%{_includedir}/finch/*


%files -n libpurple-tools
%defattr(-,root,root,-)
%{_bindir}/purple-*

%files -n libpurple
%defattr(-,root,root,-)
#%{_sysconfdir}/gconf/schemas/purple.schemas
%dir %{_datadir}/purple
%{_datadir}/purple/*
%dir %{_datadir}/sounds/purple
%{_datadir}/sounds/purple/*
%dir %{_libdir}/purple-2
%{_libdir}/purple-2/*
%{_libdir}/libpurple*.so.*

%files -n libpurple-devel
%defattr(-,root,root,-)
%{_datadir}/aclocal/purple.m4
%{_libdir}/pkgconfig/purple.pc
%{_libdir}/libpurple*.so
%dir %{_includedir}/libpurple
%{_includedir}/libpurple/*

%files -n libgnt
%{_libdir}/libgnt.so*
%dir %{_libdir}/gnt
%{_libdir}/gnt/*

%files -n libgnt-devel
%{_libdir}/pkgconfig/gnt.pc
%dir %{_includedir}/gnt
%{_includedir}/gnt/*
%{_libdir}/libgnt.so*

%changelog
