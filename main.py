from math import sqrt
import matplotlib.pyplot as plt


def tartaglia(x0, y0, vx0, vy0, alpha, beta, m, g, tf, N):
    dt = tf / N
    (Lx, Ly) = ([x0], [y0])  # Liste des abscisses et liste des ordonnées.
    (vx, vy) = (vx0, vy0)  # Initialisation du vecteur vitesse.
    for i in range(N):
        ax = - (beta / m) * sqrt(vx ** 2 + vy ** 2) * vx
        ay = - g - (beta / m) * sqrt(vx ** 2 + vy ** 2) * vy
        vx += ax * dt
        vy += ay * dt
        x = Lx[-1] + vx * dt
        y = Ly[-1] + vy * dt
        Lx.append(x)
        Ly.append(y)
        if y < 0:  # Arrêter la boucle une fois le sol atteint.
            break
    plt.plot(Lx, Ly)  # Afficher graphiquement la courbe.
    plt.show()


# tartaglia(0, 0, 10, 30, 0, 0.001, 0.005, 9.8, 50, 1000)
