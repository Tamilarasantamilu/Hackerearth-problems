n = int(input())

lst = list()

result = 1

for i in range(n+1):    

    lst.append(i)

lst.remove(int("0"))    

for x in lst:    

    result = result*x

print(result)