#NOTE, this is chromium default settings and only works with chromium.
%define checksum 0fb4c2278896d4d08ccac8195829e8f7

Name: isoft-indexhtml
Version: 4.3
Release: 1
Summary: The default settings and first startup page of Chromium browser.

License: Public Domain 
URL: http://www.i-soft.com.cn

Source0:	http://pkgs.isoft.zhcn.cc/repo/pkgs/%{name}/%{name}-%{version}.tar.gz/%{checksum}/%{name}-%{version}.tar.gz

#for chromium
Patch0: master_preferences
Patch1: Bookmarks
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
install -m 0644 %{PATCH1} %{buildroot}%{_datadir}/indexhtml

%files
%{_libdir}/chromium-browser/master_preferences
#%{_datadir}/indexhtml/Bookmarks
%dir %{_datadir}/indexhtml
%{_datadir}/indexhtml/*

%changelog
* Thu Nov 24 2016 sulit <sulitsrc@gmail.com> - 4.3-1
- modify isoft company address

* Fri Jan 08 2016 xiaotian.wu@i-soft.com.cn - 4.2-2
- fixed desktop name of bookmark.

* Fri Dec 25 2015 xiaotian.wu@i-soft.com.cn - 4.2-1
- new version, change desktop name.

* Fri Nov 27 2015 kun.li@i-soft.com.cn - 4.1-2
- Add Bookmarks

* Thu Nov 05 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 4.1-1
- new version

* Thu Nov 05 2015 Wu Xiaotian <xiaotian.wu@i-soft.com.cn> - 4.0-3
- rebuilt

* Wed Nov 04 2015 Cjacker <cjacker@foxmail.com> - 4.0-2
- Initial build
