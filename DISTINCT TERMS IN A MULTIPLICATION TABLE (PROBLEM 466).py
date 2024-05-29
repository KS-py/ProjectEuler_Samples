'''
Let P(m,n) be the number of distinct terms in an multiplication table

eg. a 3 x 4  table can looks like this

x 1 2 3 4
1 1 2 3 4
2 2 4 6 8
3 3 6 9 12

There are 8 distinct terms {1,2,3,4,6,8,9,12} therefore P(3,4) = 8

You are given P(64, 64) = 1263
P(12, 345) = 1998
P(32, 10^15) = 13826382602124302

Find P(64, 10^16)
'''

import time

#unoptimized

def distinct_terms(n, m):
    answers = []
    for i in range(1, n+1):
        for j in range(1, m+1):                  
            ans = i * j
            answers.append(ans)
            #print(ans)
            
    answers = set(answers)
    print()
    print(len(answers))

nm = pow(10, 15)
time1 = time.time()
distinct_terms(32,nm)
time2 = time.time()

time_taken = time2 - time1
print()
print(f"{time_taken} seconds")



def opt_distinct_terms(n, m):
    answers = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i != j:                    
                ans = i * j
                answers.append(ans)
                #print(ans)
            else:
                continue

    if n < m:
        num = n
    else:
        num = m

    numlist = [pow(n,2) for n in range(1,num+1)]
    print(numlist)
    print(answers)
    answers.extend(numlist)
    print(len(set(answers)))

nm = pow(10, 15)
time1 = time.time()
opt_distinct_terms(32,nm)
time2 = time.time()

time_taken = time2 - time1
print()
print(f"{time_taken} seconds")    

