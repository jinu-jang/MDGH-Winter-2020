def setup():
    global photo, zoom
    size(1300, 1000)
    photo = loadImage("image1.jpg")
    
    zoom = 0.95
    frameRate(5)
    
def draw():
    h, w = int(photo.height * zoom), int(photo.width * zoom)
    photo.resize(w, h)
    # photo.resize(w, 0) #이렇게도 가능!
    image(photo, 0, 0)
