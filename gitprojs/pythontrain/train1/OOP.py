class A:
    def g(self):
        return 'Hello world'

    pass


a = A()
b = A()
a.arg = 1
b.arg = 2
print(str(a.arg) + ' a.arg \n')
print(str(b.arg) + ' b.arg \n')

c = A()
print(str(c.g()) + ' c.g() \n')


class B:
    arg = 'Python'

    def g(self):
        return self.arg


b = B()
print(str(b.g()) + ' b.g() \n')
print(str(B.g(b)) + ' B.g(b) \n')

b.arg = 'spam'
print(str(b.arg) + ' b.arg \n')


class A:
    def __private(self):
        print('приватный метод')


a = A()
a._A__private()


class MyDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


# Ведут себя одинаково
a = dict(a=1, b=2)
b = MyDict(a=1, b=2)

b['c'] = 4
print(b)

print('\n')
print(a.get('v'))
print(b.get('v'))

print('Перегрузка операторов')


class A1:
    def go(self):
        print('Go, A!')


class B1(A1):
    def go(self, name):
        print('Go, {}'.format(name))


b1 = B1()
print(b1.go('Batman'))

print('Перегрузка операторов __init__')


class A2:
    def __init__(self, name):
        self.name = name


a = A2('Vasya')
print(a.name)


class AA:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def info(self):
        print(self.name1)
        print(self.name2)


a4 = AA(1, 2)
a4.info()
