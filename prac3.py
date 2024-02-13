import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

# object creation

ruinning = True

while ruinning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.draw.line(screen, "yellow", (0, 0), (100, 100), 10)
    pygame.draw.circle(screen, "green", (100, 100), 100, 10)

    pygame.display.update()
    clock.tick(60)