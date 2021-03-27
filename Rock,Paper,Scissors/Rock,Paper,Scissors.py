import pygame
import random

#setup pygame and window
pygame.init()
WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Rock, Paper, Scissors")

#sounds
pygame.mixer.music.load('jazz.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops = -1)

#colors
LIGHT_PINK = (255, 182, 193)
REDDISH_HUE = (201, 144, 154)
SHADOW_GREEN = (144, 201, 191)
BLUE_HUE = (144, 183, 201)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#fonts
PLAYER_FONT = pygame.font.SysFont("sansserif", 200, 1)
BUTTON_FONT = pygame.font.SysFont("sanserif", 300, 1)
WIN_FONT = pygame.font.SysFont("sanserif", 300, 1)
PLAY_AGAIN_FONT = pygame.font.SysFont("sanserif", 100, 1)

#load images
img_rock = pygame.image.load("rock.png").convert_alpha()
img_paper = pygame.image.load("paper.png").convert_alpha()
img_scissors = pygame.image.load("scissors.png").convert_alpha()

#text
player_1 = PLAYER_FONT.render("Player 1", 1, BLACK)
win_text = WIN_FONT.render("WINS!", 1, BLACK)
cpu_text = PLAYER_FONT.render("Computer", 1, BLACK)
tie = WIN_FONT.render("TIE!", 1, BLACK)
play = BUTTON_FONT.render("Play", 1, BLACK)
close = BUTTON_FONT.render("Exit", 1, BLACK)
play_again = PLAY_AGAIN_FONT.render("Play again?", 1, WHITE)
menu_return = PLAY_AGAIN_FONT.render("Menu", 1, WHITE)

#game constants
GAP = 111
IMG_WIDTH = 492

#setup clock
FPS = 60
clock = pygame.time.Clock()

#setup game loop
def main():
    
    run = True
    while run:
        play_button, close_button = menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if close_button.collidepoint(pos):
                    run = False
                if play_button.collidepoint(pos):
                    sprites = draw()
                    play = True
                    while play:
                        screen = 1
                        clock.tick(FPS)
                        while screen == 1:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        screen = 0
                                        play = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    player_pick, pos = mouse_click(sprites)
                                    pygame.time.delay(1000)
                                    sprites = draw()
                                    cpu_choice = cpu()
                                    pygame.time.delay(1000)
                                    winner(player_pick, cpu_choice)
                                    play_again_button = continue_playing()
                                    menu_return_button = return_to_menu()
                                    screen += 1
                        while screen == 2:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        screen = 0
                                        play = False
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    pos = pygame.mouse.get_pos()
                                    if menu_return_button.collidepoint(pos):
                                        screen = 0
                                        play = False
                                    if play_again_button.collidepoint(pos):
                                        sprites = draw()
                                        screen = 1
                                #while player == 2:
                                    #pygame.time.delay(1000)
                                    #sprites = draw()
                                    #cpu(sprites)
                                    #player += 1

#setup menu screen
def menu():
    win.fill(SHADOW_GREEN)
    play_width = play.get_rect().width
    play_height = play.get_rect().height
    play_button = pygame.Rect(win.blit(play, (((WIDTH - play_width) / 2) + 10, 210)))
    pygame.draw.rect(win, BLACK, ((WIDTH - play_width) / 2, 200, play_width + 25, play_height + 25), width = 10, border_radius = 50)
    close_width = close.get_rect().width
    close_height = close.get_rect().height
    close_button = pygame.Rect(win.blit(close, (((WIDTH - close_width) / 2) + 10, 610)))
    pygame.draw.rect(win, BLACK, ((WIDTH - close_width) / 2, 600, close_width + 25, close_height + 25), width = 10, border_radius = 50)
    pygame.display.update()
    return play_button, close_button

#draw play screen
def draw():
    win.fill(BLUE_HUE)
    potato = sprites()
    player1_name()
    pygame.display.update()
    return potato

#draw sprites on screen
def sprites():
    rock = pygame.Rect(win.blit(img_rock, (GAP, 250)))
    paper = pygame.Rect(win.blit(img_paper, ((2 * GAP) + IMG_WIDTH, 250)))
    scissors = pygame.Rect(win.blit(img_scissors, ((3 * GAP) + (2 * IMG_WIDTH), 250))) 
    sprites = [rock, paper, scissors]
    return sprites

#draw player 1 on screen
def player1_name():
    player_width = player_1.get_rect().width
    win.blit(player_1, ((WIDTH - player_width) / 2, 0))

#determine which image was clicked
def mouse_click(sprites):
    player_choice = 0
    rock, paper, scissors = sprites
    pos = pygame.mouse.get_pos()
    if rock.collidepoint(pos):
        win.fill(BLUE_HUE)
        win.blit(img_rock, (GAP, 250))
        player1_name()
        pygame.display.update()
        player_choice = 1
    elif paper.collidepoint(pos):
        win.fill(BLUE_HUE)
        win.blit(img_paper, ((2 * GAP) + IMG_WIDTH, 250))
        player1_name()
        pygame.display.update()
        player_choice = 2
    elif scissors.collidepoint(pos):
        win.fill(BLUE_HUE)
        win.blit(img_scissors, ((3 * GAP) + (2 * IMG_WIDTH), 250))
        player1_name()
        pygame.display.update()
        player_choice = 3
    return player_choice, pos

#determine computer choice
def cpu():
    cpu_choice = random.randint(1, 3)
    if cpu_choice == 1:
        win.fill(BLUE_HUE)
        win.blit(img_rock, (GAP, 250))
        cpu_name()
        pygame.display.update()
    elif cpu_choice == 2:
        win.fill(BLUE_HUE)
        win.blit(img_paper, ((2 * GAP) + IMG_WIDTH, 250))
        cpu_name()
        pygame.display.update()
    elif cpu_choice == 3:
        win.fill(BLUE_HUE)
        win.blit(img_scissors, ((3 * GAP) + (2 * IMG_WIDTH), 250))
        cpu_name()
        pygame.display.update()
    return cpu_choice

#draw computer on screen
def cpu_name():
    cpu_width = cpu_text.get_rect().width
    win.blit(cpu_text, ((WIDTH - cpu_width) / 2, 0))
    
#determine who the winner is
def winner(player_choice, cpu_choice):
    if (player_choice == 1 and cpu_choice == 2) or (player_choice == 2 and cpu_choice == 3) or (player_choice == 3 and cpu_choice == 1):
        win.fill(BLUE_HUE)
        cpu_width = cpu_text.get_rect().width
        win.blit(cpu_text, ((WIDTH - cpu_width) / 2, 300))
        win_text_width = win_text.get_rect().width
        win.blit(win_text, ((WIDTH - win_text_width) / 2, 450))
        pygame.display.update()
    elif (cpu_choice == 1 and player_choice == 2) or (cpu_choice == 2 and player_choice == 3) or (cpu_choice == 3 and player_choice == 1):
        win.fill(BLUE_HUE)
        player_width = player_1.get_rect().width
        win.blit(player_1, ((WIDTH - player_width) / 2, 300))
        win_text_width = win_text.get_rect().width
        win.blit(win_text, ((WIDTH - win_text_width) / 2, 450))
        pygame.display.update()
    elif (player_choice == 1 and cpu_choice == 1) or (player_choice == 2 and cpu_choice == 2) or (player_choice == 3 and cpu_choice == 3):
        win.fill(BLUE_HUE)
        tie_width = tie.get_rect().width
        win.blit(tie, ((WIDTH - tie_width) / 2, 400))
        pygame.display.update()

#button to keep playing
def continue_playing():
    play_again_width = play_again.get_rect().width
    play_again_height = play_again.get_rect().height
    play_again_button = pygame.Rect(win.blit(play_again, (((WIDTH - play_again_width) / 2) + 10, 660)))
    pygame.draw.rect(win, WHITE, ((WIDTH - play_again_width) /2, 650, play_again_width + 25, play_again_height + 25), width = 10)
    pygame.display.update()
    return play_again_button

#button to return to menu
def return_to_menu():
    return_width = menu_return.get_rect().width
    return_height = menu_return.get_rect().height
    menu_return_button = pygame.Rect(win.blit(menu_return, (((WIDTH - return_width) / 2) + 10, 810)))
    pygame.draw.rect(win, WHITE, ((WIDTH - return_width) / 2, 800, return_width + 25, return_height + 25), width = 10)
    pygame.display.update()
    return menu_return_button
                
main()
pygame.quit()