import pygame
pygame.init()
screen_width=700
screen_height=500
screen=pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption('Rocket in Space')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("rocket.png")
        self.image=pygame.transform.scale(self.image,(70,100))
        self.rect=self.image.get_rect()

    def update(self,pressed_keys):
        if(pressed_keys[pygame.K_UP]):
            self.rect.move_ip(0,-5)
        if(pressed_keys[pygame.K_DOWN]):
            self.rect.move_ip(0,5)
        if(pressed_keys[pygame.K_RIGHT]):
            self.rect.move_ip(5,0)
        if(pressed_keys[pygame.K_LEFT]):
            self.rect.move_ip(-5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height 

sprites=pygame.sprite.Group()
def start_game():
    rocket=Player()
    sprites.add(rocket)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pressed_keys=pygame.key.get_pressed()
        rocket.update(pressed_keys)
        bg = pygame.image.load("space.png")
        screen.blit(bg,(0,0))
        sprites.draw(screen)
        pygame.display.update()

start_game()