import math
##### START PROBLEM 6 #####

# The sum of the squares of the first ten natural numbers is, 385
#
# The square of the sum of the first ten natural numbers is, 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
n=100

sum_of_squares = sum(list(map(lambda i:i*i ,[i for i in range(n+1)])))


square_of_sum = sum([i for i in range(n+1)])**2

diff = square_of_sum - sum_of_squares
print(diff)

##### END PROBLEM 6 #####


#### Learn about MAP, enumerate and lambda

##### START PROBLEM 7 #####

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?

#First check if prime
import math
from time import perf_counter


start = perf_counter()

def is_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

#prime = is_prime(5)
#print(prime)

# Return Nth Prime
def n_prime(n):
    num_prime = 0
    p = 1

    while num_prime < n:
        p +=1
        if is_prime(p):
            num_prime +=1
        #print(num_prime)
    print ("\nThe {0} prime number is: {1}".format(n, p))
    #return p

n_prime(10001)
print("Time:", "{:.8f}".format(perf_counter() - start))



##### END PROBLEM 7 #####

##### START PROBLEM 8 #####

#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
from time import perf_counter


start = perf_counter()

n = n.strip("\n")
greatest_product = 0
for i in range(len(n)):
    product=1
    substr = n[i:i+13]
    for digit in substr:
        product *= int(digit)
    if greatest_product < product:
        greatest_product = product
print("Time:", "{:.8f}".format(perf_counter() - start))
print("\nGreatest product of the 13 adjacent digits: {0}".format(greatest_product))



##### END PROBLEM 8 #####

##### START PROBLEM 9 #####

### SOLUTION COURTSEY GOOGLE

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def is_pythagorean_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

for a in range(1, 1000):
    for b in range(a, 1000 - a):
        c = 1000 - a - b
        if c < b:
            break
        if is_pythagorean_triplet(a, b, c):
            print(a, b, c)
            print("Product: {}".format(a * b * c))
            exit(0)



##### END PROBLEM 9 #####


##### START PROBLEM 10 #####

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


##### END PROBLEM 10 #####
