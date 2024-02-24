# Calculo Coeficiente Angular

## Resumo
Este programacalcula o coeficiente angular (slope) de curvas. Os dados são carregados de um arquivo Excel contendo informações sobre receita, tempo e porcentagem. O coeficiente angular (slope) é calculado para cada receita e impresso na saída.

## Requisitos
- Python 3.x
- Pandas
- NumPy

## Execução
Para executar o programa, siga os passos abaixo:

0. Entre no modo `virtual environment` para desenvolvimento seguro da seguinte forma:
* Ativar o modo `virtual environment`
    - Entre na pasta onde os arquivos do projeto (principalente o `main.py`) se encontram
    - Digite no terminal `python3 -m venv .venv`
    - Depois digite `source .venv/bin/activate`
* Desativar o modo `virtual environment`
    - Digite no terminal `deactivate`

1. Instale os pacotes necessários executando o seguinte comando:
pip3 install pandas numpy

2. Execute o script principal `main.py` fornecendo o caminho para o arquivo Excel como argumento:
python3 main.py caminho_para_seu_arquivo_excel.xlsx

## Testes
Para executar os testes, siga os passos abaixo:

1. Execute o script de testes `tests.py`:
python3 tests.py
