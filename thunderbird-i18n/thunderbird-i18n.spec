Name:	    thunderbird-i18n
Version:	38.1.0
Release:	1
Summary:	Language pack for thunderbird

Group:		App/Runtime/Data
License:	MPL
URL:		http://download.cdn.mozilla.net/pub/thunderbird/releases/31.2.0/linux-x86_64/xpi
#this is a tarball of all xpi files.
Source0:    thunderbird-i18n.tar.gz

Requires:   thunderbird = %{version}	
BuildRequires: zip, unzip
%description
Language pack for thunderbird

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

