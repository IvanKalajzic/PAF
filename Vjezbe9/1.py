
import matplotlib.pyplot as plt
import bungee_jumping as bnj
p1 = bnj.bungee()
p1.set_initial_conditions(50.0, 0.0, 100.0, 45.0, 0.0, 1.22, 1.5, 70.0, 0.01)
y, el, kin, ep, uk, t = p1.bez_otpora(50.0)

fig, axs = plt.subplots(2, 2, figsize=(14, 8))

axs[0, 0].plot(t, uk)
axs[0, 0].plot(t, el)
axs[0, 0].plot(t, ep)
axs[0, 0].plot(t, kin)
axs[0, 0].set_title("Zakon ocuvanja energije bez otpora zraka")
axs[0, 0].set_ylabel("E [J]")
axs[0, 0].set_xlabel("t [s]")
axs[0, 0].legend(["Euk", "Eel", "Ep", "Ek"])

axs[0, 1].plot(t, y)
axs[0, 1].set_title("y-t")
axs[0, 1].set_ylabel("y [m]")
axs[0, 1].set_xlabel("t [s]")

p2 = bnj.bungee()
p2.set_initial_conditions(50.0, 0.0, 100.0, 45.0, 1.4, 1.22, 1.5, 70.0, 0.01)
y1, el1, kin1, ep1, uk1, t1 = p2.s_otporom(50.0)


axs[1, 0].plot(t1, uk1)
axs[1, 0].plot(t1, el1)
axs[1, 0].plot(t1, ep1)
axs[1, 0].plot(t1, kin1)
axs[1, 0].set_title("Zakon ocuvanja energije s otporom zraka")
axs[1, 0].set_ylabel("E [J]")
axs[1, 0].set_xlabel("t [s]")
axs[1, 0].legend(["Euk", "Eel", "Ep", "Ek"])

axs[1, 1].plot(t1, y1)
axs[1, 1].set_title("y-t")
axs[1, 1].set_ylabel("y [m]")
axs[1, 1].set_xlabel("t [s]")

plt.show()



