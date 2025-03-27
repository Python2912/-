import pygame
from random import randint
pygame.init()
class GameSprite(pygame.sprite.Sprite):# родительский класс
    def __init__(self, player_image,player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_1(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed
class Player_2(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
        if self.rect.y > height:
            self.rect.y -= randint(0,5)
            self.rect.y = 0
back = (200,200,55)
height = 500
width = 700
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Пинг-понг')
window.fill(back)
clock = pygame.time.Clock()

player1 = Player_1('platform.png', 50, 50, 30, 100, 10)
player2 = Player_2('platform.png', 650,50 , 30, 100, 10)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()

    pygame.display.update()
    clock.tick(40)



