"""
Sistemas de fluidos · Problemas de turbulencia (1)

Plantilla para resolver los problemas con Python. Cada problema tiene sus datos y una
función con las partes marcadas con TODO. Ejecuta el script y compara con las respuestas
del enunciado cuando las haya.

Requiere: numpy, scipy, matplotlib
"""
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

G = 9.81  # m/s²


# ------------------------------------------------------------ HERRAMIENTAS
def colebrook(Re, eD=0.0):
    """Factor de fricción de Darcy con la ecuación de Colebrook (flujo turbulento, Re > 4000).
    Re: número de Reynolds; eD: rugosidad relativa ε/D. Se resuelve numéricamente."""
    return brentq(lambda f: 1 / np.sqrt(f) + 2 * np.log10(eD / 3.7 + 2.51 / (Re * np.sqrt(f))), 1e-4, 1.0)


def haaland(Re, eD=0.0):
    """Aproximación explícita de Haaland (error < 2 % respecto a Colebrook)."""
    return (-1.8 * np.log10((eD / 3.7) ** 1.11 + 6.9 / Re)) ** -2


def regimen(Re):
    """Régimen orientativo en una tubería circular."""
    return "laminar" if Re < 2300 else ("transición (¡cuidado!)" if Re < 4000 else "turbulento")


# ------------------------------------------------------------ PROBLEMA 1
def p1():
    rho, mu = 1.145, 1.895e-5          # aire a 35 °C
    a, b, L, V = 0.15, 0.20, 10.0, 7.0  # m, m, m, m/s
    eps = 0.045e-3                      # acero comercial (m)
    # TODO: diámetro hidráulico, caudal, Re, ε/Dh, f, Δp y potencia
    pass


# ------------------------------------------------------------ PROBLEMA 2
def p2():
    rho, mu = 999.7, 1.307e-3           # agua a 10 °C
    D, L, V = 0.0012, 15.0, 0.9
    # TODO: Re (¿régimen?), f, Δp, hL, caudal y potencia
    pass


# ------------------------------------------------------------ PROBLEMA 3
def p3():
    rho, mu = 999.1, 1.138e-3           # agua a 15 °C
    D, L, Q = 0.05, 30.0, 0.009
    eps = 0.002e-3                      # acero inoxidable
    # TODO: V, Re, f (compara con ε = 0), Δp, hL y potencia
    pass


# ------------------------------------------------------------ PROBLEMA 4
def p4():
    Q, L, nu, rho = 1.5, 1500.0, 1e-6, 1000.0
    casos = {"sin recubrir": (0.70, 3e-3), "recubierto": (0.66, 0.04e-3)}   # (D, ε) en m
    # TODO: para cada caso V, Re, ε/D, f, hL y potencia; variación porcentual
    pass


# ------------------------------------------------------------ PROBLEMA 5
def p5():
    rho, mu, cp = 950.6, 0.255e-3, 4229.0   # agua a 110 °C
    D, L, Q, eps, eta = 0.60, 12000.0, 1.5, 0.002e-3, 0.80
    precio = 0.06                            # €/kWh
    # TODO: hbomba = hL; potencia eléctrica, coste diario y calentamiento por fricción
    pass


# ------------------------------------------------------------ PROBLEMA 6
def p6():
    D, L, pendiente, nu, rho = 0.12, 800.0, 0.01, 1e-6, 1000.0
    # TODO: el caudal es la incógnita. Escribe una función ec(V) que valga
    #       f(Re(V))·(L/D)·V²/(2g) − (caída de cota) y busca su raíz con brentq.
    pass


# ------------------------------------------------------------ PROBLEMAS 7 y 8
def carga_bomba(D2, Q=0.018, rho=999.1, mu=1.138e-3, eps=0.26e-3,
                L1=20.0, D1=0.06, L2=35.0, H=30.0, KL=0.5):
    """Carga de bombeo (m) del problema 7 para un diámetro D2 de la segunda tubería."""
    # TODO: V1, V2, Re1, Re2, f1, f2, hL1 (con la entrada), hL2 y la ecuación de la energía
    return np.nan


def p7():
    # TODO: llama a carga_bomba(0.04) y calcula la potencia mínima
    pass


def p8():
    D2 = np.arange(1, 11) / 100   # 1 a 10 cm
    # TODO: tabla de carga de bombeo frente a D2 y gráfica (escala logarítmica)
    pass


# ------------------------------------------------------------ PROBLEMAS 9 y 10
def p9_p10():
    rho, mu = 1.164, 1.872e-5     # aire a 30 °C
    Re_inicio, Re_final = 1e5, 3e6
    for U in (29.1, 30.0):
        # TODO: posiciones de inicio y final de la transición
        pass


if __name__ == "__main__":
    for fn in (p1, p2, p3, p4, p5, p6, p7, p8, p9_p10):
        print(f"--- {fn.__name__}")
        fn()
    plt.show()
