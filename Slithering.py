# Slithering.py

import pygame
import sys
import time
import random

pygame.init()

# Constants
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
window_width = 800
window_height = 600

# setup environment
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snekkz")
font = pygame.font.SysFont(None, 25, 1)


def myquit():
    pygame.quit()
    sys.exit(0)


clock = pygame.time.Clock()
FPS = 5
blockSize = 20
noPixel = 0


def snake(blockSize, snakeList):
    for size in snakeList:
        pygame.draw.rect(gameDisplay, black, [
                         size[0]+5, size[1], blockSize, blockSize], 2)


def message(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width/2, window_height/2])


def gameloop():
    gameExit = False
    gameOver = False
    lead_x = window_width/2
    lead_y = window_height/2
    del_x = 0
    del_y = 0
    snakeList = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(
        0, window_height-blockSize)/10.0)*10.0

# Game Loop

    while not gameExit:

        # If the game is over
        while gameOver:
            gameDisplay.fill(white)
            message("Press return key to start or Esc to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    gameOver = False
                    gameExit = True
                # Check for keypress
                if(event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_q):
                        gameExit = True
                        gameOver = False
                    if(event.key == pygame.K_RETURN):
                        gameloop()

        # Otherwise
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()
                leftArrow = event.key == pygame.K_LEFT or event.key == pygame.K_a
                rightArrow = event.key == pygame.K_RIGHT or event.key == pygame.K_d
                upArrow = event.key == pygame.K_UP or event.key == pygame.K_w
                downArrow = event.key == pygame.K_DOWN or event.key == pygame.K_s

                if leftArrow:
                    del_x = -blockSize
                    del_y = noPixel
                elif rightArrow:
                    del_x = blockSize
                    del_y = noPixel
                elif upArrow:
                    del_x = noPixel
                    del_y = -blockSize
                elif downArrow:
                    del_x = noPixel
                    del_y = blockSize

            if lead_x < 0 or lead_x >= window_width or lead_y < 0 or lead_y >= window_height:
                gameOver = True
        lead_x += del_x
        lead_y += del_y
        gameDisplay.fill(white)

        AppleThickness = 20
        print([int(randomAppleX), int(randomAppleY),
               AppleThickness, AppleThickness])
        pygame.draw.rect(gameDisplay, red, [
                         randomAppleX, randomAppleY, AppleThickness, AppleThickness])

        allspritesList = []
        allspritesList.append(lead_x)
        allspritesList.append(lead_y)
        snakeList.append(allspritesList)

        if(len(snakeList) > snakeLength):
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if(eachSegment == allspritesList):
                gameOver = True
        snake(blockSize, snakeList)
        pygame.display.update()

        if(lead_x >= randomAppleX and lead_x <= randomAppleX+AppleThickness):
            if(lead_y >= randomAppleY and lead_y <= randomAppleY+AppleThickness):
                randomAppleX = round(random.randrange(
                    0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(
                    0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1
        
        clock.tick(FPS)
    pygame.quit()
    quit()
gameloop()
