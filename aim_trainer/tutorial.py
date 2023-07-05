import math
import random
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
TOP_BAR_HEIGHT = 50
TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
LIVES = 3
LABEL_FONT = pygame.font.SysFont("comicsans",24)

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
    pygame.draw.circle(win,self.COLOR,(self.x, self.y),self.size)
    pygame.draw.circle(win,self.SECONDARY_COLOR,(self.x, self.y),self.size * 0.4)
    pygame.draw.circle(win,self.COLOR,(self.x, self.y),self.size * 0.6)
    pygame.draw.circle(win,self.SECONDARY_COLOR,(self.x, self.y),self.size * 0.8)

  def collide(self, x,y):
    dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
    return dis <= self.size

def draw(win, targets):
  # BG COLOR they make it a glob var
  win.fill((0 ,25,40))

  for target in targets:
    target.draw(win)

def formate_time(secs):
  milli = math.floor(int(secs * 1000 % 1000) / 100)
  seconds = int(round(secs % 60, 1))
  minutes = int(secs // 60) # Interger divided by 60
  return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_score_bar(win, elapsed_time, targets_pressed, misses):
  pygame.draw.rect(win,'grey',(0,0, WIDTH, TOP_BAR_HEIGHT))
  time_label = LABEL_FONT.render(f"Time: {formate_time(elapsed_time)}",1, "black")

  win.blit(time_label,(5,5))



def main():
  run = True
  targets = []
  clock = pygame.time.Clock()

  targets_pressed = 0
  clicks = 0
  misses = 0
  start_time = time.time()
  elapsed_time = time.time() - start_time

  pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

  while run:
    clock.tick(60)
    click = False
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
      if(event.type == pygame.QUIT):
        run=False
        break
      if(event.type == TARGET_EVENT):
        x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING )
        y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING )
        targets.append(Target(x,y))
      if event.type == pygame.MOUSEBUTTONDOWN:
        click = True
        clicks += 1

    for target in targets:
      target.update()

      if(target.size <= 0):
        targets.remove(target)
        misses += 1

# Break down tuple into into individual. mouse_pos is a tuple so destructures (splat operator)
      if click and target.collide(*mouse_pos):
        targets.remove(target)
        targets_pressed += 1


    if misses >= LIVES:
      pass #End game

    draw(WIN, targets);
    draw_score_bar(WIN, elapsed_time, targets_pressed, misses)
    pygame.display.update()

  pygame.QUIT

if __name__ == "__main__":
  main()
