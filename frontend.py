from cod import generator
name = input("your name\n")
print (f" Hello, {name}")
print (f" How many examples would you like?" )
while True:
    try:
        n = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
print (f"сколько чисел в примере?")
while True:
    try:
        ur = int(input(""))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

tasks = generator(n, ur)
qwerty = 0
x = 0
while x < len(tasks):
        a = tasks[x]
        print (a)
        otvet = int(input())
        if otvet == eval(a):
                print ("greaet job")
                qwerty += 1
        else:

                print ("not great job")
                print (f"cool answer is: {eval(a)}")
        x += 1
if qwerty == 0:
    print ("тебе нужно очень сильно подтянуть математику..")
elif 0.3 <= qwerty / n <= 0.4:
    print  ("треть правильных ответов. подтяни математику")
elif qwerty / n < 0.3:
    print ("меньше треети правильных ответов. Я сейчас ИЕ позову...")
elif 0.4 < qwerty / n <= 0.6:
    print ("примерно половина. не очень как-то")
elif qwerty / n > 0.6:
    print ("бог математики")
