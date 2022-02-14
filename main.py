#!/bin/python3
exp = 2
while True:
    exp += 1
    print ("Calculating", exp)
    for i in range (10 ** (exp - 2), 10 ** (exp + 1)):
        num = 0
        for j in str (i):
            num += int (j) ** exp
        if num == i:
            print (i, exp)
