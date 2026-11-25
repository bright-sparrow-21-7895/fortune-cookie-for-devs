# Fortune Cookie Wisdom for Developers — make.fun bounty entry.
#
# Concept: a real fortune cookie mixes a blessing with a warning, so this
# one is written as a warning a senior dev would tape to their monitor.
# The feared bug is not in the messy legacy module everyone complains
# about — it hides in the "obviously correct" code its author was too
# proud to test. "It has tenure" lands the joke: the bug cannot be fired,
# performance-managed, or refactored away; it has settled in for good.
import os

ENTRY = "The bug you fear most is hiding in the code you were too proud to test. It has tenure."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
