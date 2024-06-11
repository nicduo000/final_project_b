import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('skibidi vs ohio')
clock = pygame.time.Clock()

#Background Settings
bg_size = (1200,500)
background = pygame.image.load('/home/pi/p4/graphics /background')
background = pygame.transform.scale(background, bg_size)

#Enemy Settings
s_size = (150,100)
dino = pygame.image.load('/home/pi/p4/graphics /yoshi.png')
dino = pygame.transform.scale(dino, s_size)
pos_dino = 900

#Player Settings
player = pygame.image.load('/home/pi/p4/graphics /mario.png')
ps = (100,100)
player = pygame.transform.scale(player, ps)
player_gravity = 0
player_rect = player.get_rect(midbottom = (100,475))

#Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    	#Controls        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            print('jump')        
    """        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
           print('jump')
    """
    
    #background placement
    screen.blit(background,(-100,0))
    
    #enemy position
    pos_dino -= 10
    screen.blit(dino,(pos_dino,375))
    if pos_dino<-500:
        pos_dino=1000
    
    player_rect.left += 10
    screen.blit(player,player_rect)
    
    pygame.display.update()
    clock.tick(60) 