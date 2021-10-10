# Visualise Prime Numbers to find pattern emergence

Prime numbers are cool and unpredictable.

I'm not good at math, it goes over my head most of the time.

But My friend [Sai Kiran Reddy Lenkala](https://github.com/100193kiran) is , I'll try to visualise his experiments on prime numbers in this repo and maybe learn something along the way

## Requirements

- Python
- Gnuplot
- Primesieve
## Installation

```python
python -m venv venv
source venv\Scripts\activate
pip install -r requirements.txt
```

## Generate primes.csv

change the argument to generate primes till that number

```python
python sieve.py 10000
```

## Plot primes.csv

```bash
gnuplot -p primes.gnuplot
```

## Plot 1

This is a polar plot `(r,Θ)` with `r = prime number` and `Θ = (sum of its digits / 9) * 360`

for prime number `73`

```math
r = 73

sum of its digits = 7 + 3 => 10 = 1 + 0 => 1

Θ = (1 / 9) * 360 = 40°
```

![Polar Plot](output/plot.svg)

## Reference Plot

Watch [this video](https://youtu.be/EK32jo7i5LQ) from [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) to know more about patterns with prime numbers

This is a polar plot `(r,Θ)` with `r = prime number` and `Θ = prime number * 360`, recreated by me from the video.

![Spiral Polar Plot](output/plot-prime-prime.svg)
