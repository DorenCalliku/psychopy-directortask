# https://discourse.psychopy.org/t/response-to-mouse-button-up-mouse-release-instead-of-mouse-button-down/6576/3
#import modules
from psychopy.visual import Window, Rect
from psychopy.event import  Mouse

#initialise screen and mouse
display = (1366,768)
win = Window(size=display, color='white', fullscr=False, units = 'pix')
mouse = Mouse(visible=True)

#create box object
box = Rect(win,width=420,height=50, lineWidth = 3,lineColor='black', pos=(0,0), fillColor = (0.9,0.7,0.7))

#show box object until mouse click
mouse_has_been_pressed = False
while True:
    box.draw()

    if mouse.isPressedIn(box, buttons=[0] ):  # left button press
        mouse_has_been_pressed = True

    if not mouse.isPressedIn(box, buttons=[0] ) and mouse_has_been_pressed == True:
        win.close()
        mouse_has_been_pressed = False

    win.flip()
