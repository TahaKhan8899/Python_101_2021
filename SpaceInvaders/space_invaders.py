import pygame
import random

pygame.init()

# create screen (w, h)
screen = pygame.display.set_mode((800, 600))

# load background image
background = pygame.image.load('/Users/tahakhan/PycharmProjects/python101/SpaceInvaders/images/background.png')

# load player image and assign other variable for it
playerImg = pygame.image.load('/Users/tahakhan/PycharmProjects/python101/SpaceInvaders/images/player.png')
playerX = 370
playerY = 480
playerX_Change = 0

# load enemy image and assign other variable for it
enemyImg = pygame.image.load('/Users/tahakhan/PycharmProjects/python101/SpaceInvaders/images/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 3
enemyY_Change = 40

# load bullet image and assign other variable for it
bulletImg = pygame.image.load('/Users/tahakhan/PycharmProjects/python101/SpaceInvaders/images/bullet.png')
bulletX = 0
bulletY = 0
bulletY_Change = 40
bulletState = 0


def draw_player(x, y):
    screen.blit(playerImg, (x, y))


def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = 1
    screen.blit(bulletImg, (x + 16, y + 16))


# This is the game loop
running = True
while running:

    # this is the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # check for arrow keys
            if event.key == pygame.K_LEFT:
                playerX_Change = -8
            if event.key == pygame.K_RIGHT:
                playerX_Change = 8
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # place image on the screen
    screen.blit(background, (0, 0))

    # change playerX by the playerX_Change amount and draw it
    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    draw_player(playerX, playerY)

    # move enemy X and check boundaries
    enemyX += enemyX_Change
    if enemyX <= 0 or enemyX > 736:
        enemyX_Change *= -1
        enemyY += enemyY_Change
    draw_enemy(enemyX, enemyY)

    # keep drawing the bullet and moving it upwards if it's in the fire state
    if bulletState == 1:
        bulletY -= bulletY_Change
        fire_bullet(bulletX, bulletY)

    # Must be called to refresh the screen
    pygame.display.update()
