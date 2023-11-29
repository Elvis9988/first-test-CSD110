# assigning global variables
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# taking user inputs
color1 = (input("Enter first color: (Enter in lowercase) ")).lower()
color2 = (input("Enter second color: (Enter in lowercase) ")).lower()

# using if and if elif 
if color1 == RED or color1 == BLUE or color1 == YELLOW:
    print()
else:
    print ("Error: Invalid Color 1")
if color2 == RED or color2 == BLUE or color2 == YELLOW:
    print()
else:
    print ("Error: Invalid Color 2")
if color1 == color2:
    print ("The two colors you entered are the same")
        
if color1 == RED:
    if color2 == BLUE:
        print ("PURPLE")
    elif color2 == YELLOW:
        print ("ORANGE")
elif color1 == BLUE:
    if color2 == RED:
        print ("PURPLE")
    elif color2 == YELLOW:
        print ("GREEN")
elif color1 == YELLOW:
    if color2 == RED:
        print ("ORANGE")
    elif color2 == BLUE:
        print ("GREEN")