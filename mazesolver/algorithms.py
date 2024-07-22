# mazesolver/algorithms.py

import time
import heapq

def bfs(gui):
    start = gui.start
    end = gui.end

    gui.queue.put(start)
    gui.visited.add(start)

    while not gui.queue.empty():
        current = gui.queue.get()

        if current == end:
            return gui.construct_path(current)

        for neighbor in gui.get_neighbors(current):
            if neighbor not in gui.visited:
                gui.queue.put(neighbor)
                gui.visited.add(neighbor)
                gui.parent[neighbor] = current
                gui.color_cell(neighbor, "visited")

        gui.root.update()
        time.sleep(0.2)

    return None

def dfs(gui):
    stack = [gui.start]
    gui.visited.add(gui.start)

    while stack:
        current = stack.pop()

        if current == gui.end:
            return gui.construct_path(current)

        for neighbor in gui.get_neighbors(current):
            if neighbor not in gui.visited:
                stack.append(neighbor)
                gui.visited.add(neighbor)
                gui.parent[neighbor] = current
                gui.color_cell(neighbor, "visited")

        gui.root.update()
        time.sleep(0.2)

    return None

def astar(gui):
    start = gui.start
    end = gui.end

    open_set = []
    heapq.heappush(open_set, (0, start))
    gui.visited.add(start)
    g_cost = {start: 0}
    f_cost = {start: gui.heuristic(start, end)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            return gui.construct_path(current)

        for neighbor in gui.get_neighbors(current):
            tentative_g_cost = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                gui.parent[neighbor] = current
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = g_cost[neighbor] + gui.heuristic(neighbor, end)
                if neighbor not in gui.visited:
                    heapq.heappush(open_set, (f_cost[neighbor], neighbor))
                    gui.visited.add(neighbor)
                    gui.color_cell(neighbor, "visited")

        gui.root.update()
        time.sleep(0.2)

    return None
