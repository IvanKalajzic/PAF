#include <iostream> 
#include <cmath>
void polozaj(float x1, float y1, float s1, float s2, float r) {
    float d; 
    d =  sqrt(pow(s1-x1, 2)+ pow(s2-y1, 2));

    if (d > r)
    {
        std::cout << "Tocka se nalazi izvan kruznice." <<std::endl;
    }

    else if (d < 0)
    {
       std::cout << "Tocka se nalazi unutar kruznice." <<std::endl;
    }

    else 
    {
        std::cout << "Tocka se nalazi na kruznici." <<std::endl;
}
}

int main() {
    polozaj(1, 4, 2, 3, 4);
    return 0;
}    

  