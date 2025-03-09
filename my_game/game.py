import pyxel
#default fps is 30
#default screen size is 256x256
class App:

    def __init__(self):
        pyxel.init(160, 120 ,title="my game")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE): #if escape key is pressed
            pyxel.quit() #exit the game

    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE) #clear the screen with dark blue color
        pyxel.text(70, 60, "Start!", pyxel.COLOR_YELLOW) #draw text at x=70, y=60 with yellow color
        pass

App() #run the game

 
# Run the game 
# To run the game, you need to install pyxel package. 
# pip install pyxel
# 
# Run the game by executing the following command. 
# python game.py
# 