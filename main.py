# main.py

import tkinter as tk
from mazesolver.gui import MazeSolverGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()
