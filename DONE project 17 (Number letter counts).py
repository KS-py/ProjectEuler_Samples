'''
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3+3+5+4+4 = 19 letters used in total 

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?

Note: DO not count spaces or hyphens. For example, 342 (three hundred and forty two) contains 23 letters and 115(one hundred and fifteen)
 contains 20 letters. The use of "and " when writing out in numbers is in compliance with British usage. '''

names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty','thirty','forty', 'fifty',
'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']

off_names = names[:-2]   #the list of the numbers including the tens ie. twenty, thirty, forty, fifty to ninety

for i in range(8):
	for e in names[:9]:
		a = names[19+i] + e       #21 TO 99 (excluding the 10s)
		off_names.append(str(a))

for i in names[:9]:     
	a = i + names[-2]      #The whole hundreds (100, 200, to 900)
	off_names.append(a)

for elem in off_names[:9]:
	a = elem + names[-2]
	for e in off_names[:99]:     #101 to 999 (excluding the 100s)
		b = a + 'and' + e
		off_names.append(b)
off_names.append('one' + names[-1])
print(off_names)
print(len(off_names))

num_of_letters = 0
for element in off_names:
	num_of_letters += len(element)

print(f"The total number of letters in 1 to 1000 are {num_of_letters}")

