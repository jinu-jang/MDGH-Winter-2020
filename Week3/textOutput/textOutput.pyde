def setup():
    global gulim
    size(300, 300)
    # print(PFont.list())
    gulim = createFont(u'Gulim', 36)
    
def draw():
    textFont(gulim)
    textSize(50)
    fill(0) # 0 == 검은색
    text(u"안녕하세요", 30, 150)
