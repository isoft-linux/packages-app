Name: pidgin-webqq		
Version: 0.6.1
Release: 1
Summary: WebQQ Plugin for Pidgin

License: GPLv2	
URL: https://github.com/xiehuc/pidgin-lwqq
#git clone https://github.com/xiehuc/pidgin-lwqq.git
Source0: pidgin-lwqq.tar.gz
BuildRequires: libwebqq-devel libpurple-devel

%description
WebQQ Plugin for Pidgin

%prep
%setup -q -n pidgin-lwqq

%build
mkdir build
pushd build
%cmake ..
popd

make %{?_smp_mflags} -C build


%install
make install DESTDIR=%{buildroot} -C build

%find_lang pidgin-lwqq

%files -f pidgin-lwqq.lang
%{_libdir}/purple-2/libwebqq.so
%{_datadir}/icons/hicolor/*/apps/webqq.*
%{_datadir}/lwqq/
%{_datadir}/pixmaps/pidgin/

%changelog

