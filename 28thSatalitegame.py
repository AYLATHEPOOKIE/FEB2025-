import pgzrun,random
from time import time

satcur=0
timeofgame=time()
timetot=0
linedets=[]
WIDTH=800
HEIGHT=600
satalitetotal=10

satall=[]
for i in range(satalitetotal):
   sat=Actor("satalite")
   sat.pos=(random.randint(30,790),random.randint(30,590))
   satall.append(sat)

def draw():
   global timetot,satcur
   screen.blit("starsbg28th",(0,0))
   for i,j in enumerate(satall,1):
      j.draw()
      screen.draw.text(str(i),(j.pos[0],j.pos[1]+20))
   if satcur<satalitetotal:
    timetot=time()-timeofgame
    screen.draw.text(str(round(timetot,2)),(20,20),fontsize=30)
   else:
     screen.draw.text(str(round(timetot,2)),(20,20),fontsize=50) 
   
   for i in linedets:
      screen.draw.line(i[0],i[1],(161,200,230))

def update():
   pass

def on_mouse_down(pos):
   global satcur,linedets
   if satcur<satalitetotal:
      if satall[satcur].collidepoint(pos):
         if satcur:
            linedets.append((satall[satcur-1].pos,satall[satcur].pos))
         satcur+=1
      else:
         linedets=[]
         satcur=0

   

pgzrun.go()