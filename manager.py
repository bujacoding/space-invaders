class Manager:
    def __init__(self) -> None:
        self.left_to_right = True

    def change_direction(self):
        self.left_to_right = not self.left_to_right
