#include <iostream>
void funkcija(float x1, float x2, float y1, float y2) {
    float k; float l;
    k = (y2-y1)/(x2-x1);
    l = y1-k*x1;
    if (l < 0)
    {
        std::cout << "y =  " << k << "x"<< l <<std::endl;
    }

    else if (l > 0)
    {
       std::cout << "y =  " << k << "x+"<< l <<std::endl;
    }
}
     
int main() {
    funkcija(3, 4, -1, 6);
    return 0;
}    