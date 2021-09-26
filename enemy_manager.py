class EnemyManager:
    def __init__(self) -> None:
        self.left_to_right = True
        self.change_direction_reserved = False
        self.move_down = False

    def reserve_to_change_direction(self):
        self.change_direction_reserved = True

    def update(self):
        if self.change_direction_reserved:
            self.move_down = True
            self.left_to_right = not self.left_to_right
            self.change_direction_reserved = False

    def clear(self):
        self.move_down = False
