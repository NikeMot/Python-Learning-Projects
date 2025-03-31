import pygame
import math
from random import randint
from pygame import mixer


# Initialise pygame
pygame.init()

# Create the screen
screen_size = pygame.display.set_mode((800, 600))

# Player image and movement variables
player_image = pygame.image.load("space-ship.png")
player_x = 368
player_y = 472
player_x_change = 0
player_y_change = 0

# Background music
mixer.music.load("retro-streets-28824.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

##Sounds##
#Bullet sound
bullet_sound = mixer.Sound("086409_retro-gun-shot-81545.mp3")
bullet_sound.set_volume(0.5)

#Collision sound
collision_sound = mixer.Sound("retro-explode-2-236688.mp3")
collision_sound.set_volume(0.5)



# Enemy specs
enemy_image = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 6

for enemy in range(number_of_enemies):
    enemy_image.append(pygame.image.load("enemy.png"))
    enemy_x.append(randint(0, 736))
    enemy_y.append(randint(50, 236))
    enemy_x_change.append(1.5)
    enemy_y_change.append(50)

# Bullet image and movement variables
bullet_image = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 0
bullet_x_change = 0
bullet_y_change = 5
bullet_shot = False

# Score specifications
score = 0
score_font = pygame.font.Font("freesansbold.ttf", 32)
score_x = 10
score_y = 10

# Game over text
end_text = pygame.font.Font("freesansbold.ttf", 64)

def game_over():
    final_text = end_text.render("GAME OVER", True, (255, 255, 255))
    screen_size.blit(final_text, (200, 250))
    pygame.display.update()



# Score function
def show_score(x,y):
    text = score_font.render(f"Score :  {score}", True, (255, 255, 255))
    screen_size.blit(text, (x, y))

# Enemy function
def enemy(x,y,e):
    screen_size.blit(enemy_image[e], (x, y))

# Player function
def player(x,y):
    screen_size.blit(player_image, (x, y))

def shoot_bullet(x,y):
    global bullet_shot
    bullet_shot = True
    screen_size.blit(bullet_image, (x + 24, y ))

def collision_detection(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


 # Title and Icon and game assets
pygame.display.set_caption("The Great Space Invaders")
game_icon = pygame.image.load("ufo.png")
pygame.display.set_icon(game_icon)
background_image = pygame.image.load("ultra-detailed-nebula-abstract-wallpaper-4.png")


# Game loop
game_on = True
while game_on:

    # Fill the screen with a background
    screen_size.blit(background_image, (0,0))

    for event in pygame.event.get():

        #Quit game
        if event.type == pygame.QUIT:
            game_on = False

        #Arrow key events - Pressed key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 2.5

            if event.key == pygame.K_UP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player_y_change = 0
                else:
                    player_y_change = -2.5

            if event.key == pygame.K_DOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player_y_change = 0
                else:
                    player_y_change = 2.5

            if event.key == pygame.K_SPACE:

                if not bullet_shot:
                    bullet_sound.play()
                    bullet_x = player_x
                    bullet_y = player_y
                    shoot_bullet(bullet_x, bullet_y)


        #Key events - Released key
        if event.type == pygame.KEYUP:
            player_x_change = 0
            player_y_change = 0

    # Player movement control
    player_x += player_x_change
    player_y += player_y_change

    # Player boundary control - X-axis
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Player boundary control - Y-axis
    if player_y <= 336:
        player_y = 336
    elif player_y >= 536:
        player_y = 536


    # Enemy behaviour
    for ene in range(number_of_enemies):

        # Game over if enemy reaches player
        if collision_detection(enemy_x[ene], enemy_y[ene], player_x, player_y):
            for a in range(number_of_enemies):
                enemy_y[a] = 2000

            game_over()
            pygame.display.update()
            pygame.time.wait(3000)
            game_on = False

        # Enemy movement control
        enemy_x[ene] += enemy_x_change[ene]


        # Enemy boundary control
        if enemy_x[ene] < 0:
            enemy_x[ene] = 0
            enemy_x_change[ene] = 2.5
            enemy_y[ene] += enemy_y_change[ene]

        elif enemy_x[ene] > 736:
            enemy_x[ene] = 736
            enemy_x_change[ene] = -2.5
            enemy_y[ene] += enemy_y_change[ene]

        # Collision detection
        collision = collision_detection(enemy_x[ene], enemy_y[ene], bullet_x, bullet_y)
        if collision:
            collision_sound.play()
            bullet_y = player_y
            bullet_shot = False
            score += 1
            enemy_x[ene] = randint(0, 736)
            enemy_y[ene] = randint(50, 236)

        enemy(enemy_x[ene], enemy_y[ene], ene)


    # Bullet movement:
    if bullet_y <= 16:
        bullet_y = player_y
        bullet_shot = False

    if bullet_shot:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    show_score(score_x, score_y)
    player(player_x, player_y)

    # Update
    pygame.display.update()



