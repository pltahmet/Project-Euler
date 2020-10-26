kacıncı_asal=1
num=3
def isPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return False    
    return True
while True:
    if isPrime(num):
        kacıncı_asal+=1
        if(kacıncı_asal==10001):
            break        
    num+=1
print(num)