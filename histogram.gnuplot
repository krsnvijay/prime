set datafile separator ','
set style histogram rowstacked gap 0
set style fill solid 0.5 border lt -1
plot "primes.csv" u 2:1