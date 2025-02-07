import pgzrun

HEIGHT=500
WIDTH=500

def draw():
    screen.fill((131,163,162))
    screen.draw.filled_circle((250,250),100,(135,7,97))
    screen.draw.text("This is a circle :)",(50,100),fontname="cursiveboldreadablestylish",fontsize=50,color=(135,7,97),gcolor=(55,0,47),owidth=0.5,ocolor=(50,74,64))

pgzrun.go()