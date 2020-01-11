import pygame
import random
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# background
background=pygame.image.load("background.png")

# title icon
pygame.display.set_caption("space shooter")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# player image
playerImg= pygame.image.load("space.png")
playerX= 370
playerY= 480
playerX_change=0
playerY_change=0

# enemy
enemyImg=pygame.image.load("bad.png")
enemyX= random.randint(0,800)
enemyY= random.randint(50,150)
enemyX_change=2
enemyY_change=35

# bullet
bulletImg=pygame.image.load("thunder.png")
bulletX= playerX
bulletY= playerY
bulletX_change=0
bulletY_change=10

# if bullet is shown or not
bullet_state="ready"

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bulletImg,(x+16,y+10))

# game loop that makes sure the window doesnt close
running = True
while running:
    # background gets set
    screen.fill((0, 0, 0))
    
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # keystrokes
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_w or event.key==pygame.K_UP:
                playerY_change=-3
            if event.key== pygame.K_s or event.key==pygame.K_DOWN:
                playerY_change=+3
            if event.key== pygame.K_a or event.key==pygame.K_LEFT:
                playerX_change=-3
            if event.key== pygame.K_d or event.key==pygame.K_RIGHT:
                playerX_change=3
            if event.key== pygame.K_SPACE:
                if  bullet_state is "ready":
                    bulletX=playerX
                fire_bullet(bulletX,playerY)
        if event.type== pygame.KEYUP:
            if event.key== pygame.K_a or event.key== pygame.K_d or  event.key==pygame.K_RIGHT  or event.key==pygame.K_LEFT or event.key== pygame.K_s or event.key==pygame.K_DOWN or event.key== pygame.K_w or event.key==pygame.K_UP:
                playerX_change=0
                playerY_change=0
            
    #boundarys
    playerY+=playerY_change
    playerX+=playerX_change

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    elif playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY=536
    
    #bullet movement
    if bulletY<0:
        bulletY=playerY
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
        
        
    #enemy
    enemyX += enemyX_change

    if enemyX<=0:
        enemyX_change=2
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-2
        enemyY+=enemyY_change

    
    #brings player    
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    
