import pygame
pygame.init()
import math
pi = math.pi 
import random
#from replit import audio
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
width = 800
height = 600
LGREEN = (62, 245, 59)
DGREEN = (40, 143, 39)
YELLOW = (250, 250, 37)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
LILAC = (175, 95, 237)
LBLUE = (80, 221, 242)
DBLUE = (80, 99, 242)
PINK = (245, 144, 188)
CYAN = (0,150,150)

running = True
myClock = pygame.time.Clock()
finish = ["F","I","N","I","S","H"]
#img = pygame.image.load('bird.png')
#img.convert()
backgroundimg = pygame.image.load("background.png")
backgroundimg = pygame.transform.scale(backgroundimg,(width,height))
spritesheet = pygame.image.load("flyingbird.png")

coinpic = pygame.image.load("coin.png")
#------------------------------states of the game
MENUSTATE = 0  # Menu Screen
GAMESTATE = 1  # Play Game
LOSESTATE = 2  # u loose
QUITSTATE = 3
NUMSTATES = 4
#states withen game state: to make flappy bird move
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
HIT_COIN = False
#----------------------drawings for menustate and gamestate    

#-----------------------MENUSTATE------------------------
def displaytext(words,color,x,y,size):
  font = pygame.font.SysFont("arial",size)
  text = font.render(words, True, color)
  textRect = text.get_rect()
  textRect.center = (x,y)
  screen.blit(text,textRect)   
#-------------------------------------will be in main loop
def main_page(screen):
  pygame.draw.rect(screen, LBLUE, (0, 0, 800, 600)) # background drawing
  pygame.draw.rect(screen,LGREEN,(150,100,500,100))
  displaytext('Play Flappy Bird',LILAC,400,150,40)
  pygame.draw.rect(screen,LGREEN,(150,300,500,100))
  displaytext('Quit Game :(',LILAC,400,350,40)
#------------------------GAMESTATE------------------------
def pillars(topGap):
  global rectList
  topRect = pygame.Rect(550,0,100,topGap)
  bottomRect = pygame.Rect(550,topGap+230,100,height)
  rectList.append(topRect)
  rectList.append(bottomRect)
  return rectList

def load_sprites(spritesheet, DIMw,DIMh,offset):
    sprites = []
    W = spritesheet.get_width()//DIMw  #frame width
    H = spritesheet.get_height()//DIMh  #frame height
    for i in range(DIMw*DIMh-offset):  #offset is if there are extra blank frames
        x = i%DIMw*W    #x coordinate of frame
        y = i//DIMw*H   #y coordinate of frame
        sprites.append(spritesheet.subsurface(pygame.Rect(x, y, W, H))) 
        #cuts out the frame onto a subsurface then added to list
    return sprites  #sends the list back to the main program
#---------------------------------------------will be in main loop
def movement(birdrect):
  global acceleration, HIT_COIN, score
  if KEY_UP == True and birdrect[1] >10:
    a = birdrect[1] 
    birdrect[1] -=acceleration
    acceleration-=1
    if birdrect[1] >= a:
      birdrect[1] =a
    if HIT_COIN == True:
        HIT_COIN = False
        score+=1
  else:
    if birdrect[1] <580:
     birdrect[1] +=4
     if HIT_COIN == True:
        HIT_COIN = False
        score+=1
  return birdrect[1]  

def drawCoin(topGap):
  global rectList
  for element in rectList:
    coinrect = pygame.Rect(element[0],topGap+100,70,70)
    return coinrect
    break
  
