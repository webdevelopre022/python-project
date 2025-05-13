#5 star coder youtube channel
#subscribe now!
import sys, pygame
pygame.init()
size = width, height = 100, 800
speed = [1, 1]
background = 144, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing ball in pyhon")
ball = pygame.image.load('ball-removebg-preview.png')
ball_rectangle = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            ball_rectangle = ball_rectangle.move(seed)
    if ball_rectangle.left<0 or ball_rectangle.right> width:
        speed[0] = -speed[0]
    if ball_rectangle.top<0 or ball_rectangle.bottom> height:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ball_rectangle)
    pygame.display.flip()
