

while True:

    dewrite = input("Enter device for add in list: ")

    if dewrite == 'q' or dewrite == 'quit':
        break

    file = open("devices.txt", "a")

    file.write(dewrite + "\n")

    file.close
