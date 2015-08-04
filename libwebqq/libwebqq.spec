Name:       libwebqq		
Version:	0.6.0
Release:	1
Summary:	WebQQ protocol library

License:    GPL	
URL:	    https://github.com/xiehuc/lwqq	
Source0:	https://github.com/xiehuc/lwqq/archive/v%{version}.tar.gz
BuildRequires: mozjs17-devel zlib-devel libcurl-devel sqlite-devel
BuildRequires: libuv-devel

%description
WebQQ protocol library

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n lwqq-%{version}

%build
mkdir build
pushd build
%cmake -DWITH_LIBUV=ON ..
popd

make %{?_smp_mflags} -C build


%install
make install DESTDIR=%{buildroot} -C build

rm -rf %{buildroot}%{_libdir}/*.a

%files
%{_libdir}/liblwqq.so.*
%dir %{_datadir}/lwqq
%{_datadir}/lwqq/encrypt.js

%files devel
%{_includedir}/lwqq
%{_libdir}/liblwqq.so
%{_libdir}/pkgconfig/lwqq.pc

%changelog

