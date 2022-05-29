# Day 7 - Problem Solution

# Our solution works as follows. At first, we find all the possible ways in which the given input can be split into
# consecutive parts of length 1 or 2 (so e.g. for the input "123", we obtain the splits ["1", "23"], ["12", "3"],
# ["1", "2", "3"]). This is done by a recursive algorithm, whose steps are described below:

#   - Base cases: if the input is of length 1, say "i" return [["i"]];
#                 if the input is of length 2, say "ij" return [["ij"], ["i", "j"]].
#   - Inductive case: if the input is of length >= 3, apply the algorithm on input[1:] and the attach input[0] to each
#                     element of the resulting list; similarly, apply the algorithm on input[2:] and attach input[:2]
#                     to each element of the resulting list. Return the union of the two lists.

# Afterwards, we check how many of these splits result in a valid decryption, by removing those that contain parts that
# start with zero, or that are larger than 26. Finally, we return the number of splits that are left.

# ----------------------------------------------------------------------------------------------------------------------

import sys


def split(string):
    # Base cases
    if len(string) == 1:
        return [[string]]
    elif len(string) == 2:
        return [[string], [string[0], string[1]]]

    # Inductive case
    elif len(string) >= 3:
        split_list = []

        # Attach string[0] to each element of split(string[1:])
        for item in split(string[1:]):
            item.insert(0, string[0])
            split_list.append(item)

        # Attach string[:2] to each element of split(string[2:])
        for item in split(string[2:]):
            item.insert(0, string[:2])
            split_list.append(item)

        return split_list
    else:
        return []


def check(split_to_check):
    # Check whether a split leads to a valid decryption or not
    for item in split_to_check:
        if item.startswith("0") or int(item) > 26:
            return False
    return True


def decryptions_no(message):
    # Find the number of valid decryptions to a given encrypted message
    split_list = split(message)
    split_list_copy = split_list.copy()
    for split_to_check in split_list_copy:
        if not check(split_to_check):
            split_list.remove(split_to_check)

    return len(split_list)


def main():
    if len(sys.argv) != 2:
        sys.exit(
            "Usage: python day7.py encrypted_message (where encrypted_message is e.g. 1234)"
        )
    encrypted_message = sys.argv[1]
    print()
    print(f"Number of distinct decryptions = {decryptions_no(encrypted_message)}")
    print()


if __name__ == "__main__":
    main()
