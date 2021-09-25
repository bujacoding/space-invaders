from enemy import left_to_right


class Manager:
    def __init__(self) -> None:
        pass

    def change_direction(self):
        global left_to_right
        left_to_right = not left_to_right
