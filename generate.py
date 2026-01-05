#!/usr/bin/env python3
import os

from jinja2 import Environment, FileSystemLoader

# Palette definition
palette = {
    "dark": {
        "red": "#fb4934",
        "green": "#b8bb26",
        "yellow": "#fabd2f",
        "blue": "#83a598",
        "purple": "#d3869b",
        "aqua": "#8ec07c",
        "gray": "#928374",
        "orange": "#fe8019",
    },
    "light": {
        "red": "#cc2412",
        "green": "#98971a",
        "yellow": "#d79921",
        "blue": "#458588",
        "purple": "#b16286",
        "aqua": "#689d6a",
        "gray": "#a89984",
        "orange": "#d65d0e",
    },
}

env = Environment(loader=FileSystemLoader("./templates"))

user_content = env.get_template("userContent.css.jinja")
user_chome = env.get_template("userChrome.css.jinja")

for mode, colors in palette.items():
    for color_n, color in colors.items():
        print(f"Generating for - mode: {mode}, color: {color_n}")

        container = os.path.join("themes", mode, color_n)
        os.makedirs(container, exist_ok=True)

        with open(os.path.join(container, "userContent.css"), "w") as f:
            f.write(user_content.render({"Identity": color}))
        with open(os.path.join(container, "userChrome.css"), "w") as f:
            f.write(user_chome.render({"Identity": color}))
