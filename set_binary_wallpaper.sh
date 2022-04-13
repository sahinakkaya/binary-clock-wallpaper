#!/bin/bash

base_dir=`dirname "$0"`
if [ -f $base_dir/venv/bin/python ]; then
    python=$base_dir/venv/bin/python
else
    python=python
fi

$python $base_dir/binary_clock_wallpaper.py "$@"

## Use any wallpaper setter of your choice. I use nitrogen
nitrogen --set-zoom-fill $base_dir/img/result.png
#comment the above line and uncomment this if you use sway
#swaymsg -s /run/user/1000/sway-ipc.1000.*.sock output "*" bg $base_dir/img/result.png fill
