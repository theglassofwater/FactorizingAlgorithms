from math import sqrt
#import sympy
#import random
import rsa 
import timeit

# O(n**(1/2))

def is_prime(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n%2 == 0:
        return 0                                                 # every even number doesnt have to be tested if 2 isnt a factor
    for p in range(3,int(sqrt(n))+1,2):
        if n%p == 0:
            return 0
    return 1

# my implementation
def factorize(n):
    if n <= 1:
        return 0
    if n%2 == 0:
        return 2                                                  # every even number doesnt have to be tested if 2 isnt a factor
    for p in range(3,int(sqrt(n))+1,2):
        if n%p == 0 and is_prime(p):
            return p
    return 0

if __name__ == "__main__":
    print("TRAILS IN PYTHON")
    bits = 55
    num_of_runs = 1   
    print(f"num of runs per alg = {num_of_runs}, num of bits in n = {bits}")
    def test():
        p,q = rsa.prime.getprime(bits // 2), rsa.prime.getprime(bits // 2)
        n = p*q
        x = factorize(n)
        y = int(n/x)
        #print(f"n = {n}\np = {p}, prime = {is_prime(p)}\nq = {q}, prime = {is_prime(q)}")
        if x*y == n:
            print("p*q does equal n")

    time_time = timeit.Timer(test).timeit(number=num_of_runs)
    print(f"Average time of {round(time_time/num_of_runs,4)}s for {bits} bit N")
