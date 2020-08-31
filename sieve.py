# SieveOfErastothenes taken from geeksforgeeks.com

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
import sys
from math import pi


def SieveOfEratosthenes(n):

    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            yield p


def sum_digits(number):
    result = sum(int(digit) for digit in str(number))
    # exit condition
    if result <= 13:
        return result
    else:
        # recursively call sum_digits
        return sum_digits(result)


def csv_line(prime):
    x = str(prime)
    y = str(sum_digits(prime))
    z = str((sum_digits(prime)/13)*360)
    data_point = [x, y, z]
    return ','.join(data_point) + "\n"


def primes_as_csv(n):
    for prime in SieveOfEratosthenes(n):
        yield csv_line(prime)


# driver program
if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage: sieve <n>")
        sys.exit(-1)
    n = int(sys.argv[1])
    f = open("primes.csv", "w")
    for line in primes_as_csv(n):
        f.write(line)
