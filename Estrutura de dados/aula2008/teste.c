#include <stdio.h>

void dobro(int n) {
    n = n * 2;
    printf("%d\n", n);
}
int main() {
    int x = 5;
    dobro(x); // Passa o endereço de x (&)
    printf("%d\n", x); // Agora imprime 10!
    
    return 0;
}

