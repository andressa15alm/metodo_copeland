import pandas as pd

num_alternativas = int(input("Quantas alternativas você deseja inserir? "))
respostas = []

criterios = []

num_criterios = int(input("Quantos criterios você deseja inserir? "))

for i in range(num_alternativas):
    resposta = input("Digite a alternativa {}: ".format(i+1))
    respostas.append(resposta)




for i in range(num_criterios):
    criterio = input("Digite o criterio {}: ".format(i+1))
    criterios.append(criterio)



classificacoes = {}
# Coletar a classificação das alternativas para cada critério
print(''' classifique cada alternativa de acordo com a escala abaixo
            5- Muito Bom
            4- Bom
            3- Neutro
            2- Ruim
            1 - Muito ruim
            ''')
for criterio in criterios:
    classificacoes[criterio] = {}
    print("Classificação para o critério", criterio)

    for alternativa in respostas:
        classificacao = int(input("Digite a classificação para a alternativa {}: ".format(alternativa)))
        classificacoes[criterio][alternativa] = classificacao



# Criar o DataFrame com as classificações
df = pd.DataFrame(classificacoes, index=respostas)

print("\nTabela de Classificações:\n")
print(df)
matrizes = {}

for criterio in criterios:
    matriz = []
    for i in range(num_alternativas):
        linha = []
        for j in range(num_alternativas):
            if i == j:
                linha.append(0)  # Mesma alternativa, valor 0
            elif classificacoes[criterio][respostas[i]] > classificacoes[criterio][respostas[j]]:
                linha.append(1)  # Alternativa i é maior, valor +1
            elif classificacoes[criterio][respostas[i]] == classificacoes[criterio][respostas[j]]:
                linha.append(0)  # Alternativas i e j são iguais, valor 0
            else:
                linha.append(-1)  # Alternativa j é maior, valor -1
        matriz.append(linha)
    matrizes[criterio] = matriz

# Exibir as matrizes para cada critério
for criterio, matriz in matrizes.items():
    print(f"\nMatriz para o critério '{criterio}':")
    for linha in matriz:
        print(linha)




# Somar as matrizes de cada critério
matriz_decisao = [[0] * num_alternativas for _ in range(num_alternativas)]

for criterio, matriz in matrizes.items():
    for i in range(num_alternativas):
        for j in range(num_alternativas):
            matriz_decisao[i][j] += matriz[i][j]

# Aplicar as regras na matriz de decisão
for i in range(num_alternativas):
    for j in range(num_alternativas):
        if matriz_decisao[i][j] >= 1:
            matriz_decisao[i][j] = 1
        elif matriz_decisao[i][j] <= -1:
            matriz_decisao[i][j] = -1
        else:
            matriz_decisao[i][j] = 0

# Exibir a matriz de decisão
print("\nMatriz de Decisão:")
for linha in matriz_decisao:
    print(linha)

# Calcular a soma das linhas da matriz de decisão
soma_linhas = [sum(row) for row in matriz_decisao]

# Criar uma lista de tuplas com a alternativa, soma e ordenação
resultado = [(alternativa, soma) for alternativa, soma in zip(respostas, soma_linhas)]

# Ordenar a lista pelo valor da soma em ordem decrescente
resultado_ordenado = sorted(resultado, key=lambda x: x[1], reverse=True)

# Criar a nova matriz com três colunas (alternativas, soma, ordenação)
nova_matriz = [[alternativa, soma, i+1] for i, (alternativa, soma) in enumerate(resultado_ordenado)]

# Exibir a nova matriz
print("\nNova Matriz:")
for linha in nova_matriz:
    print(linha)

