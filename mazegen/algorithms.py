import random

N, E, S, W = 1, 2, 4, 8

moves: dict[tuple[int, int], tuple[int, int]] = {
    (0, 1): (N, S),
    (-1, 0): (E, W),
    (0, -1): (S, N),
    (1, 0): (W, E)
}

drawing: list[str] = [
    "#...###",
    "#.....#",
    "###.###",
    "..#.#..",
    "..#.###"
]


def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    return 0 <= x < width and 0 <= y < height


def ft_symbol(width: int, height: int) -> set[tuple[int, int]]:
    if width <= 7 or height <= 5:
        return set()
    cells = set()
    for y in range(5):
        for x in range(7):
            if drawing[y][x] == "#":
                cells.add((x, y))
    # for y in range(5):
    #     print()
    #     for x in range(7):
    #         if (x, y) in cells:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    add_x = (width - 7) // 2
    add_y = (height - 5) // 2
    cells = {(x + add_x, y + add_y) for (x, y) in cells}
    return cells


def rbt(
    grid: list[list[int]],
    start: tuple[int, int],
    rng: random.Random
) -> list[list[int]]:
    height = len(grid)
    width = len(grid[0])
    stack: list[tuple[int, int]] = [start]
    visited: set[tuple[int, int]] = {start}
    visited.update(ft_symbol(width, height))
    while len(stack) > 0:
        x, y = stack[-1]
        options: list[tuple[int, int]] = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        options = [
            (nx, ny) for nx, ny in options
            if in_bounds(nx, ny, width, height) and
            (nx, ny) not in visited
        ]
        if len(options) == 0:
            stack.pop()
            continue
        nxt: tuple[int, int] = rng.choice(options)
        nx, ny = nxt
        dx, dy = x - nx, y - ny
        og_bit, nxt_bit = moves[(dx, dy)]
        grid[y][x] &= ~og_bit
        grid[ny][nx] &= ~nxt_bit
        stack.append((nx, ny))
        visited.add((nx, ny))
    return grid


if __name__ == "__main__":
    width, height = 15, 13

    grid = [[15] * width for i in range(height)]

    rng = random.Random(42)

    grid = rbt(grid, (0, 0), rng)
    """ for row in grid:
        print(row)
    print(ft_symbol(15, 13))
    for y in range(13):
        print()
        for x in range(15):
            if grid[y][x] == 15:
                print("#", end="")
            else:
                print(".", end="") """
    """ write_output(grid, "output.txt", (0, 0), (12, 9)) """
