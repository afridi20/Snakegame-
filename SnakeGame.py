#importing the moduals 
import pygame
from random import randrange

# Initializing pygame
pygame.init()

# Creating the display
window = 600
Screen = pygame.display.set_mode([window] * 2)
clock = pygame.time.Clock()
pygame.display.set_caption('GOTY')

# Creating A random range  for random position
cell_size = 50
range_ = (cell_size // 2, window - cell_size // 2, cell_size)
get_random_position = lambda: [randrange(*range_), randrange(*range_)]

# Score
score = 0

# The snake , Snake speed  Snake movement,code
snake = pygame.Rect(0, 0, cell_size - 2, cell_size - 2)
snake.center = get_random_position()
length = 1
segment = [snake.copy()]
Snake_direction=(0,0)
dirs={pygame.K_w: 1,pygame.K_s: 1,pygame.K_a: 1,pygame.K_d: 1,}
time, time_step = 0, 120

# the code for Food its posation and hight and lenght 
food = pygame.Rect(0, 0, cell_size - 2, cell_size - 2)
food.center = get_random_position()

# creatint a loop where every thing hapen reapets itseflt until somone shuts the game down by clicken on x 
Run= True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

        # Assigning keys
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_w and dirs[pygame.K_w]:
                Snake_direction = (0,-cell_size)
                dirs={pygame.K_w: 1,pygame.K_s: 0,pygame.K_a: 1,pygame.K_d: 1,}
            if event.key == pygame.K_s and dirs[pygame.K_s]:
                Snake_direction = (0,cell_size)
                dirs={pygame.K_w: 0,pygame.K_s: 1,pygame.K_a: 1,pygame.K_d: 1,}
            if event.key == pygame.K_d and dirs[pygame.K_d]:
                Snake_direction = (cell_size,0)
                dirs={pygame.K_w: 1,pygame.K_s: 1,pygame.K_a: 0,pygame.K_d: 1,}
            if event.key == pygame.K_a and dirs[pygame.K_a]:
                Snake_direction = (-cell_size,0)
                dirs={pygame.K_w: 1,pygame.K_s: 1,pygame.K_a: 1,pygame.K_d: 0,}


    # Screen color
    Screen.fill('black')

    # Check border and self-eating
    snake_self_eating = pygame.Rect.collidelist(snake, segment[:-1]) != -1
    if (snake.left < 0 or snake.right > window or  snake.top < 0 or snake.bottom > window or snake_self_eating):
        snake.center, food.center = get_random_position(), get_random_position()
        length, Snake_direction = 1, (0, 0)
        segment = [snake.copy()]
        score = 0
        

    # Check snake pos and food pos and spawn new when they match
    if snake.colliderect(food):
        food.center = get_random_position()
        length += 1
        score += 1

    # Drawing the snake and food
    [pygame.draw.rect(Screen, 'white', segment) for segment in segment]
    pygame.draw.rect(Screen, 'red', food)

    # Draw score bord 
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, ('purple'))
    Screen.blit(score_text, (10, 10))

    # move snake
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(Snake_direction) 
        segment.append(snake.copy())
        segment= segment[-length:]

    # Updating screen
    pygame.display.update()
    clock.tick(15)










    

   
    

