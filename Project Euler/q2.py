sum=2
toplam=3
a=2
b=0
while True:
    b=toplam
    toplam+=a
    a=b
    if(toplam%2==0):
        sum+=toplam
    if(toplam>=4000000):
        break
    
print(sum)