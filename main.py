import pygame
import random
import math
from pygame import mixer

# initialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("background.jpg")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 510
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 769))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

# bullet
# ready - you can't see the bullet on the screen
# fire - The bullet is currently moving
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 510
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10
overfont = pygame.font.Font('freesansbold.ttf', 64)

winfont = pygame.font.Font('freesansbold.ttf', 50)


def showscore(x, y):
    score_value = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))


def gameovertext():
    over_text = overfont.render("Game Over You lose ", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def winovertext():
    win_text = winfont.render("Game Over You Win ", True, (255, 255, 255))
    screen.blit(win_text, (150, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 10, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletsound = mixer.Sound('laser.wav')
                    bulletsound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 769:
        playerX = 769

    for i in range(no_of_enemies):
        # game over
        if enemyY[i] > 400:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            gameovertext()
            break
        elif score == 100:
            winovertext()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 769:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # collision
        iscollision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if iscollision:
            explosionsound = mixer.Sound('explosion.wav')
            explosionsound.play()
            bulletY = 400
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 769)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)
    # bullet movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()
