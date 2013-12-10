from datetime import datetime

class LunchEvent:
    def __init__(self, place, datestring):
        self.place = place
        self.datestring = datestring
        self.date = datetime.strptime(datestring, "%Y-%m-%d")
