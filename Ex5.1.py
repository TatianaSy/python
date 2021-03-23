data = input()
f1 = open('primer1.txt', 'a')
while data != '':
    f1.write(data)
    f1.write('\n')
    data = input()