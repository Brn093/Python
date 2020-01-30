# Threads são como forks entretando são
# usados para executar objetos em um mesmo
# processo, o que lhes garante uma melhor
# performace, simplicidade, compartilhamento
# de memória e portabilidade.

# Um dos problemas mais notáveis de threads é para sincronizar
# operações, uma vez que mesmo operações simples como printar texto
# na tela pode gerar conflitos. Veremos a frente uma thread está sendo
# realmente executada pelo interpretador

import _thread as thread, time

def contador(meuId, cont):
    for i in range(cont):
        time.sleep(1)
        print('[%s] => %s' % (meuId, i))

for i in range(5):
    thread.start_new_thread(contador, (i, 5))

time.sleep(6)

print("Saindo da thread principal;")

# Note que temos a execução paralela da função
# no programa, entretando um cuidado que devemos ter
# é ao compartilhar objetos, pois se duas threads
# tentatem modificar o objeto ao mesmo tempo isso poderá causar erros