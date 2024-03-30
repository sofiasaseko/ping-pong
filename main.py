from pygame import*
from random import randint

SCREENSIZE=(700,700)
BACKCOLOR=(176,196,222)

window=display.set_mode(SCREENSIZE)
display.set_caption('ping-pong')

timer=time.Clock()

run=True

class GameSprite(sprite.Sprite):
    def __init__ (self,img,x,y,speed,width,height):
        super().__init__()
        self.image=transform.scale(image.load(img),(width,height))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y +  self.rect.height< SCREENSIZE[1]:
            self.rect.y +=self.speed

    def update_right(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y +  self.rect.height< SCREENSIZE[1]:
            self.rect.y +=self.speed

class Ball(sprite.Sprite):
    def __init__(self,img,x,y,speed_x,speed_y,width,height):
        super().__init__()
        self.image=transform.scale(image.load(img),(width,height))
        self.speed_x=speed_x
        self.speed_y=speed_y
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def update_ball(self):
        self.rect.x +=self.speed_x
        self.rect.y +=self.speed_y

        if sprite.collide_rect(self,platform_left) or sprite.collide_rect(self,platform_right):
            self.speed_x *= -1

        if self.rect.y <0 or self.rect.y> SCREENSIZE[1] - self.rect.height:
            self.speed_y *= -1

    def who_lose(self):
        if self.rect.x > SCREENSIZE[0] - self.rect.width:
            return "right"
        elif self.rect.x < 0:
            return "left"

platform_left = Player("платформа.jpeg",20,320,4,25,99)
platform_right = Player("платформа.jpeg",660,320,4,25,99)

x = randint(-5,5)
y = randint(-5,5)

ball = Ball("шар.png",330,330,x,y,50,50)

finish= False

font.init()
font=font.Font(None,50)

while run:
    for e in event.get():
        if e.type == QUIT:
            run=False
    if finish != True:
        window.fill(BACKCOLOR)
        platform_left.reset()
        platform_right.reset()
        platform_left.update_left()
        platform_right.update_right()
        ball.reset()
        ball.update_ball()

        if ball.who_lose() == "right":
            lose = font.render("RIGHT LOSE",True,(255,0,0))
            window.blit(lose,(240,20))
            finish=True

        if ball.who_lose() == "left":
            lose = font.render("Left LOSE",True,(255,0,0))
            window.blit(lose,(240,20))
            finish=True

    display.update()
    timer.tick(60)