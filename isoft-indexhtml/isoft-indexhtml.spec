#NOTE, this is chromium default settings and only works with chromium.
%define checksum dfc1cdd820aa00459c639acf4e3776ca

Name: isoft-indexhtml
Version: 4.1
Release: 1
Summary: The default settings and first startup page of Chromium browser.

License: Public Domain 
URL: http://www.i-soft.com.cn

Source0:	http://pkgs.isoft.zhcn.cc/repo/pkgs/%{name}/%{name}-%{version}.tar.gz/%{checksum}/%{name}-%{version}.tar.gz

#for chromium
Patch0: master_preferences
#default index page, only show once when chromium first run.

Requires: chromium 

BuildArch: noarch

%description
%{summary}

%prep
%setup -q

%build
%install
mkdir -p %{buildroot}%{_libdir}/chromium-browser
install -Dm 0644 index.html %{buildroot}%{_datadir}/indexhtml/index.html
install -Dm 0644 images/body_bg.gif %{buildroot}%{_datadir}/indexhtml/images/body_bg.gif
install -Dm 0644 images/title.png %{buildroot}%{_datadir}/indexhtml/images/title.png
install -m 0644 %{PATCH0} %{buildroot}%{_libdir}/chromium-browser/

%files
%{_libdir}/chromium-browser/master_preferences
%dir %{_datadir}/indexhtml
%{_datadir}/indexhtml/*

%changelog
* Thu Nov 05 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 4.1-1
- new version

* Thu Nov 05 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 4.0-3
- rebuilt

* Wed Nov 04 2015 Cjacker <cjacker@foxmail.com> - 4.0-2
- Initial build


