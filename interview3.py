integer = 12;

def numberGenerator(num):
    number = int(num)
    for x in range (0,number):
        print(str(x)*x)

numberGenerator(11)