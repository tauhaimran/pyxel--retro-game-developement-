import pyxel
#default fps is 30
#default screen size is 256x256

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:

    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT ,title="my game")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.number = 0
        self.x = 0
        
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE): #if escape key is pressed
            pyxel.quit() #exit the game
        
        #if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): #if left mouse button is pressed
            #pyxel.mouse_x
            #pyxel.mouse_y

            #if pyxel.mouse_x >= 110 and pyxel.mouse_x <= 120 and pyxel.mouse_y >= 50 and pyxel.mouse_y <= 70:
                #self.number += 1
            #elif pyxel.mouse_x >= 20 and pyxel.mouse_x <= 40 and pyxel.mouse_y >= 60 and pyxel.mouse_y <= 70:
                #self.number -= 1

    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE) #clear the screen with dark blue color
        pyxel.text( (SCREEN_WIDTH/2) - 10, SCREEN_HEIGHT/2, f"{self.number}", pyxel.COLOR_YELLOW) #draw text at x=70, y=60 with yellow color
        pyxel.text(30, 60, "-", pyxel.COLOR_WHITE) 
        pyxel.text(110, 60, "+", pyxel.COLOR_WHITE) 
        pass

App() #run the game

 
# Run the game 
# To run the game, you need to install pyxel package. 
# pip install pyxel
# 
# Run the game by executing the following command. 
# python game.py
# 