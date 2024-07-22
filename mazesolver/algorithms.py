#!/bin/python3

#####################################
#                                   #
#    GitHub    : @therboy          #
#    Developer : Reza Khodarahimi  #
#  﫥  Copyright   2024              #
#                                   #
#####################################
# mazesolver/algorithms.py

import time
import heapq
import random


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


def dijkstra(gui):
    start = gui.start
    end = gui.end

    pq = [(0, start)]
    gui.visited.add(start)
    distances = {start: 0}

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current == end:
            return gui.construct_path(current)

        if current_dist > distances[current]:
            continue

        for neighbor in gui.get_neighbors(current):
            distance = current_dist + 1

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                gui.parent[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))
                if neighbor not in gui.visited:
                    gui.visited.add(neighbor)
                    gui.color_cell(neighbor, "visited")

        gui.root.update()
        time.sleep(0.2)

    return None


def greedy_best_first_search(gui):
    start = gui.start
    end = gui.end

    open_set = [(gui.heuristic(start, end), start)]
    gui.visited.add(start)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            return gui.construct_path(current)

        for neighbor in gui.get_neighbors(current):
            if neighbor not in gui.visited:
                gui.parent[neighbor] = current
                heapq.heappush(open_set, (gui.heuristic(neighbor, end), neighbor))
                gui.visited.add(neighbor)
                gui.color_cell(neighbor, "visited")

        gui.root.update()
        time.sleep(0.2)

    return None


def bidirectional_search(gui):
    start = gui.start
    end = gui.end

    forward_queue = [start]
    backward_queue = [end]
    forward_visited = {start: None}
    backward_visited = {end: None}

    while forward_queue and backward_queue:
        # Forward search
        current = forward_queue.pop(0)
        gui.color_cell(current, "visited")

        for neighbor in gui.get_neighbors(current):
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current
                forward_queue.append(neighbor)
                if neighbor in backward_visited:
                    return gui.construct_bidirectional_path(
                        forward_visited, backward_visited, neighbor
                    )

        # Backward search
        current = backward_queue.pop(0)
        gui.color_cell(current, "visited")

        for neighbor in gui.get_neighbors(current):
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current
                backward_queue.append(neighbor)
                if neighbor in forward_visited:
                    return gui.construct_bidirectional_path(
                        forward_visited, backward_visited, neighbor
                    )

        gui.root.update()
        time.sleep(0.2)

    return None


def random_walk(gui):
    current = gui.start
    path = [current]
    gui.visited.add(current)

    while current != gui.end:
        neighbors = gui.get_neighbors(current)
        unvisited_neighbors = [n for n in neighbors if n not in gui.visited]

        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
        elif neighbors:
            next_cell = random.choice(neighbors)
        else:
            return None

        path.append(next_cell)
        gui.visited.add(next_cell)
        gui.color_cell(next_cell, "visited")
        current = next_cell

        gui.root.update()
        time.sleep(0.2)

    return path


def ida_star(gui):
    def search(path, g, f_limit):
        node = path[-1]
        f = g + gui.heuristic(node, gui.end)

        if f > f_limit:
            return f, None

        if node == gui.end:
            return f, path

        min_cost = float("inf")
        for neighbor in gui.get_neighbors(node):
            if neighbor not in path:
                path.append(neighbor)
                gui.visited.add(neighbor)
                gui.color_cell(neighbor, "visited")
                gui.root.update()
                time.sleep(0.2)

                cost, solution = search(path, g + 1, f_limit)

                if solution is not None:
                    return cost, solution

                path.pop()
                min_cost = min(min_cost, cost)

        return min_cost, None

    f_limit = gui.heuristic(gui.start, gui.end)
    while True:
        gui.visited.clear()
        cost, solution = search([gui.start], 0, f_limit)
        if solution is not None:
            return solution
        if cost == float("inf"):
            return None
        f_limit = cost

