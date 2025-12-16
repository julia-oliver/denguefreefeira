import csv

#Colunas que foram usadas na hora de mostrar os dados
coluna2 = ['Casos Suspeitos','Casos Negativos','Casos Confirmados']
coluna_casos = ['Habitantes','Casos Suspeitos','Casos Negativos', 'Casos confirmados']
colunas_sem_bairro = ['Data','Habitantes','Casos Suspeitos','Casos Negativos', 'Casos confirmados']
colunas_sem_data = ['Bairros','Habitantes','Casos Suspeitos','Casos Negativos', 'Casos confirmados']

def porcentagem_casos_totais_ultima_data(dados):
    casos_notificados = (total_c_s,total_c_c,total_c_n)
    casos_notificados_totais = sum(casos_notificados)
    #Cálculos realizados com base no total de casos notificados mais recentes.
    percentual_total_c_s = total_c_s*100/casos_notificados_totais
    percentual_total_c_n = total_c_n*100/casos_notificados_totais
    percentual_total_c_c = total_c_c*100/casos_notificados_totais
    print('\n\nPercentual referente ao total de casos mais recentes:\n')
    print(f'{coluna2[0]:^20} {coluna2[1]:^20} {coluna2[2]:^20}')
    print(f"{percentual_total_c_s:^20.1f} {percentual_total_c_n:^20.1f} {percentual_total_c_c:^20.1f}\n\n")

def dados_totais_por_data_especifica(dados,data_escolhida):

    global soma_habitantes
    global soma_suspeitos
    global soma_negativos
    global soma_confirmados
    global valores_soma

    soma_habitantes = 0
    soma_suspeitos = 0
    soma_negativos = 0
    soma_confirmados = 0 


    # Itera sobre os bairros e verifica se a data está presente
    for bairro, valores in dados.items():
        if data_escolhida in valores:
            # Obtém os valores correspondentes à data
            habitantes, suspeitos, negativos, confirmados = dados[bairro][data_escolhida]

            # Soma os valores
            soma_habitantes += habitantes
            soma_suspeitos += suspeitos
            soma_negativos += negativos
            soma_confirmados += confirmados

    valores_soma = [data_escolhida,soma_habitantes,soma_suspeitos,soma_negativos,soma_confirmados]
    #Impressão dos dados em forma de tabela
    print('\n\nEstes são os valores totais de Feira de Santana nesta específica data:\n')
    for coluna, valor in zip(colunas_sem_bairro, valores_soma):
        print(f'{coluna:^20}', end='')
    print()
    for valor in valores_soma:
        print(f'{valor:^20}', end='')
    print()
    # Retorna a soma dos valores
    return soma_habitantes, soma_suspeitos, soma_negativos, soma_confirmados

def dados_ultima_data_por_bairro (bairro,dados):
         dados_ultima_data = {}
         # Verifica se o bairro está presente nos dados
         if bairro in dados:
            # Obtém os os dados necessários
            valores = dados[bairro]
            ultima_data = max(valores.keys())
            dados_ultima_data = valores[ultima_data]

             # Cria uma tupla com os dados mais recentes
            coluna_dados_ultima_data=(ultima_data, dados_ultima_data[0], dados_ultima_data[1], dados_ultima_data[2], dados_ultima_data[3])

            # Imprime os dados mais recentes do bairro escolhido
            print(f"\nDados mais recentes do bairrro escolhido.\n")
            for coluna, valor in zip(colunas_sem_bairro, coluna_dados_ultima_data ):
                print(f'{coluna:^20}', end='')
            print()
            for valor in coluna_dados_ultima_data:
                print(f'{valor:^20}', end='')
            print()

def dados_totais_ultima_data(dados):
    global total_hab 
    global total_c_s 
    global total_c_n 
    global total_c_c
    global dados_ultima_data

    total_hab = 0
    total_c_s = 0
    total_c_n = 0
    total_c_c = 0

    print(f"\n\nDados totais mais recentes. \n")
    #Soma dos dados das últimas datas
    for bairro, valores in dados.items():
                # Obtém e soma dados
                ultimo_item = max(valores.keys())
                dados_ultima_data = valores[ultimo_item]
                total_hab += sum([dados_ultima_data[0]])
                total_c_s += sum([dados_ultima_data[1]])
                total_c_n += sum([dados_ultima_data[2]])
                total_c_c += sum([dados_ultima_data[3]])
    dados_totais = (total_hab ,total_c_s, total_c_n,total_c_c)
    # Impressão dos totais em forma de tabela
    for coluna, valor in zip(coluna_casos, dados_totais ):
                print(f'{coluna:^20}', end='')
    print()
    for valor in dados_totais:
                print(f'{valor:^20}', end='')
    print()

    return total_hab, total_c_s, total_c_n, total_c_c      

