# Maze Solver GUI 🧩🔍

This project is a graphical user interface (GUI) application for solving mazes using different algorithms like Breadth-First Search (BFS), Depth-First Search (DFS), A*, and more. The application is built using Python's Tkinter library.

## Features 🌟

🎨 Visualize the maze-solving process 
🔀 Choose between different maze-solving algorithms:
| Algorithm                                                         | Description                                                                                     |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| - [BFS](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)                 | Breadth-First Search for shortest path in an unweighted graph.                                  |
| - [DFS](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)                 | Depth-First Search for exploring all possible paths.                                            |
| - [A*](https://www.geeksforgeeks.org/a-search-algorithm/)                                     | A* Search for optimal pathfinding.                                                              |
| - [Dijkstra](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)   | Dijkstra's algorithm for shortest paths in a weighted graph.                                    |
| - [Greedy Best-First](https://www.geeksforgeeks.org/greedy-best-first-search-algorithm/)      | Greedy Best-First Search for faster, heuristic-driven pathfinding.                              |
| - [Bidirectional](https://www.geeksforgeeks.org/bidirectional-search/)                        | Bidirectional Search for quicker results by searching from both start and goal.                 |
| - [Random Walk](https://www.geeksforgeeks.org/random-walk-implementation-python/)             | Random Walk for exploring random paths.                                                         |
| - [IDA*](https://www.geeksforgeeks.org/iterative-deepening-a-algorithm-ida-artificial-intelligence/) | Iterative Deepening A* for memory-efficient search.                                             |
| - [Jump Point Search](https://www.geeksforgeeks.org/jump-search/)                             | Jump Point Search for optimized pathfinding in grid-based maps.                                 |
| - [Bellman-Ford](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/)                 | Bellman-Ford algorithm for shortest paths in graphs with negative weights.                      |
| - [Floyd-Warshall](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)             | Floyd-Warshall algorithm for all pairs shortest paths.                                          |
| - [D*](https://en.wikipedia.org/wiki/D*)                                                      | D* algorithm for dynamic pathfinding in changing environments.                                  |
| - [Theta*](https://news.movel.ai/theta-star?x-host=news.movel.ai)                              | Theta* algorithm for smoother paths with line-of-sight checks.                                  |
| - [Fringe Search](https://en.wikipedia.org/wiki/Fringe_search)                                | Fringe Search for memory-efficient pathfinding similar to A*.                                   |
| - [SMA*](https://en.wikipedia.org/wiki/SMA*)                                                  | Simplified Memory-Bounded A* for optimal pathfinding within memory constraints.                 |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
🏗️ Create and save custom mazes                              
🎭 Different visualization styles:                            
| Feature                                                         | Description                                                                                     |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| - Normal                                                       | Standard visualization.                                                                         |
| - Color Gradient                                               | Visualization with color gradients.                                                             |
| - Animation                                                    | Animated visualization of the solving process.                                                  |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
🖱️ Interactive GUI for easy maze manipulation

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
   or:
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

### 🛠️ Additional Setup for `tkinter`

You cannot install `tkinter` using `pip` because it is not available as a standalone package. Instead, it comes bundled with Python installations. Here’s how you can ensure you have it:

#### For Different Operating Systems

- **Windows:**
  Tkinter is included with the standard Python installation. If you installed Python from the official installer, you should already have it.

- **Ubuntu/Debian:**
  You can install Tkinter with:
  ```bash
  sudo apt-get install python3-tk
  ```

- **Fedora:**
  Use the following command:
  ```bash
  sudo dnf install python3-tkinter
  ```

- **macOS:**
  Tkinter is usually included with the Python installation from python.org. If you installed Python via Homebrew, you might need to install it separately:
  ```bash
  brew install python-tk
  ```

### 🧪 Verify Installation

To check if Tkinter is installed correctly, run:

```python
import tkinter
tkinter._test()
```

If a small window appears, Tkinter is working.

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
3. 🧠 Choose a solving algorithm (BFS, DFS, A*, Dijkstra, etc.).
4. 🎨 Select a visualization style.
5. ▶️ Click the "Start" button to watch the algorithm solve the maze.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any questions or inquiries, please contact Reza Khodarahimi at kh.reza10@gmail.com.

## Acknowledgements 🙏
- Thank you to all open-source projects that made this project possible.
- Thanks to the Python community for the excellent Tkinter library.
- Inspired by various maze-solving algorithms and visualizations.
