import pygame
import math
from random import randint

def scoreBoard():
    time = pygame.time.get_ticks() - timer
    score = text.render(f'{math.ceil(time / 1000)}', False, "white")
    score_rect = score.get_rect(center = (300, 30))
    screen.blit(score, score_rect)

def obsticle_move(obsticle_rect):
    if obsticle_rect:
        for i in obsticle_rect:
            i.x -= 5
            if i.bottom == 190:
                screen.blit(promp, i)
            else:
                screen.blit(ball, i)

            obsticle_rect = [obsticle for obsticle in obsticle_rect if obsticle.x > 0 ]
        return obsticle_rect
    else:
        return []
    
def jump_animation():
        global chara

        # for jumping
        if chara_rect.bottom == 273:
            chara = chara_walk_1
        else:
            chara = chara_walk_2

pygame.init()
screen = pygame.display.set_mode((600,300))
clock = pygame.time.Clock()
text = pygame.font.Font(None, 30)


forest = pygame.image.load('./images/forest.jpeg').convert()
forest = pygame.transform.scale(forest, (600, 300))

# player 
chara_walk_1 = pygame.image.load('./images/character2.png').convert_alpha()
chara_walk_2 = pygame.image.load('./images/character3.png').convert_alpha()
chara = chara_walk_1
chara_rect = chara.get_rect(topleft = (10, 190))
# chara.fill("black")

# obsticals
ball = pygame.image.load('./images/fireball.png').convert_alpha()
# ball_rect = ball.get_rect(topleft = (600, 245))

promp = pygame.image.load('./images/promp.png').convert_alpha()
# promp_rect = promp.get_rect(topleft = (600, 145))

obsticle_rect = []

gravity = 190
timer = 0
running = True
gameOn = True

# timer 
obsticle_time = pygame.USEREVENT +1
print(pygame.time.set_timer(obsticle_time,1500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and chara_rect.bottom > 260:
                chara_rect.y = 70
            if event.key == pygame.K_SPACE and not gameOn:
                gameOn = True
                obsticle_rect = []
                timer = pygame.time.get_ticks()
        
        if event.type == obsticle_time and gameOn:
            if randint(0,2):
                obsticle_rect.append(ball.get_rect(topleft = (randint(900,1500), 245)))
            else:
                obsticle_rect.append(promp.get_rect(topleft = (randint(900,1500), 145)))


    if gameOn:
        if chara_rect.top <= 190:
            chara_rect.y += 4

        # move the ball with static timer
        # ball_rect.x -= 5
        # if ball_rect.left < 0:
        #     ball_rect.x = 600


        screen.blit(forest, (0, 0))
        screen.blit(chara, chara_rect)

        # not using this due to new randomly generated obstical
        # screen.blit(ball, ball_rect)
        # screen.blit(promp, promp_rect)

        # move with dynamic timer
        obsticle_rect = obsticle_move(obsticle_rect)

        scoreBoard()
        jump_animation()

        # this code was checking if the obstical collides with is player - write new one
        # if ball_rect.colliderect(chara_rect):
        #     gameOn = False
        #     pygame.quit()
        for i in obsticle_rect:
            if i.colliderect(chara_rect):
                gameOn = False
                # pygame.quit()

    else:
        screen.fill("darkgray")

    pygame.display.update()
    clock.tick(50)