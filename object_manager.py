class ObjectManager():
    def __init__(self):
        self.objects = []

    def append(self, object):
        self.objects.append(object)

    def update(self, canvas):
        for object in self.objects:
            object.update(canvas)

    def render(self, canvas):
        for object in self.objects:
            object.render(canvas)

    def kill(self, object):
        object.onKilled()

        self.objects.remove(object)
