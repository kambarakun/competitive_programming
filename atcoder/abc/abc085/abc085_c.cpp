// c++ abc085_c.cpp -o abc085_c.out
// ./abc085_c.out

#include <iostream>

#define REP(i, n) for(int i = 0; i < (int)(n); i++)

int main() {

    int N, Y, c;
    scanf("%d%d", &N, &Y);

    REP(a, N+1){
        REP(b, N+1-a){
            c = N - a - b;
            if (Y == 10000 * a + 5000 * b + 1000 * c) {
                printf("%d %d %d\n", a, b, c);
                return 0;
            }
        }
    }

    printf("%d %d %d\n", -1, -1, -1);
}
