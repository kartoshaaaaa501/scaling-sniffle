import random
def generator(n):
        l = []
        for i in range(n):
            l.append(f"{random.randint(0, 10)} + {random.randint(0, 10)}")
        return l

name = input("your name\n")
print (f" Hello, {name}") 

print (f" How many examples would you like?" )
n = int (input())

tasks = generator(n)

for i in range (len (tasks)):
    print(tasks[i])


