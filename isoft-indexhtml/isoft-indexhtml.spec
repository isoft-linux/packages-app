#NOTE, this is chromium default settings and only works with chromium.

Name: isoft-indexhtml
Version: 4.0
Release: 2
Summary: The default settings and first startup page of Chromium browser.

License: Public Domain 
URL: http://www.i-soft.com.cn

#!!!!!!!!!!!!!!!!!!!!!!!!!!
#The reason I use 'patch' instead of 'source' is:
#the fucking koji build system will put source to another storage and keep patch in git.
#and the fucking source can not be altered or replaced if the different version of source have same file name.
#- By Cjacker.
#!!!!!!!!!!!!!!!!!!!!!!!!!!

#for chromium
Patch0: master_preferences
#default index page, only show once when chromium first run.
Patch1: index.html

Requires: chromium 

BuildArch: noarch

%description
%{summary}

%prep

%build
%install
mkdir -p %{buildroot}%{_libdir}/chromium-browser
mkdir -p %{buildroot}%{_datadir}/indexhtml
install -m 0644 %{PATCH0} %{buildroot}%{_libdir}/chromium-browser/
install -m 0644 %{PATCH1} %{buildroot}%{_datadir}/indexhtml

%files
%{_libdir}/chromium-browser/master_preferences
%dir %{_datadir}/indexhtml
%{_datadir}/indexhtml/*

%changelog
* Wed Nov 04 2015 Cjacker <cjacker@foxmail.com> - 4.0-2
- Initial build


