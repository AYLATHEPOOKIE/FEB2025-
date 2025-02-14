import pgzrun
from random import randint

TITLE="Hit the meanies"
WIDTH=500
HEIGHT=500
score=3
text=""
gameover=False
alien=Actor("meanie") # type: ignore

alien.pos=321,220

def draw():
    screen.fill((165,207,181))
    alien.draw()
    screen.draw.text(text,center=(250,40),fontname="cursiveboldreadablestylish",fontsize=50,color=(32,40,36))
    screen.draw.text(str(score),center=(250,100),fontname="cursiveboldreadablestylish",fontsize=40,color=(64,80,72))
    if gameover: 
     screen.fill((0,30,0))
     screen.draw.text("GAME OVERR!! \n The meanies have taken over.",center=(250,250),fontname="cursiveboldreadablestylish",fontsize=37,color=(160,200,180))  

def on_mouse_down(pos):
    global text,score,gameover
    if alien.collidepoint(pos):
        text="Nice"
        score+=1
        alien.pos=randint(50,450),randint(50,450)
    else:
        text=":("
        score-=1
        if score<1:
            gameover=True

        
def update():
     alien.y+=10
     if alien.y>=500:
        alien.y=0

pgzrun.go()