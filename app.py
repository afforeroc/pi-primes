import sys
import math
import pandas as pd
import datetime as dt
from tabulate import tabulate

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


def get_std_area(mf):
    return mf[0] / mf [1]


def get_b_div_a(x):
    factors = get_factors(x)
    mf = get_middle_factors(factors)
    return mf[1] / mf[0]


if __name__ == "__main__":
    LIMIT = sys.argv[1]
    start_execution = dt.datetime.now()
    PHI = 1.61803398874988
    PI = math.pi
    numbers = [x for x in range(2, int(LIMIT))]
    b_div_a_list = []
    phi_delta_list = []
    pi_delta_list = []
    for x in numbers:
        factors = get_factors(x)
        mf = get_middle_factors(factors)
        b_div_a = mf[1] / mf[0]
        phi_delta = abs(PHI - b_div_a)
        pi_delta = abs(PI - b_div_a)
        # Appends
        b_div_a_list.append(b_div_a)
        phi_delta_list.append(phi_delta)
        pi_delta_list.append(pi_delta)
    data = {
        'number':  numbers,
        'b/a': b_div_a_list, 
        'phi_delta': phi_delta_list,
        'pi_delta': pi_delta_list
    }
    print("The execution time is :", dt.datetime.now() - start_execution)
    df = pd.DataFrame(data)
    df_phi_delta = df.sort_values(by="phi_delta")
    print(df_phi_delta.head())
    print("#################")
    #print(tabulate(df_phi_delta, headers='keys', tablefmt='psql'))
    df_pi_delta = df.sort_values(by="pi_delta")
    print(df_pi_delta.head())
    #print(tabulate(df_tds_pi_delta, headers='keys', tablefmt='psql'))