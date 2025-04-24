init python:

    class Entity:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def move(self, dx, dy, max_x, max_y):
            self.x = max(0, min(self.x + dx, max_x - 1))
            self.y = max(2, min(self.y + dy, max_y - 1))


    class Player(Entity):
        pass

    class Dust(Entity):
        def respawn(self, max_x, max_y, avoid_pos):
            import random
            while True:
                new_x = random.randint(0, max_x - 1)
                new_y = random.randint(2, max_y - 1)
                if [new_x, new_y] != [avoid_pos.x, avoid_pos.y]:
                    self.x = new_x
                    self.y = new_y
                    break

    grid_size = 8  
    cell_size = 90  

    player = Player(3, 3)
    dust = Dust(0, 0)
    dust.respawn(grid_size, grid_size, player)

    dust_collected = 0

    def try_move_player(dx, dy):
        global dust_collected
        player.move(dx, dy, grid_size, grid_size)

        if player.x == dust.x and player.y == dust.y:
            dust_collected += 1
            dust.respawn(grid_size, grid_size, player)


    
    def decrement_timer():
        global game_time
        game_time -= 1
        if game_time <= 0:
            renpy.jump("dust_game_end")