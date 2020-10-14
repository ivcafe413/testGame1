from game.objects.Player import Player

class Game:
    def __init__(self):
        self.gameObjects = []
        options = type('', (), {})()
        options.x = 400
        options.y = 300
        # options.w = 20
        # options.h = 20
        # options.color = (128, 128, 128)
        options.speed = 3

        self.player = Player(options)
        self.gameObjects.append(self.player)

    # Player Actions Available (type == Key Up or Down)
    def action_left(self, type):
        # Overworld
        self.player.toggle_movement("left")

    def action_right(self, type):
        self.player.toggle_movement("right")

    def action_up(self, type):
        self.player.toggle_movement("up")

    def action_down(self, type):
        self.player.toggle_movement("down")

    def update(self):
        # No collision handling yet
        for o in self.gameObjects:
            o.update()