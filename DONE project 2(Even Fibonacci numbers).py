'''Each new term in the fibonacci sequence is generated by adding the previous two terms.
 By starting with 1 and 2, the first 10 terms will be:

1,2,3,5,8,13,21,34,55,89,............

By considering the terms in the fibonacci sequence whose values do not exceed four million,
 find the sum of the even valued terms'''

fib_list = [1,2]
even_fibs = []

i = 0
while True:
	num = fib_list[i] + fib_list[i+1]
	fib_list.append(num)
	i+=1
	if fib_list[len(fib_list) - 1] > 4000000:
		break

fib_list.pop()
print(fib_list)

for i in fib_list:
	if i%2 == 0:
		even_fibs.append(i)
print(even_fibs)

print("The sum of the even fibonacci's in the sequence is: \n")
print(sum(even_fibs))