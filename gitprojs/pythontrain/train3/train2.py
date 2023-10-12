from re import L
from tkinter import *

def dosomething(a, b):
    return a + b

# val = dosomething()
print(dosomething(1, 2))

inp = input("введите число: ")
print(inp)

l = ['s', 'p', 'i', 's', 'o', 'k']
print(l)

slovo = ''

for item in l:
    slovo = slovo + item

print(slovo)

g = []

for item in slovo:
    if item == 'o':
        continue
    g.append(item*2)

print(g)

class A:
    def b(self):
        return 'hello world'

a = A()

print(a.b())
