# Day 9 - Problem Solution

# By inspecting the encryption_algorithm.txt file, it's easy to see that the encryption algorithm works as follows:
#   - Convert each character in the message into its corresponding ASCII number;
#   - Multiply the i'th number in the resulting list by the i'th prime number and return the resulting list.

# Reversing this algorithm is simply a matter of finding the first n primes, where n is the length of the encrypted
# message, then dividing the i'th number by the i'th prime, and then converting the result back to its corresponding
# ASCII character. It is not hard to write a function that finds the first n primes using trial division; here however
# we use the function isprime from the sympy library.

# ---------------------------------------------------------------------------------------------------------------------


from sympy import isprime


def get_primes(n):
    # Get the first n prime numbers.
    step = 0
    primes = []
    while len(primes) < n:
        while not isprime(step):
            step += 1
        primes.append(step)
        step += 1

    return primes


def decrypt(encrypted):
    # Decrypt the encrypted message by dividing the i'th number in it
    # by the i'th prime number, and then converting the result to its
    # corresponding ASCII character.
    keys = get_primes(len(encrypted))
    ascii = []
    for i, letter in enumerate(encrypted):
        ascii.append(int(letter) // keys[i])

    decrypted = [chr(i) for i in ascii]

    return "".join(decrypted)


def main():
    print()
    encrypted_string = input(
        "Input the encrypted message (in the format e.g. 1, 2, 3, 4):\n"
    )
    encrypted = encrypted_string.split(", ")
    print()
    print(f"Decrypted message = {decrypt(encrypted)}")
    print()


if __name__ == "__main__":
    main()
