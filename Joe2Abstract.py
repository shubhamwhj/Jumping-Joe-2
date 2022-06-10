# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:07:55 2022

@author: Shourabh Verma
"""

def game(player_rect,door_rect,over_font,win_surf,screen,playerImgHeight,playerImgWidth,pygame,player_surf,spikes_rect,cloud,cloud1X,cloud2X,cloud3X,screen_width):
    ###############################################################################

    if(player_rect.colliderect(door_rect)):
        win_text=over_font.render("Winner!", False, (255,0,0))   
        screen.blit(win_surf,[220,100]) 
        playerImgHeight=int(playerImgHeight*0.99)
        playerImgWidth=int(playerImgWidth*0.99)
        player_surf=pygame.transform.scale(player_surf,(playerImgWidth,playerImgHeight) )
        player_rect.x=door_rect.centerx
        player_rect.midbottom=door_rect.midbottom
    
    if(player_rect.colliderect(spikes_rect)):
        win_text=over_font.render("YOU LOST!", False, (255,0,0))
        pygame.quit()
            

###############################################################################

    #display characters
    #pygame.draw.rect(screen,RED, player)
    #pygame.draw.rect(screen,GREEN, door)
    
    screen.blit(cloud, (cloud1X, 50))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud, (cloud2X, 75))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud, (cloud3X, 100))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2
    
    return cloud1X,cloud2X,cloud3X