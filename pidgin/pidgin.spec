Summary: Multiprotocol IM client
Name:pidgin
Version: 2.10.11
Release: 6 
License:GPL
URL:    http://pidgin.im/
Source:%{name}-%{version}.tar.bz2

Patch100:       pidgin-2.10.1-fix-msn-ft-crashes.patch
Patch102:       pidgin-2.10.11-do-not-disable-wall.patch

# http://hg.pidgin.im/pidgin/main/rev/2b41ba1fde8a
Patch103:       pidgin-2.10.11-send-video-enum.patch
# http://hg.pidgin.im/pidgin/main/rev/b52be4fef1de
Patch104:       pidgin-2.10.11-gst-references.patch
# http://hg.pidgin.im/pidgin/main/rev/6b4576edf2a6
Patch105:       pidgin-2.10.11-add-dtmf-support.patch
# http://hg.pidgin.im/pidgin/main/rev/2415067473ba
Patch106:       pidgin-2.10.11-gstreamer1.patch
# http://hg.pidgin.im/pidgin/main/rev/fcecf7f838e2
Patch107:       pidgin-2.10.11-rtp-tcp.patch
# http://hg.pidgin.im/pidgin/main/rev/a0906e7a6bae
Patch108:       pidgin-2.10.11-rtp-encryption.patch
# http://hg.pidgin.im/pidgin/main/rev/5f5abd63c305
Patch109:      pidgin-2.10.11-rtcp-mux.patch
# http://hg.pidgin.im/pidgin/main/rev/88b09a22b7c4
Patch110:      pidgin-2.10.11-signal-pair-established.patch
# http://hg.pidgin.im/pidgin/main/rev/a52798da5cfa
Patch111:      pidgin-2.10.11-farstream027.patch
# http://hg.pidgin.im/pidgin/main/rev/a071658c3725
Patch112:      pidgin-2.10.11-xfer-rw-file.patch
# http://hg.pidgin.im/pidgin/main/rev/8e4fa54f1662
Patch113:      pidgin-2.10.11-unlink-source.patch
# http://hg.pidgin.im/pidgin/main/rev/7767aaeade64
Patch114:      pidgin-2.10.11-init-media-optional.patch
# http://hg.pidgin.im/pidgin/main/rev/d729a9b21265
Patch115:      pidgin-2.10.11-private-media.patch
# http://hg.pidgin.im/pidgin/main/rev/4fe1034f3dce
Patch116:      pidgin-2.10.11-application-media.patch
# http://hg.pidgin.im/pidgin/main/rev/79fe6b95f105
Patch117:      pidgin-2.10.11-fix-appsrc-race.patch
# http://hg.pidgin.im/pidgin/main/rev/cbc4db14444c
Patch118:      pidgin-2.10.11-no-drain-appsink.patch


BuildRequires: GConf2

# Basic Library Requirements
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  cyrus-sasl-devel
BuildRequires:  nss-devel

BuildRequires:  startup-notification-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  libxml2-devel
BuildRequires:  krb5-devel
BuildRequires:  dbus-devel

BuildRequires:  python
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  NetworkManager-glib-devel
BuildRequires:  libSM-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  dbus-glib-devel >= 0.70
BuildRequires:  pkgconfig(avahi-client) pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils::Embed)
BuildRequires:  libidn-devel
BuildRequires:  gtkspell-devel

BuildRequires:  doxygen

Requires: libpurple = %{version}-%{release}

Requires: gstreamer-plugins-good
Requires: gstreamer-plugins-bad
Requires: xdg-utils

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
# http://pidgin.im/pipermail/devel/2011-November/010477.html
%patch100 -p0 -R -b .ftcrash
# https://developer.pidgin.im/ticket/15517
#%patch101 -p1 -b .irc-sasl
# https://developer.pidgin.im/ticket/16593
%patch102 -p1
# http://hg.pidgin.im/pidgin/main/rev/2b41ba1fde8a
%patch103 -p1
# http://hg.pidgin.im/pidgin/main/rev/b52be4fef1de
%patch104 -p1
# https://hg.pidgin.im/pidgin/main/rev/6b4576edf2a6
%patch105 -p1
# http://hg.pidgin.im/pidgin/main/rev/2415067473ba
%patch106 -p1
# http://hg.pidgin.im/pidgin/main/rev/fcecf7f838e2
%patch107 -p1
# http://hg.pidgin.im/pidgin/main/rev/a0906e7a6bae
%patch108 -p1
# http://hg.pidgin.im/pidgin/main/rev/5f5abd63c305
%patch109 -p1
# http://hg.pidgin.im/pidgin/main/rev/88b09a22b7c4
%patch110 -p1
# http://hg.pidgin.im/pidgin/main/rev/a52798da5cfa
%patch111 -p1
# http://hg.pidgin.im/pidgin/main/rev/a071658c3725
%patch112 -p1
# http://hg.pidgin.im/pidgin/main/rev/8e4fa54f1662
%patch113 -p1
# http://hg.pidgin.im/pidgin/main/rev/7767aaeade64
%patch114 -p1
# http://hg.pidgin.im/pidgin/main/rev/d729a9b21265
%patch115 -p1
# http://hg.pidgin.im/pidgin/main/rev/4fe1034f3dce
%patch116 -p1
# http://hg.pidgin.im/pidgin/main/rev/79fe6b95f105
%patch117 -p1
# http://hg.pidgin.im/pidgin/main/rev/cbc4db14444c
%patch118 -p1

autoreconf -ivf

%build
%configure  \
    --enable-nss=yes \
    --enable-gnutls=no  \
    --enable-dbus \
    --enable-avahi \
    --with-gstreamer=1.0 \
    --enable-vv \
    --enable-tcl \
    --enable-perl \
    --enable-gtkspell \
    --disable-gevolution \
    --disable-meanwhile \
    --disable-schemas-install
#new ld will not add dependency automatically
sed -i -e "s/LDFLAGS =/LDFLAGS=-lm/g" pidgin/Makefile
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# remove the perllocal.pod file and other unrequired perl bits
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'

%find_lang pidgin

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
%{_mandir}/man3/*


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
* Fri Nov 27 2015 Cjacker <cjacker@foxmail.com> - 2.10.11-6
- Merge patches back from upstream

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 2.10.11-5
- Rebuild for new 4.0 release

