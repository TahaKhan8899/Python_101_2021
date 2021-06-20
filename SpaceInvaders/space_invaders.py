import pygame

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


def draw_player(x, y):
    screen.blit(playerImg, (x, y))


# This is the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # check for arrow keys
            if event.key == pygame.K_LEFT:
                playerX_Change = -8
            if event.key == pygame.K_RIGHT:
                playerX_Change = 8
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    # place image on the screen
    screen.blit(background, (0, 0))

    # change playerX by the playerX_Change amount and draw it
    playerX += playerX_Change
    draw_player(playerX, playerY)

    # Must be called to refresh the screen
    pygame.display.update()
