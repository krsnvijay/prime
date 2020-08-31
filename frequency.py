from itertools import groupby
import csv


def count_frequency(numbers):
    return {value: len(list(freq)) for value, freq in groupby(sorted(numbers))}


with open('primes.csv') as csvfile:
    primereader = csv.reader(csvfile)
    numbers = [line[1] for line in primereader]
    print(count_frequency(numbers))
