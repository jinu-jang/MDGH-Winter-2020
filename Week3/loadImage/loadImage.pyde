def setup():
    global photo
    
    size(900, 900)
    photo = loadImage("image1.jpg")
    
def draw():
    image(photo, 0, 0)
    
