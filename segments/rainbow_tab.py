"""Sets terminal color based on cwd."""

import colorsys
import os
import random
import sys


def rainbow_tab():
    lightness = 0.8
    saturation = 0.6

    if "workspace" not in os.getcwd():
        sys.stdout.write("\033]6;1;bg;*;default\a")
        sys.stdout.flush()
        return

    random.seed(os.getcwd())

    hue = random.random()

    color = colorsys.hls_to_rgb(hue, lightness, saturation)

    r, g, b = color

    # https://www.iterm2.com/documentation-escape-codes.html
    sys.stdout.write("\033]6;1;bg;red;brightness;%d\a" % int(r * 255))
    sys.stdout.write("\033]6;1;bg;green;brightness;%d\a" % int(g * 255))
    sys.stdout.write("\033]6;1;bg;blue;brightness;%d\a" % int(b * 255))
    sys.stdout.flush()


rainbow_tab()
