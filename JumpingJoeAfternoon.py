import pygame, sys, random
from Joe2Abstract import *
#initializing pygame
pygame.init()
clock=pygame.time.Clock()

#Screen setup
screen_width=700
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

#colors
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#Images
color_surf=pygame.image.load("assets/a.jpg").convert_alpha()
background_surf=pygame.image.load("assets/environment3.png").convert_alpha()
background_surf.set_alpha(100)
door_open_surf=pygame.image.load("assets/doorOpen.png") 
cloud=pygame.image.load("assets/cloud.png")
cloud.set_alpha(200)
win_surf=pygame.image.load("assets/winscreen.png") 
ground_surf = pygame.image.load("assets/ground.png").convert_alpha()
spikes_surf = pygame.image.load("assets/spikes.png").convert_alpha()
player_surf1 = pygame.image.load("assets/joe1.PNG") 

playerImgHeight=63
playerImgWidth=40
doorHeight=100
doorWidth=100
#Image Scaling
background_surf = pygame.transform.scale(background_surf, (screen_width, 500))
color_surf = pygame.transform.scale(color_surf, (screen_width, screen_height))
door_open_surf=pygame.transform.smoothscale(door_open_surf,(100,100))
cloud = pygame.transform.scale(cloud, (100, 50))

door_surf=door_open_surf
player_surf=pygame.transform.scale(player_surf1, (playerImgWidth, playerImgHeight))
ground_surf = pygame.transform.scale(ground_surf, (screen_width, 90))
spikes_surf = pygame.transform.scale(spikes_surf, (50, 20))

#characters
player_rect=pygame.Rect(100,screen_height-145,40,63)  
ground_rect=pygame.Rect(0,screen_height-100,screen_width,40)
spikes_rect=pygame.Rect(300,screen_height-100,100,20)
door_rect=pygame.Rect(screen_width-150,screen_height-180,doorWidth,doorHeight)

velX=0
velY=0
#font
score_font=pygame.font.Font('freesansbold.ttf', 16)
over_font=pygame.font.Font('freesansbold.ttf', 25)
cloud1X = 50
cloud2X = 300
cloud3X = 550
#Game Loop
while True:
    screen.blit(color_surf, (0, 0))
    screen.blit(background_surf, (0, -150))
    screen.blit(ground_surf, (0, screen_height-90))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velX=-5
            if event.key ==pygame.K_RIGHT:
                velX=5
            if event.key ==pygame.K_UP:
                velY=-5
            if event.key ==pygame.K_DOWN:
                velY=5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                velX=0
            if event.key ==pygame.K_RIGHT:
                velX=0
            if event.key ==pygame.K_UP:
                velY=0
            if event.key ==pygame.K_DOWN:
                velY=0

    
    #moveplayer
    player_rect.x+=velX
    player_rect.y+=velY
    

    cloud1X,cloud2X,cloud3X=game(player_rect,door_rect,over_font,win_surf,screen,playerImgHeight,playerImgWidth,pygame,player_surf,spikes_rect,cloud,cloud1X,cloud2X,cloud3X,screen_width)

    screen.blit(door_surf, door_rect)
    screen.blit(player_surf, player_rect)
    screen.blit(spikes_surf, spikes_rect)
    screen.blit(spikes_surf, (spikes_rect.x+50, spikes_rect.y))
        
    
    pygame.display.flip()
    clock.tick(30)