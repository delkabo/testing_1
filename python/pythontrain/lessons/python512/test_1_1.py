""" a = 0
n = int(input())
while(n is not None):
    a = a + n
    try:
        n = int(input())
    except ValueError:
        n = None

print(a) """

a = 0
n = int(input("Enter the how much sum: "))
for item in range(n):
    try:
        item = int(input("Enter the number: "))
    except ValueError:
        item = None
    print("now a equal is " + str(a))
    a = a + item

print(a)
