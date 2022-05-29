# Day 4 - Problem Solution

# Our solution is broken down into 4 steps.
#   1) Take the string input and transform it into a matrix according to the given dimensions.
#   2) Make a new matrix representing the tilted original matrix but ignoring gravity.
#   3) Simulate the effects of gravity on the new tilted matrix. This is done step by step until no more
#      changes are possible.
#   4) Transform the tilted matrix into a string output.

# -----------------------------------------------------------------------------------------------------------------


def make_table_from_string(string, n, m):
    # Create the matrix represented by the string input.
    table_list = string.split(",")
    table = [[table_list[i * m + j] for j in range(m)] for i in range(n)]
    return table


def make_string_from_table(table, n, m):
    # Create a string representing the tilted matrix (notice the dimension flip).
    table_list = []
    for i in range(m):
        for j in range(n):
            table_list.append(table[i][j])

    return ",".join(table_list)


def tilt(table, n, m, direction):
    # Create a tilted matrix, ignoring the force of gravity.
    tilted = [[None for _ in range(n)] for _ in range(m)]
    if direction == "L":
        for i, row in enumerate(table):
            for j, item in enumerate(row):
                tilted[m - 1 - j][i] = item
    elif direction == "R":
        for i, row in enumerate(table):
            for j, item in enumerate(row):
                tilted[j][n - 1 - i] = item

    return tilted


def gravity(tilted, n, m):
    # Apply gravity on the tilted matrix.
    for j in range(n):
        # Gravity is applied step by step on each column for as long as that changes the matrix.
        while True:
            change = False
            for i in range(m - 1, -1, -1):
                # If you encounter a sphere that can be moved downards, move it down one step.
                if tilted[i][j] == "O":
                    while i < m - 1 and tilted[i + 1][j] == "X":
                        tilted[i + 1][j] = "O"
                        tilted[i][j] = "X"
                        change = True
            # Change column once no more changes can be made on the current one.
            if not change:
                break

    return tilted


def main():
    print()
    n = int(input("Input the height of the matrix (n): "))
    m = int(input("Input the width of the matrix (m): "))
    direction = input("Input the direction of the tilt (L/R): ")
    string = input("Input the matrix as a string: ")
    table = make_table_from_string(string, n, m)
    tilted = tilt(table, n, m, direction)
    tilted_gravity = gravity(tilted, n, m)
    print()
    print(f"Tilted matrix as string = {make_string_from_table(tilted_gravity, n, m)}")
    print()


if __name__ == "__main__":
    main()
