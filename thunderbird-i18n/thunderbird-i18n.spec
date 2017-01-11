Name: thunderbird-i18n
Version: 45.6.0
Release: 1
Summary: Language pack for thunderbird

License: MPL
URL: http://download.cdn.mozilla.net/pub/thunderbird/releases/%{version}/linux-x86_64/xpi
#this is a tarball of all xpi files.
Source0: thunderbird-i18n-%{version}.tar.xz

Requires: thunderbird = %{version}
 
BuildRequires: zip, unzip

BuildArch: noarch

%description
Languages pack for thunderbird

%prep
%setup -c -q

%build
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/thunderbird/extensions/
for i in *.xpi
do
 name=`basename -s .xpi $i`
 install -m0644 $i $RPM_BUILD_ROOT%{_libdir}/thunderbird/extensions/langpack-$name@thunderbird.mozilla.org.xpi
done

%files
%{_libdir}/thunderbird/extensions/langpack-*@thunderbird.mozilla.org.xpi

%changelog
* Wed Jan 11 2017 sulit - 45.6.0-1
- upgrade thunderbird-i18n to 45.6.0

* Mon Oct 26 2015 cjacker - 38.3.0-3
- Update

* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 38.2.0-2
- Rebuild for new 4.0 release

* Fri Sep 25 2015 Cjacker <cjacker@foxmail.com>
- update to 38.2.0
