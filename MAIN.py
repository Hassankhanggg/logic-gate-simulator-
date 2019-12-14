#bismillah(starting with the name of ALLAH)
'''alogorithm
1. importing libraries
2. Creating Our First Game Window
3. Changing the Title, Logo and Background Color
4. Adding Images of the gates into Our app
5. Keyboard Input Controls & Key Pressed Event (with mouse drag and drop)
6. Adding Boundaries to Our app
7. Creating the outputs /inputs
8. Movement Mechanics of the buttons
9. Adding a Background Image
10. Creating Bullets for Shooting
11. Collision Detection
12. Adding Text and Displaying logical answer'''

import pygame

#initialize the app
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))
#not gate
notimg = pygame.image.load('NAND.png')
notx = 10
noty = 50
notx_change = 2
noty_change = 0

#and gate
andimg = pygame.image.load('NAND.png')
andx = 20
andy = 50
andx_change = 0
andy_change = 0

#or gate
orimg = pygame.image.load('NAND.png')
orx = 30
ory = 50
orx_change = 0
ory_change = 0

#nand gate
nandimg = pygame.image.load('NAND.png')
nandx = 40
nandy = 50
nandx_change = 0
nandy_change = 0

#nor gate
norimg = pygame.image.load('NAND.png')
norx = 50
nory = 500
norx_change = 0
nory_change = 0

#xor gate
xorimg = pygame.image.load('NAND.png')
xorx = 600
xory = 500
xorx_change = 0
xory_change = 0

def not_gate(x,y):
    screen.blit(andimg,(notx,noty))

def and_gate(x,y):
    screen.blit(andimg,(andx,andy))

def or_gate(x,y):
    screen.blit(andimg,(orx,ory))

def nand_gate(x,y):
    screen.blit(andimg,(nandx,nandy))

def nor_gate(x,y):
    screen.blit(andimg,(norx,nory))

def xor_gate(x,y):
    screen.blit(andimg,(xorx,xory))

#------------MAIN app loop------------------
running = True
while running == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           #if mouse button is pressed cheak wheather it right  or left
        if event.type ==pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                xorx_change -=5
                print('left')
            if event.type == pygame.K_RIGHT:
                print('right')
                xorX_change +=5
        if event.type == pygame.MOUSEBUTTONDOWN:
            #xMOUSE = event.pos[0]
            #yMOUSE = event.pos[1]
            print('right')
            xorx_change += 5

    screen.fill((255,255,255))

    #not_gate()
    #and_gate()
    #or_gate()
    #nand_gate()
    #nor_gate()

    xorx = xorx_change
    xor_gate(xorx,xory)
    pygame.display.update()

