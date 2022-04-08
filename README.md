## Binary Clock Wallpaper

A python script to generate wallpaper that shows time in binary. 

Example image when the time is 7:39 PM: 
![Example image](https://raw.githubusercontent.com/Asocia/binary-clock-wallpaper/main/img/example.png) 

### How to read it?
The image shows `0111 100111 1` in binary. If you convert it to decimal you will get
`4+2+1 32+4+2+1 1` which means `7:39 PM`.

### Setting up the environment
First create a virtual environment for python and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
Then install dependencies with:
```
pip3 install -r requirements.txt
```

### Usage
Run the following command and a file named `result.png` will be created under `img` directory. You can use that file to set your wallpaper.
```
python3 binary_clock_wallpaper.py
```
The accent color can be specified from the command line using the `--color` option. Color can be either hex value or a generic color name. If it is a hex value it needs to be specified in quotes:
```
python3 binary_clock_wallpaper.py --color "#35d8dd"
python3 binary_clock_wallpaper.py --color steelblue
```

### Running it as a cronjob
You can run the helper script, `set_binary_wallpaper.sh`, as a cronjob to update your wallpaper every minute. The helper script uses `nitrogen` as wallpaper setter. Do not forget to change it if you use another program.

```
* * * * * /path/to/set_binary_wallpaper.sh
```


