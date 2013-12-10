
class LuncherPreferences:
    def __init__(self, name):
        self.name = name
        self.preferences = {}

    def update_preference(self, place, weight):
        """
        everyone's allowed up to 100 points to distribute across their places
        """
        self.preferences[place] = float(weight)

        # normalize if people try to cheat
        total_weight = sum(self.preferences.values())
        if total_weight > 100:
            for place in self.preferences:
                self.preferences[place] = self.preferences[place] * 100. / total_weight

    def parse_preference(cls, filename):
        pass
