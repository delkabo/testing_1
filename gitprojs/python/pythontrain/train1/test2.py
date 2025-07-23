i = 5
while i < 15:
    print(i)
    i = i +2

for i in 'hellO world':
    print(i * 2, end="")
print('\n')

for i in 'hello world':
    if i == 'o':
        continue
    if i == 'd':
        break
    print(i * 2, end='')

print('\n')
print(3**2)
print('\n')
spam = 'spam'
# i = 0
# while i > -4:
#     print(spam[i] + " "+ str(i))
#     i = i -1
print('\n')
numb = 0
print(spam)
while numb < 4:

    print(spam[numb] + " " + str(numb))
    numb = numb + 1

# answer = input('2+2 = ')
# if str(answer) == '4':
#     print("right answer")
# else:
#     print("wrong answer")