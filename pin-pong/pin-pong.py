from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP]  and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += 5
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w]  and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Pin-pong")
window.fill((124, 57, 2))

font.init()
font1 = font.Font(None, 90)
left_lose = font1.render("LEFT  LOSE!!!", True, (255, 0, 255))
right_lose = font1.render("RIGHT  LOSE!!!", True, (255, 0, 255))

game = True
finish = False
clock = time.Clock()

platform_r=Player('платформа.jpg', 20, 230, 10, 45, 130)
platform_l=Player('платформа.jpg', 640, 230, 10, 45, 130)
ball=GameSprite("м'яч.jpg", 350, 240, 15, 40, 40)

speed_x = 4
speed_y = 4

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill((255, 255, 255))
        platform_l.update_r()
        platform_r.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(platform_l, ball) or sprite.collide_rect(platform_r, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y <= 30 or ball.rect.y >= 470:
            speed_y *= -1
        if ball.rect.x <= 0:
            finish - True
            window.blit(left_lose, (150, 250))
        if ball.rect.x >= 700:
            finish - True
            window.blit(right_lose, (150, 250))
        platform_l.reset()
        platform_r.reset()
        ball.reset()

    clock.tick(80)
    display.update()