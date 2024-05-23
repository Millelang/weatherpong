import pygame
from ball import Ball
from object import object
from paddle import Paddle
from intersect import intersect
from weather import get_weather
from weather import get_feeling


WHITE = get_feeling()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("pong")

done = False
ball = Ball(350, 250, 10, 10, RED)
player1 = Paddle(10, 10, 10, 100, GREEN, 1)
player2 = Paddle(680, 10, 10, 100, GREEN, 2)
clock = pygame.time.Clock()


# Game loopen, där allt körs
while not done:
    ## Kolla om dem krockar med något
    if intersect(player1, ball).check() or intersect(player2, ball).check():
        ball.speed_x *= -1 ## ändrar hastigheten på bollen så att den vänder


    ball.update() ## Updaterar så att bollen rörsig 
    ## Updaterar så att paddlarna rör sig
    player1.update()
    player2.update()
    
    for event in pygame.event.get():
        ## exit för spelet
        if event.type == pygame.QUIT:
            done = True

## här ritas allt
    screen.fill(WHITE)
    ball.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    pygame.display.flip()

    clock.tick(60) ## fps

pygame.quit()