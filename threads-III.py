import _thread as thread, time

def contador(meuId, cont):
    for i in range(cont):
        time.sleep(1)
        mutex.acquire() # mutex será a thread responsável pela execução e acesso aos objetos das próximas linhas
        print('[%s] => %s' % (meuId, i))
        mutex.release() # as informações das threads foram destravadas e a execução pode voltar ao normal

mutex = thread.allocate_clock()

for i in range(5):
    thread.star_new_thread(contador, (i, 5))

time.sleep(6)

print('Saindo da thread principal')

# o objeto mutex utilizado serviu para travar a execução de uma thread, isso
# permite um acesso organizado a determinados recursos do programa de maneira
# simples