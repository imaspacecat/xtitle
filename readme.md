# Better-XWindow-I3
### Motivation
The default `xwindow` module that is included with Polybar outputs full title of application which can be long and miss. For example, if a given application such as Kitty includes a file path in its application name.

A solution to this is to use other properties such as `window_class` or `window_instance`

**comparison: title | class**

![comparison of xwindow versus enhancement script](comparison.png)


`class` will just print the application name

`name` will print the whole title
example:

class: Code

name: readme.md - i3-scripts - Visual Studio Code

### Requirements
- Python
- [i3ipc](https://pypi.org/project/i3ipc/)

### Installation
```bash
git clone https://github.com/imaspacecat/better-xwindow-i3.git
cp better-xwindow-i3/focused-window-name.py ~/.config/polybar/scripts/focused-window-name.py
```

### Usage
```
usage: focused-window-name.py [-h] [-o OUTPUT_LENGTH] {class,instance,name,title}

Returns the title or app name of the currently focused window

positional arguments:
  {class,instance,name,title}
                        print class of focused window

options:
  -h, --help            show this help message and exit
  -o OUTPUT_LENGTH, --output_length OUTPUT_LENGTH
                        max number of characters to print for title
```


Put the following in your Polybar config with the given argument (example below uses `class`)
```ini
[module/window-name]
type = custom/script
label = %output%
label-foreground = ${colors.primary}
exec = python ~/.config/polybar/scripts/focused-window-name.py class
tail = true
```

Make sure you add it to the modules displayed:
```ini
[bar/main]
...
modules-center = window-name
...
```
