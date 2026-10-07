import heapq

initial = (2, 8, 3,
           1, 6, 4,
           7, 0, 5)

goal = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)

def misplaced_tiles(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count

def manhattan_distance(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            current_row = i // 3
            current_col = i % 3

            goal_index = goal.index(tile)

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance

def get_neighbors(state):
    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "U"),
        (1, 0, "D"),
        (0, -1, "L"),
        (0, 1, "R")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors

def a_star(heuristic):

    open_list = []

    g_cost = {initial: 0}
    parent = {initial: None}
    move_taken = {}

    h = heuristic(initial)

    heapq.heappush(
        open_list,
        (h, 0, initial)
    )

    while open_list:

        f, g, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, move in get_neighbors(current):

            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                h = heuristic(neighbor)
                new_f = new_g + h

                parent[neighbor] = current
                move_taken[neighbor] = move

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor)
                )

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    return path, g_cost[goal]

def print_state(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()

print("CASE 1: MISPLACED TILES")

path, cost = a_star(misplaced_tiles)

for state in path:
    print_state(state)

print("Total Cost =", cost)

print("CASE 2: MANHATTAN DISTANCE")

path, cost = a_star(manhattan_distance)

for state in path:
    print_state(state)

print("Total Cost =", cost)