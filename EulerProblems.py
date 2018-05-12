# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:28:19 2018
https://projecteuler.net/problem=166
@author: skoryakin
"""

print(
"""
=========================================
1/50 Euler 1 - Multiples of 3 and 5
=========================================
""")
# imports
import numpy as np
#solution
threes = np.sum(range(0,1000,3))
fives = np.sum(range(0,1000,5))
fifteens = np.sum(range(0,1000,15))
threesORfives = threes + fives - fifteens
print("The sum of all the multiples of 3 or 5 below 1000 is ",threesORfives,".")

print(
"""\n
=========================================
2/50 Euler 3 - Largest prime factor
=========================================
""")
# imports
from sympy.ntheory.generate import primerange
from sympy.ntheory.primetest import isprime
def primeslist(a,b):
    primes = list(primerange(a,b))
    return primes
from math import *
def LargestPrimeFactor(n="NAN"):
    if n == "NAN":
        n = int(input("LargestPrimeFactor(n), n = "))
    num = str(n)
    rng = int(np.sqrt(n))
    primes = np.array(primeslist(1,rng))
    val = n
    while isprime(val) == False:
        vals = np.linspace(val,val,len(primes))
        print(vals)
        divs = vals/primes
        print(divs)
        counter = 0
        for i in range(len(primes)):
            if int(divs[i])==divs[i]:
                print(divs[i]," for ",primes[i])
                val = divs[i]
                print(val)
                if val == 1:
                    LPF = primes[i]
                    print("The largest prime factor of ",num," is ",LPF)
                    return LPF
                else:
                    break
            else:
                counter += 1
                if counter == len(primes):
                    print("loop encountered")
                    LPF = val
                    print("The largest prime factor of ",num," is ",LPF)
                    return LPF
LargestPrimeFactor()
print("\nCheck test cases...")
LargestPrimeFactor(600851475143)

print(
"""\n
======================================
3/50 Euler 5 - Smallest multiple
======================================
""")
#i = 100000   # my first time. it took ages
i = 200000000 # now that i know the order of magnitude (having solved once), i use this to demonstrate usability without wasting time
while any([i%1 !=0, i%2 !=0, i%3 !=0, i%4 !=0, i%5 !=0, i%6 !=0, i%7 !=0, i%8 !=0, i%9 !=0, i%10 !=0, i%11 !=0, i%12 !=0, i%13 !=0, i%14 !=0, i%15 !=0, i%16 !=0, i%17 !=0, i%18 !=0, i%19 !=0, i%20 !=0]):
    i += 20
print(i)

print(
"""\n
=========================================
4/50 Euler 7 - 10001st prime number
=========================================
""")
from sympy.ntheory.generate import prime
p = prime(10001)
print(p)
"""
----------------------------------------
========================================
----------------------------------------
"""
import time
def sieve_alg(n = 10**6):
    tick = time.time()
    PrimesTo100 = set(range(2,100))
    twos = set(range(4,100,2))
    threes = set(range(6,100,3))
    fives = set(range(10,100,5))
    sevens = set(range(14,100,7))
    elevens = set(range(22,100,11))
    PrimesTo100 = list(PrimesTo100.difference(twos,threes,fives,sevens,elevens))
#    print(PrimesTo100)
    biglist = set()
    for i in PrimesTo100:
#        print(i)
        biglist=biglist.union(set(range(i*2,n,i)))
    num = set(range(2,n))
    primes = num.difference(biglist)
#    arr = np.arange(2 , n)
    tock = time.time()
    time_delta = float(tock - tick)
#    print(primes)
    print ("It took us exactly {} seconds to generate {} prime numbers ".format(time_delta,n))
    return(list(primes))
#print ( fin [ -1])
sieve_alg()

print(
"""\n
================================================
5/50 Euler 9 - Special Pythagorean triplet 
================================================
""")
for a in range(1,999):
    for b in range(a,999):
        c=1000-a-b
        if all([c>0,a**2+b**2==c**2]):
            print(a,b,c,a*b*c)
            break

#print(
#"""
#6/50 Euler 11 - Largest Product in a Grid
#** Needs matrix file from Euler saved as E_11_matrix.txt **
#""")
#import numpy as np
#
#arr = []
#varr = []
#rarr = np.zeros((20,20))
#
#with open('E_11_matrix.txt', 'r') as f:
#    for line in f:
#        arr.append(line)
#        split_line = line.split(' ')
#        #varr.append(split_line)
#        for values in split_line:
#                value_as_int = int(values)
#                varr.append(value_as_int)
#
#for kk in range(0,20):
#    rarr[kk] = varr[kk*20:(kk+1)*20]
#
#
##print(arr)
##print(varr)
##print(rarr)
##print(rarr[1,0])
#
#prods = []
#
#def sweep(num):
#    for jj in range(0,20):
#        for kk in range(0,17):
#            prod = rarr[jj,kk]*rarr[jj,kk+1]*rarr[jj,kk+2]*rarr[jj,kk+3]
#            prods.append(prod)
##            #print(prod)
#    for jj in range(0,20):
#        for kk in range(0,17):
#            prod = rarr[kk,jj]*rarr[kk+1,jj]*rarr[kk+2,jj]*rarr[kk+3,jj]
#            prods.append(prod)
##            #print(prod)
#    for jj in range(0,17):
#        for kk in range(0,17):
#            prod = rarr[kk,jj]*rarr[kk+1,jj+1]*rarr[kk+2,jj+2]*rarr[kk+3,jj+3]
#            prods.append(prod)
##            #print(prod)
#    for jj in range(0,17):
#        for kk in range(0,17):
#            prod = rarr[kk+3,jj]*rarr[kk+2,jj+1]*rarr[kk+1,jj+2]*rarr[kk,jj+3]
#            prods.append(prod)
#            #print(prods)
##    print(prods)
#    print('//')
#    print(max(prods))
#
#sweep(4)
##print(prods)
##print(len(prods))

