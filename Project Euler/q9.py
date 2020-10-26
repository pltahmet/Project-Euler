import math
a=0
b=0
c=0
product=0
for a in range(1,500):
    for b in range(1,500):
        d=a**2+b**2
        c=math.sqrt(d)
        if(a+b+c==1000):
            product=a*b*c
            break
    if(a+b+c==1000):
        break
print(product)



