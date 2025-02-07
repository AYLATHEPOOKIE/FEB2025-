import pgzrun
from random import randint

TITLE="Shoot Aliens"
WIDTH=500
HEIGHT=500

text=""

alien=Actor("alien") # type: ignore

alien.pos=321,220

def draw():
    screen.fill((13,16,33))
    alien.draw()
    screen.draw.text(text,center=(250,40),fontname="cursivekindaglitchy",fontsize=50)

def on_mouse_down(pos):
    global text
    if alien.collidepoint(pos):
        text="Good hit"
        alien.pos=randint(50,450),randint(50,450)
    else:
        text=("Try again")

def update():
    alien.x+=5
    if alien.x>=500:
        alien.right=0

pgzrun.go()