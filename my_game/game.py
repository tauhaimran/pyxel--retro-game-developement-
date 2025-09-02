import pyxel
#default fps is 30
#default screen size is 256x256

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
STONE_INTERVAL = 60  # Interval for generating new stones

class Stone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.speed = 1
        self.collided = False

    def update(self):
        self.y += self.speed
        #if self.y > SCREEN_HEIGHT:
           #self.y = 0

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, self.width, self.height, pyxel.COLOR_BLACK)

class App:

    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT ,title="my game")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT * 4 // 5
        self.stones = []
        #self.stone_y = 0 
        #self.stone_x = SCREEN_WIDTH // 2
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
        
        if pyxel.frame_count % STONE_INTERVAL == 0:
            stone_x = pyxel.rndi(0, SCREEN_WIDTH - 8)
            self.stones.append(Stone(pyxel.rndi(0 , SCREEN_WIDTH-8), 0))

        for stone in self.stones:
            stone.update()
        
            if stone.y >= SCREEN_HEIGHT: #if rock goes out of screen
                #self.stone_y = 0 #reset rock position to top
                self.stones.remove(stone) #remove the rock from the list


            #collision detection
            if (stone.y + 8 >= self.player_y)        \
                and (stone.y <= self.player_y + 16)  \
                and (stone.x + 8 >= self.player_x)   \
                and (stone.x <= self.player_x + 16):
                #self.collision = True
                stone.collided = True
                #print("Collision detected!")
            else:
                #self.collision = False
                stone.collided = False
        
    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE) #clear the screen with dark blue color
        
        #pyxel.blt( SCREEN_WIDTH/2 - 10, stone.y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK) # ROCK
        for stone in self.stones:
            stone.draw()
            if stone.collided:
                pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_YELLOW)

        pyxel.blt( self.player_x , SCREEN_HEIGHT*4 // 5, 0, 16, 0, 16,16, pyxel.COLOR_BLACK) #player

        #if self.collision:
            #pyxel.text(SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_YELLOW)

        pass

App() #run the game

 
# Run the game 
# To run the game, you need to install pyxel package. 
# pip install pyxel
# 
# Run the game by executing the following command. 
# python game.py
# 