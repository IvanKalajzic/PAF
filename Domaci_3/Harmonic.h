class HarmonicOscilator {
    private:

    float x, v, a, t, k, m, n;
    float dt = 0.01;

    void oscilate();

    public:
    HarmonicOscilator(float x0, float v0, float a0, float t0, float K, float M);
     //~HarmonicOscilator();

    float range(float t1);
    float time(float t1);
};