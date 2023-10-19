import random


def generator (chislo, ur):
    if ur == 2:
        math = ['-', '/', '*', '+']
        result = []
        while (chislo > 0):
            x = random.randint(-150,150)
            y = random.randint(-150,150)
            znac = random.choice(math)
            if x < 0 and y < 0:
                primer = "(" + str(x) + ")" + znac + "("  + str(y) + ")"
            if y < 0 and x > 0:
                primer = str(x) + znac + "(" + str(y) + ")"
            if y > 0 and x > 0:
                primer = str(x) + znac + str(y)
            if y > 0 and x < 0:
                primer = "(" + str(x) + ")" + znac + str(y)
            eval(primer)
            chislo -= 1
            result.append(primer)
    if ur == 1:
        math = ['-', '+']
        result = []
        while (chislo > 0):
            x = random.randint(-50,50)
            y = random.randint(-50,50)
            znac = random.choice(math)
            if x < 0 and y < 0:
                primer = "(" + str(x) + ")" + znac + "("  + str(y) + ")"
            if y < 0 and x > 0:
                primer = str(x) + znac + "(" + str(y) + ")"
            if y > 0 and x > 0:
                primer = str(x) + znac + str(y)
            if y > 0 and x < 0:
                primer = "(" + str(x) + ")" + znac + str(y)
            eval(primer)
            chislo -= 1
            result.append(primer)
    print (result)
    return result
generator (int(input()), int(input()))
def proverca (primer, otvet):
    if [otvet == eval(primer)]:
        print ("правильно")

