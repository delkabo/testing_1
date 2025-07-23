def func1(a, b):
    return a + b


print(str(func1(1, 2)) + "\n")


def func2(*args):
    return args


print(str(func2(1, )) + "\n")


def func3(**kwargs):
    return kwargs


print(func3(a=1, b=2, c=3))
print("\n")
print(func3())
print("\n")
print(func3(a='python'))
print("\n")
funclamb = lambda x, y: x + y
print(funclamb(1, 2))

print("\n exceptions \n")
try:
    k = 1 / 0
except ZeroDivisionError:
    k = 0
print(k)

print("\nexceptions 2\n")
f = open('1.txt')
ints = []

try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('Это не число. Выходим.')
except Exception:
    print("Что это еще такое?")
else:
    print('Все хорошо.')
finally:
    f.close()
    print(ints)
    print("Я зкрыл файл.")

print('\n')
fl = open('1.txt', 'r')
print(fl.read())
print('\n')
print("fl.read(1): " + str(fl.read(2)))
print('\n')
for line in fl:
    print(line)
fl.close()

print('\n')
fl = open('1.txt', 'r')

print("\nЗапись в файл\n")
lnum = [str(i)+str(i-1) for i in range(20)]
print(lnum)

f = open('1.txt', 'w')
for index in lnum:
    f.write(index + '\n')

f.close()
print('\n')

f = open('1.txt', 'r')
for index in f:
    print(index, end='')

print("\nЗапись в файл\n")
with open('1.txt', 'a', encoding='utf-8') as g:
    d = int(input())
    print('1/{} = {}'.format(d, 1 / d), file=g)
