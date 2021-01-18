def setup():
    global lastKeyPressed, lastMousePressed
    
    size(500, 500)
    frameRate(1)
    
    lastKeyPressed = ' '
    lastMousePressed = None
    
def draw():
    global lastKeyPressed, lastMousePressed
    
    print('DRAW!!!')
    background(255)
    
    textSize(100)
    fill(0)
    text(lastKeyPressed, 200, 200)
    
    if (lastMousePressed == LEFT):
        text("LEFT BUTTON!", 200, 400)
    elif (lastMousePressed == RIGHT):
        text("RIGHT BUTTON!", 200, 400)
    elif (lastMousePressed == CENTER):
        text("CENTER BUTTON!", 200, 400)
    else:
        text("nothing", 200, 400)
        
        
def keyPressed():
    # print ('!!! Key Press: ', key)
    global lastKeyPressed
    lastKeyPressed = key
    
def mousePressed():
    print("mouse pressed!")
    global lastMousePressed
    lastMousePressed = mouseButton
