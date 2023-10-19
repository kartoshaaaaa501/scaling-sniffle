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
print (f"")
ur = int(input())
tasks = generator(n)

for i in range (len (tasks)):
    print(tasks[i])
  Answer =int(input())


while x < generator(n,ur):
	a = generator(n,ur)[x]
	print (a)
	otvet = int(input())
	if otvet == eval(a):
		print ("greaet job")
	else:
		print ("not great job")
	x += 1

