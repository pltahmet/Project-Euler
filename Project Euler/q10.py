toplam=0
def isPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
    return 1

for j in range(3,2000000,2):
    if isPrime(j):
        toplam+=j
print (toplam)
        