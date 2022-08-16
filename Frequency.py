import itertools

 
file = open("C:\\Users\\Luis\\Desktop\\DVM\\data\\declaration.txt")

count = 0


for x in itertools.chain.from_iterable(file):
    if x == "a":
        count += 1
    
print(count)