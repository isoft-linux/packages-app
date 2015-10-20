Name:       opencc-compat
Version:    0.4.3
Release:    2%{?dist}
Summary:    Compatible libraries for Simplified-Traditional Chinese Conversion
License:    ASL 2.0
URL:        http://code.google.com/p/opencc/
Source0:    http://opencc.googlecode.com/files/opencc-%{version}.tar.gz
Patch1: opencc-0.3.0-fixes-cmake.patch
Patch2: opencc-compat-change-so-version-to-avoid-conflict.patch

BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  doxygen

%description
OpenCC is a library for converting characters and phrases between
Traditional Chinese and Simplified Chinese.

%prep
%setup -q -n opencc-%{version}
%patch1 -p1 -b .cmake
%patch2 -p1

%build
%cmake . -DENABLE_GETTEXT:BOOL=ON -DBUILD_DOCUMENTATION:BOOL=ON
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale
rm -rf $RPM_BUILD_ROOT%{_datadir}/opencc-compat/doc

%check
ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%{_libdir}/lib*.so.*
%{_datadir}/opencc-compat

%changelog
* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- initial build to support sogoupinyin.
- change datadir and lib version to avoid conflict with opencc 1.0
