import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = location

a=0
pygame.init()
screen = pygame.display.set_mode(size=(800, 600), flags=pygame.RESIZABLE)
screen.fill((60, 240, 250))
pygame.display.set_caption('魂梦怨雪test')
pygame.display.set_icon(pygame.image.load("hmyx.jpg"))
filename=("ball.png")
location = (100, 150)
b = Snake(filename, location)
while True:
    if (a==1):
        break
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            a=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            location = (x, y)
            b = Snake(filename, location)
            screen.blit(b.image, b.rect)
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_ESCAPE):
                a=1
    pygame.display.flip()
pygame.quit()
