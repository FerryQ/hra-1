import pygame
from sys import exit
from random import randint, choice

class Eliska(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("players/upraveno.png").convert_alpha()
        player_walk_2 = pygame.transform.rotozoom(player_walk_1,30,1)
        player_walk_3 = pygame.transform.rotozoom(player_walk_1,60,1)
        player_walk_4 = pygame.transform.rotozoom(player_walk_1,90,1)
        player_walk_5 = pygame.transform.rotozoom(player_walk_1,120,1)
        player_walk_6 = pygame.transform.rotozoom(player_walk_1,150,1)
        player_walk_7 = pygame.transform.rotozoom(player_walk_1,180,1)
        player_walk_8 = pygame.transform.rotozoom(player_walk_1,210,1)
        player_walk_9 = pygame.transform.rotozoom(player_walk_1,240,1)
        player_walk_10 = pygame.transform.rotozoom(player_walk_1,270,1)
        player_walk_11 = pygame.transform.rotozoom(player_walk_1,300,1)
        player_walk_12 = pygame.transform.rotozoom(player_walk_1,330,1)
        player_walk_13 = pygame.transform.rotozoom(player_walk_1,360,1)
        self.player_walk = [player_walk_1,player_walk_2,player_walk_3,player_walk_4,player_walk_5,player_walk_6,player_walk_7,player_walk_8,player_walk_9,player_walk_10,player_walk_11,player_walk_12,player_walk_13]

        self.player_jump = pygame.image.load("players/hop.png").convert_alpha()
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (100,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("hudba/hophop.mp3")
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("players/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("players/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("players/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("hudba/hophop.mp3")
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == "fly":
            fly_frame_1 = pygame.image.load("players/Fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load("players/Fly2.png").convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load("players/snail1.png").convert_alpha()
            snail_frame_2 = pygame.image.load("players/snail2.png").convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0

        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
    def speed(self):
        self.rect.x -= randint(6,20)
        
    def animation_state(self):
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.speed()
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


pygame.init()



def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}",False,(255,255,255))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    print(current_time)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False) or pygame.sprite.spritecollide(eliska.sprite,obstacle_group,False):
        dead.play()
        obstacle_group.empty()
        return False
    else:
        return True

    

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

obstacle_group = pygame.sprite.Group()

dead = pygame.mixer.Sound("hudba/roblox.mp3")


player = pygame.sprite.GroupSingle()
player.add(Player())

eliska = pygame.sprite.GroupSingle()
eliska.add(Eliska())
 

#surfaces
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

player_stand = pygame.image.load("players/player_walk_1.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_surf = test_font.render("SRACKOMRDKA", False,(255,255,255))
game_rect = game_surf.get_rect(center = (400,50))

end_surf = test_font.render("Zmackni Enter pro zahajeni nove hry", False,(255,255,255))
end_rect = end_surf.get_rect(center = (400,100))
ovladani1 = test_font.render("Hrac 1: mezernik", False,(255,255,255))
ovladani_rect1 = ovladani1.get_rect(bottomleft = (10,350))
ovladani2 = test_font.render("Hrac 2: sipka nahoru", False,(255,255,255))
ovladani_rect2 = ovladani2.get_rect(bottomleft = (10,400))



#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer =  pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer =  pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

hrt = pygame.mixer.Sound("hudba/HRT song.mp3")
hrt.set_volume(0.2)
hrt.play()

g = 0




#Main
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
        
                      
            
        
        if game_active:
            if event.type == obstacle_timer and game_active:
                obstacle_group.add(Obstacle(choice(["fly","snail","snail"])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
                game_active = True
              
                start_time = int(pygame.time.get_ticks() / 1000)
        

            
            

    if game_active:    

                   
#Vykreslení 
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.circle(screen,"Red",pygame.mouse.get_pos(),25)
        score = display_score()

        #Player
        
        
        eliska.draw(screen)
        eliska.update()
        player.draw(screen)
        player.update()


        obstacle_group.draw(screen)
        obstacle_group.update()

        #obstacle movement
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        
        #collision
        game_active = collision_sprite()
        #game_active = collisions(player_rect,obstacle_rect_list)
        
    else:
        #player_rect.bottom(80,300)
        
        

        
        final_score_s = test_font.render(f"Tvoje nahovno skore: {score}", False,(255,255,255))
        final_rect = final_score_s.get_rect(center = (400,100))
        
        screen.fill("Gray")  
        screen.blit(player_stand,player_stand_rect)
        
        
        

        if score == 0:
            screen.blit(game_surf,game_rect)
            screen.blit(end_surf,end_rect)
            screen.blit(ovladani1,ovladani_rect1)
            screen.blit(ovladani2,ovladani_rect2)
        else:
            screen.blit(final_score_s,final_rect)

        
            

        
        

    

        
    
    
    pygame.display.update()
    clock.tick(60)
