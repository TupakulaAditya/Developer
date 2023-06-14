import pyautogui

#Basic functionalities
screenWidth, screenHeight = pyautogui.size()                   # Returns two integers, the x and y are monitors size....(The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position()            # Returns two integers, the x and y of the mouse cursor's current position.
pyautogui.mouseInfo()                                          # Retrieve the points X & Y on Sreen.
print(screenWidth,screenHeight,currentMouseX,currentMouseY)
print(pyautogui.onScreen(500, 600))                            # returns the boolean value weather that points exist on screen or not.

# Mouse funtionalities
pyautogui.moveTo(1000, 1000, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
'''
Use incase of getting an error - pyautogui.FAILSAFE=False
pyautogui.easeInQuad     # start slow, end fast
pyautogui.easeOutQuad    # start fast, end slow
pyautogui.easeInOutQuad  # start and end fast, slow in middle
pyautogui.easeInBounce   # bounce at the end
pyautogui.easeInElastic  # rubber band at the end

pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)       # moves curser to XY position according to current position.
pyautogui.scroll(100, 200, 120)                                 # (X,Y,Duration) X & Y are not mantory... used to scroll.     
dragTo(x, y, duration=num_seconds)                              # Function drags to the given coordinates by selecting everything in between.
dragRel(x, y , duration=num_seconds)                            # Function drags to the given coordinate relative to current cursor location.
'''
pyautogui.click()
#pyautogui.click(x,y,No.of.clicks,interval,button) = Click the mouse at its current location.

#keyboard Functionalities
for i in range(10):
    pyautogui.write('Hello\n Good Moning \n how are you?', interval=0.01)  # enter a text and enter new line.
    pyautogui.press('enter')                 # Simulate pressing the Enter key.

pyautogui.keyDown('shift')                   # When a user Press a Key
pyautogui.write(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')                     # when a user releases the key
pyautogui.hotkey('ctrl', 'c')                # Used to Press multiple Keys and relesing them from reverse.

im1 = pyautogui.screenshot()                 # Takes Screenshot
# im1.save("Path") to save the ss in specific path.

#Message Box Functionalities
pyautogui.alert('This is an alert box.')
pyautogui.confirm('Shall I proceed?')
pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
pyautogui.prompt('What is your name?')
k= pyautogui.password('Enter password (text will be hidden)')
print(k)


