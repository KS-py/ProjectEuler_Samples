import time

'''The sum of the squares of the first ten natural numbers is:
1**2 + 2**2 + 3**2 + 4**2 + 5**2 + ......... + 10**2 = 385
The square of the sum of the first ten natural numbers is:
  (1+2+3+.....+10)**2  = 55**2  = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
3025 - 385 = 2640
find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.'''

t0 = time.time()

def product_SOS_sum(end):
  sum_of = 0
  for i in range(end):
    sum_of += pow(i+1, 2)
  return sum_of

def product_sum_of_squared(end):
  sum_here = 0
  for i in range(end):
    sum_here += (i+1)
  return pow(sum_here, 2)

a = product_sum_of_squared(100) - product_SOS_sum(100)
print(f"The difference between the sum of squares and the SUM squared is ( {a} ) \n")
t1 = time.time()
print(f"The time used in running this code is {t1 - t0} seconds")

'''   !!!!!!!!!!!   DONE    !!!!!!!!!!!!!!!!!'''
