f1 = open('primer2.txt', 'r', encoding="utf-8")
content = f1.readline()
qstr = 0
qwords = 0
while content != '':
    qstr = qstr + 1
    string = content.split()
    qwords = len(string)
    print("в строке", qstr, "-", qwords, "слов")

    content = f1.readline()
f1.close()
print("количество строк =", qstr)