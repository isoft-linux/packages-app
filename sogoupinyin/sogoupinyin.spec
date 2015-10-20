%global debug_package %{nil}
%define _xinitrcdir %{_sysconfdir}/X11/xinit/xinitrc.d

Name: sogoupinyin
Version: 2.0.0.0066 
Release: 3%{?dist}
Summary: Sogou Pinyin input method
Summary(zh_CN): 搜狗拼音输入法

License: Proprietary and GPLv2
URL:  http://pinyin.sogou.com/linux
Group:  Applications/System
Source0: http://download.ime.sogou.com/1422868314/%{name}_%{version}_amd64.deb
#currently unused.
Source1: 55-sogoupinyin.sh

Source2: fcitx-ui-sogou-qimpanel.desktop

Source10: isoft-sogoulight1.tar.gz
 
BuildRequires: dpkg
Conflicts: fcitx-sogoupinyin
Requires: qt4
Requires: opencc-compat
Requires: fcitx >= 4.2.8.3
Obsoletes: sogou-pinyin < %{version}-%{release}

%description
Sogou Pinyin Input Method

Based on web search engine technology, Sogou Pinyin input method is
the next-generation input method designed for Internet users. As it
is backed with search engine technology, user input method can be
extremely fast, and it is much more advanced than other input method
engines in terms of the volume of the vocabulary database and its
accuracy. Sogou input method is the most popular input methods in
China, and Sogou promises it will always be free of charge.

%description -l zh_CN
搜狗拼音输入法 - 专注输入法 20 年
支持全拼简拼, 模糊拼音, 细胞词库, 云输入, 皮肤, 中英混输.
通过结合搜索引擎技术, 提高输入准确率. 更多惊喜等您体验.


