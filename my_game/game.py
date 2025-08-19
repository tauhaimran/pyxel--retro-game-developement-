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
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT * 4 // 5
        self.number = 0
        #self.x = 0
        
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE): #if escape key is pressed
            pyxel.quit() #exit the game

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += 2 #move right
        elif pyxel.btn(pyxel.KEY_LEFT):   
            self.player_x -= 2 #move left
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE) #clear the screen with dark blue color
        pyxel.blt( SCREEN_WIDTH/2 - 10, 0, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK) # ROCK
        pyxel.blt( SCREEN_WIDTH/2 , SCREEN_HEIGHT*4 // 5, 0, 16, 0, 16,16, pyxel.COLOR_BLACK) #player
        pass

App() #run the game

 
# Run the game 
# To run the game, you need to install pyxel package. 
# pip install pyxel
# 
# Run the game by executing the following command. 
# python game.py
# 