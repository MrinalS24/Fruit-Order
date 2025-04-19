import pgzrun
import random

WIDTH = 867
HEIGHT = 550

fruits = []

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

def draw():
    screen.clear()
    screen.fill(color = "pink")
    screen.blit("computer_screen",(0,0))
    number = 1
    for i in fruits:
        i.draw()
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+ 20))
        number += 1


































pgzrun.go()