import pygame
import math
import pygame_menu
from pygame import mixer
pygame.init()

#Constants
skin = ['blue']

difficulty = ['medium']

music1=['yes']

# Crear variables para el tamaño de la pantalla
screen_height = 825 # altura
screen_width = 1280 #anchura

#Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Inicializar una ventana o pantalla para su visualización
screen = pygame.display.set_mode ( [ screen_width , screen_height ] )

font = pygame.font.Font("Best Valentina TTF.ttf",25)# Cargar fuente

clock = pygame.time.Clock( )


def game_over_screen():
    text_gameover = font.render('Game Over',1,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(text_gameover,(screen_width/2 ,screen_height/2 ))
    pygame.display.update()
    pygame.time.wait(2000)
    main_menu()


def game_win_screen():
    text_winner = font.render('Winner!!!!',1,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(text_winner,(screen_width/2 ,screen_height/2 ))
    pygame.display.update()
    pygame.time.wait(3000)
    main_menu()


def start_the_game(skin,music1,difficulty):


    #Musica
    if music1==['yes']:
        mixer.music.load('background.wav')
        mixer.music.play(-1)


    #Tamaño de grilla
    tile_size = 64

    #Tamaño del personaje
    character_scale = 2.6

    heart_size = 20

    #Character 
            


    def rescale( name ,character_scale = character_scale):#x 50 y y 70 para el tamaño del personaje
        image = pygame.image.load( name ) # Pygame.image Cargar una nueva imagen desde un archivo
        return pygame.transform.scale(image , ( image.get_width()*character_scale , image.get_height()*character_scale ) ) # Agrandar imagen en posicion x y y,
    # el metodo get_width sirve para obtener el ancho de la imagen

    #Reescalar el personaje a una resolucion mayor

    if skin == ['blue']:
        sprites_right = [ rescale ( "Character/r0.png" ) , rescale ( "Character/r1.png" ), rescale ( "Character/r2.png ")]

        sprites_up = [ rescale ( "Character/u0.png" ) , rescale ( "Character/u1.png" ), rescale ( "Character/u2.png ") ]

        sprites_left = [ rescale ( "Character/l0.png" ) , rescale ( "Character/l1.png" ), rescale ( "Character/l2.png ") ]

        sprites_down = [ rescale ( "Character/d0.png" ) , rescale ( "Character/d1.png" ) ,rescale ( "Character/d2.png ")]

    elif skin == ['orange']:
        sprites_up = [ rescale ( "Character/0.png" ) , rescale ( "Character/1.png" ), rescale ( "Character/2.png ") ]
        
        sprites_left = [ rescale ( "Character/3.png" ) , rescale ( "Character/4.png" ), rescale ( "Character/5.png ") ]

        sprites_down = [ rescale ( "Character/6.png" ) , rescale ( "Character/7.png" ) ,rescale ( "Character/8.png ")]
        
        sprites_right = [ rescale ( "Character/9.png" ) , rescale ( "Character/10.png" ), rescale ( "Character/11.png ")]
    
    elif skin == ['white']:
        sprites_up = [ rescale ( "Character/0w.png" ) , rescale ( "Character/1w.png" ), rescale ( "Character/2w.png ") ]
        
        sprites_left = [ rescale ( "Character/3w.png" ) , rescale ( "Character/4w.png" ), rescale ( "Character/5w.png ") ]

        sprites_down = [ rescale ( "Character/6w.png" ) , rescale ( "Character/7w.png" ) ,rescale ( "Character/8w.png ")]
        
        sprites_right = [ rescale ( "Character/9w.png" ) , rescale ( "Character/10w.png" ), rescale ( "Character/11w.png ")]


    # Posicion inicial del sprite
    current_sprite = sprites_down

    # .get_rect Devuelve un rectángulo que cubre la superficie de la imagen.
    # Este rectángulo siempre comenzará en (0, 0) con un ancho y alto del mismo tamaño que la imagen.
    sprite_rect = sprites_down [0].get_rect()



    #Tamaño del sprite(cuadrado transparente de la imagen)
    sprite_rect.x = sprites_down[0].get_width() * character_scale
    sprite_rect.y = sprites_down[0].get_width() * character_scale

    #Controla el tamaño de las colisiones,se trabaja con el rect del sprite
    sprite_rect.size=(40,50)
    #Coordenadas iniciales del personaje,se modifica con el metodo .center del sprite rect

    sprite_rect.center=( 100 ,150 )

    # Velocidad del jugador
    speed_x = 0
    speed_y = 0

    general_speed = 4

    #Controlar animaciones
    frame_rate = 0
    current_frame = 0 #El frame actual,por ejemplo imagen 1 2 3













    #Bomb

    #counter = 0

    #Cargar el sprite de la bomba

    bomb_sprite = [ rescale('Bomb/Bomb_0.png',1.5),rescale('Bomb/Bomb_1.png',1.5),
                    rescale('Bomb/0.png',1.5),rescale('Bomb/1.png',1.5),
                    rescale('Bomb/2.png',1.5),rescale('Bomb/3.png',1.5),
                    rescale('Bomb/4.png',1.5),rescale('Bomb/5.png',1.5),
                    rescale('Bomb/6.png',1.5) ]

    #Caracteristicas bomba
    cord = 0 #Inicializar variable cordenadas de la bomba, inicializar para guardar la cordenada del jugador y poner la bomba en esa cordenada
    counter = 2#Del frame 2 en adelante de la animacion de la bomba
    initial = 0#Del frame 0 al 1 de la animacion de la bomba
    put = False #Hay una bomba activa,entonces quiero que no se ponga nada
    bomb_destroyed_block= 0 #solo para guardar valores
    character_bomb_left = 20
    bomb_list=[ initial, counter, put, cord,bomb_destroyed_block,character_bomb_left ]#Todas las caracteristicas de las bombas

    def bomb( bomb_list ): #generacion de la bomba

        if bomb_list[0] <= 2:
            
            bomb_list[0]+=0.03
            bomb_sprite_rect = pygame.Rect( 0, 0, 0, 0 )
            screen.blit( bomb_sprite[ math.floor(bomb_list[0])] , (bomb_list[3][0],bomb_list[3][1]))#Dibujar en pantalla la explosion
            
            return bomb_sprite_rect


        elif bomb_list[1] <= 7 :

            bomb_list[1]+=0.4
            if int( bomb_list[1])== 2:
                bomb_sprite_rect = pygame.Rect(bomb_list[3][0]-20,bomb_list[3][1]-20,100,100)# Rect creado artificialmente
                screen.blit( bomb_sprite[ math.floor(bomb_list[1])] , (bomb_list[3][0],bomb_list[3][1]))# Dibujar en pantalla la explosion
                return bomb_sprite_rect
            else:
                screen.blit( bomb_sprite[ math.floor(bomb_list[1])] , (bomb_list[3][0],bomb_list[3][1]))# Dibujar en pantalla la explosion
                bomb_sprite_rect = pygame.Rect(0,0,0,0)
                return bomb_sprite_rect

        elif bomb_list[1]<=8:#Resetear todos los valores para otra bomba

            bomb_list[0] = 0
            bomb_list[1] = 2
            bomb_list[2] = False
            bomb_sprite_rect = pygame.Rect(0,0,0,0) #Rect creado artificialmente
            
            return bomb_sprite_rect

    #Collision 


    def collision_blocks( collision_tile, sprite_rect, speed_x, speed_y, i=0): # Funcion para detectar collisiones con bloques(personaje)
        
        if  i == len( collision_tile ): #Llega al final de la lista
            return

        if sprite_rect.colliderect( collision_tile[ i ] ):# El sprite rect del personaje colisiona con algun tile que sea considerado bloque       
            sprite_rect.x -= speed_x #La velocidad se contrarresta con el movimiento hacia adelante o al lado
            sprite_rect.y -= speed_y #La velocidad se contrarresta con el movimiento hacia arriba o abajo

        collision_blocks( collision_tile, sprite_rect, speed_x, speed_y,  i + 1)


    def destructive_blocks_collision(block,sprite_rect,speed_x, speed_y):#Collision para los bloques destructibles
        if sprite_rect.colliderect(block):
            sprite_rect.x -= speed_x
            sprite_rect.y -= speed_y
        
    def collision_enemies(enemy_rect,sprite_rect,speed_x, speed_y,life_character,i=0):#Collision con enemigos
        if i == len(enemy_rect):
            return life_character


        if i < len(enemy_rect):
            if sprite_rect.colliderect(enemy_rect[i][6]):
                sprite_rect.x -= speed_x
                sprite_rect.y -= speed_y
                life_character-= 0.2
                return collision_enemies(enemy_rect,sprite_rect,speed_x, speed_y,life_character,i+1)
            else:
                return collision_enemies(enemy_rect,sprite_rect,speed_x, speed_y,life_character,i+1)
        

    def collision_key(sprite_rect,key_taked,key_rect):#Tomar la llave
        if sprite_rect.colliderect(key_rect):
            key_taked=1
            return key_taked
        else:
            return key_taked
        
    def collision_to_new_level(door_rect,sprite_rect,key_taked,tile_list,collision_tile,level,bomb_list):# Si se tiene la llave y se coloca el jugador en la puerta, salta de nivel

        if door_rect.colliderect(sprite_rect) and key_taked == 1:
            level+=1
        if level == 2:
            if door_rect.colliderect(sprite_rect) and key_taked == 1 :
                sprite_rect.center=( 100 ,170 )
                tile_list,collision_tile = load_tile (tile_list=[] , i=0 , j=0 , level_world = level2 , row_count=0,col_count=0,collision_tile=[] )
                key_taked = 0
                bomb_list[5 ]=20
                return tile_list,collision_tile,key_taked,level,bomb_list
            else:
                return tile_list,collision_tile,key_taked,level,bomb_list
        elif level == 3:
            if door_rect.colliderect(sprite_rect) and key_taked == 1 :
                sprite_rect.center=( 100 ,170 )
                tile_list,collision_tile = load_tile (tile_list=[] , i=0 , j=0 , level_world = level3 , row_count=0,col_count=0,collision_tile=[] )
                key_taked = 0
                bomb_list[5]=20
                return tile_list,collision_tile,key_taked,level,bomb_list
            else:
                return tile_list,collision_tile,key_taked,level,bomb_list
        else:
            return tile_list,collision_tile,key_taked,level,bomb_list
        


    

    #Destructive blocks


    destructive_block = pygame.image.load ('Block/block_destroyer.png')
    destructive_block = pygame.transform.scale(destructive_block,(tile_size,tile_size) )
    blocks = [[1,10],[1,8],[1,6],[1,4],[3,10],[3,8],[3,6],[3,4],[3,2],[5,10],[5,8],[5,6],[5,4],[5,2],[7,10],[7,8],[7,6],[7,4],[7,2],[9,10],[9,8],[9,6],[9,4],[9,2],[11,2],[11,10],[11,8],[11,6],[11,4],[11,2],[13,10],[13,8],[13,6],[13,4],[13,2],[15,10],[15,8],[15,6],[15,4],[15,2],[17,10],[17,8],[17,6],[17,4],[17,2],[18,9],[18,7],[18,5],[18,3],[2,11],[4,11],[6,11],[8,11],[10,11],[12,11],[14,11],[16,11],[18,11]  ]

    blocks2 = [[1,10],[1,8],[1,6],[1,4],[3,10],[3,8],[3,6],[3,4],[3,2],[5,10],[5,8],[5,6],[5,4],[5,2],[7,10],[7,8],[7,6],[7,4],[7,2],[9,10],[9,8],[9,6],[9,4],[9,2],[11,2],[11,10],[11,8],[11,6],[11,4],[11,2],[13,10],[13,8],[13,6],[13,4],[13,2],[15,10],[15,8],[15,6],[15,4],[15,2],[17,10],[17,8],[17,6],[17,4],[17,2],[17,9],[17,7],[17,5],[17,3],[18,9],[18,7],[18,5],[18,3]  ]

    blocks3 = [[1,10],[1,8],[1,6],[1,4],[3,10],[3,8],[3,6],[3,4],[3,2],[5,10],[5,8],[5,6],[5,4],[5,2],[7,10],[7,8],[7,6],[7,4],[7,2],[9,10],[9,8],[9,6],[9,4],[9,2],[11,2],[11,10],[11,8],[11,6],[11,4],[11,2],[13,10],[13,8],[13,6],[13,4],[13,2],[15,10],[15,8],[15,6],[15,4],[15,2],[17,10],[17,8],[17,6],[17,4],[17,2],[18,9],[18,7],[18,5],[18,3],[2,11],[4,11],[6,11],[8,11],[10,11],[12,11],[14,11],[16,11],[18,11]  ]

    block_rect= []

    def block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect=[],i=0):#Retorna los rects de los blocks para luego procesar las colisiones

        if i>=len(blocks): # Si no hay elementos que devuelva nada
            return block_rect 
        
        # Perform an action on the first block (replace with your actual logic)
        if i< len(blocks):
            block_rect.append( destructive_block_generate(blocks[i][0], blocks[i][1])      ) # Pasa coordenas(de la lista que contiene listas de posiciones en x y {y}) a la funcion que genera los bloques

        return block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect,i+1)#Vuelva a llamar al siguiente par de coordenas y asi sucesivamente



    def block_from_list_charge(blocks, sprite_rect, speed_x, speed_y,block_rect,i=0): # Genera las imagenes de los bloques destructibles
    
        if i>=len(blocks): # Si no hay elementos que devuelva nada
            
            return block_rect
        
        if i< len(blocks):
            block_rect = destructive_block_generate(blocks[i][0], blocks[i][1])      # Pasa coordenas(de la lista que contiene listas de posiciones en x y {y}) a la funcion que genera los bloques

            destructive_block_generate(blocks[i][0], blocks[i][1])# Pasa coordenas(de la lista que contiene listas de posiciones en x y {y}) a la funcion que genera los bloques
            destructive_blocks_collision( block_rect, sprite_rect, speed_x, speed_y)#Para colision de bloques generados
            
        return block_from_list_charge(blocks, sprite_rect, speed_x, speed_y,block_rect,i+1)#Vuelva a llamar al siguiente par de coordenas y asi sucesivamente



    def destructive_block_generate(x,y): #Generar bloque destructible en coordenas especificas
        destructive_block_rect = destructive_block.get_rect() #obtener el rect para el bloque
        destructive_block_rect.x = x * tile_size #Hacer del tamaño del tile en x
        destructive_block_rect.y = y * tile_size #Hacer del tamaño del tile en y
        screen.blit(destructive_block,destructive_block_rect ) #Dibujar el bloque en pantalla
        return pygame.Rect(destructive_block_rect ) #Retornar solo el rect de ese bloque destructible

    def destroy_block(bomb_rect, block_rect, blocks, blocks_new=[],bomb_list=bomb_list,score=0):#Esto toma la lista de bloques y sus rects,luego si se detecta colision,en el orden en el que se envia ese bloque no se guarda en la lista y retorna la lista de bloques.
            if block_rect==[]:
                blocks = blocks_new
                blocks_new = []
                return blocks,bomb_list,score

            if block_rect[0].colliderect(bomb_rect):
                score+=500
                return destroy_block(bomb_rect, block_rect[1:], blocks[1:], blocks_new,bomb_list,score)
            
            else:
                blocks_new.append(blocks[0])
                return destroy_block(bomb_rect, block_rect[1:], blocks[1:], blocks_new,bomb_list,score)

    def destroy_enemy(bomb_rect, list_enemy,new_list):#Si una bomba colisiona con un enemigo este muere.
            if list_enemy == []:
                return new_list

            if bomb_rect.colliderect(list_enemy[0][6]):
                return destroy_enemy(bomb_rect,list_enemy[1:],new_list)
            else:
                new_list.append(list_enemy[0])
                return destroy_enemy(bomb_rect,list_enemy[1:],new_list)
                
                





    #Enemies

    #Cada enemigo tiene 3 paramentros
    bat_current_frame = 0 # para saltar a otro fotograma en las animaciones,esto es general para todos por lo que se usa solo
    wolf_current_frame = 0




    #Cargar sprites
    bat_walk_right = [ rescale('Enemies/0.png'  ), rescale('Enemies/1.png' ), rescale('Enemies/2.png'  ), rescale('Enemies/3.png'  )   ]
    bat_walk_left = [ rescale('Enemies/5.png'  ), rescale('Enemies/6.png'), rescale('Enemies/7.png'  ), rescale('Enemies/8.png'  )   ]


    wolf_walk_right = [ rescale('Enemies/wolf0r.png',2  ), rescale('Enemies/wolf1r.png',2 ), rescale('Enemies/wolf2r.png',2  ), rescale('Enemies/wolf3r.png',2  )
                        , rescale('Enemies/wolf4r.png',2 ) , rescale('Enemies/wolf5r.png',2  )]
    wolf_walk_left = [ rescale('Enemies/wolf0.png',2  ), rescale('Enemies/wolf1.png',2 ), rescale('Enemies/wolf2.png',2  ), rescale('Enemies/wolf3.png',2  )
                        , rescale('Enemies/wolf4.png',2 ) , rescale('Enemies/wolf5.png',2  )]





    #Lista con atributos de enemigos
    #Bat current frame,posx,posy,endpos,speed,posx

    if difficulty == ['medium']:
        enemy = [[0,100,130,700,3,100,[]],[0,300,260,600,3,300,[]],[0,300,500,800,3,300,[]]   ]
        
        
        enemy_wolf = [[0,100,600,800,4,100,[]],[0,400,475,800,4,400,[]],[0,300,200,800,4,300,[]]    ]#Crear lista con las caracteristicas de losenemigos lobos.

        
        enemy3 = [[0,100,130,700,3,100,[]],[0,300,260,700,3,300,[]],[0,300,500,700,3,300,[]]   ]

    if difficulty == ['easy']:
        enemy = [[0,100,130,700,2,100,[]],[0,300,260,600,2,300,[]],[0,300,500,800,2,300,[]]   ]
        
        
        enemy_wolf = [[0,100,600,800,3,100,[]],[0,300,200,800,3,300,[]]    ]#Crear lista con las caracteristicas de losenemigos lobos.

        
        enemy3 = [[0,100,130,700,3,100,[]],[0,300,260,700,3,300,[]]   ]
    
    
    
    #Bat current frame,posx,posy,endpos,speed,posx

    if difficulty == ['hard']:
        enemy = [[0,300,260,300,6,550,[]],[0,300,500,600,6,300,[]] ,[0,500,700,900,6,300,[]],[0,500,400,900,6,300,[]]  ]
            
            
        enemy_wolf = [[0,100,600,800,7,100,[]],[0,400,475,800,7,400,[]],[0,300,200,800,7,300,[]],[0,300,700,800,7,300,[]]    ]#Crear lista con las caracteristicas de losenemigos lobos.

            
        enemy3 = [ [0,100,130,550,6,100,[]],[0,300,260,300,6,550,[]],[0,300,500,600,6,300,[]],[0,100,130,550,6,100,[]],[0,100,130,550,6,100,[]]  ]
    #Generador de enemigos



    def bat_enemy(list,i=0):#lista con atributos para generar enemigos
        if i == len(list):
            return list

        if i<len(list):
            list[i][0]+= 0.1
            list[i][0],list[i][1],list[i][4],list[i][5],list[i][6 ]= bat_enemy_aux(list[i][0],list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6])
            return bat_enemy(list,i+1)



    def bat_enemy_aux( bat_current_frame, x, y, end_x, speed_vat , start_pos,bat_enemy_rect):#Esta crea el enemigo en si

        #Velocidad del murcielago

        x = x + speed_vat 
        
        y = y + speed_vat # se tiene que crear el y personalido y devolver el 'y'

        if x > end_x:# si la pos es mayor a la especificada entonces el murcielago se devuelve
            speed_vat = -speed_vat
        if x < start_pos:# En caso de que la sea menor que el punto en el que inicia,se devuelve haciendo el movimiento un bucle
            speed_vat = -speed_vat

        if speed_vat > 0:
            current_sprite_bat = bat_walk_right

        elif speed_vat < 0:
            current_sprite_bat = bat_walk_left

        if bat_current_frame >= len( current_sprite_bat ):
            bat_current_frame = 0
        if bat_current_frame == 3:
            bat_current_frame = 0

        bat_enemy_rect= pygame.Rect(x,y,40,30)

        screen.blit( current_sprite_bat[ int( bat_current_frame ) ]  ,( x , y ) ) 

        return bat_current_frame,  x , speed_vat, start_pos,bat_enemy_rect



    #Bat current frame,posx,posy,endpos,speed,posx

    def wolf_enemy(list,i=0):#Carga los lobos,de la lista con sus atributos
        if i == len(list):
            return list

        if i<len(list):
            list[i][0]+= 0.1
            list[i][0],list[i][1],list[i][4],list[i][5],list[i][6 ]= wolf(list[i][0],list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6])
            return wolf_enemy(list,i+1)

    


    def wolf( wolf_current_frame, x, y, end_x, speed_wolf , start_pos,wolf_rect):#Este crea 1 enemigo lobo

        #Velocidad del lobo
        x = x + speed_wolf 
        
        y = y + speed_wolf # se tiene que crear el y personalido y devolver el 'y'

        if x > end_x: # si la pos en x es mayor a la especificada entonces el lobo se devuelve
            speed_wolf = -speed_wolf
        if x < start_pos:
            speed_wolf = -speed_wolf

        if speed_wolf > 0:
            current_sprite_wolf = wolf_walk_right
        elif speed_wolf < 0:
            current_sprite_wolf = wolf_walk_left

        wolf_rect= pygame.Rect(x,y,60,40)

        if wolf_current_frame >= len( current_sprite_wolf ):
            wolf_current_frame = 0
        if wolf_current_frame == 5:
            wolf_current_frame = 0

        screen.blit( current_sprite_wolf[ int( wolf_current_frame ) ]  ,( x , y ) ) 

        return wolf_current_frame,  x , speed_wolf, start_pos,wolf_rect

    
    #Keys


    key_taked=0

    def key_generator(x,y,key_taked):#Generador de llave,retorna el rect
        key_img = pygame.image.load("Key/key.png")
        key_rect = key_img.get_rect()    
        key_rect.x = x * tile_size
        key_rect.y = y * tile_size
        
        if key_taked == 0:
            screen.blit(key_img,key_rect)
            return key_rect
        else:
            return key_rect
        

    def door_generator(x,y,key_taked):#Generador puerta,retorna el door_rect
        door_img = pygame.image.load( "Key/door.png" )
        door_img = pygame.transform.scale( door_img , ( door_img.get_width() * character_scale , door_img.get_width() * character_scale  )  )
        door_rect = door_img.get_rect()    
        door_rect.x = x * tile_size
        door_rect.y = y * tile_size
        screen.blit( door_img, door_rect )
        return door_rect
            





    #Levels


    level=1



    level1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [5, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 2, 17, 18, 17, 2, 1, 1, 2, 17, 18, 2, 2, 17, 18, 2, 1, 2, 2, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [3, 2, 39, 1, 39, 2, 39, 18, 39, 2, 39, 18, 39, 2, 39, 18, 39, 1, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 17, 1, 18, 17, 18, 18, 1, 18, 1, 2, 18, 17, 18, 1, 2, 1, 18, 17, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 17, 39, 1, 39, 2, 39, 2, 39, 17, 39, 18, 39, 18, 39, 2, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 17, 2, 2, 1, 2, 1, 2, 18, 17, 18, 1, 18, 17, 2, 18, 18, 2, 17, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 2, 39, 17, 39, 1, 39, 2, 39, 18, 39, 18, 39, 1, 39, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 2, 18, 17, 2, 1, 1, 2, 18, 18, 1, 2, 1, 17, 1, 1, 1, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 18, 39, 18, 39, 1, 39, 18, 39, 18, 39, 2, 39, 17, 39, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [3, 2, 1, 18, 1, 1, 1, 17, 18, 1, 17, 17, 17, 2, 18, 1, 2, 1, 2, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 18, 1, 17, 1, 18, 17, 17, 2, 1, 18, 17, 1, 18, 1, 2, 17, 1, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [21, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]


    level2=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
            [5, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 195, 150, 196, 195, 149, 149, 149, 150, 150, 149, 149, 149, 149, 150, 149, 149, 150, 149, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 195, 150, 196, 196, 149, 150, 154, 155, 149, 196, 149, 149, 149, 149, 154, 155, 149, 150, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 149, 150, 196, 154, 155, 149, 170, 171, 149, 149, 196, 195, 196, 195, 170, 171, 149, 149, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 195, 195, 195, 170, 171, 150, 150, 149, 149, 195, 196, 149, 195, 195, 196, 149, 149, 150, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 195, 149, 150, 150, 196, 150, 149, 195, 150, 150, 154, 155, 149, 149, 150, 195, 195, 149, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 196, 150, 195, 195, 195, 149, 196, 195, 149, 150, 170, 171, 195, 149, 149, 149, 149, 150, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20],
    [20, 196, 196, 150, 154, 155, 150, 196, 195, 149, 154, 155, 150, 195, 195, 154, 155, 149, 149, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
    [20, 149, 149, 196, 170, 171, 150, 150, 149, 150, 170, 171, 149, 195, 196, 170, 171, 149, 150, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20],
    [20, 149, 149, 196, 170, 171, 150, 150, 149, 150, 170, 171, 149, 195, 196, 170, 171, 149, 150, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 20],
    [20, 150, 149, 149, 150, 150, 149, 150, 150, 149, 150, 149, 150, 150, 150, 149, 150, 150, 150, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
        [21, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 20]]



    level3=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [5, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 2, 18, 18, 17, 2, 1, 1, 2, 17, 18, 2, 2, 17, 18, 2, 1, 2, 2, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [3, 2, 39, 1, 39, 2, 39, 18, 39, 2, 39, 18, 39, 2, 39, 18, 39, 1, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 17, 1, 18, 17, 18, 18, 1, 18, 1, 2, 18, 17, 18, 1, 2, 1, 18, 17, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 17, 39, 1, 39, 2, 39, 2, 39, 17, 39, 18, 39, 18, 39, 2, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 17, 2, 2, 1, 2, 1, 2, 18, 17, 18, 1, 18, 17, 2, 18, 18, 2, 17, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 2, 39, 17, 39, 1, 39, 2, 39, 18, 39, 18, 39, 1, 39, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 2, 18, 17, 2, 1, 1, 2, 18, 18, 1, 2, 1, 17, 1, 1, 1, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 1, 39, 18, 39, 18, 39, 1, 39, 18, 39, 18, 39, 2, 39, 17, 39, 2, 1, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [3, 2, 1, 18, 1, 1, 1, 17, 18, 1, 17, 17, 17, 2, 18, 1, 2, 1, 2, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [3, 18, 1, 17, 1, 18, 17, 17, 2, 1, 18, 17, 1, 18, 1, 2, 17, 1, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [21, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]]






    #Imagenes de los tiles

    tile_1 = pygame.image.load('Tiles/_01.png')
    tile_2 = pygame.image.load('Tiles/_02.png')
    tile_3 = pygame.image.load('Tiles/_03.png')
    tile_4 = pygame.image.load('Tiles/_04.png')
    tile_5 = pygame.image.load('Tiles/_05.png')
    tile_6 = pygame.image.load('Tiles/_06.png')
    tile_17 = pygame.image.load('Tiles/_17.png')
    tile_18 = pygame.image.load('Tiles/_18.png')
    tile_20 = pygame.image.load('Tiles/_20.png')
    tile_21 = pygame.image.load('Tiles/_21.png')
    tile_22 = pygame.image.load('Tiles/_22.png')
    tile_24 = pygame.image.load('Tiles/_24.png')
    tile_32 = pygame.image.load('Tiles/_32.png')
    tile_33 = pygame.image.load('Tiles/_33.png')
    tile_34 = pygame.image.load('Tiles/_34.png')
    tile_37 = pygame.image.load('Tiles/_37.png')
    tile_39 = pygame.image.load('Tiles/_39.png')
    tile_48 = pygame.image.load('Tiles/_48.png')
    tile_49 = pygame.image.load('Tiles/_49.png')
    tile_50 = pygame.image.load('Tiles/_50.png')
    tile_51 = pygame.image.load('Tiles/_51.png')
    tile_52 = pygame.image.load('Tiles/_52.png')
    tile_53 = pygame.image.load('Tiles/_53.png')
    tile_54 = pygame.image.load('Tiles/_54.png')
    tile_55 = pygame.image.load('Tiles/_55.png')
    tile_65 = pygame.image.load('Tiles/_65.png')
    tile_66 = pygame.image.load('Tiles/_66.png')
    tile_67 = pygame.image.load('Tiles/_67.png')
    tile_68 = pygame.image.load('Tiles/_68.png')
    tile_69 = pygame.image.load('Tiles/_69.png')
    tile_70 = pygame.image.load('Tiles/_70.png')
    tile_71 = pygame.image.load('Tiles/_71.png')
    tile_72 = pygame.image.load('Tiles/_72.png')
    tile_82 = pygame.image.load('Tiles/_70.png')
    tile_148 = pygame.image.load('Tiles/_148.png')
    tile_149 = pygame.image.load('Tiles/_149.png')
    tile_150 = pygame.image.load('Tiles/_150.png')
    tile_154 = pygame.image.load('Tiles/_154.png')
    tile_155 = pygame.image.load('Tiles/_155.png')
    tile_170 = pygame.image.load('Tiles/_170.png')
    tile_171 = pygame.image.load('Tiles/_171.png')
    tile_195 = pygame.image.load('Tiles/_195.png')
    tile_196 = pygame.image.load('Tiles/_196.png')


    row_count = 0 # Numero de filas en pantalla
    col_count = 0 # Numero de columnas en pantalla
    level_world=level1
    i=0 #Numero de fila del nivel a cargar.
    j=0 #Numero de columna del nivel a cargar.
    tile_list=[]
    collision_tile=[]

    #Esta funcion lee una lista con listas,y crea el mundo,lee la lista de los tiles,luego carga esos tiles especifico en el mapa, lo que hace en escencia es
    #cargar el tile en una fila y columna especifico,empezando desde el inicio,esta funcion crea el tile el cual tiene la surface(imagen) y el rect de esa imagen,luego
    #se crea una lista en la que se guardan esas dos variables,la cual se manda a otra funcion que hace el procesamiento de esos tiles, para dibujar el mapa en pantalla
    def load_tile( tile_list, i, j, level_world, row_count , col_count, collision_tile):

        if i == ( len( level_world ) ):
            return tile_list,collision_tile

        

        if i < (len(level_world )) : 
                
            if level_world[i][j] in [1,2,3,4,5,6,17,18,20,21,22,24,32,33,34,37,39,49,50,51,52,53,54,55,65,66,67,68,69,70,71,72,82,148,149,150,154,155,170,171,195,196]:    
                if level_world[i][j] == 1:
                    tile = img_tyle(tile_1,col_count,row_count)

                if level_world[i][j] == 2:
                    tile = img_tyle(tile_2,col_count,row_count)

                if level_world[i][j] == 3:
                    tile = img_tyle(tile_3,col_count,row_count)
                    collision_tile.append( list(tile[1]) )#El tile tiene dos retornos,el img y el rect de la imagen,el que se guarda es el del rect de la imagen,en este caso el del tile

                if level_world[i][j] == 4:
                    tile = img_tyle(tile_4,col_count,row_count)

                if level_world[i][j] == 5:
                    tile = img_tyle(tile_5,col_count,row_count)
                    collision_tile.append( list(tile[1]) )

                if level_world[i][j] == 6:

                    tile = img_tyle(tile_6,col_count,row_count)
                if level_world[i][j] == 17:

                    tile = img_tyle(tile_17,col_count,row_count)    
                if level_world[i][j] == 18:

                    tile = img_tyle(tile_18,col_count,row_count)
                if level_world[i][j] == 20:

                    tile = img_tyle(tile_20,col_count,row_count)
                    collision_tile.append( list(tile[1]) )

                if level_world[i][j] == 21:
                    tile = img_tyle(tile_21,col_count,row_count)

                if level_world[i][j] == 22:
                    tile = img_tyle(tile_22,col_count,row_count)

                if level_world[i][j] == 24:
                    tile = img_tyle(tile_24,col_count,row_count)
                
                if level_world[i][j] == 32:
                    tile = img_tyle(tile_32,col_count,row_count)

                if level_world[i][j] == 33:
                    tile = img_tyle(tile_33,col_count,row_count)

                if level_world[i][j] == 34:
                    tile = img_tyle(tile_34,col_count,row_count)

                if level_world[i][j] == 37:
                    tile = img_tyle(tile_37,col_count,row_count)
                    collision_tile.append( list(tile[1]) )

                if level_world[i][j] == 39:
                    tile = img_tyle(tile_39,col_count,row_count)
                    collision_tile.append( list(tile[1]) )

                if level_world[i][j] == 49:
                    tile = img_tyle(tile_49,col_count,row_count)

                if level_world[i][j] == 50:
                    tile = img_tyle(tile_50,col_count,row_count)

                if level_world[i][j] == 51:
                    tile = img_tyle(tile_51,col_count,row_count)

                if level_world[i][j] == 52:
                    tile = img_tyle(tile_52,col_count,row_count)

                if level_world[i][j] == 53:
                    tile = img_tyle(tile_53,col_count,row_count)

                if level_world[i][j] == 54:
                    tile = img_tyle(tile_54,col_count,row_count)

                if level_world[i][j] == 55:
                    tile = img_tyle(tile_54,col_count,row_count)

                if level_world[i][j] == 65:
                    tile = img_tyle(tile_65,col_count,row_count)

                if level_world[i][j] == 66:
                    tile = img_tyle(tile_66,col_count,row_count)

                if level_world[i][j] == 67:
                    tile = img_tyle(tile_67,col_count,row_count)
                    collision_tile.append( list(tile[1]) )

                if level_world[i][j] == 68:
                    tile = img_tyle(tile_68,col_count,row_count)

                if level_world[i][j] == 69:
                    tile = img_tyle(tile_69,col_count,row_count)

                if level_world[i][j] == 70:
                    tile = img_tyle(tile_70,col_count,row_count)

                if level_world[i][j] == 71:
                    tile = img_tyle(tile_71,col_count,row_count)

                if level_world[i][j] == 72:
                    tile = img_tyle(tile_69,col_count,row_count)

                if level_world[i][j] == 82:
                    tile = img_tyle(tile_82,col_count,row_count)

                if level_world[i][j] == 148:
                    tile = img_tyle(tile_148,col_count,row_count)
                
                if level_world[i][j] == 149:
                    tile = img_tyle(tile_149,col_count,row_count)
                
                if level_world[i][j] == 150:
                    tile = img_tyle(tile_150,col_count,row_count)
                
                if level_world[i][j] == 154:
                    tile = img_tyle(tile_154,col_count,row_count)

                if level_world[i][j] == 155:
                    tile = img_tyle(tile_155,col_count,row_count)

                if level_world[i][j] == 170:
                    tile = img_tyle(tile_170,col_count,row_count)
                
                if level_world[i][j] == 171:
                    tile = img_tyle(tile_171,col_count,row_count)

                if level_world[i][j] == 195:
                    tile = img_tyle(tile_195,col_count,row_count)
                
                if level_world[i][j] == 196:
                    tile = img_tyle(tile_195,col_count,row_count)

                tile_list.append(tile) #Agrega el tile al tile list

                if j < len(level_world[i] )-1:#las filas dentro del level_world[i],esto recorre todas las filas 
                    return load_tile(tile_list , i , j + 1 , level_world , row_count ,col_count + 1,collision_tile ) # Posicion del tile en el screen,row en que fila,col en que columna
                else:
                    return load_tile(tile_list, i + 1, j=0, level_world=level_world, row_count=row_count + 1, col_count=0, collision_tile=collision_tile )
            else:
                if j == len(level_world[i])-1 :
                    return load_tile(tile_list , i+1 , j =0 , level_world=level_world , row_count=0 ,col_count=0, collision_tile=collision_tile )
                else:
                    return load_tile(tile_list , i , j + 1 , level_world , row_count ,col_count + 1, collision_tile )
                    
        

    #Esta funcion devuelve una tupla que contiene la imagen con su respectivo rect y posicion a la vez
    def img_tyle(img,col_count,row_count):
        img = pygame.transform.scale (img,(tile_size , tile_size))
        img_rect = img.get_rect()
        img_rect.x = col_count * tile_size #Acessa al x y lo modifica,esto significa que la imagen se carga en orden de izquieda a derecha,pero tomando en cuenta el tamaño del tile 
        img_rect.y = row_count * tile_size #Aceesa al 'y' y lo modifica
        tile = ( img, img_rect ) #Crea una tupla y almacena la imagen junto con el rect de la imagen
        return tile

    #Dibuja el mundo con tiles,en la lista que se le pasa,tiene la surface en el [i] y el rect en el j
    def draw_World(tile_list,i=0):
        if i< len(tile_list):
            screen.blit( tile_list[i][0], tile_list[i][1] )
            pygame.draw.rect(screen, black ,tile_list[i][1],1 ) #Esta en la superficie, el color (0,0,0) es negro y el 1 al final es el grueso del cuadro que dibuja
            draw_World( tile_list , i + 1)

    #Life

    heart = pygame.image.load('Life/heart.png')
    heart = pygame.transform.scale(heart,(heart_size,heart_size))

    life_character = 15

    def life_drop_bomb(bomb_rect, sprite_rect,life_character):#Choque de la bomba con el jugador,entonces baja vida
        if sprite_rect.colliderect(bomb_rect):
            life_character = life_character - 5
            return life_character
        else:
            return life_character


    running = True

    #Aqui van los niveles

    tile_list,collision_tile = load_tile (tile_list=[] , i=0 , j=0 , level_world = level1 , row_count=0,col_count=0,collision_tile=collision_tile )# Cargar los tile y su respectiva collision,para el primer mundo


    hud = pygame.Surface((2000,63))#Informacion del jugador en pantalla
    hud.fill("darkgrey")




    def screen_text(text, font, pos_x,pos_y ):#Funcion para colocar texto en pantalla
        
        font_text = font.render(text, True, (255,255,255)) #Render del texto
        
        screen.blit( font_text, (pos_x, pos_y))#Salida en pantalla


    block_rect = block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect,i=0) #Generar los block rects de los rompibles,pra el primer nivel,es un incializador

    points = 0



    while running: 

        if level == 4:
           game_win_screen()
           '''with open ('score.txt','w') as score_file:
            def for_read(read,i=0):
                if i == len(read):
                    read.write(points)
                    return 
                if i < len(read):
                    return for_read(read,i+1)
            for_read(score_file)'''
            



        #Timer o cronometro
        time = pygame.time.get_ticks() / 1000 #Debido a que esta en Milisegundos

        for event in pygame.event.get( ):
            if event.type == pygame.QUIT:
                running = False

        #controlar eventos que solo se puedan iniciar una vez

        if level==2:
            blocks=blocks2
        if level==3:
            blocks=blocks3

     

        #Capturar la tecla presionada
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            current_sprite = sprites_right
            current_frame += 0.13
            speed_x = + general_speed#general speed es del player
        else:
            speed_x = 0 #La velocidad al moverse en x se tiene que resetear siempre que no sea al presionar la a

        if key[pygame.K_a]:
            current_sprite = sprites_left
            current_frame += 0.13
            speed_x = -general_speed

        if key[pygame.K_s]:
            current_sprite = sprites_down
            current_frame += 0.13
            speed_y = +general_speed
        
        else:
            speed_y = 0

        if key[pygame.K_w]:
            current_sprite = sprites_up
            current_frame += 0.13#Cada movimiento de sprite dura 0.16
            speed_y = -general_speed

        sprite_rect.x += speed_x
        sprite_rect.y += speed_y
        #Para los tiles del mapa,para detectar la collision entre el player y los tiles que tienen colision

        collision_blocks(collision_tile, sprite_rect, speed_x, speed_y)

        screen.fill( (0 , 150 , 0 ))

        draw_World(tile_list)

        # Para los frames del sprite del personaje principal
        if current_frame >= len( current_sprite ):#current sprite es la lista de los sprites(son 4), current frame para ir sumando +0.13 para cambiar el frame,es decir 4 veces se presiona y se cambia de sprite al siguiente,cuando llega al 4 se hace reinicia el sprite
            current_frame = 0

        if current_frame == 3:
            current_frame = 0
        
        
        #Escritura de texto en pantalla

        screen.blit(hud,(0,0))#Dibujar el cuadro del hud en el 0,0
        screen_text( f'Time: {round(time)} s ',font , 30,30)# Se muestra el texto en pantalla,el round es para quitar los milisengundos y que de un numero entero
        screen_text( f'Score: {points} ',font , 400,30)
        screen_text( f'Bombs: {bomb_list[5]} ',font , 700,30)

        if key_taked == 0:
            screen_text( f'Key: Not found',font , 200,30)
        if key_taked == 1:
            screen_text( f'Key: Found',font , 200,30)
        
        #Area de corazones
        if life_character <= 0:
            game_over_screen()
        if life_character <=5 and life_character > 0:
            screen.blit(heart, (20,15))

        elif life_character <= 10 and life_character > 5:
            screen.blit(heart, (20,15))
            screen.blit(heart, (40,15))
        
        elif life_character <= 15 and life_character >10:
            screen.blit(heart, (20,15))
            screen.blit(heart, (40,15))
            screen.blit(heart, (60,15))

        # screen.blit para salidas en pantalla

        screen.blit( current_sprite[ int( current_frame) ] , sprite_rect )#Esto hace que el sprite presente se ejecute en secuencia,depende del current_frame.

        if key[pygame.K_SPACE] or bomb_list[2]==True:#Colocar bombas
            if bomb_list[5]>=0:
                bomb_list[2] = True   # Esta colocada la bomba 
                bomb_rect = bomb(bomb_list)#llama a la funcion que crea la bomba
                if bomb_list[1]==2.4:# Solo ocurre si llega a ese fotograma
                    bomb_list[5]= bomb_list[5]-1
                    blocks,bomb_list[4],points = destroy_block(bomb_rect,block_rect,blocks,blocks_new=[],score=points)
                    block_rect = [ ]
                    block_rect = block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect,i=0) #Generar los block rects de los rompibles
                    life_character = life_drop_bomb(bomb_rect,sprite_rect,life_character)
                    if level ==1:
                        enemy = destroy_enemy(bomb_rect,list_enemy,new_list=[])
                    if level == 2 :
                        enemy_wolf = destroy_enemy(bomb_rect,list_enemy_wolf,new_list=[])
                    if level ==3:
                        enemy3 = destroy_enemy(bomb_rect,list_enemy,new_list=[])
            elif bomb_list[5] and key_taked==False:
                game_over_screen()

        elif bomb_list[2] == False:
            bomb_list[3] =  [sprite_rect.x, sprite_rect.y]#Si no se colo ca la bomba se actualiza siempre la posicion del jugador

        if level == 2: #Genera los rects del nuevo nivel
                blocks2 = blocks
                block_rect = block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect=[],i=0) #Generar los block rects de los rompibles            
        elif level == 3:
                blocks3 = blocks
                block_rect = block_list_generate(blocks, sprite_rect, speed_x, speed_y,block_rect=[],i=0) #Generar los block rects de los rompibles



        if level == 1:#Generar llaves y puertas
            key_rect = key_generator(5,10,key_taked)#Generador de llave
            door_rect = door_generator(9,8,key_taked)#generador puerta

        elif level == 2:

            key_rect = key_generator(15,10,key_taked)#Generador de llave
            door_rect = door_generator(11,8,key_taked)

        elif level == 3:
            key_rect = key_generator(13,10,key_taked)#Generador de llave
            door_rect = door_generator(7,2,key_taked)

        block_from_list_charge(blocks, sprite_rect ,speed_x ,speed_y,block_rect) #Dibujar los cuadros destructibles

        key_taked = collision_key(sprite_rect,key_taked,key_rect)

        tile_list,collision_tile,key_taked,level,bomb_list = collision_to_new_level(door_rect,sprite_rect,key_taked,tile_list,collision_tile,level,bomb_list)
        
        
        if level == 1:
            list_enemy = bat_enemy(enemy)
            life_character = collision_enemies(list_enemy,sprite_rect ,speed_x,speed_y,life_character )


        if level == 2:

            list_enemy_wolf = wolf_enemy(enemy_wolf)
            life_character = collision_enemies(list_enemy_wolf,sprite_rect ,speed_x,speed_y,life_character )

        if level == 3:
            list_enemy = bat_enemy(enemy3)
            life_character = collision_enemies(list_enemy,sprite_rect ,speed_x,speed_y,life_character )

            


        # Actualizar pantalla
        pygame.display.flip()

        #FPS
        clock.tick(60)



def change_skin(value, value1):#seleccion de menu de skin
    skin[0] = value1

def change_difficulty(value, value1):#seleccion de menu de dificultad
    difficulty[0] = value1
 
def music(value, value1):#seleccion de menu de musica
    music1[0] = value1

def main_menu():

    about = ['Nombre: Isaac Valle Granados',
             'Asignatura: Taller programacion',
             'Carrera:Ingenieria en computadores',
                '2024',
                'Profesor Leonardo Araya',
                'Costa Rica',
                'Version 0.1',
                'El personaje se mueve con las teclas w,a,s,d y coloca bombas con space, el objetivo del juego es encontrar la llave y pasar el nivel dirigiendose a la puerta',
                'Los enemigos no tienen colisiones en el mapa debido a que se espera tengan una ventaja frente al jugador,ademas se pueden eliminar con bombas']
    
    surface = pygame.display.set_mode((1280, 800))# crear ventana para el menu


    menu = pygame_menu.Menu('Welcome to bomberman vintage,from Isaac Valle Granados Group 3',
                             1280, 
                             800,
                        theme=pygame_menu.themes.THEME_SOLARIZED	)

    menu.add.text_input('Name :', default='Bomberman')#Entrada de texto
    menu.add.button('Play', start_the_game, skin, music1, difficulty)#Presionar para jugar


    menu.add.selector('Select skin ',
                           [('Blue', 'blue'),
                            ('Orange', 'orange'),
                            ('White', 'white')],
                           onchange=change_skin,
                           selector_id='select_skin')
    
    menu.add.selector('Select difficulty ',
                           [('Medium', 'medium'),
                            ('Easy', 'easy'),
                            ('Hard', 'hard')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')
    
    menu.add.selector('Music',
                      [('No','no'),
                       ('Yes','yes')],
                       onchange=music,
                        selector_id='music'
                      )
    
    about_menu = pygame_menu.Menu(
        height=800,
        theme=pygame_menu.themes.THEME_SOLARIZED,
        title='Submenu',
        width=1280
    )

    menu.add.button('About', about_menu)#Presionar para jugar

    about_menu.add.label(about[0], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[1], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[2], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[3], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[4], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[5], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[6], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[7], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)
    about_menu.add.label(about[8], align=pygame_menu.locals.ALIGN_LEFT, font_size=20)

    about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to main menu', pygame_menu.events.RESET)


    menu.add.button('Quit', pygame_menu.events.EXIT)



    menu.mainloop(surface)




main_menu()#Llamar al menu principal