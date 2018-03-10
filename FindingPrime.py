'''
Created on Mar 10, 2018

@author: Tenzin
'''

number=int(input("Enter a positive number greater than 0: "))

if number>1:
    for i in range(2,number):
        if (number%1)==0:
            print(number,"is not a prime number")
            print(i,"times",number/i,"is",number)
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")