import pygame
import random

pygame.init()
  
# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")

scary_event = 1
HAPPEN = pygame.event.Event(pygame.USEREVENT, mytype = scary_event) 


def game():
    exit_game = False
    game_over = False
    # Creating a game loop
    while not exit_game:
        
        
        
        
        
        fire_random = random.randint(0, 100)
        if fire_random > 99:
            pygame.event.post(HAPPEN)
        
        for event in pygame.event.get():  # For Loop
            if event.type == pygame.QUIT:
                exit_game = True
      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("You have pressed right arrow key")
                elif event.key == pygame.K_LEFT:
                    print("You have pressed left arrow key")
            if event.type == pygame.USEREVENT:
                if event.mytype == scary_event:
                    print ("I happened")
        
      
    pygame.quit()
    quit()
game()
