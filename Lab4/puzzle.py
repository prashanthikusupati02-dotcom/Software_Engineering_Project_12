
import random


class Puzzle:
    def __init__(self, size=4):
        if size not in (3, 4, 5):
            raise ValueError("Puzzle size must be 3, 4, or 5.")

        self.size = size
        self.board = self.make_board()

    def make_board(self):
        # Start with the solved arrangement
        tiles = list(range(1, self.size * self.size)) + [0]
        board = [
            tiles[r * self.size:(r + 1) * self.size]
            for r in range(self.size)
        ]

        # Scramble by making legal moves of the blank
        previous_blank = None

        for _ in range(100):
            blank_r, blank_c = next(
                (r, row.index(0))
                for r, row in enumerate(board)
                if 0 in row
            )

            neighbours = []
            for dr, dc in [
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]:
                nr, nc = blank_r + dr, blank_c + dc

                if (
                    0 <= nr < self.size
                    and 0 <= nc < self.size
                    and (nr, nc) != previous_blank
                ):
                    neighbours.append((nr, nc))

            # Avoid immediately undoing the previous move
            nr, nc = random.choice(neighbours)
            previous_blank = (blank_r, blank_c)

            board[blank_r][blank_c], board[nr][nc] = (
                board[nr][nc],
                board[blank_r][blank_c]
            )

        return board

    def blank_pos(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return r, c

    def move(self, direction):
        directions = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1),
        }

        if direction not in directions:
            return False

        r, c = self.blank_pos()
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (
            0 <= nr < self.size
            and 0 <= nc < self.size
        ):
            return False

        self.board[r][c], self.board[nr][nc] = (
            self.board[nr][nc],
            self.board[r][c]
        )
        return True

    def solved(self):
        expected = list(range(1, self.size * self.size)) + [0]
        return sum(self.board, []) == expected
