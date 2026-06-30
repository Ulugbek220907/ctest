#include <stdio.h>
#include <limits.h>

int reverse(int x){
    int result = 0;
    int res = 0;
    res = x;
    int a = 0;
    while (res != 0){
        a = res%10;
        if (result > INT_MAX / 10 || (result == INT_MAX / 10 && a > 7)) {
            return 0;
        }
        if (result < INT_MIN / 10 || (result == INT_MIN / 10 && a < -8)) {
            return 0;
        }
        result = (result*10)+a;

        res /= 10;
    }
    return result;  
}

int main(){
    int a = 12345678912;

    printf("%d", reverse(a));


    return 0;
}