#!/bin/bash

base_dir=`dirname "$0"`
if [ -f $base_dir/venv/bin/python ]; then
    python=$base_dir/venv/bin/python
else
    python=python
fi

$python $base_dir/binary_clock_wallpaper.py

## Use any wallpaper setter of your choice. I use nitrogen
nitrogen --set-zoom-fill $base_dir/img/result.png
