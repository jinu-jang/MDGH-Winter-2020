def setup():
    global amugeona
    
    size(900, 900)
    background('#AE329C')
    
    amugeona = 100
    
def draw():
    background('#AE329C')
    # global amugeona
    # amugeona = amugeona + 1
    
    # noStroke()
    stroke('#FE3F9C')
    strokeWeight(10)
    line(amugeona, 100, amugeona + 30, 430)
    
