integer = 12;

def numberGenerator(num):
    number = int(num)
    for x in range (0,number + 1):
        print(str(x)*x)


numberGenerator(11)