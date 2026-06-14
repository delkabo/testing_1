def cube_natur(max):
    for x in range(max):
        yield x**3

get_decition = cube_natur(7)
for cube in get_decition:
    print(cube)


cube_nature_gen = (n**3 for n in range(7))
for i in cube_nature_gen:
    print(i)