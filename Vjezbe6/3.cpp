#include <iostream> 
#include <cmath>

void cijeli_brojevi(int a, int b) {
    for (int i = a; i <= b; i++) {
        std::cout << i << std::endl;
    }
}  
int main() {
    cijeli_brojevi(1, 10);
    return 0;
}         

