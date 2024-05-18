import pygame 
pygame.init()

class Player():
    def __init__(self,x,y,width,height,image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))  # Зміна розміру зображення
        self.rect = self.image.get_rect()
        self.rect.x = x # координати по ширині
        self.rect.y = y # координати по висоті
        self.width = width # ширина
        self.height = height # висота
    def move(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            self.rect.x -= 3
        if keys [pygame.K_DOWN]:
            self.rect.y += 3
        if keys [pygame.K_RIGHT]:
            self.rect.x += 3
        if keys [pygame.K_UP]:
            self.rect.y -= 3
    def move1(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_a]:
            self.rect.x -= 3
        if keys [pygame.K_s]:
            self.rect.y += 3
        if keys [pygame.K_d]:
            self.rect.x += 3
        if keys [pygame.K_w]:
            self.rect.y -= 3
    def move(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            self.rect.x -= 3
        if keys [pygame.K_DOWN]:
            self.rect.y += 3
        if keys [pygame.K_RIGHT]:
            self.rect.x += 3
        if keys [pygame.K_UP]:
            self.rect.y -= 3

pygame.mixer.music.load('image/sound1.mp3')
pygame.mixer.music.play()

window = pygame.display.set_mode((800, 750))
pygame.display.set_caption("Гра з персонажем")

# Колір фону
bg_color = (255, 255, 255)
player = Player(100, 100, 150, 100, 'image/neymar.jpg')
player2 = Player(300, 100, 150, 100, 'image/messi.jpg')
player3 = Player(300, 300, 150, 100, 'image/CR7.jpg')


background_image = pygame.image.load('image/FIELD2.jpg')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (800, 750)) # задання розмірів фонового зображення
# Головний цикл гри
clock = pygame.time.Clock()
game = True
while game:
    # Перевірка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background_image, (0, 0))    # Оновлення екрану

    window.blit(player.image, (player.rect.x, player.rect.y))  # Відображення зображення гравця
    window.blit(player2.image, (player2.rect.x, player2.rect.y))  # Відображення зображення гравця
    window.blit(player3.image, (player3.rect.x, player3.rect.y))  # Відображення зображення гравця

    player.move()
    player2.move1()
    clock.tick(60)
    pygame.display.update()
pygame.quit()       
        