"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

 """

def fib(depth):
    #returns fib sequence as a list
    lst = []
    for number in xrange(depth):
        if number not in (1,0):
            lst.append( lst[-1] + lst[-2])
        else:
            lst.append(number) 
    return lst

#lets find for which depth fib sequence exceedes 4 mil
i = 1
while fib(i)[-1] < 4 * 10 **6:
    i += 1


#since the while loop incremented i one extra time lets remove one from it
i -= 1

#now we got depth, lets get the list and filter out the even values

lst = fib(i)
evenLst = [number for number in lst if number % 2 == 0]

#we have the list, lets print out the sum of it

print sum(evenLst)

