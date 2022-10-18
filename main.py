import pygame 
from pygame.locals import *
from sys import exit
from random import randint

from Item import Item
from Player import Player
from Mochila import Mochila

#importando itens: 
from ItemsClasses.Halter import Halter
from ItemsClasses.Anilha import Anilha
from ItemsClasses.Frango import Frango
from ItemsClasses.Batata import Batata
from ItemsClasses.Seringa import Seringa

#iniciando o  pygame
pygame.init()

player_bag = Mochila()
print(player_bag.get_mochila())

GAME_NAME = "Hypertro.py: Em busca do shape"

#definindo o tamanho da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#definindo o nome da janela
pygame.display.set_caption(GAME_NAME)

#variavel que vai controlar o framerate
frame_rate = pygame.time.Clock()

#posição da bolinha (temporário)
object_position_x = 0
object_position_y = 0

#tamanho da plataforma
plataform_width = 640
plataforma_height = 50

#posição do player


#placar e número de falhas
score = 0
fails = 0

#variavel que seta as informações do texto que vai aparecer o placar
#Parâmetros = (nomeDaFonte, tamanho, negrito?, itálico?)
display_text = pygame.font.SysFont('arial', 40, True, True)

items_down_velocity = 1

#função que gera um valor aleatório pra bolinha(temporário)
def generate_random_position():
    global object_position_x
    global object_position_y
    object_position_y = 0
    object_position_x = randint(1, SCREEN_WIDTH)




        


#instanciando grupo de sprites do projeto
player_sprites_group = pygame.sprite.Group()
items_sprites_group = pygame.sprite.Group()

#Instanciando o objeto player
player = Player(SCREEN_HEIGHT, plataforma_height, generate_random_position)
#adicionando o player ao grupo de sprites 
player_sprites_group.add(player)


items_instances = [Halter(), Seringa(), Batata(), Frango(), Anilha()]
items_list = []
for instances in items_instances:
    items_list.append(Item(SCREEN_WIDTH, instances),)
for item in items_list:
    items_sprites_group.add(item)

bg = pygame.image.load("./assets/background2.png")

#while padrão para um jogo do py game(deve ser infinito)
while True:
    #definindo framerate
    frame_rate.tick(500)

    #definindo a cor de fundo com rgb
    screen.fill((255,0,255))
    screen.blit(bg, (0,0))
  

    #mensgem que irá aparecer na tela
    score_message = f'Coletados: {score}'
    fails_message = f'Falhas = {fails}'

    #formatando a mensgem que vai apareer para o formato desejado
    #primeiro parametro é a mensagem, segundo é o anti-alinsign(algo assim)
    #e o tereiro é a cor da imagem
    score_formated_message = display_text.render(score_message, True, (255, 255, 255))
    fails_formated_message = display_text.render(fails_message, True, (255, 0, 0))
    #esse for irá captar todos os eventos que acontecerem
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #ações realizadas ao manter a tecla pressionada
   
     

    #criando a plataforma(temporáro)
    #primeiro parâmetro é onde o nosso objeto será criando
    #segundo parâmetro é a cor
    #terceiro parâmetro é a posição
    #quarto parâmetro é altura e largura
    plataform = pygame.draw.rect(screen, (255, 0 ,0), (
                                        SCREEN_WIDTH-plataform_width, 
                                        SCREEN_HEIGHT-plataforma_height, 
                                        plataform_width, 
                                        plataforma_height))


    #colocando todos os sprites do nosso grupo de sprites na tela
    teste = player_sprites_group.draw(screen)
    teste = items_sprites_group.draw(screen)
    #dando update neles a cada iteração do while
    player_sprites_group.update()
    items_sprites_group.update()


  
    for item in items_sprites_group:
        if player.get_rect().colliderect(item.get_rect()):
            print('Coletou!')
            item.reset()

            items_list[randint(0, len(items_list)-1)].set_start_down(True, 'MAIN')

            score += 1
            player_bag.add_item(item.get_item_type())

    #verificando se a bolinha já chegou ao fim da tela
    if (item.item_fall()):
        print('Não pegou :/')
        fails +=1 
        if(fails >= 3):
            pass
    else:
        object_position_y += 1

   
    #blit é para jogar nossa mensagem do score lá na tela
    #o primeiro parâmetro é a mensagem já formatada
    #e o segundo é a posição
    
    screen.blit(score_formated_message, (370, 40))
    screen.blit(fails_formated_message, (100, 40))
    #esse flip é pra atualizar tudo a cada iteração
    pygame.display.flip()