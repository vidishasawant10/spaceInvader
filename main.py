import pygame
# initialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space.png")
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 510
playerX_change = 0

def player(x,y):
    screen.blit(playerimg, (x, y))

# game loop
running = True
while running:
    screen.fill((20, 50, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >= 769:
        playerX = 769

    player(playerX, playerY)
    pygame.display.update()



