#include <stdio.h>
int chainNum=1;

//recursive func
int rec(long long int num){
    
    if(num == 1){
        return 0;
    }
    else if(num % 2 == 0){
        num /= 2;
        chainNum+=1;
        return rec(num);
    }
    else{
        num = 3 * num + 1;
        chainNum+=1;
        return rec(num);
    }    
}

int main(){
    int biggestChain=0, number=0;

    for(long long int i = 999999 ; i > 100000 ; i--){
        chainNum = 1;
        rec(i);
        if(chainNum > biggestChain){
            biggestChain = chainNum;
            number = i;
            printf("%d\n",number);
        }
    }
    printf("%d",number);
    
    return 0;
}