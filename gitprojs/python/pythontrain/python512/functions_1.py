a = []

def foo(arg1, arg2):
  a.append("foo")

foo(a.append("arg1"), a.append("arg2"))

print(a)


b = a.pop(0)
print("b = " + str(b))
print("a = " + str(a))