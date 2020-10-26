liste=range(100,1000)
def palindromic(num):
    strnum=str(num)
    uzunluk=len(strnum)
    for i in range(uzunluk//2):
        if(strnum[i]!=strnum[uzunluk-1-i]):
            return False
    return True               
        
big=0
for i in liste[::-1]:
    for j in liste[::-1]:
        value=i*j
        if palindromic(value):
            if(value>big):
                big=value
            print(i,j,big)
        