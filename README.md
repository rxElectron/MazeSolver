
# Maze Solver GUI 🧩🔍

This project is a graphical user interface (GUI) application for solving mazes using different algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), and A*. The application is built using Python's Tkinter library.

## Features 🌟

- 🎨 Visualize the maze-solving process
- 🔀 Choose between different maze-solving algorithms (BFS, DFS, A*)
- 🏗️ Create and save custom mazes
- 🎭 Different visualization styles: Normal, Color Gradient, Animation
- 🖱️ Interactive GUI for easy maze manipulation

## Installation 💻

1. Clone the repository:
   ```bash
   git clone https://github.com/therboy/MazeSolver.git
   cd MazeSolver
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀

Run the application:
```bash
python main.py
```

This will launch the Maze Solver GUI, where you can create, solve, and visualize mazes.

## File Structure 📁

| File/Directory             | Description                                        |
|----------------------------|----------------------------------------------------|
| `main.py`                  | Main entry point for the application.              |
| `mazesolver/gui.py`        | Contains the main GUI class and Tkinter setup.     |
| `mazesolver/algorithms.py` | Contains the maze-solving algorithms.              |
| `mazesolver/visualization.py` | Contains the visualization methods.            |
| `mazesolver/builder.py`    | Contains the maze builder functionality.           |
| `requirements.txt`         | List of dependencies for the project.              |
| `README.md`                | Detailed documentation for the project.            |

## How to Use 📝

1. 🚀 Launch the application using `python main.py`.
2. 🏗️ Use the GUI to create a maze or load an existing one.
3. 🧠 Choose a solving algorithm (BFS, DFS, or A*).
4. 🎨 Select a visualization style.
5. ▶️ Click the "Solve" button to watch the algorithm solve the maze.

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements 🙏

- Thanks to the Python community for the excellent Tkinter library.
- Inspired by various maze-solving algorithms and visualizations.