def jump_point_search(gui):
    def identify_successors(node):
        successors = []
        for direction in directions:
            jp = jump(node, direction)
            if jp:
                successors.append(jp)
        return successors

    def jump(node, direction):
        x, y = node
        dx, dy = direction
        nx, ny = x + dx, y + dy

        if not gui.is_valid_cell((nx, ny)) or gui.is_wall((nx, ny)):
            return None

        if (nx, ny) == gui.end:
            return (nx, ny)

        # Check for forced neighbors
        if dx != 0 and dy != 0:
            if (gui.is_valid_cell((x + dx, y)) and gui.is_wall((x + dx, y + dy))) or \
               (gui.is_valid_cell((x, y + dy)) and gui.is_wall((x + dx, y + dy))):
                return (nx, ny)
        else:
            if dx != 0:
                if (gui.is_valid_cell((nx + dx, ny)) and gui.is_wall((nx + dx, ny - 1))) or \
                   (gui.is_valid_cell((nx + dx, ny)) and gui.is_wall((nx + dx, ny + 1))):
                    return (nx, ny)
            else:
                if (gui.is_valid_cell((nx, ny + dy)) and gui.is_wall((nx - 1, ny + dy))) or \
                   (gui.is_valid_cell((nx, ny + dy)) and gui.is_wall((nx + 1, ny + dy))):
                    return (nx, ny)

        return jump((nx, ny), direction)

    start = gui.start
    goal = gui.end
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    open_list = {start}
    closed_list = set()
    parents = {start: None}

    while open_list:
        current = min(open_list, key=lambda x: gui.heuristic(x, goal))
        open_list.remove(current)

        if current == goal:
            return gui.construct_path(goal)

        closed_list.add(current)

        for successor in identify_successors(current):
            if successor in closed_list:
                continue

            if successor not in open_list:
                open_list.add(successor)
                parents[successor] = current

    return None

def bellman_ford(gui):
    start = gui.start
    goal = gui.end
    distance = {start: 0}
    parents = {start: None}
    vertices = [(i, j) for i in range(gui.height) for j in range(gui.width) if not gui.is_wall((i, j))]

    for _ in range(len(vertices) - 1):
        for x in range(gui.height):
            for y in range(gui.width):
                if gui.is_wall((x, y)):
                    continue
                for neighbor in gui.get_neighbors((x, y)):
                    if (x, y) not in distance:
                        distance[(x, y)] = float('inf')
                    if neighbor not in distance:
                        distance[neighbor] = float('inf')
                    if distance[(x, y)] + 1 < distance[neighbor]:
                        distance[neighbor] = distance[(x, y)] + 1
                        parents[neighbor] = (x, y)

    if goal in parents:
        path = []
        current = goal
        while current:
            path.append(current)
            current = parents[current]
        return path[::-1]

    return None


def floyd_warshall(gui):
    dist = {}
    next_node = {}

    for i in range(gui.height):
        for j in range(gui.width):
            if not gui.is_wall((i, j)):
                dist[(i, j)] = {}
                next_node[(i, j)] = {}
                for ni in range(gui.height):
                    for nj in range(gui.width):
                        if not gui.is_wall((ni, nj)):
                            dist[(i, j)][(ni, nj)] = float("inf")
                            next_node[(i, j)][(ni, nj)] = None
                dist[(i, j)][(i, j)] = 0
                for neighbor in gui.get_neighbors((i, j)):
                    dist[(i, j)][neighbor] = 1
                    next_node[(i, j)][neighbor] = neighbor

    for k in dist:
        for i in dist:
            for j in dist:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    start = gui.start
    goal = gui.end
    if next_node[start][goal] is None:
        return None

    path = []
    current = start
    while current != goal:
        path.append(current)
        current = next_node[current][goal]
    path.append(goal)
    return path


def d_star(gui):
    def expand(node):
        return [(neighbor, 1) for neighbor in gui.get_neighbors(node)]

    start = gui.start
    goal = gui.end
    open_list = {start}
    closed_list = set()
    parents = {start: None}
    g_scores = {start: 0}
    f_scores = {start: gui.heuristic(start, goal)}

    while open_list:
        current = min(open_list, key=lambda x: f_scores.get(x, float("inf")))
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        open_list.remove(current)
        closed_list.add(current)

        gui.color_cell(current, "visited")
        gui.root.update()
        time.sleep(0.2)

        for neighbor, cost in expand(current):
            if neighbor in closed_list:
                continue

            tentative_g_score = g_scores[current] + cost

            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g_score >= g_scores.get(neighbor, float("inf")):
                continue

            parents[neighbor] = current
            g_scores[neighbor] = tentative_g_score
            f_scores[neighbor] = g_scores[neighbor] + gui.heuristic(neighbor, goal)

    return None


