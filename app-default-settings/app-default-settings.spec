Name: app-default-settings
Version: 0.1
Release: 3 
Summary: Default settings for some applications

License: BSD 
#google chrome preferences for hide system titlebar by default.
Source0: Preferences 

#sogou pinyin default config files to hide statusBar by default and disable SwitchCEKey.
Source1: sogouEnv.ini

%description
Default settings for some applications, will apply to every user when user account created.

%prep

%build

%install
mkdir -p %{buildroot}/etc/skel/.config/google-chrome/Default
install -m 0644 %{SOURCE0} %{buildroot}/etc/skel/.config/google-chrome/Default/

mkdir -p %{buildroot}/etc/skel/.config/SogouPY/
install -m 0644 %{SOURCE1} %{buildroot}/etc/skel/.config/SogouPY/

%files
/etc/skel/.config

%changelog
* Tue Oct 13 2015 Cjacker <cjacker@foxmail.com>
- add default settings for sogou pinyin:
- 1, hide statusbar by default.
- 2, disable switchKey by default, it's annoying.
- 3, set quanban default to inactive.

* Fri Aug 21 2015 Cjacker <cjacker@foxmail.com>
- created.
- add default settings for google-chrome to disable native window titlebar.
