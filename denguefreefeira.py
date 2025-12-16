#Autor: Julia Gonçalves Oliveira
#Componente Curricular: MI Algoritmos 
#Concluido em: 30/05/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


import csv
import funções


sair = 1

def ler_arquivo_csv(nome_arquivo,encoding='utf-8'):
    dados = {}
    #O arquivo CSV é aberto usando o nome fornecido e lido linha por linha.
    with open(nome_arquivo, newline='', encoding=encoding) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pular o cabeçalho
        for row in reader:
            data = row[0]
            bairro = row[1]
            habitantes = int(row[2])
            casos_suspeitos = int(row[3])
            casos_negativos = int(row[4])
            casos_confirmados = int(row[5])

            #Se os dados não estiverem presentes, eles são criados
            if bairro not in dados:
                dados[bairro] = {}

            if data not in dados[bairro]:
                dados[bairro][data] = [habitantes, casos_suspeitos, casos_negativos, casos_confirmados]
    return dados

while sair > 0:
    nome_arquivo = "denguefreefeira.csv"
    dados = ler_arquivo_csv(nome_arquivo)
    menu1 = int(input('\n[1]Informações sobre a Dengue \n[2]Visualizar dados. \n[3]Atualizar dados. \n[4]Sair\n\n'))
    match menu1:
        case 1:
            #Texto retirado de 
            print('É uma doença infecciosa febril aguda, que pode se apresentar de forma benigna ou grave, dependendo de alguns fatores, entre eles: o vírus envolvido, infecção anterior pelo vírus da dengue e fatores individuais como doenças crônicas\n')
            print('A doença é transmitida pela picada da fêmea do mosquito Aedes aegypti. Não há transmissão pelo contato direto com um doente ou suas secreções, nem por meio de fontes de água ou alimento.\n')
            print('Seus principais sintomas são: \n-Febre. \n-Dores de cabeça. \n-Dores pelo corpo. \n-Náuseas \n-Manchas vermelhas na pela \nSangramento(no caso de dengue hemorrágica).\n')
            print('A melhor forma de se evitar a dengue é combater os focos de acúmulo de água, locais propícios para a criação do mosquito transmissor da doença. Para isso, é importante não acumular água em latas, entre outros.')
            print('Devido a esta problemática o software foi criado.\nObrigada por usar "Dengue Free Feira!" ')
        case 2:
            menu2 = int(input('\n[1]Dados por data. \n[2]Dados mais recentes por bairro. \n[3]Dados totais dos bairros. \n[4]Comparar datas.\n\n'))
            match menu2:
                case 1:
                    data_escolhida = input('Data escolhida')
                    funções.dados_totais_por_data_especifica(dados,data_escolhida)
                    funções.acessar_dados_por_data(data_escolhida)  
                case 2:
                    bairro = input('Bairro escolhido: ')
                    funções.dados_ultima_data_por_bairro (bairro,dados)
                    funções.dados_totais_ultima_data(dados)
                    funções.porcentagem_casos_totais_ultima_data(dados)
                case 3:
                    bairro = input('Bairro escolhido: ')
                    funções.imprimir_dados_por_bairro(bairro, dados)
                case 4:
                    funções.comparar_datas()
        case 3:           
            funções.adicionar_dados(nome_arquivo)
        case 4:
              sair -= 1