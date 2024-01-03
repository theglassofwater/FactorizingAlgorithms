# import primefac
# import math
# import sympy
# import random
import rsa 
import timeit
import trails_division.trails as trails
import pollards_rho.rho as rho


def testing_trails():
    x = trails.factorize(n)
    #if x == p or x == q:
    #    print("correct")

def testing_rho():
    x = rho.factorize(n)
    #if x == p or x == q:
    #    print("correct")


if __name__ == "__main__":
    global p,q,n_bits,n
    n_bits = 55
    p,q = rsa.prime.getprime(n_bits // 2), rsa.prime.getprime(n_bits // 2)
    n = p*q
    num_of_runs = 5
    print(f"num of runs per alg = {num_of_runs}, num of bits in n = {n_bits}")
    time_rho = timeit.Timer(testing_rho).timeit(number=num_of_runs)
    time_trails = timeit.Timer(testing_trails).timeit(number=num_of_runs)
    print(f"Average time of trails is {round(time_trails/num_of_runs,4)}s for {n_bits} bit N")
    print(f"Average time of rho is {round(time_rho/num_of_runs,4)}s for {n_bits} bit N")