%prep
# Extract DEB package
dpkg-deb -X %{SOURCE0} %{_builddir}/%{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
pushd %{_builddir}/%{name}-%{version}

# 55-sogoupinyin.sh script
#install -d %{buildroot}%{_xinitrcdir}
#install -m0755 %{SOURCE1} %{buildroot}%{_xinitrcdir}/55-%{name}.sh

# binary files
install -d %{buildroot}%{_bindir}
install -m 0755 usr/bin/* %{buildroot}%{_bindir}/

#!!!!!!!!!!!!!!!!!!!!!!!
#HACK!!!!!!!!!!!!!
#change sogou-qimpanl ELF to use new version library of opencc
#sed -i "s/libopencc.so.1/libopencc.so.2/g" %{buildroot}%{_bindir}/sogou-qimpanel


# library files
install -d %{buildroot}%{_libdir}/fcitx
install -m 0644 usr/lib/*-linux-gnu/fcitx/* %{buildroot}%{_libdir}/fcitx/

# desktop file
install -d %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/fcitx-ui-sogou-qimpanel.desktop

# autostart desktop file
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop

# fcitx files
install -d %{buildroot}%{_datadir}/fcitx
cp -r usr/share/fcitx/* %{buildroot}%{_datadir}/fcitx/

# sogou input method schemes
install -d %{buildroot}%{_datadir}/fcitx-%{name}
cp -r usr/share/fcitx-%{name}/* %{buildroot}%{_datadir}/fcitx-%{name}/

# glib schemas
install -Dm 0644 usr/share/glib-2.0/schemas/50_%{name}.gschema.override \
   %{buildroot}%{_datadir}/glib-2.0/schemas/50_%{name}.gschema.override

# icon files
for i in 16x16 48x48 128x128; do
install -d %{buildroot}%{_datadir}/icons/hicolor/$i/apps
install -m 0644 usr/share/icons/hicolor/$i/apps/fcitx-%{name}.png \
 %{buildroot}%{_datadir}/icons/hicolor/$i/apps/
done
install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 usr/share/pixmaps/*.png %{buildroot}%{_datadir}/pixmaps/

# locale file
install -Dm 644 usr/share/locale/zh_CN/LC_MESSAGES/fcitx-%{name}.mo \
 %{buildroot}%{_datadir}/locale/zh_CN/LC_MESSAGES/fcitx-%{name}.mo

# mime file
install -Dm 644 usr/share/mime/packages/fcitx-ui-sogou-qimpanel.xml \
 %{buildroot}%{_datadir}/mime/packages/fcitx-ui-sogou-qimpanel.xml

# skin, cell files
install -d %{buildroot}%{_datadir}/sogou-qimpanel
cp -r usr/share/sogou-qimpanel/* %{buildroot}%{_datadir}/sogou-qimpanel/

# default skin
#HACK!!!!!!!!!!!!!
#change sogou-qimpanl to use "isoft-sogoulight1" skin.
#the length of "skin name" should be equal to the length of "ubuntukylin-dark1"
sed -i "s/ubuntukylin-dark1/isoft-sogoulight1/g" %{buildroot}%{_bindir}/sogou-qimpanel

#install the skin
tar zxf %{SOURCE10} -C %{buildroot}%{_datadir}/sogou-qimpanel/skin/
rm -rf %{buildroot}%{_datadir}/sogou-qimpanel/skin/ubuntukylin-*

# doc files
install -d %{buildroot}%{_datadir}/doc/%{name}
cp usr/share/doc/%{name}/* %{buildroot}%{_datadir}/doc/%{name}/

# version information
install -d %{buildroot}%{_datadir}/%{name}
echo "%{version}" > %{buildroot}%{_datadir}/%{name}/sogou-version

# rename files
pushd %{buildroot}%{_datadir}/sogou-qimpanel/cell/defaultCell
for i in *;do
  j=`echo "$i"|sed 's|【.*】||'`
  if [ "$i" != "$j" ];then
    mv "$i" "$j"
  fi
done
popd

pushd %{buildroot}%{_datadir}/sogou-qimpanel/recommendSkin/skin
rm -rf "三国杀"* *"路飞" *"团兵"*
for i in *;do
  j=$(echo "$i"|sed 's|[【〖].*[】〗]||')
  if [ "$i" == "【优客】简约" ];then
    j="优客简约"
  fi
  if [ "$i" != "$j" ];then
    mv "$i" "$j"
  fi
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post
# install
if [ "0$1" -eq "1" ]; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || true
    update-desktop-database -q || true
    update-mime-database %{_datadir}/mime || true
    INPUTRC=`readlink /etc/alternatives/xinputrc|awk -F'/' '{print $6}'`
    if [ "$INPUTRC" != "fcitx.conf" ]; then
        alternatives --set xinputrc /etc/X11/xinit/xinput.d/fcitx.conf
    fi
    ldconfig
fi

# update
if [ "0$1" -eq "2" ]; then
    INPUTRC=`readlink /etc/alternatives/xinputrc|awk -F'/' '{print $6}'`
    if [ "$INPUTRC" != "fcitx.conf" ]; then
 alternatives --set xinputrc /etc/X11/xinit/xinput.d/fcitx.conf
    fi
fi

%preun
# uninstall
if [ "0$1" -eq "0" ];then
    pkill sogou > /dev/null 2>&1
fi

%postun
# uninstall
if [ "0$1" -eq "0" ]; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas >/dev/null 2>&1 || true
    update-desktop-database -q || true
    update-mime-database %{_datadir}/mime || true
    INPUTRC=`readlink /etc/alternatives/xinputrc|awk -F'/' '{print $6}'`
    if [ "$INPUTRC" == "fcitx.conf" ]; then
 alternatives --auto xinputrc
    fi
    ldconfig
fi

%files
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/autostart/fcitx-ui-sogou-qimpanel.desktop
%{_bindir}/sogou-*
%{_libdir}/fcitx/
#%{_xinitrcdir}/
%{_datadir}/applications/*.desktop
%{_datadir}/fcitx/
%{_datadir}/fcitx-%{name}/
%{_datadir}/glib-2.0/
%{_datadir}/icons/hicolor/*/apps/fcitx-%{name}.png
%{_datadir}/locale/
%{_datadir}/mime/packages/
%{_datadir}/pixmaps/
%{_datadir}/sogou-qimpanel/
%{_datadir}/%{name}/
%{_datadir}/doc/%{name}/


%changelog
* Mon Oct 19 2015 Cjacker <cjacker@foxmail.com>
- update to 2.0.0.0066

* Tue Oct 13 2015 Cjacker <cjacker@foxmail.com>
- initial build.
- hack sogou-qimpanel ELF to use own theme

