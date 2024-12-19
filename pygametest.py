
# import pygame
# import random

# pygame.init()

# screen = pygame.display.set_mode((800, 400))
# screen.fill((0, 0, 1))

# font = pygame.font.Font(None, 30)
# text_surface = font.render("0", True, (0,0,0))

# #test_surface = pygame.Surface((800,100))
# #test_surface.fill((200, 211, 5))
# #screen.blit(test_surface, (0, 300))

# player_surface = pygame.Surface((20, 20))
# player_rect = player_surface.get_rect(midbottom = (15, 295))

# player_surface.fill((255,255,245))
# screen.blit(player_surface, player_rect)


# bomb_surface = pygame.Surface((20, 20))
# bomb_surface.fill((1,1,1))
# bombs = [] 

# #test2 = pygame.image.load("C:/Users/salaz/Pictures/Screenshots/CopyFolio.png")

# #test2.fill((200, 211, 5))

# pygame.display.set_caption("Bombs away")
# clock = pygame.time.Clock()



# FirstKeyPress = False
# WPressed = False
# SPressed = False
# APressed = False
# DPressed = False

# Speed = 3

# SPAWN_BOMB_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(SPAWN_BOMB_EVENT, 100)

# TEXT_EVENT = pygame.USEREVENT + 2
# pygame.time.set_timer(TEXT_EVENT, 1000)

# def move_bombs():
#     # """Update the position of all bombs and remove those off the screen."""
#     # for bomb in bombs[:]:  # Iterate over a copy of the list
#     #     bomb["y"] += bomb["speed"]
#     #     if bomb["y"] > 400:  # Remove bombs that move out of bounds
#     #         bombs.remove(bomb)
#     """Update bomb positions and remove off-screen bombs."""
#     for bomb in bombs[:]:  # Iterate over a copy of the list
#         bomb["rect"].y += bomb["speed"]  # Move bomb down
#         if bomb["rect"].y > 400:  # Remove bombs off-screen
#             bombs.remove(bomb)

# def draw_bombs():
#     # """Draw all bombs on the screen."""
#     # for bomb in bombs:
#     #     screen.blit(bomb_surface, (bomb["x"], bomb["y"]))
#     """Draw bombs on the screen."""
#     for bomb in bombs:
#         screen.blit(bomb_surface, bomb["rect"].topleft)

# seconds = 0

# while True:
#     #screen.fill((255, 10, 51))
#     screen.fill((0, 150, 255))

#     screen.blit(text_surface, (20, 20))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:
#                 if FirstKeyPress == False: FirstKeyPress = True
#                 if WPressed == False: WPressed = True
#             if event.key == pygame.K_s:
#                 if FirstKeyPress == False: FirstKeyPress = True
#                 if SPressed == False: SPressed = True
#             if event.key == pygame.K_a:
#                 if FirstKeyPress == False: FirstKeyPress = True
#                 if APressed == False: APressed = True
#             if event.key == pygame.K_d:
#                 if FirstKeyPress == False: FirstKeyPress = True
#                 if DPressed == False: DPressed = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_w:
#                 if WPressed == True: WPressed = False
#             if event.key == pygame.K_s:
#                 if SPressed == True: SPressed = False
#             if event.key == pygame.K_a:
#                 if APressed == True: APressed = False
#             if event.key == pygame.K_d:
#                 if DPressed == True: DPressed = False
#         if event.type == SPAWN_BOMB_EVENT:
#             # bombs.append({
#             #     "x": random.randint(0, 780),
#             #     "y": 0,
#             #     "speed": random.randint(4, 8),
#             # }) 
#             bomb_rect = bomb_surface.get_rect(topleft=(random.randint(0, 780), 0))
#             bombs.append({
#                 "rect": bomb_rect,
#                 "speed": random.randint(4, 8),
#             })
    
#         if event.type == TEXT_EVENT:
#             seconds = seconds + 1
#             text_surface = font.render(str(seconds), True, (0,0,0))
#     #snake move left

#     if FirstKeyPress == False:
#         player_rect.x += 1
#         screen.blit(player_surface, player_rect)
#     elif WPressed == False and SPressed == False and APressed == False and DPressed == False:
#        screen.blit(player_surface, player_rect)
    
#     if WPressed == True:
#         player_rect.y -= Speed
#         screen.blit(player_surface, player_rect)
#     elif SPressed == True:
#         player_rect.y += Speed
#         screen.blit(player_surface, player_rect)
#     elif APressed == True:
#         player_rect.x -= Speed
#         screen.blit(player_surface, player_rect)
#     elif DPressed == True:
#         player_rect.x += Speed
#         screen.blit(player_surface, player_rect)
       
    
#     move_bombs()
#     draw_bombs()
#     player_rect.clamp_ip(screen.get_rect()) #limit player within screen