def theta_star(gui):
    def line_of_sight(start, end):
        x0, y0 = start
        x1, y1 = end
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x = x0
        y = y0
        n = 1 + dx + dy
        x_inc = 1 if x1 > x0 else -1
        y_inc = 1 if y1 > y0 else -1
        error = dx - dy
        dx *= 2
        dy *= 2

        for _ in range(n):
            if gui.is_wall((x, y)):
                return False
            if error > 0:
                x += x_inc
                error -= dy
            else:
                y += y_inc
                error += dx

        return True

    start = gui.start
    goal = gui.end
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: gui.heuristic(start, goal)}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor in gui.get_neighbors(current):
            if neighbor in came_from and line_of_sight(came_from[current], neighbor):
                tentative_g_score = g_score[came_from[current]] + gui.heuristic(
                    came_from[current], neighbor
                )
            else:
                tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float("inf")):
                if neighbor in came_from and line_of_sight(
                    came_from[current], neighbor
                ):
                    came_from[neighbor] = came_from[current]
                else:
                    came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + gui.heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

                gui.color_cell(neighbor, "visited")
                gui.root.update()
                time.sleep(0.2)

    return None


def fringe_search(gui):
    def expand(node):
        return [(neighbor, 1) for neighbor in gui.get_neighbors(node)]

    start = gui.start
    goal = gui.end
    fringes = {0: [start]}
    visited = set()
    parents = {start: None}
    costs = {start: 0}

    flimit = gui.heuristic(start, goal)
    while True:
        while fringes.get(flimit, []):
            current_fringes = fringes[flimit]
            fringes[flimit] = []
            for node in current_fringes:
                if node == goal:
                    path = []
                    while node is not None:
                        path.append(node)
                        node = parents[node]
                    return path[::-1]

                if node in visited:
                    continue

                visited.add(node)
                gui.color_cell(node, "visited")
                gui.root.update()
                time.sleep(0.2)

                for child, cost in expand(node):
                    if child in visited:
                        continue

                    g = costs[node] + cost
                    h = gui.heuristic(child, goal)
                    f = g + h

                    if f > flimit:
                        if child not in fringes:
                            fringes[f] = []
                        fringes[f].append(child)
                        if child not in costs:
                            costs[child] = g
                        if child not in parents:
                            parents[child] = node
                    elif child not in costs or g < costs[child]:
                        costs[child] = g
                        parents[child] = node
                        if child not in fringes:
                            fringes[flimit] = []
                        fringes[flimit].append(child)

            if not fringes[flimit]:
                del fringes[flimit]
        if not fringes:
            return None
        flimit = min(fringes.keys())


def sma_star(gui):
    class Node:
        def __init__(self, state, parent=None, g=0, h=0):
            self.state = state
            self.parent = parent
            self.g = g
            self.h = h
            self.f = g + h
            self.children = []

    def expand(node):
        if not node.children:
            for neighbor in gui.get_neighbors(node.state):
                child = Node(
                    neighbor, node, node.g + 1, gui.heuristic(neighbor, gui.end)
                )
                node.children.append(child)
        return node.children

    start_node = Node(gui.start, None, 0, gui.heuristic(gui.start, gui.end))
    open_list = [start_node]
    closed_set = set()
    memory_limit = 1000  # Adjust this value based on available memory

    while open_list:
        current = min(open_list, key=lambda x: x.f)
        open_list.remove(current)

        if current.state == gui.end:
            path = []
            while current:
                path.append(current.state)
                current = current.parent
            return path[::-1]

        closed_set.add(current.state)
        gui.color_cell(current.state, "visited")
        gui.root.update()
        time.sleep(0.2)

        for child in expand(current):
            if child.state in closed_set:
                continue

            if child not in open_list:
                open_list.append(child)
            elif child.g < next(
                node.g for node in open_list if node.state == child.state
            ):
                open_list.remove(
                    next(node for node in open_list if node.state == child.state)
                )
                open_list.append(child)

        if len(open_list) > memory_limit:
            worst = max(open_list, key=lambda x: x.f)
            open_list.remove(worst)
            if worst.parent and all(
                child in closed_set for child in worst.parent.children
            ):
                worst.parent.children.remove(worst)
                if (
                    worst.parent not in open_list
                    and worst.parent.state not in closed_set
                ):
                    open_list.append(worst.parent)

    return None
