import particle

p1 = particle.Particle()
p1.__init__()
p1.set_initial_conditions(0.0, 0.0, 10.0, 60.0)
p1.relativna_pogreska_u_dometu()
p1.reset()

#Kada pokrenem ovaj program, program mi ne vrati ni gresku, a ni rjesenje. Kao da racunalo obavlja naredbe, ali nikako da zavrsi. 

