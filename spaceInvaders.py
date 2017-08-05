## Space Invaders - Dan Buganim
import turtle
import os

## TODO:
##
##1. Check collisons for the bullet
##2. Make the enemies into clones of turtle instead of stamps so they can move

## Take this down if you want to see something cool
turtle.tracer(1, 0)

SCREEN_X = 700
SCREEN_Y = 700

BORDER_X = 300
BORDER_Y = 300

BARRIER_WIDTH = 80
BARRIER_HEIGHT = 54

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 20
PLAYER_SPEED = 10

ENEMY_SIZE = 20
ENEMY_SPEED = 10
TIME_STEP = 100

BULLET_SPEED = 40
IS_BULLET_ACTIVE = False

UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
SPACE_BAR = "space"

##Shapes
shapes_list = ["enemySpaceShip.gif", "enemySpaceShip2.gif", "enemySpaceShip3.gif", "playerSpaceShip.gif", "barrier.gif", "bullet.gif"]


## Lists
barrier_pos_list = []
barrier_stamp_list = []

enemy_pos_list = []
enemy_stamp_list = []

## Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(SCREEN_X, SCREEN_Y)

## Register Shapess
for i in shapes_list:
    screen.register_shape(i)

##Draw the border
def drawBorder():
    border = turtle.clone()
    border.speed(0)
    border.color("white")
    border.pu()
    border.setposition(-BORDER_X, -BORDER_Y)
    border.pensize(3)
    border.pd()

    for side in range(4):
        border.fd(BORDER_X * 2)
        border.lt(90)

    border.pu()
    border.hideturtle()

## Create the player
player = turtle.clone()
player.color("lightblue")
player.shape("playerSpaceShip.gif")
player.pu()
player.lt(90)
player.setposition(0, -250)

## Create the enemy
enemyStartX = -220
enemyStartY = 150
enemy = turtle.clone()
enemy.shape("enemySpaceShip.gif")
enemy.pu()
enemy.speed(0)
enemy.setposition(enemyStartX, enemyStartY)

##Create the bullet
bullet = turtle.clone()
bullet.shape("bullet.gif")
bullet.speed(0)
bullet.pu()
bullet.hideturtle()

for count in range(5):
    for i in range(0, 441, 40):
        if count == 0:
            enemy.shape("enemySpaceShip3.gif")
        elif count >= 3:
            enemy.shape("enemySpaceShip2.gif")
        else:
            enemy.shape("enemySpaceShip.gif")
    
        if i == 0 and count == 0:
            pass
        else:
            enemy.goto(enemyStartX + i, enemyStartY)
            
        enemyPos = enemy.pos()
        enemy_pos_list.append(enemyPos)

        enemyStamp = enemy.stamp()
        enemy_stamp_list.append(enemyStamp)
        
        if i % 440 == 0 and i != 0:
            enemyStartY -= 40

## Get rid of the real enemy
enemy.goto(10000, 100000)

## Debugging
for i in enemy_pos_list:
    print(i)

## Create the barriers
barrier = turtle.clone()
barrier.shape("barrier.gif")
barrier.pu()
barrier.setposition(-BORDER_X + 105, -BORDER_Y + 150)

for i in range(3):
    barrierPos = barrier.pos()
    barrier_pos_list.append(barrierPos)

    barrierStamp = barrier.stamp()
    barrier_stamp_list.append(barrierStamp)

    barrier.fd(80 + 50)
    

def left():
      playerPos = player.pos()

      if (playerPos[0] - PLAYER_WIDTH) >= -BORDER_X:
          player.goto(playerPos[0] - PLAYER_SPEED, playerPos[1])

def right():    
    playerPos = player.pos()
    
    if (playerPos[0] + PLAYER_WIDTH) <= BORDER_X:
        player.goto(playerPos[0] + PLAYER_SPEED, playerPos[1])

def playerBullet():
    global IS_BULLET_ACTIVE
    bullet.showturtle()

    if IS_BULLET_ACTIVE != True:
        playerPos = player.pos()
        bullet.setposition(playerPos[0], playerPos[1] + BULLET_SPEED)

    IS_BULLET_ACTIVE = True
    
def moveBullet():
    global IS_BULLET_ACTIVE
    if IS_BULLET_ACTIVE == True:
        bullet.sety(bullet.pos()[1] + BULLET_SPEED)

    if bullet.pos() in enemy_pos_list:
        IS_BULLET_ACTIVE = False
        bullet.hideturtle()

    if bullet.pos()[1] >= BORDER_Y:
        IS_BULLET_ACTIVE = False
        bullet.hideturtle()

    ## TODO: bullet-barrier collision detection
##    for i in range(len(barrier_pos_list)):
##        if barrier.pos()[0] < barrier_pos_list[i][0] and  barrier.pos()[0] > barrier_pos_list[i][0] - BARRER_WIDTH / 2  and barrier.pos()[1] >= barrier_pos_list[i][1]:
##             IS_BULLET_ACTIVE = False
##             bullet.hideturtle()   

    turtle.ontimer(moveBullet, 100)
    
def moveEnemy():
    pass 

    turtle.ontimer(moveEnemy, TIME_STEP)

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(playerBullet, SPACE_BAR)
##turtle.onkeypress(playerShot, SPACE_BAR)
turtle.listen()

drawBorder()
moveEnemy()
moveBullet()
##moveBullet()
