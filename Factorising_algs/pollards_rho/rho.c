#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
//#include <stddef.h>
#include <stdint.h>
//#include <sha.h>
// use extended euclidean algorithm for GCD
// then figure our how to replicate the python code 

unsigned long long factorize(unsigned long long n);
unsigned long long trying(unsigned long long n, int c);
unsigned long long formula(unsigned long long n, unsigned long long x, int c);
unsigned long long gcd(unsigned long long x, unsigned long long y);
unsigned long long extendedGCD(unsigned long long a, unsigned long long b, unsigned long long *x, unsigned long long *y);
unsigned long long b_gcd(unsigned long long num1, unsigned long long num2);
bool is_prime(unsigned long long n);

//uint64_t myVar; // i dont think i will need this at all tbh 

void main(){
	printf("POLLARDS RHO IN C\n");
    unsigned long long p,q,n,x,y;
    clock_t begin = clock();


    p = 112333409;
    q = 101075699;
    n = p*q;
    //n = 6216194779103943559; // differnet n to p*q
    x = factorize(n);
    y = n/x;
    printf("n = %lld\np = %lld, prime = %d\nq = %lld, prime = %d\n", n, x, is_prime(x), y, is_prime(y));
    if (x*y == n){
        printf("p*q does equal n\n");
    }

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("time taken = %.3f", time_spent);
}

unsigned long long factorize2(unsigned long long n){
    unsigned long long r,t,d,x,y;
    int c = 1;
    r = 2;
    t = 2;
    while (d == 1){
        t = formula(n,t,c);
        r = formula(n,formula(n,r,c),c);
        d = gcd((x-y)%n, n);
        if (n > d > 1){
            return d;
        }
    }
}


unsigned long long factorize(unsigned long long n){
    unsigned long long r,t,p;
    int c = 1;
	while (true){
		p = trying(n,c);
		if (p){
			return p;
		}
		c++;
	}
	



}

unsigned long long trying(unsigned long long n, int c){
    unsigned long long r,t,gcd_num,x,y;
    r = 2;
    t = 2;
    while (true){
        r = formula(n, formula(n,r,c),c);
        t = formula(n,t,c);
		
        gcd_num = b_gcd(t-r,n); // this one is quicker 
		//gcd_num = extendedGCD(t-r,n,&x,&y);
		if (gcd_num == n){
			return 0;
		}
		if (gcd_num > 1){
			return gcd_num;
		}
	
    }

}

unsigned long long formula(unsigned long long n, unsigned long long x, int c){
    unsigned long long power;
    power = pow(x,2);
    return (power+c) % n;
}

unsigned long long gcd(unsigned long long y, unsigned long long x){ //  always x > y 
	// x = 888, y = 54 
	unsigned long long holder; // this is the last x value 
	while (y != 0){
		holder = y;
		y = x%y;
		x = holder;
	}
	return holder;
}
unsigned long long extendedGCD(unsigned long long a, unsigned long long b, unsigned long long *x, unsigned long long *y) {
    // Base case
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }

    // Recursive call
    unsigned long long x1, y1;
    unsigned long long gcd = extendedGCD(b, a % b, &x1, &y1);

    // Update x and y using results of recursive call
    *x = y1;
    *y = x1 - (a / b) * y1;

    return gcd;
}

unsigned long long b_gcd(unsigned long long num1, unsigned long long num2)
{
	unsigned long long pof2, tmp;
	if (!num1 || !num2) {
		return (num1 | num2);
	}

	// pof2 is the greatest power of 2 deviding both numbers .
	// We will use pof2 to multiply the returning number .
	pof2 = 0;
	while(!(num1 & 1) && !(num2 & 1)) {
		// gcd(even1, even1) = pof2 * gcd(even1/pof2, even2/pof2)
		num1 >>=1;
		num2 >>=1;
		pof2++;
	}

	do {
		while (!(num1 & 1)) {
			num1 >>=1;
		}
		while (!(num2 & 1)) {
			num2 >>=1;
		}
		// At this point we know for sure that
		// num1 and num2 are odd
		if (num1 >= num2) {
			num1 = (num1 - num2) >> 1;
		}
		else {
			tmp = num1;
			num1 = (num2 - num1) >> 1;
			num2 = tmp;
		}
	} while (!(num1 == num2 || num1 == 0));

	return (num2 << pof2);
}

bool is_prime(unsigned long long n){
    if (n <= 1){
        return false;
    }
    if (n == 2){
        return true;
    }
    int usable_root_n = sqrt(n)+1;
    if (n%2 == 0){
        return false;
    }
    for (int p=3; p < usable_root_n; p = p+2){
        if (n%p == 0){
            return false;
        }
    }
    return true;
}