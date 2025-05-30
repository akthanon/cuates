def calcular_pi_leibniz(iteraciones):
    pi = 0
    for i in range(iteraciones):
        pi += (-1) ** i / (2 * i + 1)
    return pi * 4

print("π ≈", calcular_pi_leibniz(1_000_000))
