import pgzrun,random
from time import time

timeofgame=time()
timetot=0
WIDTH=800
HEIGHT=600
satalitetotal=10

satall=[]
for i in range(satalitetotal):
   sat=Actor("satalite")
   sat.pos=(random.randint(30,790),random.randint(30,590))
   satall.append(sat)

def draw():
   global timetot
   screen.blit("starsbg28th",(0,0))
   for i,j in enumerate(satall,1):
      j.draw()
      screen.draw.text(str(i),(j.pos[0],j.pos[1]+20))
   timetot=time()-timeofgame
   screen.draw.text(str(round(timetot,2)),(20,20),fontsize=30)

def update():
   pass 
pgzrun.go()