import pygame
import random
import math
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
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemy=6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("bad.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(35)

# bullet
bulletImg=pygame.image.load("thunder.png")
bulletX= playerX
bulletY= playerY
bulletX_change=0
bulletY_change=10

# if bullet is shown or not
bullet_state="ready"

#score
score_value=0
font = pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

#game over
over_font= pygame.font.Font("freesansbold.ttf",32)

def game_over_text():
    over_text =font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
    
def show_score(x,y):
    score =font.render("Score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bulletImg,(x+16,y+10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<30:
        return True
    else:
        return False
    
def playerCollision(enemyX,enemyY,playerX,playerY):
    distance=math.sqrt((math.pow(enemyX-playerX,2))+(math.pow(enemyY-playerY,2)))
    if distance<30:
        return True
    else:
        return False
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
    for i in range(num_of_enemy):
        #game over
        mainCollision=playerCollision(enemyX[i],enemyY[i],playerX,playerY)
        if mainCollision:
            
            for j in range(num_of_enemy):
                enemyY[j]=2000
            game_over_text()  
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]

    #collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=playerY
            bullet_state="ready"
            score_value+=1
            enemyX[i]= random.randint(0,735)
            enemyY[i]= random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    #brings player    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
    
