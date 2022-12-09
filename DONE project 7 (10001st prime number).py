#completed
import math
import time
'''By listing the first six prime numbers: 2,3,5,7,11,13
We can see that the 6th prime number is 13
What is the 10001st prime number?'''

'''
The prime numbers obey the equation 6k +/- 1 apart from 2 and 3
hence we do the mod of the primes list then we append to the primes list
'''

def is_prime(num):
	if num <= 1:
		print("False")
		return False
	if num == 2:
		print("True")
		return True
	if num > 2 and num % 2 == 0:
		print("False")
		return False

	max_div = math.floor(math.sqrt(num))
	for i in range(3, max_div + 1):
		if num % i == 0:
			print("False")
			return False 
	print("True")
	return True

t0 = time.time()
c = 0 
for i in range(200000):
	x = is_prime(i)
	if x == True:
		c+= 1
		if c == 10001:
			print(f"The 10001st prime number is {i}")
			break

t1 = time.time()
print(f"The time used is {t1 - t0} \n")
print(c)
