
class LunchPlace:
    def __init__(self, name):
        self.name = name
        self.tags = set()

    def add_tag(self, tag):
        self.tags.add(tag)
