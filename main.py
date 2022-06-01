import pygame
import random
import time
#ЦВЕТА
BLACK = (0,0,0)
RED = (255,0,0)
BACK = (0,255,0)
#ЗАПУСК БИБЛИОТЕКИ
pygame.init()
#ПАРАМЕТРЫ ЭКРАНА
width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Змейка')
s_size = 20
head_x = width // 2 // s_size * s_size
head_y = height // 2 // s_size * s_size
#ПАРАМЕТРЫ ЗМЕИ
s_size = 20
s_speed = 5
vx = 0
vy = 0

snake = []
s_lenght = 1

def get_food():
    x = random.randint(0, width - s_size) // s_size * s_size
    y = random.randint(0, width - s_size) // s_size * s_size
    return x,head_y
food_x,food_y = get_food()


def show_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win,BLACK,(x[0],x[1],s_size,s_size))

def show_score():
    msg = score_font.render(f'Счёт: {s_lenght-1}',True,BLACK)
    win.blit(msg,(5,5))

#ТАЙМЕР И ГЛАВНАЯ ПЕРЕМЕННАЯ
clock = pygame.time.Clock()
run = True
score_font = pygame.font.SysFont(None, 20)
font = pygame.font.SysFont(None,25)
while run:

    if head_x < 0 or head_x > width - s_size or head_y < 0 or head_y > height - s_size:
        msg = font.render('YOU LOSE!',True,RED)
        win.blit(msg,(200,250))
        pygame.display.update()
        time.sleep(3)
        run = False

    win.fill(BACK)
    show_score()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                vx = 0
                vy = -s_size
            if e.key == pygame.K_DOWN:
                vx = 0
                vy = s_size
            if e.key == pygame.K_LEFT:
                vx = -s_size
                vy = 0
            if e.key == pygame.K_RIGHT:
                vx = s_size
                vy = 0

    head_x += vx
    head_y += vy 

    pygame.draw.rect(win,BLACK,(head_x,head_y,s_size,s_size))

    pygame.draw.rect(win,RED,(food_x,food_y,s_size,s_size))

    pygame.draw.rect(win,BLACK,(head_x,head_y,s_size,s_size))

    snake.append((head_x, head_y))
    if len (snake) > s_lenght:
        del snake [0]

    show_snake(snake)

    if head_x == food_x and head_y == food_y:
        food_x,food_y = get_food()
        s_lenght += 1
    
    pygame.display.update()
    clock.tick(s_speed)

    pygame.display.update()
    clock.tick(s_speed)