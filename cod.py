import random

def generator (chislo, ur):
    
    math = ['-', '//', '*', '+']
    result = []

    while chislo > 0:
        qwe = 0
        x = random.randint(-10,10)
        primer = str(x)
        while qwe < ur - 1:
            
            znac = random.choice(math)
            if znac == '*' or '//':
                x = random.randint(-10,10)
                if znac == '//' and x == 0:
                    x = 1
            else:
                x = random.randint(-30,30)
            if x < 0:
                primer += znac + "(" + str(x) + ")"
            else:
                primer += znac + str(x)
            qwe += 1
        chislo -= 1
        
        result.append(primer)
    return result
