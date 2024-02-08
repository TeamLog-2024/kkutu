import pygame
from random import randint as ri

g = 3

class NormalNote:
    speed = g
    # sound = open("sound.mp4")

# class Beterugiusu:
#     sound = "Beterugiusu.mp4"
#     tick = 30
#     # div = 

class Select:
    map = ""
    sound = ""
    tick = 30

pygame.init()
size = [1920, 1080]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("staticmix")

done = False
clock = pygame.time.Clock()

select = input("곡 선택 : ")
music = Select()
music.map = f"{select}.txt"
music.sound = f"{select}.txt"
f = open(music.map, "r")
g = open(music.sound, "r")
map = f.readline()
sound = g.read()

tic = 0
combo = 0
correct = False
notes = []
while not done:
    clock.tick(music.tick)
    moment = int(tic / 5)

    if map[moment] == " ":
        correct = False

    elif map[moment] == "/":
        note = NormalNote
        notes.append(note)
        correct = True

    for i in notes:
        location = ri(1,4)
        pygame.draw.rect(screen, (0,0,255), [560 + (location - 1) * 200, 900 - i.speed, 560 + location * 200, 850 - i.speed], 0)

    if map[moment] == "=":
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255,255,255))

    print(map[moment])
    tic  += 1
    pygame.display.flip()


pygame.quit()