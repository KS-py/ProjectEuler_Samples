'''
CHAMPERNOWNE'S CONSTANT

An irrational decimal fraction is created by concatenating the positive integers:
0.1234567891011121314151617181920212223.......

It can be seen that the 12th digit of the fractional part is 1
If Dn represents the nth digit of the fractional part, find the value of the following expression:
D1 x D10 x D100 x D1000 x D10000 x D100000 x D1000000
'''

a = []
b = "0."

for i in range(1000000):
	a.append(i+1)

for i in range(len(a) - 1):
	c = str(a[i])
	b += c 

frac_part = b[2:]
print(frac_part)

champernowne = int(frac_part[0]) * int(frac_part[9]) * int(frac_part[99]) * int(frac_part[99]) * int(frac_part[999]) * int(frac_part[9999]) * int(frac_part[99999]) * int(frac_part[999999])
print(champernowne)

