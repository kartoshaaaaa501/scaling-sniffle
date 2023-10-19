
import random


def generator (chislo):
    chislo1 = chislo
    math = ['-', '/', '*', '+']
    result = []
    while (chislo > 0):
        x = random.randint(-150,150)
        y = random.randint(-150,150)
        znac = random.choice(math)
        primer = str(x) + znac + str(y)
        eval(primer)
        chislo -= 1
        result.append(primer)
    print (result)
    return result
    
#enerator (int(input()))


def proverca (primer, otvet):
    if [otvet == eval(primer)]:
        print ("правильно")
