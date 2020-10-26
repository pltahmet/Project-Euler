a=20
i=1
while True:
    if(a%i==0):
        i+=1
    else:
        i=1
        a+=20
    if(i==21):
        break 
print(a)