print(
"""
7/50 Euler 16 - Power Digit Sum
""")

def int_sum(var):
    sep = [int(i) for i in str(var)]
    #print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)

int_sum(2**1000)

print('//')

print(
"""
8/50 Euler 20 - Factorial Int Sum
""")

def factorial(num):
    nxt = num - 1
    fact = num
    while nxt > 1:
        fact = fact*nxt
        nxt += -1
    return(fact)


def int_sum(var):
    sep = [int(i) for i in str(var)]
    #print(sep)
    sumnum = 0
    for kk in range(0,len(sep)):
        sumnum += sep[kk]
    print(sumnum)


int_sum(factorial(100))

print('//')

print(
"""
9/50 Euler 25 - 1000 Digit Fibonacci Number
""")

def fib_len(num):
    a,b = 1,0
    for kk in range(1,num**2):
        b = a + b
        a = b - a
        #print(kk,b)
        sep = [int(i) for i in str(b)]
        if len(sep) >= num:
            break
    #print(b)
    return(kk)


print(fib_len(1000))

print('//')

print(
"""
================================================
10/50 Euler Problem 26 : Reciprocal cycles
================================================
""")
from sympy import sieve
def f(N):
    #since this algorithm breaks for N<8, the following is included
    if N < 8:
        return 3
    # the for loop below takes a list of primes up to N, sorts from largest to
    # smallest, and iterates through this list.
    #   - it makes sense that higher numbers will have higher reciprocal cycles
    #   - in the loop, we look for a 
    for number in list(sieve.primerange(1,N))[::-1]:
        print(number)
        digits = 1
        powerof10 = 10
        while powerof10 % number != 1:
            digits += 1
            powerof10 *= 10
#        print(digits,powerof10)
        if number-1 == digits:
            return number
N = 1000
print("d=", f(N))

