# importing libraries
import pygame
import time
import random

snake_speed = 7

# Window size
window_x = 720
window_y = 480
game_x = 420
game_y = 420

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
beige = pygame.Color(250, 235, 215)
mud = pygame.Color(139, 131, 120)
khaki = pygame.Color(205, 192, 176)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))


# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake random default position 
snake_position = [(random.randrange(30, (game_x //10)) * 10 - 30) + 150,
                                   	(random.randrange(30, (game_y//10)) * 10 - 30) + 50]

# defining first block of snake body
snake_body = [snake_position]

# defining shedding machenism
snake_shedding = []

# fruit position the first fruit won't appear on edges or collide with snake
fruit_position = [(random.randrange(30, (game_x //10)) * 10 - 30) + 150,
                                   (random.randrange(30, (game_y//10)) * 10 - 30) + 50]
while fruit_position in snake_body or fruit_position in snake_shedding:
	fruit_position = [(random.randrange(30, (game_x //10)) * 10 - 30) + 150,
                                   (random.randrange(30, (game_y//10)) * 10 - 30) + 50]
                                   
# setting default snake direction 
direction = None

# initial score
score = 0

# displaying Score function
def show_score(color, font, size):
  
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size, bold = True)
    
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the 
    # text surface object
    score_rect = score_surface.get_rect()
    score_rect = (140, 10)
    # displaying text
    game_window.blit(score_surface, score_rect)
    
def branding(color, font, size):
  
    # creating font object branding_font 
    branding_font = pygame.font.SysFont(font, size, bold = True)
    
    # create the display surface object
    branding_surface = branding_font.render('VaLeHo', True, color)
    branding_surface = pygame.transform.rotate(branding_surface, 90)
    
    # create a rectangular object for the 
    # text surface object
    branding_rect = branding_surface.get_rect()
    branding_rect.right = 150
    branding_rect.bottom = window_y
    # displaying text
    game_window.blit(branding_surface, branding_rect)

# game reset function
def game_reset():
    global snake_position, snake_body, snake_speed, snake_shedding
    global fruit_position
    global direction, change_to
    global score
    
    snake_speed = 7
    snake_shedding = []
    snake_position = [(random.randrange(30, (game_x //10)) * 10 - 30) + 150,
                                   	(random.randrange(30, (game_y//10)) * 10 - 30) + 50]
    snake_body = [snake_position]
    
    fruit_position = [(random.randrange(30, (game_x //10)) * 10 - 30) + 150,
                                   (random.randrange(30, (game_y//10)) * 10 - 30) + 50]
                                   
    direction = None

    score = 0
   
# game over function
def game_over():
    # creating font
    game_over_font = pygame.font.SysFont('Roboto', 50, bold = True)
    game_reset_font = pygame.font.SysFont('Roboto', 27)
    count_down_font = pygame.font.SysFont('Roboto', 170, bold = True)
    
    # creating a text surface on which text will be drawn
    game_over_surface = game_over_font.render('Your Score is : ' + str(score), True, mud)
    game_reset_surface = game_reset_font.render('Continue ? (press any key) ', True, mud)
    
    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()
    game_reset_rect = game_reset_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_reset_rect.midtop = (window_x/2, window_y/4 + 50)
    
    # blit will draw the text on screen and erase all other content
    pygame.draw.rect(game_window, beige, [150, 50, game_x, game_y], 0)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_reset_surface, game_reset_rect)
    pygame.display.flip()
    
    # the game will close after 10 seconds
    count_down = 10
    while count_down >= 0 :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        # refresh only the part of the count down number
        count_down_surface = count_down_font.render(str(count_down), True, mud)
        count_down_rect = pygame.draw.rect(game_window, beige, [150, 200, game_x, game_y - 200], 0)
        text_rect = count_down_surface.get_rect(midtop=count_down_rect.midtop)
        
        # Clear the countdown display area before drawing new countdown number
        game_window.blit(count_down_surface, text_rect)
        
        # Update display and decrease countdown
        pygame.display.update(count_down_rect)
        count_down -= 1
        
        
        time.sleep(1)
         
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()

# Main Function
while True:
  
    # handling key events
    for event in pygame.event.get():
       # Key press event to start the game direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
             
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism 
    # if fruits and snakes collide then scores will be 
    # incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_position = [(random.randrange(0, (game_x //10)) * 10) + 150,
                                           (random.randrange(0, (game_y//10)) * 10) + 50]
        # spawn new fruit if it is inside snake body or sheddings
        while fruit_position in snake_body or fruit_position in snake_shedding:
        	fruit_position = [(random.randrange(0, (game_x //10)) * 10) + 150,
                                           (random.randrange(0, (game_y//10)) * 10) + 50]
        # increase snake speed gradually
        if snake_speed < 17:
            snake_speed += 0.7
    else:
        # snake will grow to the first 4 blocks
        if len(snake_body) <= 4: pass
        else:
        	snake_body.pop()
        
    # snake will shed when it gets too long
    if len(snake_body) >= 17:
    	snake_shedding += snake_body[1:]
    	snake_body = [snake_position]
    	snake_speed = 7
    	
    game_window.fill(beige)
    window = pygame.draw.rect(game_window, beige, [150, 50, game_x, game_y], 0)
    window_border = pygame.draw.rect(game_window, mud, [140, 40, game_x + 20, game_y + 20], 10)
    
    for pos in snake_shedding:
    	pygame.draw.circle(game_window, mud, 
          	(pos[0] + 4, pos[1] + 4), 5)
          
    for pos in snake_body:
        #Snake body gets lighter to the tail
        offset = min (mud[0] - khaki[0], 
        							mud[1] - khaki[1], 
        							mud[2] - khaki[2]) // len(snake_body)
        color = (mud[0] - offset * snake_body.index(pos), 
        			   mud[1] - offset * snake_body.index(pos),
        			   mud[2] - offset * snake_body.index(pos))
        pygame.draw.circle(game_window, color, 
          (pos[0] + 4, pos[1] + 4), 5)
        
    pygame.draw.circle(game_window, khaki,(
      fruit_position[0] + 5, fruit_position[1] + 5), 5)

    # Game Over conditions
    if snake_position[0] < 150 or snake_position[0] > game_x + 140:
        game_over()
        game_reset()
                    
    if snake_position[1] < 50 or snake_position[1] > window_y - 20:
        game_over()
        game_reset()
    
    # Touching the snake body or sheddings
    if snake_position in snake_shedding:
    			   game_over()
    			   game_reset()
    			   
    if len(snake_body) > 4:
    			if snake_position in snake_body[1:]:
    			   game_over()
    			   game_reset()
    
    # displaying score continuously
    show_score(mud, 'Roboto', 30)
    branding(mud, 'Roboto', 50)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)