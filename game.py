# Import a library of functions called 'pygame'
import pygame
import graph as graphs
from graph import Graph
from graph import Node
import drawablenode
from drawablenode import *
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PAD = (5, 5)
ROWS = 10
COLS = 10
WIDTH = 30
HEIGHT = 30
SCREEN_WIDTH = COLS * (PAD[0] + WIDTH) + PAD[1]
SCREEN_HEIGHT = ROWS * (PAD[0] + HEIGHT) + PAD[1]
# Set the height and width of the SCREEN
for x in range(COLS):
    for y in range(ROWS):
        n = Node(x, y)
        if (x >= 5 and x <= 6 and y >= 5 and y <= 8):
            n.walkable = False
leftWall = True if x % COLS == 0 else False
rightWall = True if x % COLS == COLS - 1 else False
topWall = True if y % ROWS == 0 else False
bottomWall = True if y % ROWS == 0 else False

if(leftWall or rightWall or topWall or bottomWall):
    n.walkable = False



SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
search_space = Graph([ROWS, COLS])

NODES = []
for i in range(ROWS):
    for j in range(COLS):
        node = search_space.get_node([i, j])
        NODES.append(DrawableNode(node))
selectionNode = NODES[0]
pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
DONE = False
CLOCK = pygame.time.Clock()
# Click = NODES[1] + NODES[2]

pygame.font.init()
font1 = pygame.font.Font(None, 14)
font2 = pygame.font.Font(None, 28)
while not DONE:
    
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    CLOCK.tick(10)
    
    for event in pygame.event.get():  # User did something
       if event.type == pygame.MOUSEBUTTONDOWN:
           print str(pygame.mouse.get_pos())
           print str(selectionNode.x or selectionNode.y)
       if event.type == pygame.KEYDOWN:
           print "KEYPRESS"
           if pygame.key.get_pressed()[pygame.K_UP]:
            selectionNode.y -= selectionNode.width + 5

           if pygame.key.get_pressed()[pygame.K_DOWN]:
               selectionNode.y += selectionNode.width + 5
           if pygame.key.get_pressed()[pygame.K_LEFT]:
                  selectionNode.x -= selectionNode.width + 5
                
           if pygame.key.get_pressed()[pygame.K_RIGHT]:
               selectionNode.x += selectionNode.width + 5
           if pygame.key.get_pressed()[pygame.K_ESCAPE]:
               DONE = True
       if event.type == pygame.QUIT:  # If user clicked close
            DONE = True
       if selectionNode >= COLS or ROWS:
           walkable = False
          # Flag that we are DONE so we exit this loop
    # All drawing code happens after the for loop and but
    # inside the main while DONE==False loop.

    # Clear the SCREEN and set the SCREEN background
    SCREEN.fill(WHITE)
    # Draw a circle
    for i in NODES:
        i.draw(SCREEN, font1)
    pygame.draw.rect(SCREEN, WHITE, [selectionNode.x, selectionNode.y, selectionNode.width, selectionNode.height])
    
   

    # Go ahead and update the SCREEN with what we've drawn.
    # This MUST happen after all the other drawing commands.
    bg = pygame.Surface((SCREEN.get_size()[0] / 3, SCREEN.get_size()[1] / 3))
    bg.fill(BLACK)
    textrect = bg.get_rect()
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()
