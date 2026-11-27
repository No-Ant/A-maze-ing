class OutputError(Exception):
    def __init__(self, message: str = "Output error!") -> None:
        super().__init__(message)


def write_output(
    grid: list[list[int]],
    path: str,
    entry: tuple[int, int],
    exit: tuple[int, int]
) -> None:
    width = len(grid[0])
    height = len(grid)
    try:
        with open(path, "w") as file:
            for y in range(height):
                if y != 0:
                    file.write("\n")
                for x in range(width):
                    file.write("{0:x}".format(grid[y][x]))
            file.write("\n\n")
            file.write(f"{entry[0]},{entry[1]}\n")
            file.write(f"{exit[0]},{exit[1]}\n")
    except (OSError, UnicodeDecodeError) as e:
        raise OutputError(f"Error opening output file: {e}") from e
