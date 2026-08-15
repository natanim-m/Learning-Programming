import pygame
import random as r
pygame.init()
size=400,400 #divisble into 20x20, easy size, rectangular size will take more thinking for good proportions, this is square
screen=pygame.display.set_mode(size)
black=0,0,0
running=True
green=124,252,0 # snake color, green, dim to 87, 176, 0
red=164,0,0 # apple color, red, dim to 115, 0, 0
white=255,255,255
keybinds = {
"up": [pygame.K_w, pygame.K_UP],
"down": [pygame.K_s, pygame.K_DOWN],
"right": [pygame.K_d, pygame.K_RIGHT],
"left": [pygame.K_a, pygame.K_LEFT]
}
class Start_Button:
    def __init__(self, color, x, y, width, height, text):
        super().__init__()
        self.rect=pygame.Rect(x,y,width,height)
        self.color=color
        self.text=text
        self.x=self.rect.x
        self.y=self.rect.y
        self.font=pygame.font.Font(None,30)
        self.text_surface = self.font.render(text,True,black)
        self.text_rect=self.text_surface.get_rect(center=self.rect.center)
    def buttoncreator(self, surface):
        pygame.draw.rect(surface,self.color,self.rect,border_radius=5)
        surface.blit(self.text_surface,self.text_rect)
        
class floatingText:
    def __init__(self,x,y,color,text):
        self.x=x
        self.y=y
        self.color=color
        self.text=text
        self.font=pygame.font.Font(None,40)
        self.alpha=255
    def textcreator(self,surface):
        text_surface = self.font.render(self.text, True, self.color).convert_alpha()
        surface.blit(text_surface, (self.x, self.y))
class Snake(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x=200
        self.rect.y=200
        self.x_change=0
        self.y_change=0
    def update(self,body,):
        global rollback
        next_x=self.rect.x+self.x_change
        next_y=self.rect.y+self.y_change
        static=self.x_change==0 and self.y_change==0
        if (next_x,next_y) in body and not static:
            rollback=True
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        if rollback==True:
            self.rect.x-=self.x_change
            self.rect.y-=self.y_change
            self.y_change=0
            self.x_change=0

class Apple(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.randomize(body)
    def randomize(self,body):
        while True:
            self.rect.x=r.randrange(0,400,20)
            self.rect.y=r.randrange(0,400,20)
            if (self.rect.x,self.rect.y) not in body:
                break
gameOver=False
gameStarted = False
clock=pygame.time.Clock()
player_snake = Snake(green,20,20)
body=[(200,200)]
initapple=Apple(red,20,20)
start_btn = Start_Button(green, 135, 175, 130, 50, "START")
restart_btn = Start_Button(green, 140, 250, 130, 50, "RESTART")
gameOverText = floatingText(120,150,white,"GAME OVER!")
frame_counter=0
pendingchange_x=0
pendingchange_y=0
rollback=False
def resetFunc():
    global gameOver
    global pendingchange_x
    global pendingchange_y
    global gameOver
    global rollback
    global player_snake
    body[1:]=[]
    body[0] = (200,200)
    initapple.randomize(body)
    pendingchange_x=0
    pendingchange_y=0
    player_snake.x_change=0
    player_snake.y_change=0
    player_snake.rect.x=200
    player_snake.rect.y=200
    gameOver=False
    rollback=False
def gameOverscreen():
    dimmingoverlay=pygame.Surface((400,400), pygame.SRCALPHA)
    dimmingoverlay.fill((0,0,0,170))
    screen.blit(dimmingoverlay,(0,0))
    restart_btn.buttoncreator(screen)
    gameOverText.textcreator(screen)
while running:
    screen.fill(black)
    head_pos = (player_snake.rect.x, player_snake.rect.y)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if gameOver and event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if restart_btn.rect.collidepoint(event.pos):
                resetFunc()
        if not gameStarted and event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if start_btn.rect.collidepoint(event.pos):
                gameStarted=True
        if gameStarted and event.type==pygame.KEYDOWN:
            if event.key in keybinds["up"] and player_snake.y_change==0 and not gameOver:
                pendingchange_x=0
                pendingchange_y=-20
            if event.key in keybinds["down"] and player_snake.y_change==0 and not gameOver:
                pendingchange_x=0
                pendingchange_y=20
            if event.key in keybinds["right"] and player_snake.x_change==0 and not gameOver:
                pendingchange_x=20
                pendingchange_y=0
            if event.key in keybinds["left"] and player_snake.x_change==0 and not gameOver:
                pendingchange_x=-20
                pendingchange_y=0
    if not gameStarted:
        start_btn.buttoncreator(screen)
    else:
        frame_counter+=1
        if frame_counter % 15==0 and not gameOver:
            player_snake.x_change=pendingchange_x
            player_snake.y_change=pendingchange_y
            if not head_pos in body[1:]:
                player_snake.update(body)
            if (
                player_snake.rect.x < 0
                or player_snake.rect.x >= 400
                or player_snake.rect.y < 0
                or player_snake.rect.y >= 400
                ):
                    rollback=True
                    gameOver=True
                    player_snake.rect.x -= player_snake.x_change
                    player_snake.rect.y -= player_snake.y_change
                    player_snake.x_change = 0
                    player_snake.y_change = 0

            if player_snake.x_change != 0 or player_snake.y_change != 0:
                if not gameOver:
                    body.insert(0,(player_snake.rect.x,player_snake.rect.y))
                if initapple.rect.x==player_snake.rect.x and initapple.rect.y==player_snake.rect.y:
                    initapple.randomize(body)
                else:
                    body.pop()
            body[0] = (player_snake.rect.x, player_snake.rect.y)
            next_tile = (player_snake.rect.x + player_snake.x_change, player_snake.rect.y + player_snake.y_change)
            if next_tile in body[:-1]:
                gameOver = True
        for segment in body:
            screen.blit(player_snake.image,segment)
        screen.blit(initapple.image,initapple.rect)
        if gameOver:
            gameOverscreen()
    pygame.display.flip()
    clock.tick(60)