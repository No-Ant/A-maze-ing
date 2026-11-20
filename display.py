#pseudocode

#def render(grid, entry, exit, path, show_path):

    # 1. Make a big canvas, all walls
    #canvas = (2*height + 1) rows x (2*width + 1) columns, filled with WALL

    # 2. For every cell in the maze:
    #for each cell (x, y):
        #the cell's spot on the canvas is (2*y + 1, 2*x + 1)
        #make that spot OPEN
            #(or LOCKED colour if the cell value is 15, the "42")

        # open the tile next to it for every side that has no wall
        #if north wall is open: make the tile above it OPEN
        #if east wall is open:  make the tile to the right OPEN
        #if south wall is open: make the tile below it OPEN
        #if west wall is open:  make the tile to the left OPEN

    # 3. Draw the path (optional)
    #if show_path:
        #start at the entry cell
        #for each letter in the path (N, E, S, W):
            #move one step in that direction
            #paint the in-between tile PATH
            #paint the new cell PATH

    # 4. Draw entry and exit on top
    #paint entry cell ENTRY colour
    #paint exit cell EXIT colour

    # 5. Show it
    #clear the screen
    #print the canvas row by row

#actual one
WALL = "\033[47m  \033[0m"
OPEN = "  "
ENTRY = "\033[42m  \033[0m"
EXIT = "\033[41m  \033[0m"
PATH = "\033[44m  \033[0m"
LOCKED = "\033[45m  \033[0m"   # the "42"


def render(grid, entry, exit_, path, show_path):
    h, w = len(grid), len(grid[0])
    c = [[WALL] * (2 * w + 1) for _ in range(2 * h + 1)]
    for y in range(h):
        for x in range(w):
            cy, cx = 2 * y + 1, 2 * x + 1
            v = grid[y][x]
            c[cy][cx] = LOCKED if v == 15 else OPEN
            if not v & 1: c[cy - 1][cx] = OPEN   # N open
            if not v & 2: c[cy][cx + 1] = OPEN   # E open
            if not v & 4: c[cy + 1][cx] = OPEN   # S open
            if not v & 8: c[cy][cx - 1] = OPEN   # W open
    if show_path:
        x, y = entry
        for d in path:
            dx, dy = {"N": (0, -1), "E": (1, 0),
                      "S": (0, 1), "W": (-1, 0)}[d]
            c[2 * y + 1 + dy][2 * x + 1 + dx] = PATH  # tile between
            x, y = x + dx, y + dy
            c[2 * y + 1][2 * x + 1] = PATH            # next cell
    c[2 * entry[1] + 1][2 * entry[0] + 1] = ENTRY
    c[2 * exit_[1] + 1][2 * exit_[0] + 1] = EXIT
    print("\033[H\033[J", end="")                     # clear screen
    print("\n".join("".join(row) for row in c))