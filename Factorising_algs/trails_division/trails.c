#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>
#include <stdint.h>

int is_prime(unsigned long long n);
unsigned long long factorize(unsigned long long n);

void main(){
	printf("TRAILS IN C\n");
    unsigned long long p,q,n,x,y;
    clock_t begin = clock();


	p = 68121853;
	q = 97023187;
    n = p*q;
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

int is_prime(unsigned long long n){
    if (n <= 1){
        return 0;
    }
    if (n == 2){
        return 1;
    }
    unsigned long long usable_root_n = sqrt(n)+1;
    if (n%2 == 0){
        return 0;
    }
    for (unsigned long long p=3; p < usable_root_n; p = p+2){
        if (n%p == 0){
            return 0;
        }
    }
    return 1;
}

unsigned long long factorize(unsigned long long n){ // this only factorizes if number found is prime!!
    if (n <= 2){
        return 0;
    }
    unsigned long long usable_root_n = sqrt(n)+1;
    if (n%2 == 0){
        return 2;
    }
    for (unsigned long long p=3; p < usable_root_n; p = p+2){
        if (n%p == 0 && is_prime(p)){
            return p;
        }
    }
    return 0;
}


