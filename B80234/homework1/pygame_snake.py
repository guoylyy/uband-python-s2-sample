# -*- coding: utf-8 -*-
import pygame
import random

SCALE = 20  #地图中有多少格
SIZE = 20   #每一格的大小
WIDTH = SCALE * SIZE
HEIGHT = SCALE * SIZE

DIRECT = [[0,-1],[-1,0],[0,1],[1,0]]
dirt = 1 #蛇前进的方向
snake = [[4,3],[5,3],[6,3]]
apple = [3,1]

def screen_show(screen):
    screen.fill([255,255,255])
    img = pygame.image.load("beach_ball.png")
    apple_img = pygame.transform.scale(img,(SIZE,SIZE))
    screen.blit(apple_img, [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2])
    for body in snake:
        pygame.draw.rect(screen, [0, 255,0], [body[0]*SIZE,body[1]*SIZE, SIZE - 1, SIZE - 1])
    #pygame.draw.circle(screen, [255, 0, 0], [apple[0]*SIZE + SIZE / 2, apple[1]*SIZE + SIZE / 2], SIZE/2)
    pygame.display.flip()
def apple_update(): #苹果被吃掉后的位置, 随机位置
    apple[0] = random.randint(0,19)
    apple[1] = random.randint(0,19)
    if [apple[0],apple[1]] in snake:
        apple[0] = random.randint(1, 19)
        apple[1] = random.randint(1, 19)
def end_game():
    if snake.count(snake[0]) >1: #打结
        return True


def snake_update():
    global dirt
    score = 0
    new_body = [0,0]
    new_body[0] = (snake[0][0] + DIRECT[dirt][0]) % SCALE
    new_body[1] = (snake[0][1] + DIRECT[dirt][1]) % SCALE
    if new_body == apple:
        snake.insert(0, new_body)
        apple_update()
        score = score + 10
    else:
        snake.insert(0, new_body)
        snake.pop()
    return score
def show_score(screen):
    score = snake_update()
    font = pygame.font.Font(None,20)
    text = font.render('your score is %d' % (score), True, [255,0,0])
    screen.blit(text,[0,20])
    pygame.display.flip()
def w_down_cb():
    if snake[0][0] != snake[1][0]: #不能后退
        global dirt
        dirt = 0
    #snake_update()

def s_down_cb():
    if snake[0][0] != snake[1][0]:
        global dirt
        dirt = 2
    #snake_update()
def a_down_cb():
    if snake[0][1] != snake[1][1]:
        global dirt
        dirt = 1
   # snake_update()
def d_down_cb():
    if snake[0][1] != snake[1][1]:
        global dirt
        dirt = 3
   # snake_update()
def show_text(screen):
    font = pygame.font.Font(None, 100)
    text = font.render("Game over", True, [255, 0, 0])
    screen.blit(text, [50,50])
    pygame.display.flip()
def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True

    while running:
        pygame.time.delay(200) # 50ms
        snake_update()
        screen_show(screen)
        show_score(screen)

        if end_game():
            show_text(screen)
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    w_down_cb()
                elif event.key == pygame.K_s:
                    s_down_cb()
                elif event.key == pygame.K_a:
                    a_down_cb()
                elif event.key == pygame.K_d:
                    d_down_cb()
    pygame.quit()

if __name__ == '__main__':
    main()
