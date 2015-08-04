Name:           pidgin-indicator
Version:        0.9
Release:        1.2
Summary:        StatusNotifierItem tray icon plugin for Pidgin
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/philipl/pidgin-indicator
Source:         https://github.com/philipl/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:  pkgconfig(pidgin)
Recommends:     %{name}-lang = %{version}

%description
This plugin provides a StatusNotifierItem tray icon, for use in
KDE Plasma 5, Unity, Elementary and other environments.

It provides all the same functionality as the original tray icon
but not in exactly the same way:
 * The 'smart' click behaviour that either shows the buddy list or
   unread messages is now activated by a middle-click – because
   left click on an libappindicator always opens the menu.
 * As the SNI-icon is a separate process from pidgin itself, there
   are sometimes conflicts with Focus Stealing Prevention when you
   use the indicator to go to unread messages. You may need to
   disable FSP for Pidgin to get around this.
 * Due to how libappindicator work, the middle-click action must
   also be a menu item, so it's the new Show/Hide item at the top
   of the menu.
 * Due to libappindicator limitations, some of the special icons
   can't be shown next to menu items any more.

%prep
%setup -q

sed -i 's/Ubuntu Indicator/Pidgin Indicator/g' src/pidgin-indicator.c
sed -i 's/Indicator icon for Ubuntu Unity/Indicator icon/g' src/pidgin-indicator.c
sed -i 's/Show a Unity Indicator icon in Ubuntu/Show a Indicator icon in KDE 5/g' src/pidgin-indicator.c
%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING AUTHORS
%{_libdir}/pidgin/
%{_datadir}/icons/hicolor/*/status/%{name}-nothing.png

%changelog
