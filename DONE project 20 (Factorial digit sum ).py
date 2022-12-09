'''
n! means n x (n-1) x .... x 3 x 2 x 1
For example, 10! = 10 x 9 x ....x 3 x 2 x 1 = 3628800
and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27
Find the sum of the digits in the number 100!
'''

def factorial(num):
	x = 0
	if num == 1:
		return 1
	if num == 2:
		return 2
	else:
		x = num * factorial(num - 1)
	return x 

hundred_fact = factorial(100)
hun = str(hundred_fact)

sum_of_nums = 0
for i in range(len(hun)):
	sum_of_nums += int(hun[i])

print(sum_of_nums)

# ======= DONE =======