print(
"""
================================================
11/50 Euler Problem 27 :Quadratic primes
================================================
""")
import numpy as np
from sympy import isprime

def f(n,a=1,b=41):
    return n**2 + a*n + b
foo = f(0)
bar = f(39)
foobar = np.array([])
for i in range(40):
    foobar = np.append(foobar,f(i))
#print(foo,bar,foobar)
def N(a,b):
    primes = []
    for n in range(max(abs(a),abs(b))):
        num = f(n,a,b)
#        print(num)
        if isprime(num):
            primes.append(num)
        else:
            break
    nprimes = len(primes)
    return(nprimes)

best = 40
bestvals = []
for a in range(-1000,1001):
    for b in range(2,1001):
        nprimes = N(a,b)
        if nprimes > best:
            best = nprimes
            bestvals=[a,b]
prod = np.prod(bestvals)
print("a,b=",bestvals,"\na*b=",prod)


print(
"""
================================================
12/50 Euler Problem 28: Number spiral diagonals
================================================
""")
import numpy as np
n = 1001
squares = np.square(list(range(1,n+1,2)),dtype="float")[::-1][:-1]
diagvals = []    
for i in squares:
    diagvals.append(i)
    for n in range(1,4):
#        print(n)
        diagvals.append(i-n*np.sqrt(i)+n)
diagvals.append(1.0)
diagsum = np.sum(diagvals)
print(diagsum)


print(
"""
================================================
13/50 Euler Problem 30 : Digit fifth powers
================================================
""")
import numpy as np
def digitextract(num="NAN"):
    if num == "NAN":
        num = input("Enter a number: ")
    loop = True
    while loop:
        try:
            num = int(float(num))
            loop = False
        except(ValueError):
            print("\nYou have not entered a number.")
            num = input("Enter a number: ")
    digits = [num%10]
    digit = int(num/10)
    while digit != 0:
        digits.append(digit%10)
        digit = int(digit/10)
    digits = np.array(digits[::-1])
    return digits

def numcheck(num="NAN"):
    digits = digitextract(num)
    digisum = sum(digits**5)
    if digisum == num:
        print("This one works: ",num)
        return num
    else:
        return 0

numbers = []
for i in range(10,999999):
    number = numcheck(i)
    if number != 0:
        numbers.append(number)
print("All of these numbers work: ",numbers)
print("The sum of these numbers is: ",sum(numbers))

print(
"""
================================================
14/50 Euler Problem 32: Pandigital products
================================================
""")
numstrings = []
nums=[]
for num in range(1000,100000):
    for i in range(1,1000):
        if (num/i)%1==0:
            numstrings.append(str(int(num/i))+str(i)+str(num))
            nums.append(num)
pandigits = []
for numstring in numstrings:
    if len(numstring)==9:
        digits = digitextract(numstring)
        digitset = set(digits)
#        print(digits)
        if digitset == {1,2,3,4,5,6,7,8,9}:
            print("foobar@!@!@!@!!!")
            print(digits)
            pandigits.append(digits)
shortstrings= []
for i in pandigits:
    shortstrings.append(i[5:])
specialnums=[]
for i in shortstrings:
    specialnum = ""
    for n in i:
        specialnum+=str(n)
    specialnums.append(int(specialnum))
specialnums = list(set(specialnums))
print(specialnums)
print(sum(specialnums))

print(
"""
===========================================
15/50 Euler 36 - Double-Base Palindromes
===========================================
""")
def BaseConvert(n):
    b2 = []
    while n >= 1:
        b2.insert(0, 1 if n%2==1 else 0)
        n = n//2
    return b2
def palindrome1(n):
    thing = [int(i) for i in str(n)]
    if thing == thing[::-1]:
        return True
    else:
        return False
def palindrome2(n):
    thing_2 = BaseConvert(n)
    if thing_2 == thing_2[::-1]:
        return True
    else:
        return False
