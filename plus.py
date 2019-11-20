import pygame
import random

pygame.init()
#pointA = (0, 0)
#pointB = (, 575)
#pointC = (1100, 625)
#pointD = (1150, 75)


#print(pointA[0])

currentPoint = (600, 350)

screen = pygame.display.set_mode([1200, 700])

BACKGROUND = pygame.Color(200,200, 200, 0)
GREEN = pygame.Color(0, 170, 50, 0)
BLACK = pygame.Color(0, 0, 0, 0)
BLUE = pygame.Color(0, 90, 180, 0)

screen.fill(BACKGROUND)

pygame.display.set_caption('Bootleg Fractal')

pygame.display.update()

clock = pygame.time.Clock()

#scale = 1./3.

T = []
T.append(lambda x, y : ((x+1200)/3, y/3))
T.append(lambda x, y : ((x)/3, (y+700)/3))
T.append(lambda x, y : ((x+1200)/3, (y+700)/3))
T.append(lambda x, y : ((x+2400)/3, (y+700)/3))
T.append(lambda x, y : ((x+1200)/3, (y+1400)/3))


pygame.draw.circle(screen, BLUE, currentPoint, 2)
#pygame.draw.circle(screen, GREEN, pointA, 4)
#pygame.draw.circle(screen, GREEN, pointB, 4)
#pygame.draw.circle(screen, GREEN, pointC, 4)
#pygame.draw.circle(screen, GREEN, pointD, 4)

newPoint = currentPoint

iterations = 0

myfont = pygame.font.SysFont('helvetica', 14)

running = 1
while (running):
    for events in pygame.event.get():
        if events.type is pygame.QUIT:
            running = 0
    if (iterations < 20000):
	direction = int(random.random() * 5)
	target = (0, 0)
    

	pygame.draw.circle(screen, BLACK, currentPoint, 2)

	newPoint = T[direction](currentPoint[0], currentPoint[1])

	pygame.draw.circle(screen, BLUE, newPoint, 2)

	currentPoint = newPoint

	iterations += 1

	text = myfont.render('Iterations: {}'.format(iterations), 0, BLACK)
    
	pygame.draw.rect(screen, BACKGROUND, pygame.Rect(10, 10, 105, 20), 0)

	screen.blit(text, (10, 10))
	
	pygame.display.update()

pygame.quit()
