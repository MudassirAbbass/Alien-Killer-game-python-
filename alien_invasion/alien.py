import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Draw the alien as a simple colored rectangle (no image needed).
        self.image = pygame.Surface((40, 30))
        self.image.fill((100, 255, 100))
        # Draw a simple face on the alien
        pygame.draw.circle(self.image, (0, 0, 0), (13, 12), 4)   # left eye
        pygame.draw.circle(self.image, (0, 0, 0), (27, 12), 4)   # right eye
        pygame.draw.rect(self.image, (0, 0, 0), (10, 22, 20, 3)) # mouth

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
