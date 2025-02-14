import pgzrun, time
from random import randint

TITLE="Hit the meanies"
WIDTH=500
HEIGHT=500
score=0
text=""

alien=Actor("meanie") # type: ignore

alien.pos=321,220

def draw():
    screen.fill((165,207,181))
    alien.draw()
    screen.draw.text(text,center=(250,40),fontname="cursiveboldreadablestylish",fontsize=50,color=(32,40,36))
    screen.draw.text(str(score),center=(250,100),fontname="cursiveboldreadablestylish",fontsize=40,color=(64,80,72))

def on_mouse_down(pos):
    global text,score
    if alien.collidepoint(pos):
        text="Nice"
        score+=1
        alien.pos=randint(50,450),randint(50,450)
    else:
        text=":("
        score-=1

        
def update():
     alien.y+=10
     if alien.y>=500:
        alien.y=0

pgzrun.go()