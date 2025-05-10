import pgzrun
import random
import time
#import kivy

#from kivy import Clock


WIDTH = 867
HEIGHT = 550

fruits = []
lines = []

starttime = 0
totaltime = 0

nextfruit = 0

apple = Actor("apple")
fruits.append(apple)
orange = Actor("orange")
fruits.append(orange)
pineapple = Actor("pineappe")
fruits.append(pineapple)
banana = Actor("banana")
fruits.append(banana)
grapes = Actor("grapes")
fruits.append(grapes)
guava = Actor("guava")
fruits.append(guava)
lychee = Actor("lychee")
fruits.append(lychee)
mango = Actor("mango")
fruits.append(mango)
pear = Actor("pear")
fruits.append(pear)
watermelon = Actor("watermelon")
fruits.append(watermelon)

for fruit in fruits:
    fruit.pos = (random.randint(60,800),random.randint(70,500))


random.shuffle(fruits)

starttime = time.time()
counter = 0
timecount = 5

def timer():
    global counter
    if timecount == 0:
        counter =+ 1
    timecount -= 1



def draw():
    global totaltime
    screen.clear()
    screen.fill(color = "pink")
    screen.blit("computer_screen",(0,0))
    number = 1
    for i in fruits:
        i.draw()
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+ 20))
        number += 1
    for m in lines:
        screen.draw.line(m[0],m[1], (255,255,255))
    """if nextfruit < len(fruits):
        totaltime = time.time() - starttime
        screen.draw.text(str(round(totaltime, 1)), (25,25), color = "white")
    else:
        screen.draw.text(str(round(totaltime, 1)), (25,25), color = "white")"""
    
    if nextfruit < len(fruits):
        timer()
        screen.draw.text(str(counter),(25,25),color = "white" )


    



def on_mouse_down(pos):
    global lines, nextfruit
    if nextfruit < len(fruits):
        if fruits[nextfruit].collidepoint(pos):
            if nextfruit:
                lines.append((fruits[nextfruit-1].pos,fruits[nextfruit].pos))
            nextfruit += 1
        else:
            lines = []
            nextfruit = 0


#Clock.schedule_interval(timer,5)



































pgzrun.go()