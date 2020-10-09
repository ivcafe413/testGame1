import pygame

from game.objects.GObject import GObject

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        
# class Head(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self) 
#         self.image, self.rect = load_image('head.jpg', -1)
#         screen = pygame.display.get_surface()
#         self.area = screen.get_rect()
#         self.STEP = 9
#         self.MARGIN = 12
#         self.xstep = self.STEP 
#         self.ystep = 0
#         self.dizzy = 0
#         self.direction = 'right'
class Player(pygame.sprite.Sprite):
    def __init__(self, options):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('ManRun1', -1)
        self.speed = options.speed

        # Movement Flags
        # self.moving = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.collidable = True

    def toggle_movement(self, direction):
        if direction == 'left':
            self.moving_left = not self.moving_left
        elif direction == 'right':
            self.moving_right = not self.moving_right
        elif direction == 'up':
            self.moving_up = not self.moving_up
        elif direction == 'down':
            self.moving_down = not self.moving_down

    def update(self):
        # Movement Update
        self.moving = False
        if self.moving_left:
            dx = -(min(self.speed, self.left))
            self.moving = True
        elif self.moving_right:
            dx = min(self.speed, 800 - self.right)
            self.moving = True
        if self.moving_up:
            dy = -(min(self.speed, self.top))
            self.moving = True
        elif self.moving_down:
            dy = min(self.speed, 600 - self.bottom)
            self.moving = True
            
        if not self.moving:
            return
            
        if not 'dx' in vars():
            dx = 0
        if not 'dy' in vars():
            dy = 0
            
        self.move(dx, dy)

    # def draw(self, surface):
        # pygame.draw.rect(surface, self.color, self.bounds)

def jsonMap(do):
    do.color = (do.r, do.g, do.b)
    do.speed = do.s
    return do