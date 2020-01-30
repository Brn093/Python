# Threads são como forks entretando são
# usados para executar objetos em um mesmo
# processo, o que lhes garante uma melhor
# performace, simplicidade, compartilhamento
# de memória e portabilidade.

# Um dos problemas mais notáveis de threads é para sincronizar
# operações, uma vez que mesmo operações simples como printar texto
# na tela pode gerar conflitos. Veremos a frente uma thread está sendo
# realmente executada pelo interpretador

import _thread 

def filho(tid):                 # função filho
    print('Olá da thread', tid) # imprime Olá da thread com o id

def pai():                      # função pai
    i = 0                       # cria um variável
    while True:                 
        i+=1
        _thread.start_new_thread(filho, (i,)) # inicia a thread filho
        if input() == 'q':
            break

pai()