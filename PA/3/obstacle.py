import pygame
import random


class Cactus(pygame.sprite.Sprite):
    def __init__(self, images, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = random.choice(images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()


class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self, images, position, speed):
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed

        self.refresh_rate = 10
        self.refresh_counter = 0

    def refresh(self):
        if self.image == self.images[0]:
            self.image = self.images[1]
        else:
            self.image = self.images[0]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.refresh_counter == self.refresh_rate:
            self.refresh()
            self.refresh_counter = 0
        self.refresh_counter += 1

        self.rect.left += self.speed
        if self.rect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


