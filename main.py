import sys 
import pygame
from settings import settings
from ship import Ship
from bullet import Bullet




class AlienInvasion:
    def __init__(self) :
        pygame.init()
        self.settings = settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
            )
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Shoot the Aliens!")
        self.bg_color = self.settings.bg_color

    def run_game (self):
        while True:
             self._check_events()
             self.ship.update()
             self.bullets.update()
             self._update_secreen()
    def _check_events(self):
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_d:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_a:
                        self.ship.moving_left = True
                    if event.key == pygame.K_SPACE:
                         self._fire_bullet()
                          
                elif event.type == pygame.KEYUP:
                    if event.key ==pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key ==pygame.K_d:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                            self.ship.moving_left = False
                    elif event.key == pygame.K_a:
                            self.ship.moving_left = False
                          

    def _fire_bullet(self):
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)


    def _update_secreen(self):
         self.screen.fill(self.bg_color)
         self.ship.blitme()
         for bullet in self.bullets.sprites():
              bullet.draw_bullet()
         self.ship.update()
         pygame.display.flip()



if __name__ == "__main__":
    print(1)
    ai = AlienInvasion()
    ai.run_game()
