import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Sneak Peek')
screen = pygame.display.set_mode((600,500),0,32)
 
player = pygame.Rect(250,300,40,80)
 
tiles = [pygame.Rect(550,450,50,50),pygame.Rect(500,450,50,50),pygame.Rect(450,450,50,50),pygame.Rect(400,450,50,50),pygame.Rect(350,450,50,50),pygame.Rect(300,450,50,50),pygame.Rect(250,450,50,50),pygame.Rect(200,450,50,50),pygame.Rect(150,450,50,50),pygame.Rect(100,450,50,50),pygame.Rect(50,450,50,50),pygame.Rect(0,450,50,50)
,pygame.Rect(50,400,50,50),
pygame.Rect(350,350,50,50),pygame.Rect(100,350,50,50),
pygame.Rect(350,300,50,50),pygame.Rect(100,300,50,50),
pygame.Rect(300,250,50,50),pygame.Rect(150,250,50,50),
pygame.Rect(300,200,50,50),pygame.Rect(150,200,50,50),
pygame.Rect(300,150,50,50),pygame.Rect(150,150,50,50),
pygame.Rect(250,100,50,50),pygame.Rect(200,100,50,50),
pygame.Rect(250,50,50,50),pygame.Rect(200,50,50,50),

pygame.Rect(550,0,50,50),pygame.Rect(0,0,50,50)
]
 
def collision_test(rect,tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions
 
def move(rect,movement,tiles):
    rect.x += movement[0]
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right
    rect.y += movement[1]
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect
 
right = False
left = False
up = False
down = False
    
 
# loop #
while True:
    
    # clear display #
    screen.fill((0,0,0))
 
    movement = [0,0]
    if right == True:
        movement[0] += 5
    if left == True:
        movement[0] -= 5
    if up == True:
        movement[1] -= 5
    if down == True:
        movement[1] += 5
 
    player = move(player,movement,tiles)
 
    pygame.draw.rect(screen,(255,255,255),player)
 
    for tile in tiles:
        pygame.draw.rect(screen,(255,0,0),tile)
    
    # event handling #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
            if event.key == K_LEFT:
                left = True
            if event.key == K_DOWN:
                down = True
            if event.key == K_UP:
                up = True
            if event.key == K_1:
                player = pygame.Rect(player.left,player.top,80,40)
                print("Fell on the side")
            if event.key == K_2:
                player = pygame.Rect(player.left,player.top,40,80)
                print("Stood back up")
            if event.key == K_0:
                print("game info for yall")
                print(player.right)
                print(player.top)

           
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                right = False
            if event.key == K_LEFT:
                left = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_UP:
                up = False

            
    
    # update display #
    pygame.display.update()
    mainClock.tick(60)