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
        self.stone_y = 0 
        self.stone_x = SCREEN_WIDTH // 2
        self.collision = False
        #self.x = 0
        
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE): #if escape key is pressed
            pyxel.quit() #exit the game

        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH - 13:
            self.player_x += 1 #move right
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -3 :   
            self.player_x -= 1 #move left
        
        self.stone_y += 1 #rock falls down
        if self.stone_y > SCREEN_HEIGHT: #if rock goes out of screen
            self.stone_y = 0 #reset rock position to top

        #collision detection
        if (self.stone_y + 8 >= self.player_y)        \
            and (self.stone_y <= self.player_y + 16)  \
            and (self.stone_x + 8 >= self.player_x)   \
            and (self.stone_x <= self.player_x + 16):
            self.collision = True
            #print("Collision detected!")
        else:
            self.collision = False
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE) #clear the screen with dark blue color
        pyxel.blt( SCREEN_WIDTH/2 - 10, self.stone_y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK) # ROCK
        pyxel.blt( self.player_x , SCREEN_HEIGHT*4 // 5, 0, 16, 0, 16,16, pyxel.COLOR_BLACK) #player

        if self.collision:
            pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_YELLOW)

        pass

App() #run the game

 
# Run the game 
# To run the game, you need to install pyxel package. 
# pip install pyxel
# 
# Run the game by executing the following command. 
# python game.py
# 