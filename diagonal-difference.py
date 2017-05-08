#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

soma_princ = 0 
i = 0
while i < n:
    soma_princ = soma_princ + a[i][i]
    i = i + 1

soma_sec = 0
i = 0
j = n-1
while i < n:
    soma_sec = soma_sec + a[i][j]
    i = i + 1
    j = j - 1

diferenca = soma_princ - soma_sec
if diferenca < 0:
    diferenca = diferenca * -1

print(diferenca)
