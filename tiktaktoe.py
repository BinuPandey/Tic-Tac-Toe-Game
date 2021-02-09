#1. Using turtle to draw the board
#2. Creating functions to draw "X" and "O"
#3. Set it up to enter numbers 1 through 9, so that computer draws "X"s and "O"s in the corresponding spot
# For eg: _1|_2|_3|
#         _4|_5|_6|
#         _7|_8|_9|
#4. Creating a representation of the board in the code so that computer knows the state of the game
#5. Using turtle to give announcement to the players if they pickup invalid spot. For eg: if spot (2) is already
#   taken by you or the other player, and you pick it again, then you'll get notified 
#6. Creating function to check if anyone win the game, and use turtle to announce the victory of a correct winner
#7. Creating function for the computer to play as "O"
#8. Check if the computer won
#9. Creating a function to check if it's a tie, and use turtle to announce if it was a tie

# Let's Code.......................................................
#1. Using turtle to draw the board
import turtle 

# Draw the grid of the board
def drawBoard():
  # Draw both horizontal lines
  for i in range(2):
    drawer.penup()
    drawer.goto(-300, 100 - 200 * i)
    drawer.pendown()
    drawer.forward(600)
  drawer.right(90)
  # Draw both vertical lines
  for i in range(2):
    drawer.penup()
    drawer.goto(-100 + 200 * i, 300)
    drawer.pendown()
    drawer.forward(600)
        
# Update the screen with the new changes
  screen.update()

# Defining Turtle instance
drawer = turtle.Turtle()
drawer.pensize(5)
drawer.speed(6)
drawer.ht()

# setting up turtle color to purple 
drawer.color("Purple")

# getting a Screen to work on 
screen = turtle.Screen()
#screen.tracer(0)

#Draw the board
drawBoard()


