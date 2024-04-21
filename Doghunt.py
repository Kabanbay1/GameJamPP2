import pygame,random,time,sys
from pygame.locals import *

pygame.init()
CYCLE=random.randint(1,4)#Зависит от цикла игры а не от рандома
SCREEN_HEIGHT=600
SCREEN_WIDTH=400
SPEED=3+CYCLE
SCORE_B=0
SCORE_G=0

FPS = 60
FramePerSec = pygame.time.Clock()
def Doghunt():
    global SCORE_G
    global SCORE_B
    background=pygame.image.load("Race/AnimatedStreet.png")

    font = pygame.font.SysFont("Verdana", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font.render("Game Over", True, "BLACK")

    DISPLAYSURF = pygame.display.set_mode((400,600))
    DISPLAYSURF.fill((255,255,255))

    done = False


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__() 
            self.image = pygame.image.load("Assets/car.png")
            self.rect = self.image.get_rect()
            self.rect.center = (160, 520)

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            if self.rect.right < SCREEN_WIDTH:        
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5, 0)

    class Dog1(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog1.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH-140), 0)  
        def move(self):
            self.rect.move_ip(0,SPEED)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B+=1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    class Dog2(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog2.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH-140), 0)  
        def move(self):
            self.rect.move_ip(0,SPEED+1)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B+=1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    class Dog3(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog3.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH-140), 0)    
        def move(self):
            self.rect.move_ip(0,SPEED-1)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B+=1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    Pl=Player()
    D1=Dog1()
    D2=Dog2()
    D3=Dog3()

    dogs=pygame.sprite.Group()
    dogs.add(D1)
    dogs.add(D2)
    dogs.add(D3)

    all_sprites=pygame.sprite.Group()
    all_sprites.add(Pl)
    all_sprites.add(D1)
    all_sprites.add(D2)
    all_sprites.add(D3)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        DISPLAYSURF.blit(background, (0,0))
        scores = font_small.render(str(SCORE_B)+"/"+str(10-CYCLE), True, "RED")
        scores1 = font_small.render(str(SCORE_G), True, "YELLOW")
        DISPLAYSURF.blit(scores1, (360 ,10))    
        DISPLAYSURF.blit(scores, (10,10))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()
        
        collided_dog = pygame.sprite.spritecollideany(Pl, dogs)
        if collided_dog:
            # pygame.mixer.Sound().play("Race/catch.mp3")       
            SCORE_G += 1
            collided_dog.kill()

            # Add a new dog sprite
            new_dog = random.choice([D1, D2, D3])
            new_dog.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
            dogs.add(new_dog)
            all_sprites.add(new_dog)

        if SCORE_B==10-CYCLE:
            time.sleep(0.5)                
            DISPLAYSURF.fill((255,0,0))
            DISPLAYSURF.blit(game_over, (30,250))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
                    
        pygame.display.update()
        FramePerSec.tick(FPS)

Doghunt()