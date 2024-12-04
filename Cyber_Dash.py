from pygame.sprite import Group
from turtledemo.penrose import start
import pygame
from pygame import display
from sys import exit
from random import randint, choice



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        player_walk1 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_1.png').convert_alpha()
        player_walk2 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_2.png').convert_alpha()
        player_walk3 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_3.png').convert_alpha()
        player_walk4 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_4.png').convert_alpha()
        player_walk5 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_5.png').convert_alpha()
        player_walk6 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_6.png').convert_alpha()
        player_walk7 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_7.png').convert_alpha()
        player_walk8 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_8.png').convert_alpha()
        player_walk9 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_9.png').convert_alpha()
        player_walk10 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_10.png').convert_alpha()

        self.player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8, player_walk9, player_walk10]
        self.player_index = 0
        self.player_jump = pygame.image.load('CS50x_finalProject/graphics/Player/frame_3.png').convert_alpha()



        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('CS50x_finalProject/audio/cartoon_jump.mp3')
        self.jump_sound.set_volume(0.2)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity =- 20
            self.jump_sound.play()

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.2
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]



    def update(self):
        self.player_input()
        self.player_gravity()
        self.animation_state()




class MovingPillar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('CS50x_finalProject/graphics/small_pillar.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
    
    def update(self):
        self.rect.x -= 3.5
        self.destroy()

        if self.rect.x < -500:
            self.respawn()

    
    def destroy(self):
        if self.rect.x <= -550:
            self.kill()
    
    def respawn(self):
        self.rect.x = 800
        self.rect.y = 250 




class MovingPillarAd(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('CS50x_finalProject/graphics/moving_pillar_ad2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
    
    def update(self):
        self.rect.x -= 3.5
        self.destroy()

        if self.rect.x < -500:
            self.respawn()

    
    def destroy(self):
        if self.rect.x <= -550:
            self.kill()
    
    def respawn(self):
        self.rect.x = 799
        self.rect.y = 252


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'Drone':
            drone_frame1 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk1.png').convert_alpha()
            drone_frame2 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk2.png').convert_alpha()
            drone_frame3 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk3.png').convert_alpha()
            drone_frame4 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk4.png').convert_alpha()
            self.frames = [drone_frame1, drone_frame2, drone_frame3, drone_frame4]
            y_pos = 210
        else:
            dragon_frame1 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk1.png').convert_alpha()
            dragon_frame2 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk2.png').convert_alpha()
            dragon_frame3 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk3.png').convert_alpha()
            dragon_frame4 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk4.png').convert_alpha()
            self.frames = [dragon_frame1, dragon_frame2, dragon_frame3, dragon_frame4]
            y_pos = 300


        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.15
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# score func
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = pixel_font.render(f'Score: {current_time}',True, (245,241,227))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time


# obstacle movement logic
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(dragon_surf,obstacle_rect)
            else:
                screen.blit(drone_surf,obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []


# player collision func
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

# player animation func
def player_animation():
    global player_surf, player_index
    #play walking animation if the player is on floor
    if player_rect.bottom < 300:
        #jump
        player_surf = player_jump
    else:
        #walk
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]



# Screen res & basic game logic
pygame.init()
screen = display.set_mode((800, 400))
pygame.display.set_caption('Cyber Dash')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
bg_Music = pygame.mixer.Sound('CS50x_finalProject/audio/dark_wave.mp3')
game_active = bg_Music.play()
bg_Music.set_volume(0.1)



# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

moving_pillar = MovingPillar(800, 300)
sprite_group = pygame.sprite.Group(moving_pillar)

moving_pillar_ad = MovingPillarAd(800, 290)
sprite_group2 = pygame.sprite.Group(moving_pillar_ad)


# Font
pixel_font = pygame.font.Font('CS50x_finalProject/font/CyberpunkCraftpixPixel.otf', 35)
score_font = pygame.font.Font('CS50x_finalProject/font/CyberpunkCraftpixPixel.otf', 20)


# New cursor image
new_cursor = pygame.image.load('CS50x_finalProject/graphics/cursor/new_cursor.png')

# Hide old cursor
pygame.mouse.set_visible(False)



# Backgroud & crosswalk image
sky_surface = pygame.image.load('CS50x_finalProject/graphics/cyber_back5.jpg').convert()
ground_surface = pygame.image.load('CS50x_finalProject/graphics/1.png').convert_alpha()
crosswalk_surface = pygame.image.load('CS50x_finalProject/graphics/crosswalk_pale2.png').convert_alpha()

#vfx background
vfx_back = pygame.image.load('CS50x_finalProject/graphics/vfx_back.png').convert_alpha()

#start screen background
start_screen_back = pygame.image.load('CS50x_finalProject/graphics/back_blur.png').convert()


# Pillars Ads
pillar2_surface = pygame.image.load('CS50x_finalProject/graphics/Pillar2.png').convert_alpha()
pillar2_body_surface = pygame.image.load('CS50x_finalProject/graphics/pillar2_body.png').convert_alpha()
pizzaAd_surface = pygame.image.load('CS50x_finalProject/graphics/pizza_ad.png').convert_alpha()

#small pillar
small_pillar = pygame.image.load('CS50x_finalProject/graphics/small_pillar.png').convert_alpha()
moving_pillar_ad = pygame.image.load('CS50x_finalProject/graphics/moving_pillar_ad2.png').convert_alpha()


#start screen frame
screen_frame = pygame.image.load('CS50x_finalProject/graphics/Logo2.png').convert_alpha()




# dragon model
dragon_frame1 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk1.png').convert_alpha()
dragon_frame2 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk2.png').convert_alpha()
dragon_frame3 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk3.png').convert_alpha()
dragon_frame4 = pygame.image.load('CS50x_finalProject/graphics/dragon/walk4.png').convert_alpha()

dragon_frames = [dragon_frame1, dragon_frame2, dragon_frame3, dragon_frame4]
dragon_frame_index = 0
dragon_surf = dragon_frames[dragon_frame_index]


# Drone model
drone_frame1 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk1.png').convert_alpha()
drone_frame2 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk2.png').convert_alpha()
drone_frame3 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk3.png').convert_alpha()
drone_frame4 = pygame.image.load('CS50x_finalProject/graphics/Drone/drone_walk4.png').convert_alpha()

drone_frames = [drone_frame1, drone_frame2, drone_frame3, drone_frame4]
drone_frame_index = 0
drone_surf = drone_frames[drone_frame_index]


# list for all obstacles
obstacle_rect_list = []


# Player model
player_walk1 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_1.png').convert_alpha()
player_walk2 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_2.png').convert_alpha()
player_walk3 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_3.png').convert_alpha()
player_walk4 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_4.png').convert_alpha()
player_walk5 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_5.png').convert_alpha()
player_walk6 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_6.png').convert_alpha()
player_walk7 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_7.png').convert_alpha()
player_walk8 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_8.png').convert_alpha()
player_walk9 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_9.png').convert_alpha()
player_walk10 = pygame.image.load('CS50x_finalProject/graphics/Player/frame_10.png').convert_alpha()

player_walk = [player_walk1, player_walk2, player_walk3, player_walk4, player_walk5, player_walk6, player_walk7, player_walk8, player_walk9, player_walk10]
player_index = 0
player_jump = pygame.image.load('CS50x_finalProject/graphics/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0


# intro screen
player_stand = pygame.image.load('CS50x_finalProject/graphics/Player/idle_frame_1.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400, 150))


# game name (start screen)
game_name = pixel_font.render('Cyber Dash', True, (255, 191, 0))
game_name_rect = game_name.get_rect(midtop = (400, 30))

# game instructions (start screen)
game_message = pixel_font.render('Press space to run', True, (255,234,0))
game_message_rect = game_message.get_rect(midbottom = (400, 340))

game_message_two = pixel_font.render('Press space to run again!', True, (255,234,0))
game_message_rect_two = game_message_two.get_rect(midbottom = (400, 390))


# timer logic (obstacles & models animations)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

dragon_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(dragon_animation_timer, 400)

drone_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(drone_animation_timer, 200)



# all events logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                   if player_rect.bottom >= 300: player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300: player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time =  int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['Drone', 'dragon', 'dragon', 'dragon'])))

            if event.type == dragon_animation_timer:
                if dragon_frame_index == 0: dragon_frame_index = 1
                else: dragon_frame_index = 0
                dragon_surf = dragon_frames[dragon_frame_index]

            if event.type == drone_animation_timer:
                if drone_frame_index == 0: drone_frame_index = 1
                else: drone_frame_index = 0
                drone_surf = drone_frames[drone_frame_index]


# drawing surfaces & in game logic
    if game_active:
        screen.blit(sky_surface, (0, -100))
        screen.blit(ground_surface, (0, 300))
        screen.blit(crosswalk_surface, (-180, -280))

        screen.blit(pillar2_surface, (600, 267))
        screen.blit(pillar2_body_surface,(581, 165))
        screen.blit(pizzaAd_surface, (585, 176))

        screen.blit(vfx_back,(0,0))
    
        
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Draw new cursor
        screen.blit(new_cursor, pos)



        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        sprite_group.draw(screen)
        sprite_group.update()

        sprite_group2.draw(screen)
        sprite_group2.update()


        game_active = collision_sprite()

        #display func
        score = display_score()


    # start screen
    else:        
        screen.blit(start_screen_back, (-20,-100))
        screen.blit(player_stand, player_stand_rect)

        pos = pygame.mouse.get_pos()
        screen.blit(new_cursor, pos)
        
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        #screen frame
        screen.blit(screen_frame,(223,10))



        score_message = score_font.render(f'Your score: {score}', True, (255,69,0))
        score_message_rect = score_message.get_rect(midbottom = (400, 122))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(game_message_two, game_message_rect_two)

    # update everything, draw all elements & fps lock
    pygame.display.update()
    clock.tick(60)

