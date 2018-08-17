# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 12:47:44 2018

@author: tbowers


== ROUGH DRAFT HARDCODED SOLUTION ==
Works for problem #50 on Calculator Game for Android.
"""

def op1(num):
    return num * 3

def op2(num):
    return num - 9

def op3(num):
    return num * -1

def op4(num):
    return num // 10

def test_path(f, x):
    y = x
    for i in range(len(f)):
        y = o[f[i]](y)
    print(y)
    return y

m = 6
n = 4
o = [op1, op2, op3, op4]
g = 126
x = 111
y = None
p = []

current = [0, 0, 0, 0, 0, 0]

while current[0] < n:
    while current[1] < n:
        while current[2] < n:
            while current[3] < n:
                while current[4] < n:
                    while current[5] < n:
                        p.append(current.copy())
                        current[5] = current[5] + 1
                    current[4] = current[4] + 1
                    current[5] = 0
                current[3] = current[3] + 1
                current[4] = 0
                current[5] = 0
            current[2] = current[2] + 1
            current[3] = 0
            current[4] = 0
            current[5] = 0
        current[1] = current[1] + 1
        current[2] = 0
        current[3] = 0
        current[4] = 0
        current[5] = 0
    current[0] = current[0] + 1
    current[1] = 0
    current[2] = 0
    current[3] = 0
    current[4] = 0
    current[5] = 0

print(print(len(p), 'paths generated total'))

for i in range(len(p)):
    if test_path(p[i], x) == g:
        print(p[i], 'is the correct path')
        break