def findPalindromes(n):
    if type(n) == float or int:
        arr = []
        num = 0
        for kk in range(0, n):
            if palindrome1(kk) and palindrome2(kk) == True:
                arr.append(palindrome2(kk))
                num += kk
        return(num)


print(findPalindromes(1000000))

print(
"""
=========================================
16/50 Euler 39 - Integer Right Triangles
=========================================
""")
upperlim = 1000
t_max, p_max = 0, 0  #L must be an even integer

for p in range(0, upperlim+1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_max: t_max, p_max = t, p
 
print("max perimeter under ",upperlim,"is", p_max)
print(t_max, " triangles in set")

print(
"""
=========================================
17/50 Euler 2 - Even Fibonacci Numbers
=========================================
""")
def fibs(x):
    foobar = [1, 1]
    while True:
        val = foobar[-1] + foobar[-2]
        if val > x:
            break
        foobar.append(val)
    return foobar

fibseq = fibs(4000000)
evenfibs = [fibseq[x] for x in range(2, len(fibseq), 3)]
print(sum(evenfibs))

print(
"""
==========================================
18/50 Euler 4 - Largest Palindrome Product
==========================================
""")
n = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 n = a * b
print(n)


print(
"""
==============================
19/50 Euler 10 - Sum of Primes
==============================
""")
sieve = [True] * 2000000 # Sieve is faster for 2M primes
def mark(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

for x in range(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]: mark(sieve, x)

print(sum(i for i in range(2, len(sieve)) if sieve[i]))



print(
"""
==========================================
21/50 Euler 6 - Sum Square Difference
==========================================
""")
import numpy as np
def squaresumdifference(n):
    return sum([i for i in range(n+1)])**2-sum([i**2 for i in range(n+1)])
diff = squaresumdifference(100)
print(diff)


print(
"""
==========================================
22/50 Euler 4 - Largest palindrome product
==========================================
""")
def LargestPalindromeProduct(min=100,max=999):
    biggest = 0
    for a in range(min,max + 1):
        for b in range(a + 1, max + 1): # avoid duplicates
            prod = a*b
            if prod > biggest and str(prod)==(str(prod)[::-1]):
                biggest = prod
    return biggest
L = LargestPalindromeProduct()
print(L)


print(
"""
===========================================
23/50 Euler 8 - Largest product in a series
===========================================
""")
s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
biggest = 0
for i in range(0, len(s) - 13):
    prod = 1
    for j in range(i, i + 13):
        prod *= int(s[j: j + 1])
    if prod > biggest:
        biggest = prod
print (biggest)

print(
"""
==============================
24/50 Euler 10 - Sum of Primes
==============================
""")

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum
primesum = prime_sum(2000000)
print(primesum)

print(
"""
==========================================
25/50 Euler 11 - Largest product in a grid
==========================================
""")

L = []
L.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
L.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
L.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
L.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
L.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
L.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
L.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
L.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
L.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
L.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
L.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
L.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
L.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
L.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
L.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
L.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
L.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
L.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
L.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
L.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
 
M = [i.split() for i in L]
M = [[int(j) for j in i] for i in M]
 
# there are 20 rows, each containing 20 integers
max_prod = 0
 
for i in range(20):
    for j in range(16):
        # right/left products
        prod = M[i][j]*M[i][j+1]*M[i][j+2]*M[i][j+3]
        if prod > max_prod: max_prod = prod
        # up/down products
        prod = M[j][i]*M[j+1][i]*M[j+2][i]*M[j+3][i]
        if prod > max_prod: max_prod = prod
 
# diagonal products
for i in range(16):
    for j in range(16):
        prod = M[i][j]*M[i+1][j+1]*M[i+2][j+2]*M[i+3][j+3]
        if prod > max_prod: max_prod = prod
for i in range(3,20):
    for j in range(16):
        prod = M[i][j]*M[i-1][j+1]*M[i-2][j+2]*M[i-3][j+3]
        if prod > max_prod: max_prod = prod

print(max_prod)

print(
"""
===================================================
26/50 Euler 12 - Highly divisible triangular number
===================================================
""")
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2
print(triangle)

print(
"""
==========================================
27/50 Euler 14 - Longest Collatz sequence
==========================================
""")
limit = 1000000
collatz_length = [0] * limit
collatz_length[1] = 1
max_length = [1,1]
 
for i in range(1,1000000):
    n,s = int(i),0
    TO_ADD = [] # collatz_length not yet known
    while n > limit - 1 or collatz_length[n] < 1:
        TO_ADD.append(n)
        if n % 2 == 0: n = int(n/2)
        else: n = int(3*n + 1)
        s += 1
    # collatz_length now known from previous calculations
    p = collatz_length[n]
    for j in range(s):
        m = TO_ADD[j]
        if m < limit:
            new_length = collatz_length[n] + s - j
            collatz_length[m] = new_length
            if new_length > max_length[1]: max_length = [i,new_length]
print(max_length)

print(
"""
==========================================
28/50 Euler 15 - Lattice paths
==========================================
""")
def nRoutes(size):
    L = [1] * size
    for i in range(size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[size - 1]
n = nRoutes(20)
print(n)


print(
"""
==========================================
29/50 Euler 16 - Power digit sum
==========================================
""")
def pow2sum(exp):
    bignumber = list(str(2**1000))
    return sum([int(i) for i in bignumber])
n = pow2sum(1000)
print(n)


print(
"""
==========================================
30/50 Euler 20 - Digital Factorial Sum
==========================================
""")

def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
def digitsum(n):
    return sum([int(i) for i in str(n)])
result = digitsum(factorial(100))
print(result)


print(
"""
==========================================
31/50 Euler 21 - Amicable Numbers
==========================================
""")

def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s
def amicable_pairs_xrange(low,high):
    L = [sum_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs]) 
ans = sum_pairs(amicable_pairs_xrange(1,10000))
print(ans)



print(
"""
#==========================================
#32/50 Euler 18 - Maximum Path Sum
#==========================================
#""")
#def recSumAtRow(rowData, rowNum):
#    for i in range(len(rowData[rowNum])):
#        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
#    if len(rowData[rowNum])==1: return rowData[rowNum][0]
#    else: return recSumAtRow(rowData, rowNum-1)
#rows = []
#with open('problem-18-data') as f:
#    for line in f:
#        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
#result = recSumAtRow(rows, len(rows)-2)

print(
"""
==========================================
33/50 Euler 17 - Number Letter Counts
==========================================
""")
S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
D = [0,3,6,6,5,5,5,7,6,6]
H = 7
T = 8
 
total = 0
for i in range(1,1000):
    c = i % 10 # singles digit
    b = ((i % 100) - c) / 10 # tens digit
    a = ((i % 1000) - (b * 10) - c) / 100 # hundreds digit
 
    if a != 0:
        total += S[a] + H # "S[a] hundred
        if b != 0 or c != 0: total += 3 # "and"
    if b == 0 or b == 1: total += S[int(b * 10 + c)]
    else: total += D[b] + S[c]
total += S[1] + T

 

print(
"""
==========================================
34/50 Euler 34 - Digit Factorial Sum
==========================================
""")
def factorial(n):
    if n == 0: return 1
    else: return n * factorial(n - 1)
def findFactorialSum():
    factorials = [factorial(x) for x in range(0, 10)] # pre-calculate products
    total_sum = 0
    for k in range(10, factorial(9) * 7): # 9999999 is way more than its fact-sum
        tmp = k
        total = 0
        while tmp > 0:
            total += factorials[tmp % 10]
            tmp //= 10
        if total == k:
            total_sum += k
    return total_sum
print(findFactorialSum())


print(
"""
==========================================
35/50 Euler 35 - Circular Primes
==========================================
""")
def getPrimesBelowN(n=1000000):
    """ Sieve of Eratosthenes """
    from math import ceil
    roundUp = lambda n, prime: int(ceil(float(n) / prime))

    primes = [True] * n
    primes[0] = False
    primes[1] = False
    primeList = []

    for currentPrime in range(2, n):
        if not primes[currentPrime]:
            continue
        primeList.append(currentPrime)
        for multiplicant in range(2, roundUp(n, currentPrime)):
            primes[multiplicant * currentPrime] = False
    return primeList
primes = getPrimesBelowN()
def isCircularPrime(primes, number):
    number = str(number)
    for i in range(0, len(number)):
        rotatedNumber = number[i:len(number)] + number[0:i]
        if not primes[int(rotatedNumber)]:
            return False
    return True

print(
"""
===========================================
36/50 Euler 33 - Digit cancelling fractions
===========================================
""")
import fractions
p = fractions.Fraction(1,1)
for a in range(10, 100, 1):
    for b in range(a+1, 100, 1):
        if b % 10 == 0 or a == b: continue
        La, Lb = [a/10, a%10], [b/10, b%10]
        if any(i in Lb for i in La) and not all(i in Lb for i in La):
            if La[0] in Lb: x = La[0]
            else: x = La[1]
            La.remove(x)
            Lb.remove(x)
            if a*Lb[0] == b*La[0]: p *= fractions.Fraction(int(La[0]),int(Lb[0]))
print(p)



print(
"""
===========================================
37/50 Euler 37 - Truncatable primes
===========================================
""")
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n 
    # for all odd numbers
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True
 
def peel_left(i):
    """Remove digits left to right,
    then check for prime number"""
    x = list(str(i))
    for n in range(1, len(x)):
        y = x[n:]
        s = int(''.join(y))
        if isprime(s):
            continue
        else:
            return "False"
    return "True"
 
def peel_right(i):
    """"Remove digits right to left,
    then check for prime number"""
    x = list(str(i))
    for n in range(1, len(x)):
        y = x[:(-n)]
        s = int(''.join(y))
        if isprime(s):
            continue
        else:
            return "False"
    return "True"
L = []
for i in range(10, 1000000):
    if isprime(i):
        if (peel_left(i) == "True") and (peel_right(i) == "True"):
            L.append(i)
        else:
            continue
    else:
        continue
print("L = ", L)
print("Answer = ", sum(L))


 

print(
"""
=================================
38/50 Euler 29 - Distinct powers
=================================
""")
limit = 101 
for a in range(2,limit):
    for b in range(2,limit):
        c = a**b
        if c in L: pass
        # else: L.append(c) # old list version
        L.add(c) # new version with set
print(len(L))


print(
"""
=================================
39/50 Euler 31 - Coin sums
=================================
""")
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print(ways[target])



print(
"""
========================================
40/50 Euler 40 - Champernowne's constant
========================================
""")
x = ''
for n in range(1000000):
    x = x + str(n)
    if len(x) > 1000000:
        break
    else:
        continue
soln = int(x[1]) * int(x[10]) * int(x[100]) \
         * int(x[1000]) * int(x[10000]) * \
         int(x[100000]) * int(x[1000000])
print(soln)


print(
"""
========================================
41/50 Euler 38 - Pandigital multiples
========================================
""")
def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)
def pan():
    for n in range(9487, 9213, -1):
        p = str(n*1) + str(n*2)
        if is_pandigital(p): return p
    return "None found."
print(pan())



#print(
#"""
#========================================
#42/50 Euler 42 - Coded triangle numbers
#========================================
#""")
#with open('words.txt','r') as f:
#    words = f.read().split(',')
#    words = [list(word.strip('\"')) for word in words]
#    f.close()
#m = max([len(word) for word in words])
#triangles = [n*(n + 1)/2 for n in range(1,2*m)]
#vals = {}
#s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#for c in s:
#    vals[c] = s.index(c) + 1
#triangle_words = 0
#for word in words:
#    if sum([vals[c] for c in word]) in triangles:
#        triangle_words += 1
#print(triangle_words)

print(
"""
========================================
43/50 Euler 43 - Sub-string divisibility
========================================
""")
from itertools import permutations
primes = [17, 13, 11, 7, 5, 3, 2]
total = 0
for i in permutations('0123456789'):
  if i[0] == '0':
    continue 
  n = ''.join(list(i))
  valid = True
  for j in range(0, len(primes)):
    x = n[len(primes) - j:len(primes) - j + 3]
    if int(x) % primes[j]:
      valid = False
      break
  if valid:
    print('Valid number: %s' % n)
    total += int(n)
print('Total: %d' % total)



print(
"""
========================================
44/50 Euler 44 - Pentagon Numbers
========================================
""")
def pent():
    ps = set()
    i = 1000
    while True:
        i += 1
        s = (3*i*i - i) // 2
        for Pj in ps:
            if s-Pj in ps and s-2*Pj in ps: 
                return s-2*Pj
        ps.add(s)
print(pent())

print(
"""
=======================================================
45/50 Euler 45 - Triangular, pentagonal, and hexagonal
======================================================
""")
p = 165
h = 143
h = 84*p + 97*h - 38
print(h*(2*h - 1))


print(
"""
============================================
46/50 Euler 46 - Goldbach's Other Conjecture
============================================
""")
n = 5
f = 1
primes = set()
while True:
    if all(n % p for p in primes):
        primes.add(n)
    else:
        if not any((n-2*i*i) in primes for i in range(1, n)):
            break
    n += 3-f
    f = -f
print(n)



print(
"""
========================================
47/50 Euler 47
========================================
""")
def p44(L, nf, ns):
    L+= ns
    f = [0]*L
    c = 0
    for n in range(2, L):
        if f[n] == nf:
            c+= 1
            if c == ns:
                print(n-ns+1)
                c-= 1
        else:
            c = 0
            if f[n] == 0: f[n::n] = [x+1 for x in f[n::n]]
        return
p44(300000,4,4)

print(
"""
========================================
48/50 Euler 48
========================================
""")
total = 0
tally = ''
for i in range(1, 1001):
    total = total + (i ** i)
x = str(total)
y = len(x) - 10
s = x[y:]
print("Answer = ", s)

print(
"""
========================================
49/50 Euler 49
========================================
""")

from itertools import permutations
def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime
def create(b):
    for i in range(len(b)):
        for j in range(i+1, len(b)):
            difference = b[j] - b[i]
            if b[j] + difference in b:
                return str(b[i])+str(b[j])+str(b[j]+difference)
    return False
primes = sieve(10000)
primes = [x for x in primes if x > 1487]
for i in primes:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if len(a) >= 3:
        if create(a):
            print(create(a))
            break


print(
"""
========================================
50/50 Euler
========================================
""")

import gmpy
def isprime(n):
    """Return True of False - Prime number"""
    if gmpy.is_prime(n):
        return True
    else:
        return False
def prime_list():
    """Create prime number list below 1000000"""
    L = []
    for n in range(1, 1000000):
        if isprime(n):
            L.append(n)
    return L
def add_primes(primes, switch):
    """Return the last number in the list (largest prime),
    and the in-loop counter (consecutive numbers)"""
    counter = switch # start with this prime number
    in_counter = 0
    sum = 0
    L = []
    while sum < 1000000:
        sum = sum + primes[counter]
        if isprime(sum):
            L.append(sum)
        in_counter += 1 # in loop counter
        counter += 1
    if L[-1] < 1000000:
        return L[-1], in_counter
    elif L[-1] > 1000000:
        print("****")
        return L[-2], in_counter
primes = prime_list()
main_counter = 0
for switch in range(0, 20):
    x = add_primes(primes, switch)
    print(x[0], x[1])
    if x[0] > main_counter:
        main_counter = x[0]
print("Answer = ", main_counter)
