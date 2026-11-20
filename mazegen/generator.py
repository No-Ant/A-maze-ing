import random
from collections import deque

#wall bits; a set bit (1111) = 16  means CLOSED WALLS
N , S, W, E = 1, 2, 4, 8

#direction letters: on bit order: (W, S, E, N)
DIRECTION: dict[str, tuple[int, int, int, int]] = {
	"N": (N, S, 0, -1),
	"E": (E, W, 1, 0),
	"S": (S, N, 0, 1),
	"W": (W, E, -1, 0),
}

#generate a maze and expose grid and short path
#atributes: grid[y][x] is an int 0-15(16 is closed walls)

#__init__: store parameters and validate them
#raises ValueError if the size, entry or exit are invalid
class Mazegenerator:


	def __init__(
	self,
	width: int,
	height: int,
	entry: tuple[int, int],
	exit_: tuple[int, int],
	perfect: bool = True,
	seed: int | None = None,			
	) -> None:

		self.width = width
		self.height = height
		self.entry = entry
		self.exit_ = exit_
		self.perfect = perfect
		self.random = random.Random(seed) #same seed = same maze
		self.grid: list[list[int]] = []
		self.fortytwo: set[tuple[int, int]] = set()
		self.validate()

#raise ValueError with a clear message
# it checks size, bonds and makes sure entry != exit
	def _validate(self) -> None:
		pass


# build self.grid. need to call this before solve()
	def generate(self) -> None:
		self.grid = [[15] * self.width for _ in range(self.height)]
		self._place_42()
		self._carve() # recursive backtracker
		if not self.perfect:
			self._add_loops() #remove walls, avoid 3x3 open areas


#fill the self.fortytwo with 42 in the middle
#REMINDER: if maze too small, print an error and return
	def _place_42(self) -> None:
		pass


#carves a perfect maze, skipping pocked cells
#REMMINDER: pick a start cell, iterative DFS with a stack
	def _carve(self) -> None:
		pass


#remove some walls to create loops when perfect=False
	def _add_loops() -> None:
		pass


#open the wall on side d of (x, y) AND on the neighbour
	def _open_wall(self, x: int,y: int, d: str) -> None:
		bit, opp, dx, dy = DIRECTION[d]
		self.grid[y][x] &= ~bit
		self.grid[y + dy][x + dx] &= ~opp


#returns the short path to the maze
#REMINDER: BFS from self.entry, remeber where each cell came from, then rebuild the path as N|E|S|W letters
	def solve(self) -> str:
		deque() #BFS queue goes here
		return ""


if __name__ == "__main__":
	g = Mazegenerator(10, 8, (0, 0), (9, 7), True, 42)
	g.generate()
	for row in g.grid:
		print("".join(f"{c:X}" for c in row))
	print(g.solve())