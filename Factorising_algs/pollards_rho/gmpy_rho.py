from gmpy2 import isqrt, gcd, is_prime
import timeit
import rsa

def factorize(n, seed=2, p=2, c=1):
        if is_prime(n):
            return n
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
        if n % 5 == 0:
            return 5
        f = lambda x: x ** p + c
        x, y, d = seed, seed, 1
        while d == 1:
            x = f(x) % n
            y = f(f(y)) % n
            d = gcd((x - y) % n, n)
            if n > d > 1:
                return d

# def factorize(n):
#     # print(f"N = {n}")
#     #sqrt_n = int(math.sqrt(n))+1
#     sqrt_n = n
#     def trial(f):
#         r = t = 2
#         while True:
#             r = f(f(r))
#             t = f(t)
#             gcd_num = gcd(abs(r-t), n)
#             if gcd_num == n:
#                 return False
#             elif gcd_num > 1: 
#                 return gcd_num
#     c = 1
#     while True:
#         def f(x):
#             return ((x**2)+c) % sqrt_n
#         p = trial(f)
#         if p:
#             # q = int(n/p)
#             # print(f"p = {p}, q = {q}, p*q is N = {p*q == n}")
#             return p
#         c+=1
        
if __name__ == "__main__":
    print("POLLARDS RHO IN PYTHON")
    n_bits = 55
    num_of_runs = 1000
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

