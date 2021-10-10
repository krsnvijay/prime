import sys
from functools import cache

import primesieve


@cache
def sum_digits(number):
    """
    Sums all the digits of a number recursively to a single digit number
    eg: 192 = 1 + 9 + 2 = 12
      => 12 = 1 + 2 = 3
      so 192 will turn to 3
    """
    result = sum(int(digit) for digit in str(number))
    # exit condition
    if result < 10:
        return result
    else:
        # recursively call sum_digits
        return sum_digits(result)


def primes_to_digits(number):
    """
    Generator fn to get a prime number and a sum of its digits
    """
    it = primesieve.Iterator()
    prime = it.next_prime()
    while prime < number:
        agg_prime = sum_digits(prime)
        yield prime, agg_prime
        prime = it.next_prime()


def count_frequencies(number):
    """
    Counts the frequencies of digit sum of primes in a given range
    """
    freq = {}
    for prime, agg in primes_to_digits(number):
        if agg in freq:
            freq[agg] += 1
        else:
            freq[agg] = 1
    print(f"{number}: {freq}")


def check_consecutive_primes(number):
    """
    Checks if prev prime and next prime have the same digit sum
    """
    primes_digits = primes_to_digits(number)
    prev = next(primes_digits)
    for cur in primes_digits:
        result = True
        if prev[1] == cur[1]:
            result = False
            print(prev, cur, result)
        yield prev, cur, result
        prev = cur


def prime_digits_to_csv(generator, full_log="output\prime2digits_all.csv", false_log="output\prime2digits_false.csv"):
    """
    Logs the comparision results
    """
    full_log_file = open(full_log, 'w')
    false_log_file = open(false_log, 'w')
    for prime, agg_prime, result in generator:
        if not result:
            false_log_file.write(f"{prime},{agg_prime},{result}\n")
        full_log_file.write(f"{prime},{agg_prime},{result}\n")
    full_log_file.close()
    false_log_file.close()


if __name__ == "__main__":
    number = 100000
    if sys.argv == 3:
        number = int(sys.argv[2])
    prime_digits_to_csv(check_consecutive_primes(number))
    # count_frequencies(1000000000)
