GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(*state[i:i + 3])
    print()


def get_moves(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            yield tuple(new_state)


def depth_limited_dfs(state, depth, limit, path):
    if state == GOAL:
        return path

    if depth == limit:
        return None

    for next_state in get_moves(state):

        if next_state not in path:
            result = depth_limited_dfs(
                next_state,
                depth + 1,
                limit,
                path + [next_state]
            )

            if result:
                return result

    return None


def iddfs(initial):
    for limit in range(50):
        result = depth_limited_dfs(
            initial,
            0,
            limit,
            [initial]
        )

        if result:
            return result

    return None


initial = tuple(map(int, input("Enter 9 values: ").split()))

solution = iddfs(initial)

if solution:
    print("\nSolution:")

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)

    print("Total moves:", len(solution) - 1)

else:
    print("No solution found.")