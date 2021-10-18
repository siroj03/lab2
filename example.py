a=list(map(int,input()))
a.insert(0,0)
f=[]
fo=['r1','r2','i1','r3','i2','i3','i4']

if a[1]%2!=(a[3]+a[5]+a[7])%2:
    f.append(1)
if a[2]%2!=(a[3]+a[6]+a[7])%2:
    f.append(2)
    
if a[4]%2!=sum(a[5:8])%2:
    f.append(4)
    
if len(f)>0:
    x=sum(f)
    print('Ошибка в цифре:',fo[x-1])
    
for i in range(len(a)):
    if bin(i)[2:].count('1')>1:
        print(a[i],end='')
