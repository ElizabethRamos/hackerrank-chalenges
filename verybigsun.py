#!/bin/python

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


#loop com while
i = 0
soma = 0
while i < len(arr):
    soma = soma+arr[i]
    i = i+1
    
#loop com for
soma = 0
for numero in arr:
    soma = soma + numero

#soma usando sum
soma = sum(arr)
    
print (soma)    



