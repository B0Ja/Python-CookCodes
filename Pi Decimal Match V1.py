# -*- coding: utf-8 -*-
"""
Created on Sun May 15 10:06:33 2016
@author: Brijesh J

Python 2.7.11

Checking for unique matches of number in the Pi decimals

Using the code snippet from [https://www.daniweb.com/programming/software-development/code/216718/approximation-of-pi-python]

The underlying Spigot algorithm is referenced from: http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf


"""

print "MATCH A NUMBER IN PI DECIMALS \n"
print "Enter an interesting number to match like Erdos number, Phone number.... anything! \n"

number = str(raw_input("Enter a number to match: "))

decimal = int(raw_input("\nEnter the number of decimals of Pi to check: ") or 100000)



#Check header comments
#Pi decimal denerators

def pi_generate():
    """generator to approximate pi"""
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3

    while True:
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = (10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x)
        else:
            q, r, t, k, m, x = (q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2)

digits = pi_generate()

# build a list of characters, the leading 3 and n decimals
pi_list = []

for i in range (decimal + 1):
    pi_list.append(str(digits.next()))
    #print pi_list      #Uncomment to see a nice pyramid building

# Joining the list into a string
pi_str = "".join(pi_list)

str1 = pi_str[1:]
len__ = len(str1)
pi_num = int(str1)

for digits in range(0,len__):
    
    if number in str1:        
        print "\nThe number has a match!"
        break
    else:
        print "\nIts a unique number!"
        break