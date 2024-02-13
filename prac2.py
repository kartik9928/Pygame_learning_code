import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,260))
clock = pygame.time.Clock()

# pygame surface
back = pygame.image.load('./images/gelexy.jpg').convert()
smile = pygame.image.load('./images/smile.png').convert_alpha()
head = pygame.image.load('./images/head.png').convert_alpha()
rect_head = head.get_rect(center = (600,100))
bor = pygame.Surface((100,100))
center = pygame.Surface((5,5))
center.fill("red")
head2 = pygame.image.load('./images/head.png').convert_alpha()
rect_head2 = head2.get_rect(center = (100,100))

x_var = -100
x_back = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # surface
    screen.blit(back,(x_back,0))
    screen.blit(smile,(x_var,0))
    x_back -=1
    x_var += 5
    if x_var > 810 :
        x_var =-100
        x_back = 0
        rect_head2.left = 0

    screen.blit(head,rect_head)
    screen.blit(bor,(600,100))
    screen.blit(center,(600,100))

    rect_head2.left += 5
    screen.blit(head2,rect_head2)

    # collid
    print(rect_head2.colliderect(rect_head))

    # mouse collid
    mouse_pos = pygame.mouse.get_pos()
    if rect_head.collidepoint(mouse_pos):
        print("mouse collied")


    pygame.display.update()
    clock.tick(60)
