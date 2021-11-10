from os import system
from time import sleep
from keyboard import is_pressed

## INPUT DATA ######################################################
frames    = 0

map_width = 10
map_heigh = 10

invader_x = 2
invader_y = 1

bullet_x  = 1
bullet_y  = 10
bullet_shot = False 

player_x  = 2
player_y  = 10
step_x    = 1
## INPUT DATA ######################################################

while True:
    frames +=1

#### INVADER MOVEMENT ##############################################

    if invader_x != 1 and invader_x != map_width:
        invader_x += step_x
    else:
        invader_y += 1
        step_x = step_x * -1
        invader_x += step_x
    
#### INVADER MOVEMENT ##############################################

#### BULLET MOVEMENT ###############################################
    
    if bullet_shot and bullet_y != 1:
        bullet_y -= 1
    elif bullet_x == invader_x and bullet_y == invader_y:
        print("YOU WIN!!!")
        break
    else:
        bullet_shot = False
    
#### BULLET MOVEMENT ###############################################
    system("cls")
## DRAW THE MAP ####################################################

    print()
    for x in range(1, map_width+3):
        print("⍟", end = " ")
    print()

    for y in range(1, map_heigh+1):
        print("⍟", end = " ")
        for x in range(1, map_width+1):
            if x == invader_x and y == invader_y:
                print("👾", end = "")
            elif x == player_x and y == player_y:
                print("😸", end = "")
            elif x == bullet_x and y == bullet_y and bullet_shot: 
                print("💣", end = "")
            else:
                print(".", end = " ")
        print("⍟")

    for x in range(1, map_width+3):
        print("⍟", end = " ")
    print()
    print("frames:", frames)
    print()

## DRAW THE MAP ####################################################
    
###### GAME OVER CONDITIONS ########################################
    if invader_y == map_heigh:
        print("GAME OVER!!!")
        break
###### GAME OVER CONDITIONS ########################################
    
    sleep(0.5)

## INTERACT WITH THE USER ##########################################

    if is_pressed("a") and player_x > 1:
        player_x -= 1
    if is_pressed ("d") and player_x < map_width:
        player_x += 1
    if is_pressed (" "):
        bullet_shot = True
        bullet_y = map_heigh - 1
        bullet_x = player_x  
        
## INTERACT WITH THE USER ##########################################

