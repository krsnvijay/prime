set datafile separator ','
set polar
set angle degrees
set grid polar
plot "primes.csv" using 3:1 linetype 7 ps .6
