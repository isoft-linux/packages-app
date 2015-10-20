#!/bin/sh
set -e

[ -x /usr/bin/fcitx ] || exit 0

if [ -x /usr/bin/im-config ] && [ ! -f $HOME/.xinputrc ]; then
    /usr/bin/im-config -n fcitx && export XMODIFIERS="@im=fcitx" || true
elif [ -x /usr/bin/imsettings-switch ] && [ ! -f $HOME/.config/imsettings/xinputrc ]; then
    /usr/bin/imsettings-switch -qf fcitx.conf && export XMODIFIERS="@im=fcitx" || true
elif [ ! -x /usr/bin/im-config ] && [ ! -x /usr/bin/imsettings-switch ]; then
    if [ "$XMODIFIERS" != "@im=fcitx" ]; then
        export XMODIFIERS="@im=fcitx"
    fi
fi

if [ "$XMODIFIERS" == "@im=fcitx" ]; then
    if [ -f /usr/lib/gtk-2.0/*/immodules/im-fcitx.so ] || \
       [ -f /usr/lib64/gtk-2.0/*/immodules/im-fcitx.so ]; then
        if [ -f /usr/lib/gtk-3.0/*/immodules/im-fcitx.so ] || \
           [ -f /usr/lib64/gtk-3.0/*/immodules/im-fcitx.so ]; then
                export GTK_IM_MODULE=fcitx
        fi
    fi
    if [ -f /usr/lib/qt4/plugins/inputmethods/qtim-fcitx.so ] || \
       [ -f /usr/lib64/qt4/plugins/inputmethods/qtim-fcitx.so ]; then
        export QT_IM_MODULE=fcitx
        if [ -f /usr/lib/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so ] || \
           [ -f /usr/lib64/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so ]; then
                export QT_IM_MODULE=fcitx
        fi
    fi
fi

