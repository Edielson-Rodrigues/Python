import random

class Sorteio:

    def sortear():
        #lendo o arquivo, atribuindo valor na variável 'arquivo'
        with open('Lista.txt', 'r', encoding='utf-8') as arquivo:
            lista = arquivo.readlines()

        #Retirando o '\n' dos componentes da lista
        for i in range(len(lista)): 
            lista[i] = lista[i].replace('\n', '')
                
        totalDeGrupos = len(lista) // 5
        gruposDefinitivos = []; posicoesSorteadas = []

        #formando os grupos
        for i in range(int(totalDeGrupos)):
            cont = 0
            condicao = True
            grupo = []
            
            while condicao:
                numeroSorteado = None
                while cont < 5:  #montando grupos de 5
                    numeroSorteado = random.randrange(0, len(lista)) #sorteando
                    if numeroSorteado in posicoesSorteadas: numeroSorteado = None #vereficando se a pessoa já foi sorteada
                    else:
                        grupo.append(lista[numeroSorteado]) #adicionando pessoa0 no grupo
                        posicoesSorteadas.append(numeroSorteado) #guardando as posições já sorteadas 
                        cont += 1
                    if cont == 5:
                        gruposDefinitivos.append(grupo)
                        condicao = False
        
        #vereficando se alguém ficou sem grupo
        if len(lista) % 5 != 0:
            for i in range(len(posicoesSorteadas)):
                if posicoesSorteadas.count(i) == 0: #procurando quem tá sem grupo e adcionando no primeiro grupo
                    gruposDefinitivos[0].append(lista[i])

        #apresentando resultado
        print('-'*55)
        print(f'Resultado:\nTotal de estudantes: {len(lista)}\nTotalizando {totalDeGrupos} grupos')
        print('-'*12, 'Apresentando Grupos sorteados', '-'*12)

        for i in range(len(gruposDefinitivos)):
            print(f'\nGrupo {i+1}: {len(gruposDefinitivos[i])} Estudantes')
            for x in range(len(gruposDefinitivos[i])):
                print('    ',gruposDefinitivos[i][x])

    
    sortear()

Sorteio()

'''
OBS: Para o programa funcionar crie um arquivo txt 'Lista.txt', ou caso prefira mude o nome, mas lembre-se de alterar o nome no código,
    após criar o arquivo, o preencha com algum tipo de lista ou texto, (para funcionar ele deverá está no mesmo diretório que o arquivo python, caso contrário
    será necesssário informar o caminho no with).
'''