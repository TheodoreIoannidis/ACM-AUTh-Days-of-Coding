# Day 5 - Problem Solution

# The only real "difficulty" is in obtaining all the possible pairs of line segments. While this can be easily
# done manually, the combinations function from the itertools library does it automatically.

# ----------------------------------------------------------------------------------------------------------------

from itertools import combinations


def max_area(height):
    # Find the maximal area among the areas of the admissible rectangles.
    n = len(height)
    area = 0
    for i, j in combinations(range(n), 2):
        new_area = min([height[i], height[j]]) * abs(i - j)
        if new_area > area:
            area = new_area

    return area


def main():
    print()
    height_string = input("Input the list of heights (in the format e.g. 1,2,3,4):\n")
    height = [int(i) for i in height_string.split(",")]
    print()
    print(f"Max area = {max_area(height)}")
    print()


if __name__ == "__main__":
    main()
