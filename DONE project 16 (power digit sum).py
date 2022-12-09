'''2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26
What is the sum of the digits of the number 2^1000? '''

a = pow(2, 1000)
b = list(str(a))

sum_var = 0
for item in b:
	c = int(item)
	sum_var += c 
print(sum_var)
	