def draw_background(screen,birdrect,backgroundX):
    global rectList, topGap, score
    screen.blit(backgroundimg,(backgroundX,0))
    screen.blit(backgroundimg,(backgroundX+width,0))
    displaytext("SCORE: "+str(score),WHITE,600,30,32)
    for element in rectList:
      pygame.draw.rect(screen,LGREEN,element) 
    #birdrect.center = 300,ypos
    pygame.draw.rect(screen,BLACK,drawCoin(topGap))
    screen.blit(coinpic,drawCoin(topGap))
    pygame.draw.rect(screen,BLACK,birdrect)
    screen.blit(sprites[framecount//5%len(sprites)],(birdrect))
    #screen.blit(img, birdrect)

#------------------------------------ LOSER PAGE
#--------------------------seen in loop
def losepage(screen):
  pygame.draw.rect(screen,PINK,(0,0,screen.get_width(),screen.get_height()))
  pygame.draw.rect(screen,LBLUE,(150,100,500,100))
  displaytext('Play Again?',DBLUE,400,150,40)
  displaytext('YOU LOSE ^-^ ',RED,400,250,70)
  pygame.draw.rect(screen,LGREEN,(150,300,500,100))
  displaytext('Quit Game :(',LILAC,400,350,40)
#------------------------------------------------------------------
def getNewState(but, curState,x,y):
    if but == 1 and curState == MENUSTATE and 150<x<650 and 100<y<200:
      return GAMESTATE #during menu state if button clicked, gamestate begins
    elif but == 1 and curState == MENUSTATE and 150<x<650 and 300<y<400:
      return QUITSTATE
    elif but ==1 and curState == LOSESTATE and 150<x<650 and 100<y<200:
      print("you lost")
      return GAMESTATE
    elif but ==1 and curState == LOSESTATE and 150<x<650 and 300<y<400: 
      return QUITSTATE
    else :
      print ("check test")
#-------------------------------------rect collision check
def collision(ypos,pilla):
  if ypos.colliderect(pilla):
    return True
  return False
#--------------------------------------MAIN LOOP TIME  
myClock = pygame.time.Clock()
running = True

birdrect = pygame.Rect(100,310,50,50) 
backgroundX = 0
state = MENUSTATE
rectList=[]
rectList = pillars(300)
framecount = 0
topGap = 300 #initial value
score = 0

while running:
  framecount+=1
  sprites = load_sprites(spritesheet, 3,3,0)
  for evnt in pygame.event.get():
    if evnt.type == pygame.QUIT:
      running = False
#----------------------------CHECKING KEY EVENTS
    #KEYDOWN
    if evnt.type == pygame.KEYDOWN:
      if evnt.key == pygame.K_LEFT:
        KEY_LEFT = True
      if evnt.key == pygame.K_RIGHT:
        KEY_RIGHT = True
      if evnt.key == pygame.K_UP and KEY_UP ==False: 
        KEY_UP =True
        acceleration = 15
    if evnt.type == pygame.KEYUP:
      if evnt.key == pygame.K_LEFT:
        KEY_LEFT = False
      if evnt.key == pygame.K_RIGHT :
        KEY_RIGHT = False
      if evnt.key == pygame.K_UP:
        KEY_UP =False
#------------------------CHECKING MOUSE CLICK EVENTS 
    if evnt.type == pygame.MOUSEBUTTONDOWN:
      button = evnt.button
      a,b = evnt.pos
      state = getNewState(button,state,a,b) 
#-----------------------------------------EXIT FOR LOOP
  #CHECK FOR STATE AND EXCECUTE BASED ON SPECIFIC STATE
  if state == MENUSTATE:
    main_page(screen)
  if state ==GAMESTATE:  
    birdrect[1]  = movement(birdrect)
    draw_background(screen,birdrect,backgroundX)
    backgroundX-=2
    if backgroundX<-1*width:
      backgroundX = 0
    for element in rectList:
        element[0]-=3
        if element[0]<70:
          rectList.clear()
          topGap = random.randint(150,450)
          rectList = pillars(topGap)
          drawCoin(topGap)
    for element in rectList:
      if collision(birdrect, element) == True:
        state = LOSESTATE
    if collision(birdrect, drawCoin(topGap)) == True and drawCoin(topGap)[0]==145:
      HIT_COIN = True
      #print(score)                                        #fix collision and check jump
  if state == LOSESTATE:
    losepage(screen)
    birdrect = pygame.Rect(100,310,50,50) 
    backgroundX = 0
    rectList=[]
    rectList = pillars(300)
    framecount = 0
    topGap = 300 #initial value
    score = 0
  if state == QUITSTATE:
    running=False
  pygame.display.flip()
  myClock.tick(60)
pygame.quit()
