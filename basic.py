import pygame
import random

pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Мини-игра: Сбор мусора")


map_image = pygame.transform.scale(pygame.image.load("Assets/street.png"), (screen_width, screen_height))
player_images_right = [pygame.transform.scale(pygame.image.load(f"Assets/walking{i}.png"), (64, 64)) for i in range(1, 4)]
player_images_left = [pygame.transform.scale(pygame.image.load(f"Assets/walking{i}m.png"), (64, 64)) for i in range(1, 4)]
trash_image = pygame.transform.scale(pygame.image.load("Assets/garbage ver 3.png"), (20, 20))

class Map:
    def __init__(self, image):
        self.image = image

    def draw(self):
        screen.blit(self.image, (0, 0))

class Player:
    def __init__(self, images_right, images_left):
        self.images_right = images_right
        self.images_left = images_left
        self.current_images = self.images_right  
        self.index = 0
        self.image = self.current_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 2  
        self.is_moving = False  
        self.direction = "right"  
        self.animation_timer = 0  
        self.animation_delay = 10  

    def update_animation(self, dx):
        if self.is_moving:
            if dx < 0:  
                self.direction = "left"
                self.current_images = self.images_left
            else: 
                self.direction = "right"
                self.current_images = self.images_right

            self.animation_timer += 1
            if self.animation_timer >= self.animation_delay:
                self.animation_timer = 0
                self.index += 1
                if self.index >= len(self.current_images):
                    self.index = 0

                self.image = self.current_images[self.index]

    def move(self, dx, dy):
        self.is_moving = (dx != 0 or dy != 0)  
        new_x = self.rect.x + dx * self.speed
        new_y = self.rect.y + dy * self.speed
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y

    def draw(self):
        screen.blit(self.image, self.rect)


class Trash:
    def __init__(self, image, map_image):
        self.image = image
        self.rect = self.image.get_rect()
        self.map_image = map_image
        self.spawn_trash()

    def spawn_trash(self):
        while True:
            x = random.randint(0, screen_width - self.rect.width)
            y = random.randint(0, screen_height - self.rect.height)
            pixel_color = self.map_image.get_at((x, y))
            if pixel_color == (0, 0, 0):
                self.rect.x = x
                self.rect.y = y
                break

    def draw(self):
        screen.blit(self.image, self.rect)
map = Map(map_image)
player = Player(player_images_right, player_images_left)
trash_list = [Trash(trash_image, map_image) for _ in range(20)]

score = 0
font = pygame.font.Font(None, 36)
game_over = False


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1

        player.move(dx, dy)
        player.update_animation(dx)

        for trash in trash_list[:]:
            if player.rect.colliderect(trash.rect):
                trash_list.remove(trash)
                score += 1

        if score >= 20:
            game_over = True

        
        screen.fill((0, 0, 0))  
        map.draw()
        player.draw()
        for trash in trash_list:
            trash.draw()

        
        score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
      
        game_over_text = font.render("Игра завершена!", True, (255, 0, 0))
        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 20))

    pygame.display.update()
    clock.tick(30) 