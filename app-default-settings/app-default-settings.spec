Name: app-default-settings
Version: 0.1
Release: 1
Summary: Default settings for some applications

License: BSD 
#google chrome preferences for hide system titlebar by default.
Source0: Preferences 

%description
Default settings for some applications, will apply to every user when user account created.

%prep

%build

%install
mkdir -p %{buildroot}/etc/skel/.config/google-chrome/Default
install -m 0644 %{SOURCE0} %{buildroot}/etc/skel/.config/google-chrome/Default/

%files
/etc/skel/.config

%changelog
* Fri Aug 21 2015 Cjacker <cjacker@foxmail.com>
- created.
