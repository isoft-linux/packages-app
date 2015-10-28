#PepperFlash Plugin binary directly from google-chrome.

%define debug_package %{nil}

Name: pepperflash 
Version: 19.0.0.185
Release: 2
Summary: Flash plugin for chromium browser

License: Commercial

#token from google-chrome
Source0: PepperFlash.tar.gz 

#export correct commandline args for chromium
Source1: chromium-pepperflash.sh

%description
%{summary}

%prep
%build
%install
mkdir -p %{buildroot}%{_libdir}/
tar zxf %{SOURCE0} -C %{buildroot}%{_libdir}/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/

%files
%{_libdir}/PepperFlash
%{_sysconfdir}/profile.d/chromium-pepperflash.sh

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 19.0.0.185-2
- Rebuild for new 4.0 release

* Thu Sep 22 2015 Cjacker <cjacker@foxmail.com>
- update to pepper flash from chrome 45.0.2454.99 

* Sat Sep 19 2015 Cjacker <cjacker@foxmail.com>
- initial build.
