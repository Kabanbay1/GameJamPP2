import pygame
import random
import time
import sys
from pygame.locals import *

# Create display window
pygame.init()
CYCLE = 1
G_S = 0
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000
SPEED = 3 + CYCLE
SCORE_B = 0
SCORE_G = 0

menu_state = "main"
font = pygame.font.SysFont("arialblack", 40)
font_small = pygame.font.SysFont("Verdana", 20)
maP = pygame.image.load("Assets/map.png")
Map = pygame.transform.scale(maP, (1000, 800))
bg = pygame.image.load("Race/AnimatedStreet.png")
m3 = pygame.image.load("Assets/minigame3.png")
mb = pygame.image.load("Assets/play.png")
meb = pygame.transform.scale(mb, (50, 50))
mg3 = pygame.transform.scale(m3, (50, 50))
FPS = 60
FramePerSec = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')


# Load button images
basic_img = pygame.image.load("Assets/minigame1.png").convert_alpha()
bas_im=pygame.transform.scale(basic_img,(50,50))
m_i=pygame.image.load("Assets/minigame2.png")
m_b=pygame.transform.scale(m_i, (50,50))

def Doghunt():
    global SCORE_G
    global SCORE_B
    global G_S
    global CYCLE
    game_over = font.render("Game Over", True, "BLACK")
    completed = font.render("Completed", True, "YELLOW")

    background = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    done = False

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/car.png")
            self.rect = self.image.get_rect()
            self.rect.center = (900, 700)

        def move(self):
            pressed_keys = pygame.key.get_pressed()
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-15, 0)
            if self.rect.right < SCREEN_WIDTH:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(15, 0)

    class Dog1(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog1.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

        def move(self):
            self.rect.move_ip(0, SPEED)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    class Dog2(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog2.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

        def move(self):
            self.rect.move_ip(0, SPEED + 1)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    class Dog3(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("Assets/dog3.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

        def move(self):
            self.rect.move_ip(0, SPEED - 1)
            if (self.rect.top > SCREEN_HEIGHT):
                global SCORE_B
                SCORE_B += 1
                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 140), 0)

    Pl = Player()
    D1 = Dog1()
    D2 = Dog2()
    D3 = Dog3()

    dogs = pygame.sprite.Group()
    dogs.add(D1)
    dogs.add(D2)
    dogs.add(D3)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(Pl)
    all_sprites.add(D1)
    all_sprites.add(D2)
    all_sprites.add(D3)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(background, (0, 0))
        scores = font_small.render(str(SCORE_B) + "/" + str(10 - CYCLE), True, "RED")
        scores1 = font_small.render(str(SCORE_G), True, "YELLOW")
        DISPLAYSURF.blit(scores1, (360, 10))
        DISPLAYSURF.blit(scores, (10, 10))

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
            new_dog.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            dogs.add(new_dog)
            all_sprites.add(new_dog)
        if SCORE_G == 5 * CYCLE:
            G_S += 1  

        if SCORE_B == 10 - CYCLE:
            time.sleep(0.5)
            DISPLAYSURF.fill((255, 0, 0))
            DISPLAYSURF.blit(game_over, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            DISPLAYSURF.fill((202, 228, 241))
            start_button.visible = True
            CYCLE+=1
            return

        if SCORE_G == 5 * CYCLE:
            time.sleep(0.5)
            DISPLAYSURF.fill((200, 200, 200))
            DISPLAYSURF.blit(completed, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            menu_button.visible = True
            CYCLE+=1
            return

        pygame.display.update()
        FramePerSec.tick(FPS)

def basic():
    global G_S
    global CYCLE
    screen_width = 1000
    screen_height = 800
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
    trash_list = [Trash(trash_image, map_image) for _ in range(20+CYCLE)]

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
                G_S += 1
                CYCLE+=1
                running = False

            
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
            basic_button.visible = False  # Hide the button after the game is over

        pygame.display.update()
        clock.tick(30) 

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos) and self.visible:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen if it's visible
        if self.visible:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

class MenuButton():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos) and self.visible:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen if it's visible
        if self.visible:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

def maze():
    global G_S
    global CYCLE
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("A Maze Game")

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255) 
    GOLD = (255, 215, 0)

    # Define player and wall sizes
    PLAYER_SIZE = 24
    WALL_SIZE = 24

    # Maze size
    MAZE_WIDTH = SCREEN_WIDTH // WALL_SIZE
    MAZE_HEIGHT = SCREEN_HEIGHT // WALL_SIZE

    # Generate random maze
    def generate_maze():
        maze = [["X" for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]

        def recursive_backtracking(x, y):
            maze[y][x] = " "
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < MAZE_WIDTH and 0 <= ny < MAZE_HEIGHT and maze[ny][nx] == "X":
                    maze[y + dy][x + dx] = " "
                    recursive_backtracking(nx, ny)

        recursive_backtracking(1, 1)
        return maze

    # Function to draw the maze
    def draw_maze(maze):
        for y, row in enumerate(maze):
            for x, char in enumerate(row):
                if char == "X":
                    pygame.draw.rect(screen, WHITE, (x * WALL_SIZE, y * WALL_SIZE, WALL_SIZE, WALL_SIZE))

    # Player class
    class Player(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
            self.image.fill(GOLD)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    # Create player
    player = Player(PLAYER_SIZE, PLAYER_SIZE)

    # Generate and draw maze
    maze = generate_maze()

    # Timer variables
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    game_over = False

    # Main game loop
    running = True
    while running:
        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        # Check if the game is over
        if not game_over:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if maze[player.rect.y // WALL_SIZE][(player.rect.x - PLAYER_SIZE) // WALL_SIZE] == " ":
                            player.rect.x -= PLAYER_SIZE
                    elif event.key == pygame.K_RIGHT:
                        if maze[player.rect.y // WALL_SIZE][(player.rect.x + PLAYER_SIZE) // WALL_SIZE] == " ":
                            player.rect.x += PLAYER_SIZE
                    elif event.key == pygame.K_UP:
                        if maze[(player.rect.y - PLAYER_SIZE) // WALL_SIZE][player.rect.x // WALL_SIZE] == " ":
                            player.rect.y -= PLAYER_SIZE
                    elif event.key == pygame.K_DOWN:
                        if maze[(player.rect.y + PLAYER_SIZE) // WALL_SIZE][player.rect.x // WALL_SIZE] == " ":
                            player.rect.y += PLAYER_SIZE

            # Check if the player reached the end of the maze
            if player.rect.x >= (MAZE_WIDTH - 2) * WALL_SIZE and player.rect.y >= (MAZE_HEIGHT - 2) * WALL_SIZE:
                game_over = True
                CYCLE+=1
                G_S+=1

            # Check if time has run out
            if elapsed_time >= 120:
                game_over = True
                CYCLE+=1

        # Clear the screen
        screen.fill(BLACK)

        # Draw the maze
        draw_maze(maze)

        # Draw the player
        screen.blit(player.image, player.rect)

        # Display timer
        if not game_over:
            font = pygame.font.Font(None, 36)
            text = font.render(f"Time: {int(max(120 - elapsed_time, 0))}", True, "RED")
            screen.blit(text, (10, 10))

        # Display game over message
        if game_over:
            font = pygame.font.Font(None, 72)
            text = font.render("Game Over!", True, "RED")
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

            # Exit the game loop when the game is over
            running = False

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)



start_button = Button(775, 25, mg3, 0.8)
basic_button = Button(460, 600, bas_im, 1)
maze_button = Button(100,400,m_b, 1)
menu_button = MenuButton(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 50, meb, 1)
basic_game_button = MenuButton(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 50, meb, 1)
maze_game_button = MenuButton(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 50, meb, 1)

# game loop
run = True
while run:

    DISPLAYSURF.blit(Map,(0,0))
    Scores1 = font_small.render(str(G_S), True, "YELLOW")
    DISPLAYSURF.blit(Scores1, (360, 10))
    if menu_state == "main":
        if start_button.draw(DISPLAYSURF):
            menu_state = "doghunt"
            Doghunt()
            start_button.visible = False

    if menu_state == "doghunt":
        if menu_button.draw(DISPLAYSURF):
            menu_state = "main"
            SCORE_B = 0
            SCORE_G = 0
            menu_button.visible = False

    if menu_state == "main":
        if basic_button.draw(DISPLAYSURF):
            menu_state = "basic"
            basic()
            basic_button.visible = False

    if menu_state == "basic":
        if basic_game_button.draw(DISPLAYSURF):
            menu_state = "main"
            SCORE_B = 0
            SCORE_G = 0
            basic_game_button.visible = False

    if menu_state == "main":
        if maze_button.draw(DISPLAYSURF):
            menu_state = "maze"
            maze()
            maze_button.visible = False

    if menu_state == "maze":
        if maze_game_button.draw(DISPLAYSURF):
            menu_state = "main"
            SCORE_B = 0
            SCORE_G = 0
            maze_game_button.visible = False

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
    if start_button.visible == False and maze_game_button.visible == False and basic_game_button.visible == False:
        if G_S==3:
            DISPLAYSURF.fill((200,200,200))
            font = pygame.font.Font(None, 72)
            text = font.render("Congrats!", True, (255,255,0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            DISPLAYSURF.blit(text, text_rect)
        else:
            DISPLAYSURF.fill((255,0,0))
            font = pygame.font.Font(None, 72)
            text = font.render("Your Score:"+str(G_S)+"/3", True, (0,0,0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            DISPLAYSURF.blit(text, text_rect)


    pygame.display.update()

pygame.quit()
