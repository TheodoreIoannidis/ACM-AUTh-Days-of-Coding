# Day 1 - Problem Solution

# To get the total number of complete decks, it suffices to keep track of how many times each card appears
# in the given decks, and then find the minimum of these numbers (call it d). By subtracting d from the number
# of occurrences of each card, one can then obtain the number and type of the leftover cards.

# -----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

from cards import CARDS


def decks_count(decks_start):
    # Input: list of (possibly incomplete) decks.
    # Output: number of decks, list of extra cards.

    # Count how many times each card appears in the decks.
    cards_frequency_dict = {card: 0 for card in CARDS}
    for deck in decks_start:
        for card in deck:
            cards_frequency_dict[card] += 1

    # Get the minimum number of occurrences of each card; this is the number of complete decks.
    complete_decks_no = min([cards_frequency_dict[card] for card in CARDS])

    # Subtract the number of decks from the number of occurrences of each card to get the number of cards
    # of each type that are left. Store each card in a new list as many times as its leftover frequency.
    extra_cards = []
    for card in CARDS:
        extra_cards.extend(
            [card for _ in range(cards_frequency_dict[card] - complete_decks_no)]
        )

    return complete_decks_no, extra_cards


def plot_extra_cards(extra_cards):
    # Visualise the extra cards frequencies via a bar chart.
    cards_frequency_dict = {card: 0 for card in CARDS}
    for card in extra_cards:
        cards_frequency_dict[card] += 1
    cards = list(cards_frequency_dict.keys())
    count = list(cards_frequency_dict.values())

    plt.figure(figsize=(20, 5))
    plt.bar(cards, count, color="maroon")
    plt.title("Extra cards frequencies:")
    plt.xticks(rotation=90)
    plt.yticks([i for i in range(max(count) + 1)])
    plt.show()


def main():
    print()
    decks_start_no = int(
        input("How many (possibly incomplete) decks are you starting with? ")
    )
    print()
    print(
        f"Please enter {decks_start_no} decks using the following format "
        "(where the following is an example of a complete deck):"
    )
    print()
    print(", ".join([f"'{card}'" for card in CARDS]))

    decks_start = []
    for _ in range(decks_start_no):
        print()
        decks_start.append(input("Input a deck: ").replace("'", "").split(", "))

    complete_decks_no, extra_cards = decks_count(decks_start)
    print()
    print(f"Number of complete decks = {complete_decks_no}")
    print()
    print(f"Extra cards = {extra_cards}")
    print()
    plot_extra_cards(extra_cards)


if __name__ == "__main__":
    main()