def acessar_dados_por_data(data_escolhida):
    nome_arquivo = "denguefreefeira.csv"
    dados = ler_arquivo_csv(nome_arquivo, encoding='utf-8') 

    global dados_por_data
    dados_por_data = {}
    print('\n\nEstes são os dados por bairro nesta data:\n')
    for coluna in colunas_sem_data:
        print(f'{coluna:^20}', end='')
    print()

    # Variáveis para armazenar os totais de casos notificados na data escolhida
    total_suspeitos_data = sum(valores[data_escolhida][1] for valores in dados.values() if data_escolhida in valores)
    total_negativos_data = sum(valores[data_escolhida][2] for valores in dados.values() if data_escolhida in valores)
    total_confirmados_data = sum(valores[data_escolhida][3] for valores in dados.values() if data_escolhida in valores)

    for bairro, valores in dados.items():
        if data_escolhida in valores:
            # Obtém dados da data específica
            dados_por_data = valores[data_escolhida]
            coluna1 = [bairro, dados_por_data[0], dados_por_data[1], dados_por_data[2], dados_por_data[3]]
            for valor in coluna1:
                print(f'{valor:^20}', end='')
            print()

    print('\n\nPorcentagens em relação ao total de casos notificados nesta data:\n')
    coluna_p_bairro = ['Bairro','Casos Suspeitos','Casos Negativos','Casos Confirmados']
    print(f'{coluna_p_bairro[0]:^20} {coluna_p_bairro[1]:^20} {coluna_p_bairro[2]:^20} {coluna_p_bairro[3]:^20}')
    for bairro, valores in dados.items():
        if data_escolhida in valores:
            # Calculo das porcentagens
            percentual_data_c_s = (valores[data_escolhida][1] * 100) / total_suspeitos_data
            percentual_data_c_n = (valores[data_escolhida][2] * 100) / total_negativos_data
            percentual_data_c_c = (valores[data_escolhida][3] * 100) / total_confirmados_data
            print(f"{bairro:^20} {percentual_data_c_s:^20.1f} {percentual_data_c_n:^20.1f} {percentual_data_c_c:^20.1f}")

    return dados_por_data

def imprimir_dados_por_bairro(bairro, dados):
    casos_totais_bairro = 0

    if bairro in dados: # Verifica se o bairro está presente nos dados
        print(f"\nBairro: {bairro}")
        for data_escolhida, valores in dados[bairro].items():
            print(f"\nData: {data_escolhida}")
            # Formata os valores do bairro para imprimir
            valores_bairro = (valores[0],{valores[1]},{valores[2]},{valores[3]})
            valores_bairro = tuple(str(valor).replace("{", "").replace("}", "") for valor in valores_bairro)
             # Imprime os valores do bairro
            for coluna, valor in zip(coluna_casos, valores_bairro):
                print(f'{coluna:^20}', end='')
            print()
            for valor in valores_bairro:
                print(f'{valor:^20}', end='')
            print()
            casos_totais_bairro  += sum(valores[1:4])

            # Calcula o percentual referente ao total de casos nesta data
            print('\nPercentual referente ao total de casos nesta data:\n')
            percentual_data_c_s = (valores[1] * 100)/casos_totais_bairro
            percentual_data_c_n = (valores[2] * 100)/casos_totais_bairro
            percentual_data_c_c = (valores[3] * 100)/casos_totais_bairro
            coluna2 = ['Casos Suspeitos','Casos Negativos','Casos Confirmados']
            print(f'{coluna2[0]:^20} {coluna2[1]:^20} {coluna2[2]:^20}')
            print(f"{percentual_data_c_s:^20.1f} {percentual_data_c_n:^20.1f} {percentual_data_c_c:^20.1f}")

    else:
        print('O bairro especificado não foi encontrado nos dados.')

