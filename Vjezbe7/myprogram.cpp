#include <iostream>
#include <Particle.h>

int main()
{
    Particle p1(10, 30, 0, 15);
    Particle p2(30, 60, 0, 0);

    std::cout << "Domet cestice 1: " << p1.range() << "m" << std::endl;

    std::cout << "Vrijeme leta cestice 1: " << p1.time() << "s" << std::endl;

    std::cout << "Domet cestice 2: " << p2.range() << "m" << std::endl;

    std::cout << "Vrijeme leta cestice 2: " << p2.time() << "s" << std::endl;

    return 0;
};
