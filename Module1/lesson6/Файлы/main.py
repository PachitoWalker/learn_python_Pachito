myfile = open('text.txt')
# data = myfile.read()
# print(data)


for line in myfile.readlines():
    print(line, end='')

myfile.close()