#!/usr/bin/env python

import argparse
import sys
from i3ipc import Connection, Event

parser = argparse.ArgumentParser(
    description="Returns the given property of the currently focused window"
)
parser.add_argument(
    "-o",
    "--output_length",
    type=int,
    help="max number of characters to print for title",
)
parser.add_argument(
    "prop",
    choices=["class", "instance", "name", "title"],
    type=str,
    help="print class of focused window",
)

args = parser.parse_args()
prop = args.prop
output_length = args.output_length

i3 = Connection()


def get_focused_window_prop(prop: str):
    focused = i3.get_tree().find_focused()
    output = ""
    if prop == "name":
        output = focused.name
    elif prop == "class":
        output = focused.window_class
    elif prop == "instance":
        output = focused.window_instance
    elif prop == "title":
        output = focused.window_title

    return output


def on_window(i3: Connection, e: Event):
    focused = i3.get_tree().find_focused()
    if e.change == "focus" or e.change == "move" or e.change == "title":
        output = get_focused_window_prop(prop)
        if output_length is None:
            print(output, flush=True)
        else:
            print(output[:output_length], flush=True)


i3.on("window", on_window)

try:
    print(get_focused_window_prop(prop), flush=True)
    i3.main()
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
