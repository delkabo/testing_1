s = 1
l = []
fo = open("newfole.txt", 'a')
while True:
    z = input("Введите значение (для отмены введите q):")
    if z == 'q':
        break
    fo.write("Значение равно: " + str(z) + "\n")

fo.close()

fo = open("newfole.txt", 'r')
for item in fo:
    print(item, end="")
    l.append(item)

fo.close()

print(l)
print('элемент равен: ' + str(l[1]))

lst = ["11111 " + str(item * 2) for item in l]


def nfunc(x):
    x = str(x) + " 123 "
    return x


for item in lst:
    print(nfunc(item), end="")

for item in l:
    print(item, end="")

print("/////////////////")
dictnr = dict(potato='pot pot', tomato='tom tom')
print(dictnr['potato'], end="")
print("/////////////////")
dictnr.pop('potato')
print(dictnr)
