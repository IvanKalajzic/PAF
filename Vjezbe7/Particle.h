class Particle {
    private:

    float x, y, t, Vx, Vy;
    float dt = 0.01;
    float g = 9.81;

    void evolve();

    public:
    Particle(float v0, float theta, float x0, float y0);
     //~Particle();

    float range();
    float time();
};