def comparar_datas():
    nome_arquivo = "denguefreefeira.csv"
    dados = ler_arquivo_csv(nome_arquivo)
    comparações = {}

    # Solicita ao usuário um bairro, uma data mais antiga e uma data mais recente
    bairro_comparação = input ('Bairro a ser comparado: ')  
    data1 = input('Data mais antiga neste formato 00/00/0000: ')
    data2 = input('Data mais recente neste formato 00/00/0000: ')
    if bairro_comparação in dados:
        if data1 in dados[bairro_comparação] and data2 in dados[bairro_comparação]:
            valores_data1 = dados[bairro_comparação][data1]
            valores_data2 = dados[bairro_comparação][data2]

            # Calcula as diferenças entre os valores das duas datas
            for i, (valor1, valor2) in enumerate(zip(valores_data1, valores_data2)):
                chave = f'comparacao_{i}' 
                comparações[chave] = valor1 - valor2
                if 'comparacao_1' in comparações and 'comparacao_2' in comparações and 'comparacao_3' in comparações:

                    # Calcula os percentuais de diferença em relação aos valores da primeira data
                    percentual_comparação_c_s = comparações['comparacao_1'] * 100 / valores_data1[1]
                    percentual_comparação_c_n = comparações['comparacao_2'] * 100 / valores_data1[2]
                    percentual_comparação_c_c = comparações['comparacao_3'] * 100 / valores_data1[3]
            
            # Imprime as diferenças e os percentuais de diferença
            print('\nPorcentagens e valores totais de diferenças entre os dias:')
            print(f'{coluna2[0]:^20} {coluna2[1]:^20} {coluna2[2]:^20}')
            print(f"{abs(percentual_comparação_c_s):^20.1f} {abs(percentual_comparação_c_n):^20.1f} {abs(percentual_comparação_c_c):^20.1f}")
            print(f"{comparações['comparacao_1']:^20} {comparações['comparacao_2']:^20} {comparações['comparacao_3']:^20}")
            
             # Imprime se houve aumento, queda ou se os números permaneceram os mesmos
            if percentual_comparação_c_s < 0:
                print(f"Houve um aumento de {abs(percentual_comparação_c_s):.1f}% e {abs(comparações['comparacao_1']):.1f} no número de casos suspeitos.")
            elif percentual_comparação_c_s > 0:
                print(f"Houve uma queda de {abs(percentual_comparação_c_s):.1f}% e {abs(comparações['comparacao_1']):.1f} no número de casos suspeitos.")
            else:
                print("O número de casos suspeitos permaneceu o mesmo.")

            if percentual_comparação_c_n < 0:
                print(f"Houve um aumento de {abs(percentual_comparação_c_n):.1f}% e {abs(comparações['comparacao_2']):.1f} no número de casos notificados.")
            elif percentual_comparação_c_n > 0:
                print(f"Houve uma queda de {abs(percentual_comparação_c_n):.1f}% e {abs(comparações['comparacao_2']):.1f} no número de casos notificados.")
            else:
                print("O número de casos notificados permaneceu o mesmo.")

            if percentual_comparação_c_c < 0:
                print(f"Houve um aumento de {abs(percentual_comparação_c_c):.1f}% e {abs(comparações['comparacao_3']):.1f} no número de casos confirmados.")
            elif percentual_comparação_c_c > 0:
                print(f"Houve uma queda de {abs(percentual_comparação_c_c):.1f}% e {abs(comparações['comparacao_3']):.1f} no número de casos confirmados.")
            else:
                print("O número de casos confirmados permaneceu o mesmo.")

def ler_arquivo_csv(nome_arquivo,encoding='utf-8'):
    dados = {}

    with open(nome_arquivo, newline='',encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            data = row[0]
            bairro = row[1]
            habitantes = int(row[2])
            casos_suspeitos = int(row[3])
            casos_negativos = int(row[4])
            casos_confirmados = int(row[5])

            if bairro not in dados:
                dados[bairro] = {}

            if data not in dados[bairro]:
                dados[bairro][data] = [habitantes, casos_suspeitos, casos_negativos, casos_confirmados]
    return dados

def adicionar_dados(nome_arquivo,encoding='utf-8'):
    try:
        dados = ler_arquivo_csv(nome_arquivo)
        # Solicita ao usuário os dados para adicionar ou modificar
        bairro = input("Informe o nome do bairro: ")
        data = input("Informe a data (no formato dd/mm/aaaa): ")
        habitantes = int(input("Informe o número de habitantes: "))
        casos_suspeitos = int(input("Informe o número de casos suspeitos: "))
        casos_negativos = int(input("Informe o número de casos negativos: "))
        casos_confirmados = int(input("Informe o número de casos confirmados: "))

        # Verifica se o bairro já existe no dicionário
        if bairro in dados:
            if data in dados[bairro]:
                # Modifica os dados existentes
                dados[bairro][data] = (habitantes, casos_suspeitos, casos_negativos, casos_confirmados)
                print("Dados modificados com sucesso!")
            else:
                dados[bairro][data] = (habitantes, casos_suspeitos, casos_negativos, casos_confirmados)
                print("Dados adicionados com sucesso!")
        else:
            dados[bairro] = {data: (habitantes, casos_suspeitos, casos_negativos, casos_confirmados)}
            print("Dados adicionados com sucesso!")

        # Salva os dados de volta no arquivo CSV
        with open(nome_arquivo, 'w', newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Data", "Bairro", "Habitantes", "Casos Suspeitos", "Casos Negativos", "Casos Confirmados"])
            for bairro, valores in dados.items():
                for data in sorted(valores.keys()):  
                    dados_bairro = valores[data]
                    writer.writerow([data, bairro] + list(dados_bairro))

        print("Dados salvos no arquivo CSV.")

    except Exception as e:
        print("Ocorreu um erro:", e)
