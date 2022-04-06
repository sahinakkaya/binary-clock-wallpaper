#!/bin/bash

base_dir=`dirname "$0"`

$base_dir/venv/bin/python $base_dir/binary_clock_wallpaper.py

## Use any wallpaper setter of your choice. I use nitrogen
nitrogen --set-zoom-fill $base_dir/img/result.png
