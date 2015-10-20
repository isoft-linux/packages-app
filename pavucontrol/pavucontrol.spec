Name:           pavucontrol
Version:        3.0
Release:        4%{?dist}
Summary:        Volume control for PulseAudio

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://freedesktop.org/software/pulseaudio/%{name}
Source0:        http://freedesktop.org/software/pulseaudio/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  pulseaudio-libs-devel >= 3.0
BuildRequires:  gtkmm-devel
BuildRequires:  libsigc++-devel lynx
BuildRequires:  desktop-file-utils
BuildRequires:  libcanberra-devel
BuildRequires:  intltool

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK based volume control
tool ("mixer") for the PulseAudio sound server. In contrast to classic mixer
tools this one allows you to control both the volume of hardware devices and
of each playback stream separately.

%prep
%setup -q

%build
export CXXFLAGS="-std=c++11"

%configure
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make V=1 install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/README
rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/README.html
rm $RPM_BUILD_ROOT/usr/share/doc/pavucontrol/style.css

%find_lang %{name}

#hide menu item
echo "NoDisplay=true" >> $RPM_BUILD_ROOT%{_datadir}/applications/pavucontrol.desktop

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/pavucontrol.desktop

%files -f %{name}.lang
%license LICENSE
%doc doc/README
%{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_datadir}/applications/pavucontrol.desktop

%changelog
