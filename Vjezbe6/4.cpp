#include <iostream>
void rjesenje_sustava(float a1, float b1, float c1, float a2, float b2, float c2) {
    float x; float y ;
    y = (c2*a1-a2*c1)/(b2-a2*b1);
    x = (c1-b1*y)/a1;
    std::cout << x << std::endl;
    std::cout << y << std::endl;
}
int main() {
    rjesenje_sustava(1, 2, 3, 4, 5, 6);
    return 0;
}    
    


