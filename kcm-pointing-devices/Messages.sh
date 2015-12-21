#!/bin/sh

$EXTRACTRC `find . -prune -o \( -name \*.rc -o -name \*.ui -o -name \*.kcfg \) -print` >> rc.cpp
$XGETTEXT rc.cpp `find . -prune -o \( -name \*.cpp -o -name \*.h \) -print` -o $podir/kcm_pointingdevices.pot

$XGETTEXT `find . -name \*.qml -o -name \*.js` -o $podir/kcm_pointingdevices2.pot

cat $podir/kcm_pointingdevices2.pot >> $podir/kcm_pointingdevices.pot
rm -rf $podir/kcm_pointingdevices2.pot
