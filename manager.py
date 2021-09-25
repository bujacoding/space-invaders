import enemy


class Manager:
    def __init__(self) -> None:
        pass

    def change_direction(self):
        enemy.left_to_right = not enemy.left_to_right
