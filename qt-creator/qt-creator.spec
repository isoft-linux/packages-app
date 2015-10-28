%global _python_bytecompile_errors_terminate_build 0

Name: qt-creator
Version: 3.5.1
Release: 4 
Summary: Lightweight and cross-platform IDE for Qt
License: LGPLv2 with exceptions
URL: http://www.qtsoftware.com/developer/qt-creator
Source0: http://get.qt.nokia.com/qtcreator/%{name}-opensource-src-%{version}.tar.gz
Source1: qtcreator.desktop
Patch0: qt-creator-clean-debugger-list.patch

BuildRequires:  desktop-file-utils

BuildRequires:       qt5-qtbase-devel
BuildRequires:       qt5-qtwebkit-devel
BuildRequires:       qt5-qtdeclarative-devel
BuildRequires:       qt5-qttools-devel
BuildRequires:       qt5-qtxmlpatterns-devel
BuildRequires:       qt5-qtscript-devel
BuildRequires:       qt5-qtimageformats-devel

Requires:       qt5-qtbase-devel
Requires:       qt5-qtwebkit-devel
Requires:       qt5-qtdeclarative-devel
Requires:       qt5-qttools-devel
Requires:       qt5-qtxmlpatterns-devel
Requires:       qt5-qtscript-devel
Requires:       qt5-qtimageformats-devel
Requires:       qt5-qtquickcontrols

%description
Qt Creator (previously known as Project Greenhouse) is a new,
lightweight, cross-platform integrated  development environment (IDE)
designed to make development with the Qt application framework
even faster and easier.

%prep
%setup -q -n %{name}-opensource-src-%{version}

%build
QTDIR="%{_qt5_prefix}" ; export QTDIR ; \
PATH="%{_qt5_bindir}:$PATH" ; export PATH ; \
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \

qmake -r IDE_LIBRARY_BASENAME=%{_lib}
make %{?_smp_mflags}
make docs

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT/%{_prefix}
make install_docs INSTALL_ROOT=$RPM_BUILD_ROOT/%{_prefix}

desktop-file-install                                    \
--add-category="Development"                            \
--dir=%{buildroot}%{_datadir}/applications              \
%{SOURCE1}


%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &>/dev/null
  gtk3-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/qtcreator
%{_datadir}/qtcreator
%{_datadir}/applications/qtcreator.desktop
%{_datadir}/icons/hicolor/*/apps/QtProject-qtcreator.*
%{_docdir}/qtcreator

%changelog
* Sun Oct 25 2015 Cjacker <cjacker@foxmail.com> - 3.5.1-4
- Rebuild for new 4.0 release

* Sat Oct 17 2015 Cjacker <cjacker@foxmail.com>
- update to 3.5.1

* Fri Aug 21 2015 Cjacker <cjacker@foxmail.com>
- update to 3.5.0
- add -style fusion to desktop file to avoid crash, see: https://bugs.kde.org/show_bug.cgi?id=347524
- clean debugger list, avoid very slow startup when lldb exist.
