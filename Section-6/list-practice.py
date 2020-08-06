def stringGenerator(list):
    newStr = ''
    for i in range(len(list)):
        newStr += list[i] + ' '

    print(newStr)

test = ['my', 'dude', 'is', 'going', 'off']
stringGenerator(test)
