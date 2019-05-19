class Storage():
    def __init__(self):
        self.values = {}

    def add(self, key, value):
        self.values[key] = value

    def get(self, key):
        if key in self.values:
            return self.values[key]
        else:
            return None
