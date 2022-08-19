import pygame
from sys import exit
from random import randint

pygame.init()

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6

            screen.blit(snail_surface,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}",False,(255,255,255))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    print(current_time)
    return current_time

    

#Okno
screen = pygame.display.set_mode((800,400))

#Title
pygame.display.set_caption("Kundohvízdi")

#Ikona
icon = pygame.image.load("graphics/xdd.png")
pygame.display.set_icon(icon)

#framerate
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
 

#surfaces
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

#text_surface = test_font.render("Zmrde jedem tvrde", False,(255,255,255))
#text_rect = text_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load("players/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800,300))

obstacle_rect_list = []

player_surf = pygame.image.load("players/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load("players/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,250))

game_surf = test_font.render("SRACKOMRDKA", False,(255,255,255))
game_rect = game_surf.get_rect(center = (400,50))

end_surf = test_font.render("Zmackni Enter pro zahajeni nove hry", False,(255,255,255))
end_rect = end_surf.get_rect(center = (400,100))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)




#Main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                game_active = True
                snail_rect.x = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        
        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900,1100),300)))
            

    if game_active:    

                   
#Vykreslení 
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,"#c0e9ec",text_rect)
        #pygame.draw.rect(screen,"#c0e9ec",text_rect,10)
        pygame.draw.circle(screen,"Red",pygame.mouse.get_pos(),25)
        #screen.blit(text_surface,text_rect)
        #screen.blit(snail_surface,snail_rect)
        score = display_score()

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)     

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        
        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:

        final_score_s = test_font.render(f"Tvoje nahovno skore: {score}", False,(255,255,255))
        final_rect = final_score_s.get_rect(center = (400,100))
        screen.fill("Gray")  
        screen.blit(player_stand,player_stand_rect)
        

        if score == 0:
            screen.blit(game_surf,game_rect)
            screen.blit(end_surf,end_rect)
        else:
            screen.blit(final_score_s,final_rect)
    

        
    
    
    pygame.display.update()
    clock.tick(60)
