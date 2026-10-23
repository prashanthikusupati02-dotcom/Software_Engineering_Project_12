
import time
from puzzle import Puzzle


class SlidingPuzzle:
    def __init__(self, size=4):
        self.size = size
        self.puzzle = Puzzle(self.size)
        self.moves = 0
        self.started = time.monotonic()
        self.completed = False

    def display(self):
        print()
        for row in self.puzzle.board:
            print(" ".join(f"{x or ' ':>2}" for x in row))

        elapsed = int(time.monotonic() - self.started)
        print("Moves:", self.moves, " Time:", elapsed, "s")

    def run(self):
        print(
            "Sliding Puzzle — W/A/S/D moves the tile into "
            "the blank. Q quits."
        )

        while True:
            self.display()

            if self.puzzle.solved():
                self.completed = True
                print("Solved!")
                return

            key = input("> ").strip().lower()

            if key == "q":
                return

            if key not in ("w", "a", "s", "d"):
                print("Use W/A/S/D or Q to quit.")
                continue

            if not self.puzzle.move(key):
                print("That move is not possible.")
                continue

            self.moves += 1

            if self.puzzle.solved():
                self.display()
                self.completed = True
                print("Solved!")
                return
