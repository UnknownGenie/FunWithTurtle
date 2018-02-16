
# This code moves turtle from one point to another by calculating angle between
# the two points. Angle is calculated using an application of dot product, that
# is further corrected by checking the location of point respective to current
# point, whether left or right so the turtle.left and turtle.right functions can
# be used respectively. 
# This code contains some variables their description is as follows: 

#     These pooints are used to calculate the lines. 
#      np = next point
#      lp = last point
#      cp = current point

#     These variables are used to store co-ordinates of lines
#      l1 = line 1
#      l2 = Line 2

#     left is a boolean that decides the orientation or the angle to take.     
      
      

# Getting necessary files for operation.
import turtle
from math import sqrt,acos,pi

# Calculates dot product of two lines/vectors.
def dot_prod(a, b):
        return sum([x * y for x, y in zip(a, b)])

# Decides whether to rotate turtle left or right
def isleft(p0,p1):
  global left

  x = int(p1[0]-p0[0])
  y = int(p1[1]-p0[1])
  if x:
    if x < 0:
      left =  True
    else:
      left =  False
  else:
    if y > 0:
      left =  True
    else:
      left =  False

# Calculates magnitude of a line or a vector.
def mag(a):
  coordinates_square = [(x ** 2) for x in a]
  return sqrt(sum(coordinates_square))       

# Calculates angle
def get_angle(lp,cp,np):
  global left 
  
  l1 =  [round(x-y) for x,y in zip(cp,lp)]
  l2 =  [round(x-y) for x,y in zip(np,cp)]
  
  isleft(cp,np)
  angle = acos((dot_prod(l1,l2) / (mag(l1) * mag(l2)))) * (180 / pi)
  
  return angle
  
#Draws line from current point to next point given the length and turtle object.
def draw_line(np,l,turtle):
    global lp, left
    
    angle = get_angle(lp,turtle.pos(),np)
    lp = turtle.pos()

# Correction for left/right    
    if turtle.heading() >= 180:
      left = not left
    
    if left:
      turtle.lt(angle)
    else:
      turtle.rt(angle)
    
    turtle.fd(l)
     
#   Draws M.
def draw_M(turtle):
    global lp
    np = (0,100)
    draw_line(np,turtle.distance(np),turtle)
    
    np = (50,40)
    draw_line(np,turtle.distance(np),turtle)
    
    np = (100,100)
    draw_line(np,turtle.distance(np),turtle)
    
    np = (100,0)
    draw_line(np,turtle.distance(np),turtle)    

# Resetting variables to the defaults
    lp = (-100,0)
    turtle.setheading(0)

#   Draws F.     
def draw_F(turtle):
    global lp
    np = (130,70)
    draw_line(np,turtle.distance(np),turtle)
    
    np = (180,70)
    draw_line(np,turtle.distance(np),turtle)

# Changing loation and manually setting the last point.    
    turtle.penup()
    turtle.setpos(130,70)
    lp = (180,70)
    turtle.pendown()
    
    np = (130,100)
    draw_line(np,turtle.distance(np),turtle)
    
    np = (200,100)
    draw_line(np,turtle.distance(np),turtle)

# Resetting to the defaults   
    lp = (-100,0)
    turtle.setheading(0)
    
# Drawing my initials that are M and F.    
def draw_myinitials(ben):
    draw_M(ben)
   
#   Changing location of turtle.
    ben.pu()
    ben.setpos(130,0)
    ben.pd()
    
    draw_F(ben)
    
#   Hiding Turtle. 
    ben.ht()   

# Initializes the turtle and other required objects.    
def initialize():
    global lp,left
    window = turtle.Screen()
    window.bgcolor("white")
    ben = turtle.Turtle()    
    ben.speed(1)  
    ben.width(5)
    
    lp = (-100,0) # last point supposed initially
    left = True 
    return window, ben


window, ben = initialize()
draw_myinitials(ben)
window.exitonclick()
