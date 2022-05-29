# Day 8 - Problem Solution

# One way to solve the problem (not the most efficient but certainly one of the fastest to code) is the following:
# First initialise a dictionary keeping track of the "cost" of each digit, that is the number of segments that are
# used in the digit's 7-segment representation. Then, for given integers n, k and a digit m, calculate the cost of
# each k-digit number, starting from 99...9 and going backwards, until you hit the first k-digit number which does
# not contain m and with cost at most cost(n). Note that during this process it is important to work with strings
# rather than integers, because e.g. 0000 is a valid input of cost 24 (whereas if it was converted to an integer
# it would become the number 0 of cost 6).

# -------------------------------------------------------------------------------------------------------------------


COSTS = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}


def cost(n):
    # Calculate the total cost (in segments) of n.
    cost_n = 0
    for i in n:
        cost_n += COSTS[i]

    return cost_n


def find_max_no(n, k, m):
    # Find the largest k-digit integer which does not contain m and which
    # has cost <= cost(n).
    cost_n = cost(n)
    # Start from 99...9 and keep going backwards until you hit a number with
    # the desired properties, or you run out of k-digit numbers.
    num = 10**k - 1
    while num >= 10 ** (k - 1):
        num_str = str(num)
        if m not in num_str and cost(num_str) <= cost_n:
            return num_str
        num = num - 1

    return None


def main():
    print()
    n = input("Input the number whose segments you want to use (n): ")
    k = int(input("Input the desired number of digits of the output (k): "))
    m = input("Input the digit you want to avoid in the output (m): ")
    print()
    answer = find_max_no(n, k, m)
    if answer == None:
        print(
            f"There is no {k}-digit number that can be written with at most "
            f"{cost(n)} segments while avoiding the digit {m}."
        )
    else:
        print(
            f"The maximum {k}-digit number that can be written with at most "
            f"{cost(n)} segments while avoiding the digit {m} is {answer} "
            f"(which uses {cost(answer)} segments)."
        )
    print()


if __name__ == "__main__":
    main()
