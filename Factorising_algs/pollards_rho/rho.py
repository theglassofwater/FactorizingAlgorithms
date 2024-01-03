# initialise by picking x0 and f() and put rabbit and turtle on x0 
# loop: then move rabbit and turtle, and calculate gcd(turtle-rabbit, n)
#    if gcd == 1: go to next interation
#    if gcd == n: failure, pick new x0 and f() (rare to happen if n is big)
#    else:  proper factor of n is found, turtple-rabbit = factor, gcd is another


# kinda recursive process because proper factor found might not be prime. so will ahve to repeat

# O(p**(1/2))
# comparison to trails = O(n**0.5),O(p**0.5) <= O(n**1/4) as p can be at largest n**0.5

import math
#import sympy
#import random
import rsa 
import timeit


# USING SYMPY MULTIPLIES TIMES BY 100 WTF!!
# def f(x,n):
#     return sympy.Mod(sympy.Pow(x,2)+1, n)

# def pollards_rho(n):
#     def trial(f):
#         r = t = 2
#         while True:
#             r = f(f(r))
#             t = f(t)
#             gcd = sympy.gcd(t-r, n)
#             if gcd == n:
#                 return False
#             elif gcd > 1: 
#                 return gcd
#     c = 1
#     while True:
#         def f(x):
#             return sympy.Mod(sympy.Pow(x,2)+c, n)
#         d = trial(f)
#         if d:
#             return d
#         c+=1

def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n%2 == 0:
        return 0                                                 # every even number doesnt have to be tested if 2 isnt a factor
    for p in range(3,int(math.sqrt(n))+1,2):
        if n%p == 0:
            return 0
    return 1

def gcd(y,x):  # math.gcd is much much quicker.
    # x > y 
    holder = 0
    while (y != 0):
        holder = y
        y = x%y
        x = holder
    return holder
def factorize(n):
    # print(f"N = {n}")
    #sqrt_n = int(math.sqrt(n))+1
    sqrt_n = n
    def trial(f):
        r = t = 2
        while True:
            r = f(f(r))
            t = f(t)
            gcd_num = math.gcd(abs(r-t), n)
            if gcd_num == n:
                return False
            elif gcd_num > 1: 
                return gcd_num
    c = 1
    while True:
        def f(x):
            return ((x**2)+c) % sqrt_n
        p = trial(f)
        if p:
            # q = int(n/p)
            # print(f"p = {p}, q = {q}, p*q is N = {p*q == n}")
            return p
        c+=1
        

if __name__ == "__main__":
    print("POLLARDS RHO IN PYTHON")
    n_bits = 55
    num_of_runs = 100
    print(f"num of runs per alg = {num_of_runs}, num of bits in n = {n_bits}")
    def test():
        p,q = rsa.prime.getprime(n_bits // 2), rsa.prime.getprime(n_bits // 2)
        n = p*q
        # print(n)
        x = factorize(n)
        y = int(n/x)
        # print(f"n = {n}\np = {p}, prime = {is_prime(p)}\nq = {q}, prime = {is_prime(q)}")
        # if x*y == n:
        #     print("p*q does equal n")
    time_time = timeit.Timer(test).timeit(number=num_of_runs)
    print(f"Average time is {round(time_time/num_of_runs,4)}s")

