from datetime import datetime

class LunchVisit:
    def __init__(self, place, datestring):
        self.place = place
        self.datestring = datestring
        self.date = datetime.strptime(datestring, "%Y-%m-%d")

        self.discount = 1
        self.compute_discount()

    def compute_discount(self):

        # FIXME this could be a thousand times smarter..
        days_since = (datetime.now() - self.date).days
        if days_since <= 7:
            self.discount = 0
        elif days_since <= 7*2:
            self.discount = 1/3.
        elif days_since <= 7*3:
            self.discount = 2/3.
        else:
            self.discount = 1

