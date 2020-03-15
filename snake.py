import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('eric - snake')

fclock = pygame.time.Clock()

food = (4, 5)
body = [(1, 1), (1, 2)]
head = (1, 3)

times = 0
direction = "right"
old_direction = "right"
alive = True
pause = False

BLOCK = 0, 0, 0
GREEN = 0, 255, 0
RED = 255, 0, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255
back_color = WHITE


def new_draw_rect(zb, color, screen):
    pygame.draw.rect(screen, color, ((zb[1]) * 50 + 1, (zb[0]) * 50 + 1, 48, 48))


def get_front(head, direction):
    x, y = head
    if direction == "up":
        x = x - 1
    elif direction == "left":
        y = y - 1
    elif direction == "down":
        x = x + 1
    elif direction == "right":
        y = y + 1
    return x % 12, y % 16


def ask_alive(front, body):
    x, y = front
    if x < 0 or x > 12 or y < 0 or y > 16:
        return False
    if front in body:
        return False
    return True


def new_food(head, body):
    i = 0
    while i < 100:
        x = random.randint(0, 11)
        y = random.randint(0, 15)
        if (x, y) != head and (x, y) not in body:
            return (x, y), True
        i += 1
    else:
        return (0, 0), False


def direction_yes_no(direction, old_direction):
    d = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if d[direction] == old_direction:
        return old_direction
    return direction


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_SPACE:
                pause = not pause
    print(times, alive, pause)
    if times >= 20 and alive and (not pause):
        direction = direction_yes_no(direction, old_direction)
        old_direction = direction
        front = get_front(head, direction)
        alive = ask_alive(front, body)
        if alive:
            body.append(head)
            head = front
            print(head, front, food)
            if food == head:
                food, alive = new_food(head, body)
            else:
                body.pop(0)
        else:
            back_color = BLOCK
            pygame.display.set_caption("eric - game over")
        times = 0
    else:
        times += 1

    screen.fill(back_color)
    new_draw_rect(food, RED, screen)
    for i in body:
        new_draw_rect(i, BLUE, screen)
    new_draw_rect(head, GREEN, screen)

    fclock.tick(100)
    pygame.display.update()

