
from game import SlidingPuzzle


def main():
    print("Sliding Puzzle")
    print("Choose board size:")
    print("1. 3 x 3")
    print("2. 4 x 4")
    print("3. 5 x 5")

    choice = input("Enter your choice (1-3): ").strip()

    sizes = {
        "1": 3,
        "2": 4,
        "3": 5,
    }

    if choice not in sizes:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return

    game = SlidingPuzzle(sizes[choice])
    game.run()


if __name__ == "__main__":
    main()