#     #Check if player touches the bomb       
#     for bomb in bombs:
#         if player_rect.colliderect(bomb["rect"]):
#             screen.fill((0, 0, 0))
#             seconds = 0
#             text_surface = font.render(str(seconds), True, (0,0,0))

#     pygame.display.flip()
#     clock.tick(60)
    




import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 400))
screen.fill((0, 0, 1))

font = pygame.font.Font(None, 30)
text_surface = font.render("0", True, (0,0,0))

#test_surface = pygame.Surface((800,100))
#test_surface.fill((200, 211, 5))
#screen.blit(test_surface, (0, 300))

player_surface = pygame.Surface((20, 20))
player_rect = player_surface.get_rect(midbottom = (15, 295))

player_surface.fill((255,255,245))
screen.blit(player_surface, player_rect)


bomb_surface = pygame.image.load("C:/Users/salaz/Downloads/meteorite.webp")
bomb_surface = pygame.transform.scale(bomb_surface, (20, 20))
bomb_surface.fill((1,1,1))
bombs = [] 

#test2 = pygame.image.load("C:/Users/salaz/Pictures/Screenshots/CopyFolio.png")

#test2.fill((200, 211, 5))

pygame.display.set_caption("Bombs away")
clock = pygame.time.Clock()



FirstKeyPress = False
WPressed = False
SPressed = False
APressed = False
DPressed = False

Speed = 3

SPAWN_BOMB_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_BOMB_EVENT, 100)

TEXT_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(TEXT_EVENT, 1000)

def move_bombs():
    # """Update the position of all bombs and remove those off the screen."""
    # for bomb in bombs[:]:  # Iterate over a copy of the list
    #     bomb["y"] += bomb["speed"]
    #     if bomb["y"] > 400:  # Remove bombs that move out of bounds
    #         bombs.remove(bomb)
    """Update bomb positions and remove off-screen bombs."""
    for bomb in bombs[:]:  # Iterate over a copy of the list
        bomb["rect"].y += bomb["speed"]  # Move bomb down
        if bomb["rect"].y > 400:  # Remove bombs off-screen
            bombs.remove(bomb)

def draw_bombs():
    # """Draw all bombs on the screen."""
    # for bomb in bombs:
    #     screen.blit(bomb_surface, (bomb["x"], bomb["y"]))
    """Draw bombs on the screen."""
    for bomb in bombs:
        screen.blit(bomb_surface, bomb["rect"].topleft)

seconds = 0

while True:
    #screen.fill((255, 10, 51))
    screen.fill((0, 150, 255))

    screen.blit(text_surface, (20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if FirstKeyPress == False: FirstKeyPress = True
                if WPressed == False: WPressed = True
            if event.key == pygame.K_s:
                if FirstKeyPress == False: FirstKeyPress = True
                if SPressed == False: SPressed = True
            if event.key == pygame.K_a:
                if FirstKeyPress == False: FirstKeyPress = True
                if APressed == False: APressed = True
            if event.key == pygame.K_d:
                if FirstKeyPress == False: FirstKeyPress = True
                if DPressed == False: DPressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if WPressed == True: WPressed = False
            if event.key == pygame.K_s:
                if SPressed == True: SPressed = False
            if event.key == pygame.K_a:
                if APressed == True: APressed = False
            if event.key == pygame.K_d:
                if DPressed == True: DPressed = False
        if event.type == SPAWN_BOMB_EVENT:
            # bombs.append({
            #     "x": random.randint(0, 780),
            #     "y": 0,
            #     "speed": random.randint(4, 8),
            # }) 
            bomb_rect = bomb_surface.get_rect(topleft=(random.randint(0, 780), 0))
            bombs.append({
                "rect": bomb_rect,
                "speed": random.randint(4, 8),
            })
    
        if event.type == TEXT_EVENT:
            seconds = seconds + 1
            text_surface = font.render(str(seconds), True, (0,0,0))
    #snake move left

    if FirstKeyPress == False:
        player_rect.x += 1
        screen.blit(player_surface, player_rect)
    elif WPressed == False and SPressed == False and APressed == False and DPressed == False:
       screen.blit(player_surface, player_rect)
    
    if WPressed == True:
        player_rect.y -= Speed
        screen.blit(player_surface, player_rect)
    elif SPressed == True:
        player_rect.y += Speed
        screen.blit(player_surface, player_rect)
    elif APressed == True:
        player_rect.x -= Speed
        screen.blit(player_surface, player_rect)
    elif DPressed == True:
        player_rect.x += Speed
        screen.blit(player_surface, player_rect)
       
    
    move_bombs()
    draw_bombs()
    player_rect.clamp_ip(screen.get_rect()) #limit player within screen

    #Check if player touches the bomb       
    for bomb in bombs:
        if player_rect.colliderect(bomb["rect"]):
            screen.fill((0, 0, 0))
            seconds = 0
            text_surface = font.render(str(seconds), True, (0,0,0))

    pygame.display.flip()
    clock.tick(60)