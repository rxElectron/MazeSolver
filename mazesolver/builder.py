#!/bin/python3

#####################################
#                                   #
#    GitHub    : @therboy          #
#    Developer : Reza Khodarahimi  #
#  﫥  Copyright   2024              #
#                                   #
#####################################
# mazesolver/builder.py

def enable_maze_builder(gui):
    gui.canvas.bind("<Button-1>", gui.place_wall)
    gui.canvas.bind("<Button-3>", gui.set_start_end)
    gui.clear_button.config(text="Save", command=gui.save_custom_maze)
    gui.status_label.config(text="Left-click to place walls, right-click to set start/end points", fg="blue")
