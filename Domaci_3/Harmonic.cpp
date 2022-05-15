#include <Harmonic.h>
#include <math.h>
#include <iostream>

HarmonicOscilator::HarmonicOscilator(float x0, float v0, float a0, float t0, float K, float M);
{
    x = x0;
    v = v0;
    t = t0;
    a = a0;
    k = K;
    m = M;
}

void HarmonicOscilator::oscilate()
{
        t = t + dt;
        a = (k/m)*x;
        v = v + a*dt;
        x = x - v*dt;

}        

float HarmonicOscilator::range(float t1)
{
    n = int(t1/dt);
    for(int i=0; i<n; i++){
        oscilate();
    }
    return x;
};

float HarmonicOscilator::time(float t1)
{
    n = int(t1/dt);
    for(int i=0; i<n; i++){
        oscilate();
    }
    return t;
};



    
