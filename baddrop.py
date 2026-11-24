import pygame

class Baddrop:
    def __init__(self, x, y):
        self.speed = .25

        self.image = pygame.image.load('baddrop.png').convert_alpha()

        self.image = pygame.transform.scale_by(self.image, 0.025)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, gumdrop):
        # follow the good drop guy 
        if self.rect.x < gumdrop.rect.x:
            self.rect.x += self.speed

        elif self.rect.x > gumdrop.rect.x:
            self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)