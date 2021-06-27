import pygame
import random
from math import *

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
enemyX = []
enemyY = []
enemyX_Change = []
enemyY_Change = 40

# populate the lists with initial values
numberOfEnemies = 6
for i in range(0, numberOfEnemies):
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_Change.append(3)

# load bullet image and assign other variable for it
bulletImg = pygame.image.load('/Users/tahakhan/PycharmProjects/python101/SpaceInvaders/images/bullet.png')
bulletX = 0
bulletY = 0
bulletY_Change = 40
bulletState = 0

score = 0

font = pygame.font.Font('freesansbold.ttf', 32)
fontX = 10
fontY = 10


def drawScore():
    scoreImage = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(scoreImage, (fontX, fontY))


def draw_player(x, y):
    screen.blit(playerImg, (x, y))


def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = 1
    screen.blit(bulletImg, (x + 16, y + 16))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    deltaX = enemyX - bulletX
    deltaY = enemyY - bulletY
    distance = sqrt(deltaX**2 + deltaY**2)

    if distance < 27:
        return True
    return False


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
                if bulletState == 0:
                    bulletX = playerX
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

    # enemy loop
    for enemyNumber in range(0, numberOfEnemies):

        # move enemy X and check boundaries
        enemyX[enemyNumber] += enemyX_Change[enemyNumber]
        if enemyX[enemyNumber] <= 0 or enemyX[enemyNumber] > 736:
            enemyX_Change[enemyNumber] *= -1
            enemyY[enemyNumber] += enemyY_Change
        draw_enemy(enemyX[enemyNumber], enemyY[enemyNumber])

        collision = isCollision(enemyX[enemyNumber], enemyY[enemyNumber], bulletX, bulletY)
        if collision:
            bulletY = 0
            bulletState = 0
            enemyX[enemyNumber] = random.randint(0, 735)
            enemyY[enemyNumber] = random.randint(50, 150)
            score += 1
            print(score)

    # keep drawing the bullet and moving it upwards if it's in the fire state
    if bulletY <= 0:
        bulletY = playerY
        bulletState = 0
    if bulletState == 1:
        bulletY -= bulletY_Change
        fire_bullet(bulletX, bulletY)

    drawScore()
    # Must be called to refresh the screen
    pygame.display.update()
