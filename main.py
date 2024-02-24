import pandas as pd
import functions

# Inicio do programa.
# Carregar os dados do arquivo Excel.
arquivo_excel = "caminho_para_seu_arquivo_excel.xlsx"  # Substitua "caminho_para_seu_arquivo_excel.xlsx" pelo caminho do seu arquivo.
dados_excel = pd.read_excel(arquivo_excel)

# Para cada receita, calcular o slope.
for i, receita in dados_excel.groupby('Receita'):
    # Normalizar os valores de %.
    receita['Porcentagem_Normalizada'] = functions.normalizar(receita['Porcentagem'])

    # Calcular o slope para cada receita.
    slope = functions.calcular_slope(receita['Tempo'], receita['Porcentagem_Normalizada'])
    
    # Imprimir o slope.
    print(f"Slope para a receita {i}: {slope}")
    
# Fim do programa.