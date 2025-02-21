import pgzrun, random

WIDTH=600
HEIGHT=500
game_over=False
score=0

bee=Actor("bee")
bee.pos=(300,250)
flower=Actor("flower")
flower.pos=(random.randint(40,560),random.randint(40,460))

def draw():
    screen.blit("bg21st",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score),center=(250,40),fontname="cursiveboldreadablestylish",fontsize=50)
    if game_over:
        screen.fill((237,150,0))
        screen.draw.text("You return to the hive - you collected "+str(score)+" flowers",center=(250,240),fontname="cursiveboldreadablestylish",fontsize=20)

def update():
    global score
    if keyboard.left and bee.x>0:
        bee.x-=5
    if keyboard.right and bee.x<601:
        bee.x+=5
    if keyboard.up and bee.y>0:
        bee.y-=5
    if keyboard.down and bee.y<501:
        bee.y+=5
    if bee.colliderect(flower):
        score+=1
        flower.pos=(random.randint(40,560),random.randint(40,460))

def gameoveristrue():
    global game_over
    game_over=True
clock.schedule(gameoveristrue,60)

pgzrun.go()
