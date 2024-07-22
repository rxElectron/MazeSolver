# mazesolver/gui.py

import tkinter as tk
import time
import queue
import threading
from .algorithms import *
from .visualization import color_gradient, animate_path
from .builder import enable_maze_builder


class MazeSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver with BFS")

        self.mazes = {
            "Maze 1": [
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "Maze 2": [
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "Maze 3": [
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            ],
            "Maze 4": [
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        }

        self.start = (0, 0)
        self.end = (8, 9)
        self.maze = self.mazes["Maze 1"]

        self.width = len(self.maze[0])
        self.height = len(self.maze)

        # Create canvas for maze visualization...
        self.cell_width = 50
        self.cell_height = 50
        self.canvas = tk.Canvas(
            self.root,
            width=self.width * self.cell_width,
            height=self.height * self.cell_height,
        )
        self.canvas.pack()

        # Dropdown menu to select maze...
        self.maze_var = tk.StringVar(self.root)
        self.maze_var.set("Maze 1")
        self.maze_menu = tk.OptionMenu(
            self.root, self.maze_var, *self.mazes.keys(), command=self.select_maze
        )
        self.maze_menu.pack(side=tk.LEFT, padx=10)

        # Create buttons...
        self.start_button = tk.Button(
            self.root, text="Start", command=self.start_solving
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_path)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        self.exit_button.pack(side=tk.LEFT, padx=10)

        # Status label...
        self.status_label = tk.Label(
            self.root, text="Select a maze and click 'Start' to find path", fg="blue"
        )
        self.status_label.pack(pady=10)

        # Define colors for maze visualization...
        self.colors = {
            "start": "blue",
            "end": "green",
            "path_found": "orange",
            "path_traversed": "yellow",
            "visited": "gray",
            "wall": "black",
            "open": "white",
        }

        # Initialize BFS variables...
        self.queue = queue.Queue()
        self.visited = set()
        self.parent = {}

        self.algorithm_var = tk.StringVar(self.root)
        self.algorithm_var.set("BFS")
        self.algorithm_menu = tk.OptionMenu(
            self.root,
            self.algorithm_var,
            "BFS",
            "DFS",
            "A*",
            "Dijkstra",
            "Greedy Best-First",
            "Bidirectional",
            "Random Walk",
            "IDA*",
            "Jump Point Search",
            "Bellman-Ford",
            "Floyd-Warshall",
            "D*",
            "Theta*",
            "Fringe Search",
            "SMA*",
        )
        self.algorithm_menu.pack(side=tk.LEFT, padx=10)

        self.visualization_var = tk.StringVar(self.root)
        self.visualization_var.set("Normal")
        self.visualization_menu = tk.OptionMenu(
            self.root, self.visualization_var, "Normal", "Color Gradient", "Animation"
        )
        self.visualization_menu.pack(side=tk.LEFT, padx=10)

    def select_maze(self, maze_name):
        """
        Selects a maze from the available mazes and draws it on the canvas.

        Args:
            maze_name (str): The name of the maze to select.
        """
        self.maze = self.mazes[maze_name]
        self.draw_maze()

    def draw_maze(self):
        """
        Draws the current maze on the canvas.

        This method first clears the canvas, then iterates through the maze matrix and draws a rectangle for each cell. The color of the rectangle is determined by the value in the maze matrix:
        - 0 (open path) is drawn as white
        - 1 (wall) is drawn as black
        - The start cell is drawn as blue
        - The end cell is drawn as green

        The rectangles are drawn using the `create_rectangle()` method of the canvas, with the coordinates calculated based on the cell width and height.
        """
        self.canvas.delete("all")

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                x1 = j * self.cell_width
                y1 = i * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height
                color = "white"  # Default color for open paths

                if self.maze[i][j] == 1:
                    color = "black"  # Walls
                elif (i, j) == self.start:
                    color = "blue"  # Start point
                elif (i, j) == self.end:
                    color = "green"  # End point

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def start_solving(self):
        """
        Starts the maze-solving process in a separate thread.
        """
        threading.Thread(target=self.solve_maze).start()

    def solve_maze(self):
        """
        Attempts to solve the current maze using the selected algorithm.

        This method first clears any existing path, updates the status label to indicate that a path
        is being found, and then calls the appropriate algorithm method based on the selected algorithm.

        If a path is found, it is highlighted on the canvas and the status label is updated to indicate
        that a path has been found. If no path is found, the status label is updated to indicate that no path was found.
        """
        self.clear_path()
        self.status_label.config(text="Finding path...", fg="blue")
        self.root.update()

        algorithm = self.algorithm_var.get()

        if algorithm == "BFS":
            path_found = bfs(self)
        elif algorithm == "DFS":
            path_found = dfs(self)
        elif algorithm == "A*":
            path_found = astar(self)
        elif algorithm == "Dijkstra":
            path_found = dijkstra(self)
        elif algorithm == "Greedy Best-First":
            path_found = greedy_best_first_search(self)
        elif algorithm == "Bidirectional":
            path_found = bidirectional_search(self)
        elif algorithm == "Random Walk":
            path_found = random_walk(self)
        elif algorithm == "IDA*":
            path_found = ida_star(self)
        elif algorithm == "Jump Point Search":
            path_found = jump_point_search(self)
        elif algorithm == "Bellman-Ford":
            path_found = bellman_ford(self)
        elif algorithm == "Floyd-Warshall":
            path_found = floyd_warshall(self)
        elif algorithm == "D*":
            path_found = d_star(self)
        elif algorithm == "Theta*":
            path_found = theta_star(self)
        elif algorithm == "Fringe Search":
            path_found = fringe_search(self)
        elif algorithm == "SMA*":
            path_found = sma_star(self)

        if path_found:
            self.highlight_path(path_found)
            self.status_label.config(text="Path found!", fg="green")
        else:
            self.status_label.config(text="No path found!", fg="red")

    def color_cell(self, cell, color):
        """
        Colors a cell in the maze canvas with the specified color.

        Args:
            cell (tuple): The (x, y) coordinate of the cell to be colored.
            color (str): The color to use for filling the cell.

        Returns:
            None
        """
        x, y = cell
        x1, y1 = y * self.cell_width, x * self.cell_height
        x2, y2 = x1 + self.cell_width, y1 + self.cell_height
        if color in self.colors:
            fill_color = self.colors[color]
        else:
            fill_color = color  # Assuming color is a hex color string
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="gray")

    def highlight_path(self, path):
        """
        Highlights the path found in the maze based on the selected visualization style.
        """
        visualization = self.visualization_var.get()
        if visualization == "Color Gradient":
            color_gradient(self, path)
        elif visualization == "Animation":
            animate_path(self, path)
        else:
            for x, y in path:
                self.color_cell((x, y), "path_traversed")
                self.root.update()
                time.sleep(0.2)
            self.color_cell(self.end, "path_found")

    def clear_path(self):
        """
        Clears the path in the maze solver by resetting the queue, visited set, and parent dictionary.
        It then redraws the maze and updates the status label to indicate that a new path should be selected.
        """
        self.queue = queue.Queue()
        self.visited = set()
        self.parent = {}
        self.draw_maze()
        self.status_label.config(
            text="Select a maze and click 'Start' to find path", fg="blue"
        )

    def exit_game(self):
        """
        Exits the Tkinter application.
        """
        self.root.quit()
        exit()

    def enable_maze_builder(self):
        """
        Enables interactive maze building mode where users can click to place walls and define start/end points.
        """
        self.canvas.bind("<Button-1>", self.place_wall)
        self.canvas.bind("<Button-3>", self.set_start_end)
        self.clear_button.config(text="Save", command=self.save_custom_maze)
        self.status_label.config(
            text="Left-click to place walls, right-click to set start/end points",
            fg="blue",
        )

    def place_wall(self, event):
        """
        Places a wall at the clicked cell position on the canvas.
        """
        x, y = event.x // self.cell_width, event.y // self.cell_height
        self.maze[y][x] = 1
        self.draw_maze()

    def set_start_end(self, event):
        """
        Sets the start or end point at the clicked cell position on the canvas.
        """
        x, y = event.x // self.cell_width, event.y // self.cell_height
        if self.start == (0, 0) and self.end == (8, 9):
            self.start = (y, x)
        else:
            self.end = (y, x)
        self.draw_maze()

    def save_custom_maze(self):
        """
        Saves the custom maze configuration.
        """
        self.mazes["Custom Maze"] = self.maze
        self.maze_var.set("Custom Maze")
        self.maze_menu["menu"].add_command(
            label="Custom Maze", command=lambda: self.select_maze("Custom Maze")
        )
        self.clear_button.config(text="Clear", command=self.clear_path)
        self.status_label.config(
            text="Custom maze saved. Click 'Start' to find path", fg="green"
        )

    def heuristic(self, cell, goal):
        """
        Heuristic function for A* algorithm. Uses Manhattan distance.
        """
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def get_neighbors(self, cell):
        """
        Returns a list of neighboring cells that are valid and unvisited in the current maze.

        This method takes a cell coordinate as input and returns a list of all neighboring cells
        that are within the bounds of the maze and have a value of 0 (i.e. are unvisited).
        The possible movements are right, left, down, and up.

        Args:
            cell (tuple): The (x, y) coordinate of the current cell.

        Returns:
            list: A list of (x, y) coordinate tuples representing the valid, unvisited neighboring cells.
        """
        x, y = cell
        neighbors = []

        # Define possible movements (right, left, down, up)
        movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(self.maze)
                and 0 <= ny < len(self.maze[0])
                and self.maze[nx][ny] == 0
            ):
                neighbors.append((nx, ny))

        return neighbors

    def construct_bidirectional_path(
        self, forward_visited, backward_visited, meet_point
    ):
        path = []
        current = meet_point
        while current:
            path.append(current)
            current = forward_visited[current]
        path.reverse()

        current = backward_visited[meet_point]
        while current:
            path.append(current)
            current = backward_visited[current]

        return path

    def is_valid_cell(self, cell):
        x, y = cell
        return 0 <= x < self.height and 0 <= y < self.width and not self.is_wall(cell)

    def is_wall(self, cell):
        x, y = cell
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return True
        return self.maze[x][y] == 1

    def construct_path(self, end):
        """
        Constructs the path from the start to the end of the maze.

        This method takes the end cell as input and reconstructs the path from the end cell back
        to the start cell by following the parent pointers stored in the `self.parent` dictionary.
        The path is returned as a list of cell coordinates in the order they should be traversed.

        Args:
            end (tuple): The (x, y) coordinate of the end cell.

        Returns:
            list: A list of (x, y) coordinate tuples representing the path from the start to the end cell.
        """
        path = []
        current = end
        while current in self.parent:
            path.append(current)
            current = self.parent[current]
        path.append(self.start)
        path.reverse()
        return path


if __name__ == "__main__":
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()
