#!/usr/bin/python3

def disp():
    print('God is good')

def mul(x, function):
    for i in range(x):
        function()

mul(4, disp)
