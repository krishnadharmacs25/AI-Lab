# 8 Puzzle using Depth Limited DFS
# Solution in exactly 2 moves

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(*state[i:i+3])
    print()


def get_neighbors(state):
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(state, goal, depth, max_depth, path, visited):

    # Goal test
    if state == goal:
        return path

    # Depth limit
    if depth >= max_depth:
        return None

    visited.add(state)

    for next_state in get_neighbors(state):

        if next_state not in visited:

            result = dfs(
                next_state,
                goal,
                depth + 1,
                max_depth,
                path + [next_state],
                visited
            )

            if result is not None:
                return result

    return None


# ---------------- MAIN ----------------

print("8 PUZZLE USING DEPTH LIMITED DFS")
print("---------------------------------")

# Initial state exactly 2 moves from goal
initial_state = (
    1, 2, 3,
    4, 5, 6,
    0, 7, 8
)

MAX_DEPTH = 2

print("\nInitial State:")
print_board(initial_state)

print("Goal State:")
print_board(GOAL)

visited = set()

solution = dfs(
    initial_state,
    GOAL,
    0,
    MAX_DEPTH,
    [initial_state],
    visited
)

if solution is not None:

    print("Goal State Found!")
    print("\nSolution Path:")

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)

    print("Total moves:", len(solution) - 1)

else:
    print("Goal not found within 2 moves.")