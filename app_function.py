import sys
import math
import pandas as pd
import datetime as dt

def is_prime(x):
  for i in range(2,int(math.sqrt(x))+1):
    if (x % i) == 0:
      return 0
  return 1


def has_exact_square(x):
    if int(math.sqrt(x)) - math.sqrt(x) == 0.0:
        return 1
    return 0


def get_factors(x) :
    if x == 0:
        return [0, 1]
    if x == 1:
        return [1, 1]
    factors = []
    i = 1
    while i <= x :
        if (x % i==0) :
            factors.append(i)
        i = i + 1
    return factors


def get_middle_factors(factors):
    if len(factors) % 2 == 0:
        a = factors[len(factors)//2 - 1]
        b = factors[len(factors)//2]
        return [a, b]
    else:
        a = factors[len(factors)//2]
        return [a, a]


def get_b_div_a(x):
    factors = get_factors(x)
    mf = get_middle_factors(factors)
    return mf[1] / mf[0]


if __name__ == "__main__":
    LIMIT = sys.argv[1]
    start_execution = dt.datetime.now()
    PHI = 1.61803398874988
    TDS_PI = 1.12837916709551
    numbers = [x for x in range(2, int(LIMIT))]
    df = pd.DataFrame(numbers, columns=['number'])
    df['b/a'] = df['number'].apply(get_b_div_a)
    df['phi_delta'] = abs(PHI-df['b/a'])
    phi_delta_min_idx = df["phi_delta"].idxmin()
    print(df.loc[phi_delta_min_idx])
    print("The execution time is :", dt.datetime.now() - start_execution)
