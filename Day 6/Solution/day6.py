# Day 6 - Problem Solution

# The solution algorithm works as follows:
#   1) Find all the sweets you can buy with your current amount of money. If there are none, then the algorithm terminates.
#   2) Find the sweet i among those you can buy such that diff[i] = A[i] - B[i] is minimal.
#   3) Buy sweet i as many times as possible; that is, while A[i] <= E, set E <- E - diff[i] and increase the number of
#      sweets bought by 1.
#   4) Go back to (1).

# -------------------------------------------------------------------------------------------------------------------------


from math import inf


def max_sweet_no(E, A, B):
    # E = initial money
    # A = prices (list)
    # B = returns (list)
    max_sweets = 0
    while True:
        available_catalogue = [
            (price, money_back) for (price, money_back) in list(zip(A, B)) if price <= E
        ]
        if not available_catalogue:
            break

        min_diff = inf
        for price, money_back in available_catalogue:
            if price - money_back < min_diff:
                min_diff = price - money_back

        while price <= E:
            max_sweets += 1
            E -= min_diff

    return max_sweets


def main():
    print()
    E = int(input("Give the initial amount of money (E): "))
    A = [
        int(i)
        for i in input(
            "Give the list of prices (A) as a string (e.g. 1,2,3,4):\n"
        ).split(",")
    ]
    B = [
        int(i)
        for i in input(
            "Give the list of money you get back (B) as a string (e.g. 1,2,3,4):\n"
        ).split(",")
    ]
    print()
    print(f"Max number of sweets you can buy = {max_sweet_no(E, A, B)}")
    print()


if __name__ == "__main__":
    main()
