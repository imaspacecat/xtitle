## Motivation
The default `xwindow` module that is included with Polybar outputs full title of application which can be long and miss. For example, if a given application such as Kitty includes a file path in its application name.

A solution to this is to use other properties such as the window `class` or `instance`

## Requirements
- Python
- [python-xlib](https://pypi.org/project/python-xlib/) (should be installed by default if you are on xorg)

## Installation
```bash
git clone https://github.com/imaspacecat/xtitle.git
cp xtitle/window-name.py ~/.config/polybar/scripts/window-name.py
```
put the following in your polybar `config.ini`
```ini
[module/window-name]
type = custom/script
label = %output%
label-foreground = ${colors.foreground}
exec = /location/of/script/window-name.sh
tail = true
```
and then
```ini
[bar/main]
...
modules-center = window-name
...
```

## Screenshots
![Alt text](example.png)

## Credit
Thank you to [ssokolow](https://gist.github.com/ssokolow) who wrote the script I modified