import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
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

        # Check if time has run out
        if elapsed_time >= 120:
            game_over = True

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    draw_maze(maze)

    # Draw the player
    screen.blit(player.image, player.rect)

    # Display timer
    if not game_over:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Time: {int(max(120 - elapsed_time, 0))}", True, WHITE)
        screen.blit(text, (10, 10))

    # Display game over message
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        # Exit the game loop when the game is over
        running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()