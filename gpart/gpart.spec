Summary: A program for recovering corrupt partition tables
Name:    gpart
Version: 0.3
Release: 2
License: GPLv2+
URL:     https://github.com/baruch/gpart/
Source0: https://github.com/baruch/%{name}/archive/0.3.tar.gz#/%{name}-%{version}.tar.gz

# BuildRequires: glibc-kernheaders
BuildRequires: autoconf
BuildRequires: automake

ExcludeArch: s390 s390x

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%prep
%setup -q
autoreconf -f -i

%build
%configure
make %{?_smp_mflags}

%install
%{make_install}


%files
%doc COPYING Changes README.md
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Thu Dec 03 2015 sulit <sulitsrc@gmail.com> - 0.3-2
- Init for isoft4
- It's required by gparted
