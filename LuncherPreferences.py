
class LuncherPreferences:
    def __init__(self, name):
        self.name = name
        self.preferences = {}

    def update(self, place, weight):
        self.preferences[place] = float(weight)

    def normalize(self):
        """
        everyone's allowed up to 100 points to distribute across their places
        after all preferences are placed, normalize to be out of 100
        """
        total_weight = sum(self.preferences.values())
        for place in self.preferences:
            self.preferences[place] = self.preferences[place] * 100. / total_weight
