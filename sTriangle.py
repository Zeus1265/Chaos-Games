import pygame
import random

pygame.init()
pointA = (650, 75)
pointB = (120, 575)
pointC= (1100, 625)

#print(pointA[0])

currentPoint = (600, 550)

screen = pygame.display.set_mode([1200, 700])

BACKGROUND = pygame.Color(200,200, 200, 0)
GREEN = pygame.Color(0, 170, 50, 0)
BLACK = pygame.Color(0, 0, 0, 0)
BLUE = pygame.Color(0, 90, 180, 0)

screen.fill(BACKGROUND)

pygame.display.set_caption('Bootleg Fractal')

pygame.display.update()

clock = pygame.time.Clock()

pygame.draw.circle(screen, BLUE, currentPoint, 2)
pygame.draw.circle(screen, GREEN, pointA, 4)
pygame.draw.circle(screen, GREEN, pointB, 4)
pygame.draw.circle(screen, GREEN, pointC, 4)

newPoint = currentPoint

iterations = 0

myfont = pygame.font.SysFont('helvetica', 14)

running = 1
while (running):
    for events in pygame.event.get():
        if events.type is pygame.QUIT:
            running = 0

    direction = int(random.random() * 3)
    target = (0, 0)
    
    if direction is 0:
        target = pointA
    elif direction is 1:
        target = pointB
    else:
        target = pointC

    pygame.draw.circle(screen, BLACK, currentPoint, 2)

    newPoint = ((target[0] + newPoint[0])/2, (target[1] + newPoint[1])/2)

    pygame.draw.circle(screen, BLUE, newPoint, 2)

    currentPoint = newPoint

    iterations += 1

    text = myfont.render('Iterations: {}'.format(iterations), 0, BLACK)
    
    pygame.draw.rect(screen, BACKGROUND, pygame.Rect(10, 10, 100, 20), 0)

    screen.blit(text, (10, 10))

    pygame.display.update()
    #clock.tick(240)

pygame.quit()
