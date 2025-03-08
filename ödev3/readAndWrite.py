def readAndWrite():
    file = open("msg.txt", "a+")
    msg = input("mesajinizi girin: ")
    file.write(msg + '\n')
    file.close()

for i in range(1,6):
    print(f"{i}.ci ", end="")
    readAndWrite()

file = open("msg.txt", "r+")
file.seek(0)
print(file.read())
file.truncate(0)
file.close()