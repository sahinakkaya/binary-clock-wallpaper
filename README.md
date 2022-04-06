## Binary Clock Wallpaper

A python script to generate wallpaper that shows time in binary. 

![Example image](https://raw.githubusercontent.com/Asocia/binary-clock-wallpaper/main/example.png) 

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
Run the following command and a file named `result.png` will be created. You can use that file to set your wallpaper.
```
python3 binary_clock_wallpaper.py
```

### Running it as a cronjob
You can run the helper script as a cronjob to update your wallpaper every minute. The helper script uses `nitrogen` as wallpaper setter. Do not forget to change it if you use another program.

```
* * * * * /path/to/set_binary_wallpaper.sh
```


