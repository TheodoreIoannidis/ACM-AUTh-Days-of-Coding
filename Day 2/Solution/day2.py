# Day 2 - Problem Solution

# This is one of these problems where you just have to write code which does exactly what you are asked to do.

# -----------------------------------------------------------------------------------------------------------------------


from termcolor import colored


def input_data():
    # Get the required data (RAM size, cache size, addresses to be visited).
    # Returns the cache size and the sequence of addresses.

    # Ask for the RAM size.
    while True:
        try:
            ram_size = int(input("Give RAM size:\n"))
            if ram_size <= 1:
                raise Exception()
            break
        except:
            print("The RAM size needs to be an integer greater than 1.")

    # Ask for the cache size.
    while True:
        try:
            cache_size = int(input("Give cache size (< RAM size):\n"))
            if cache_size <= 0 or cache_size >= ram_size:
                raise Exception()
            break
        except:
            print(
                "The cache size needs to be a positive integer smaller than the RAM size."
            )

    # Ask for the number of addresses to be visited.
    while True:
        try:
            num_addresses = int(input("Give number of addresses:\n"))
            if num_addresses <= 0:
                raise Exception()
            break
        except:
            print("The number of addresses needs to be a positive integer.")

    # Ask for the addresses to be visited.
    addresses = []
    print(f"Give addresses (0-{ram_size-1}):")
    for i in range(num_addresses):
        while True:
            try:
                address = int(input(f"Address {i+1}: "))
                if address < 0 or address >= ram_size:
                    raise Exception()
                break
            except:
                print(
                    f"The address needs to be an integer in the range (0-{ram_size-1})."
                )

        addresses.append(address)

    return cache_size, addresses


def print_cache(cache, hit, ind):
    # Print a colored version of the cache to indicate whether the request
    # is a hit (green) or a miss (red).
    cache_print_list = []
    for i, entry in enumerate(cache):
        if i == ind:
            if hit:
                cache_print_list.append(colored(str(entry), "green"))
            else:
                cache_print_list.append(colored(str(entry), "red"))
        else:
            cache_print_list.append(str(entry))

    return "[" + ", ".join(cache_print_list) + "]"


def main():
    print()
    # Get input data.
    cache_size, addresses = input_data()
    print()

    cache = ["X" for _ in range(cache_size)]
    for address in addresses:
        ind = address % cache_size
        # If address mod cache size is occupied by address, then it's a hit.
        if cache[ind] == address:
            print(colored("hit!", "green"))
            hit = True
        # Otherwise, it is a miss.
        else:
            print(colored("miss!", "red"))
            cache[address % cache_size] = address
            hit = False

        print("Cache: " + print_cache(cache, hit, ind))
    print()


if __name__ == "__main__":
    main()
