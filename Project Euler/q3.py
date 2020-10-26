
value=600851475143
i=2
while True:
    if(i==value):
        print(i)
        break
    if(value%i==0):
        value=value/i
        i=2  
    i+=1

