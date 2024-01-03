import math
import sympy 
import random
import rsa 
import timeit

# factoring and and finding decrete log tied together
# check if prime with probability primality test (i always use nice n so not needed)
# b-smooth is a numbers largest prime factor

# let a be int, let L be int
# good L has to be found, that is devisiable by p-1 and not devisiable by q-1
# compute gcd(n, a**L - 1) , a**l == 1 mod p, so p divides a**l - 1
# this reveals factor, if factor not legitamite factor(1 or n), then change L
# 

def factorize(n):
    a = 2
    i = 2
    k = 2**(math.factorial(i))
    while True:
        gcd = math.gcd((a**k) - 1,n)
        if gcd != 1 and gcd != n:
            return gcd
        else:
            i += 1
            k = int(pow(k,i,n))

    
if __name__ == "__main__":
    bits = 15
    def test():
        p,q = rsa.prime.getprime(bits // 2), rsa.prime.getprime(bits // 2)
        n = p*q

        x = factorize(n)
        if x == p or x == q:
            print("correct")
    num_of_runs = 5
    time_time = timeit.Timer(test).timeit(number=num_of_runs)
    print(f"Average time of {round(time_time/num_of_runs,4)}s for {bits} bit N")


