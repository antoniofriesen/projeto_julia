import pandas as pd
import numpy as np

# Função para calcular o slope.
def calcular_slope(tempo, porcentagem):
    # Calcula o slope utilizando regressão linear.
    coeficientes = np.polyfit(tempo, porcentagem, 1)
    # slope é o primeiro coeficiente.
    slope = coeficientes[0]
    return slope

# Função para normalizar os valores entre 0 e 100%.
def normalizar(valores):
    # Normaliza os valores entre 0 e 100%.
    max_valor = max(valores)
    return [(x / max_valor) * 100 for x in valores]

if __name__ == "__main__":
    calcular_slope()
    normalizar()