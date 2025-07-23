with open('/home/kamil/docs/pythontrain/text_log.txt', 'a') as file:
    file.write('hello python with \n')
file.close()

with open('/home/kamil/docs/pythontrain/text_log.txt', 'r') as file:
    for line in file:
        print(line, end="")
file.close()

# Чтение и запись в файл
FILENAME = "messages.txt"

messages = list()

for i in range(4):
    message = input("Введите строку " + str(i+1) + ": ")
    messages.append(message + "\n")

with open(FILENAME, "a") as file1:
    for message in messages:
        file1.write(message)

print("Считанные сообщения")
with open(FILENAME, "r") as file:
    for message in file:
        print(message, end="")


