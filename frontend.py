import random
from cod import generator

#ef generator(n):
#       l = []
#       for i in range(n):
#           l.append(f"{random.randint(0, 10)} + {random.randint(0, 10)}")
#       return l


name = input("your name\n")
print (f" Hello, {name}") 

print (f" How many examples would you like?" )
n = int (input())
print (f"какой уровень?")
ur = int(input())

tasks = generator(n, ur)
x = 0
while x < len(tasks):
	a = tasks[x]
	print (a)
	otvet = int(input())
	if otvet == eval(a):
		print ("greaet job")
	else:
		print ("not great job")
	x += 1

