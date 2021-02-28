import pygame
i: int = 0
pygame.init()
pygame.mixer.music.load('t.mp3')
n = input('Digite "s" para começar a musica e "n" para parar: ')
for n in n:
    if (n == 's'):
        pygame.mixer.music.play()
        pygame.event.wait()
        print('Aproveite!')
        n = input()
    elif (n == 'n'):
        pygame.mixer.music.stop()
        print('Musica parada!')
        n = input()
    else:
        print('Erro!!!')

