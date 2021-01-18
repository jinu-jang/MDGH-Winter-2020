def setup():
    global photo, zoom, origH, origW, origPhotoPixels
    photo = loadImage("image1.jpg")
    zoom = 1.0
    origW = photo.width
    origH = photo.height
    
    size(1000, 1000)

def draw():
    global photo
    background(255)
    photo = loadImage("image1.jpg")
    photo.resize(int(origW * zoom), 0)
    image(photo, 0, 0)
    
def mouseDragged():
    global zoom
    
    zoom += float(pmouseY - mouseY) / origW
    
    if (zoom < 0.1):
        zoom = 0.1
