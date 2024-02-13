import pygame
import math
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.chara_walk_1 = pygame.image.load('./images/character2.png').convert_alpha()
        self.chara_walk_2 = pygame.image.load('./images/character3.png').convert_alpha()
        self.image = self.chara_walk_1
        self.rect = self.image.get_rect(topleft = (10, 190))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('./images/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 270:
            self.image = self.chara_walk_2
            self.gravity = -15
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 270:
            self.image = self.chara_walk_1
            self.rect.bottom = 270

    def update(self):
        self.player_input()
        self.apply_gravity()


class Obsticle(pygame.sprite.Sprite):
    def __init__(self, tye):
        super().__init__()
        if tye == 'up':
            self.obst = pygame.image.load('./images/fireball.png').convert_alpha()
            self.y_pos = 245
        else:
            self.obst = pygame.image.load('./images/promp.png').convert_alpha()
            self.y_pos = 145
        self.image = self.obst
        self.rect = self.image.get_rect(topleft = (randint(900,1500), self.y_pos))

    def destroy(self):
        if self.rect.x < 0:
            self.kill()
    
    def update(self):
        self.rect.x -= 6
        self.destroy()
                                        


def scoreBoard():
    time = pygame.time.get_ticks() - timer
    score = text.render(f'{math.ceil(time / 1000)}', False, "white")
    score_rect = score.get_rect(center = (300, 30))
    screen.blit(score, score_rect)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obsticle_group, False):
        obsticle_group.empty()
        return False
    else:
        return True

# def obsticle_move(obsticle_rect):
#     if obsticle_rect:
#         for i in obsticle_rect:
#             i.x -= 5
#             if i.bottom == 190:
#                 screen.blit(promp, i)
#             else:
#                 screen.blit(ball, i)

#             obsticle_rect = [obsticle for obsticle in obsticle_rect if obsticle.x > 0 ]
#         return obsticle_rect
#     else:
#         return []
    
# def jump_animation():
#         global chara

#         # for jumping
#         if chara_rect.bottom == 273:
#             chara = chara_walk_1
#         else:
#             chara = chara_walk_2

pygame.init()
screen = pygame.display.set_mode((600,300))
clock = pygame.time.Clock()
text = pygame.font.Font(None, 30)


forest = pygame.image.load('./images/forest.jpeg').convert()
forest = pygame.transform.scale(forest, (600, 300))

# GRoup
player = pygame.sprite.GroupSingle()
player.add(Player())

obsticle_group = pygame.sprite.Group()

bgSound = pygame.mixer.Sound('./images/bgsound.mp3')
bgSound.set_volume(0.5)
bgSound.play(loops = -1)

# player 
# chara_walk_1 = pygame.image.load('./images/character2.png').convert_alpha()
# chara_walk_2 = pygame.image.load('./images/character3.png').convert_alpha()
# chara = chara_walk_1
# chara_rect = chara.get_rect(topleft = (10, 190))
# chara.fill("black")

# obsticals
# ball = pygame.image.load('./images/fireball.png').convert_alpha()
# ball_rect = ball.get_rect(topleft = (600, 245))

# promp = pygame.image.load('./images/promp.png').convert_alpha()
# promp_rect = promp.get_rect(topleft = (600, 145))

# obsticle_rect = []

gravity = 190
timer = 0
running = True
gameOn = True

# timer 
obsticle_time = pygame.USEREVENT +1
print(pygame.time.set_timer(obsticle_time,1600))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE and chara_rect.bottom > 260:
        #         chara_rect.y = 70
            if event.key == pygame.K_SPACE and not gameOn:
                gameOn = True
                timer = pygame.time.get_ticks()
        
        if event.type == obsticle_time and gameOn:
            obsticle_group.add(Obsticle(choice(['up', 'up', 'down'])))
            # if randint(0,2):
            #     obsticle_rect.append(ball.get_rect(topleft = (randint(900,1500), 245)))
            # else:
            #     obsticle_rect.append(promp.get_rect(topleft = (randint(900,1500), 145)))


    if gameOn:
    #     if chara_rect.top <= 190:
    #         chara_rect.y += 4

        # move the ball with static timer
        # ball_rect.x -= 5
        # if ball_rect.left < 0:
        #     ball_rect.x = 600


        screen.blit(forest, (0, 0))
        # screen.blit(chara, chara_rect)
        player.draw(screen)
        player.update()
        obsticle_group.draw(screen)
        obsticle_group.update()


        # not using this due to new randomly generated obstical
        # screen.blit(ball, ball_rect)
        # screen.blit(promp, promp_rect)

        # move with dynamic timer
        # obsticle_rect = obsticle_move(obsticle_rect)

        scoreBoard()
        # jump_animation()

        gameOn = collision_sprite()
        # this code was checking if the obstical collides with is player - write new one
        # if ball_rect.colliderect(chara_rect):
        #     gameOn = False
        #     pygame.quit()
        # for i in obsticle_rect:
        #     if i.colliderect(chara_rect):
        #         gameOn = False
        #         # pygame.quit()

    else:
        screen.fill("darkgray")

    pygame.display.update()
    clock.tick(50)