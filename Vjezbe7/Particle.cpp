#include <Particle.h>
#include <math.h>
#include <iostream>

Particle::Particle(float v0, float theta, float x0, float y0)
{
    
    x = x0;
    y = y0;

    Vx = v0*cos((theta/180)*3.1416);
    Vy = v0*sin((theta/180)*3.1416);
}

void Particle::evolve()
{
        t = t + dt;

        Vx = Vx + 0.0;
        Vy = Vy - g*dt;

        x = x + Vx*dt;
        y = y + Vy*dt;
}        

float Particle::range()
{
    while (y >= 0){
        evolve();
    }
    return x;
};

float Particle::time()
{
    while (y >= 0){
        evolve();
    }
    return t;
};



    
