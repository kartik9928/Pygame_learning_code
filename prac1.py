import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("game 1")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None,50)

# variable
test_v1 = 0

# surface in pygame
test_surface = pygame.Surface((50,50))
test_surface.fill('red')

back = pygame.image.load('./images/back.jpeg')
chara = pygame.image.load('./images/chara.png')

text_surf = test_font.render("new Game", False, "green")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # display surfaces
    screen.blit(test_surface,(0,0))
    screen.blit(back,(0,0))
    screen.blit(chara,(0,0))
    screen.blit(text_surf,(250,250))

    pygame.display.update()
    clock.tick(60)