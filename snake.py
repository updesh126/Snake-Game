import os
from pandas_datareader import test
import pygame
import random

pygame.init()
#color
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

def backM():
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1, 0.0)

def welcome():
    exit_game=False
    while not exit_game:
        gamewindow.fill((255,210,200))
        text_screen("Welcome to snakes Game",black,240,250)
        text_screen("Press Space to play",black,290,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    backM()
                    gameloop()
        
        
        pygame.display.update()
        clock.tick(30)





def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 20
    fps = 30
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    score = 0
    snk_list = []

    snk_lenght = 1

    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()


    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            if int(hiscore)>score:
                text_screen("Game Over! press Enter to Continune ", red, 100, screen_height/2)
                text_screen("Hiscore:"+str(hiscore)+"   " +"your Scour:"+str(score),red,200,500)
            else:
                text_screen("Game Over! press Enter to Continune ",red, 100, screen_height/2)
                text_screen("New Hiscore:"+str(hiscore),red,250,500)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10:
                score += 10
                
                pygame.mixer.music.load("sound_1.wav")
                pygame.mixer.music.play()
                pygame.time.delay(100)
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_lenght += 5
                backM()

                if score>int(hiscore):
                    hiscore=score



            gamewindow.fill(white)
            text_screen("score:" + str(score) +"Hiscore:" + str(hiscore), red, 5, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)



            if len(snk_list) > snk_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('sound_2.wav')
                pygame.mixer.music.play()

                
            if snake_x < 0 or snake_y < 0 or snake_x > screen_width or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('sound_2.wav')
                pygame.mixer.music.play()


            # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()