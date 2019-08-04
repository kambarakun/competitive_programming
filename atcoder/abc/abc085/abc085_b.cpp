// c++ abc085_b.cpp -o abc085_b.out
// ./abc085_b.out

#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)

int main() {

    int N;
    scanf("%d", &N);

    int A[N];
    REP(i, N){
        scanf("%d", &A[i]);
    }

    sort(A, A + N);

    int ans = 1;

    REP(i, N-1){
        if (A[i] != A[i+1]) {
            ans += 1;
        }
    }

    printf("%d\n", ans);
}
