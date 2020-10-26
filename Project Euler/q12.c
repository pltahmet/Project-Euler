#include <stdio.h>

int numDivisor(int number){
    int num=1;
        for(int i=1; i <number; i++){
            if(number % i == 0){
                num++;
            }            
        }                
    return num;
}

int main(){
    int divisor=0, value, j=1;
    while(1){
        value = (j*(j+1))/2 ;
        if(numDivisor(value)>500){
            printf("%d",value);
            break;
        }
        j++;
    } 
    
    return 0;
}