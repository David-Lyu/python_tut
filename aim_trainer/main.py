import math
import random
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("AIM Trainer")

class Target:
  MAX_SIZE = 30
  GROWTH_RATE = 0.2
  COLOR = 'red'
  SECONDARY_COLOR = 'white'

  def __init__(self,x,y) -> None:
    self.x = x
    self.y = y
    self.size = 0
    self.grow = True

  def update(self):
    if(self.size + self.GROWTH_RATE >= self.MAX_SIZE):
      self.grow = False

    if(self.grow):
      self.size += self.GROWTH_RATE
    else:
      self.size -= self.GROWTH_RATE
  def draw(self, win):
    pygame.draw.circle(win,self.COLOR,(self.x, self.y),self.size * 0.4)
    pygame.draw.circle(win,self.SECONDARY_COLOR,(self.x, self.y),self.size)
    pygame.draw.circle(win,self.COLOR,(self.x, self.y),self.size * 0.6)
    pygame.draw.circle(win,self.SECONDARY_COLOR,(self.x, self.y),self.size * 0.8)

def draw(win, targets):
  # BG COLOR they make it a glob var
  win.fill((0 ,25,40))

  for target in targets:
    target.draw(win)

  pygame.display.update();

def main():
  run = True
  targets = []
  clock = pygame.time.Clock()

  pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if(event.type == pygame.QUIT):
        run=False
        break
      if(event.type == TARGET_EVENT):
        x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING )
        y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING )
        targets.append(Target(x,y))

    draw(WIN, targets);
    for target in targets:
      target.update
  pygame.QUIT

if __name__ == "__main__":
  main()