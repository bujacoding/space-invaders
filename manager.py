class Manager:
    def __init__(self) -> None:
        self.left_to_right = True
        self.change_direction_reserved = False

    def reserve_to_change_direction(self):
        self.change_direction_reserved = True

    def update(self):
        if self.change_direction_reserved:
            self.left_to_right = not self.left_to_right
            self.change_direction_reserved = False
