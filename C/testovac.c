#include <stdio.h>
#include <stdlib.h>


int main(){
    char charray[5];
    double num = 04.12;
    charray[0] = '0';
    sprintf(charray, "%.2f", num);
    printf(charray);

}