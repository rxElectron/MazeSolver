#!/bin/python3

#####################################
#                                   #
#    GitHub    : @therboy          #
#    Developer : Reza Khodarahimi  #
#  﫥  Copyright   2024              #
#                                   #
#####################################
# mazesolver/visualization.py

import time

def color_gradient(gui, path):
    gradient_colors = ["#ff0000", "#ff4000", "#ff8000", "#ffbf00", "#ffff00", "#bfff00", "#80ff00", "#40ff00", "#00ff00"]
    for i, (x, y) in enumerate(path):
        color = gradient_colors[i % len(gradient_colors)]
        gui.color_cell((x, y), color)
        gui.root.update()
        time.sleep(0.1)
    gui.color_cell(gui.end, "path_found")

def animate_path(gui, path):
    for (x, y) in path:
        gui.color_cell((x, y), "path_traversed")
        gui.root.update()
        time.sleep(0.05)
    gui.color_cell(gui.end, "path_found")
