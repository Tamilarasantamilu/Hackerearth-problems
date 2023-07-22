x=input()

s1=0

s2=0

for i in range(len(x)):
    if x[i]=='z':
        s1=s1+1

else:
    s2=s2+1
if(s2/s1==2):
    print("No")
else:
    print("Yes")