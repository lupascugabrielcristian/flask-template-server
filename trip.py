from dataclasses import dataclass

@dataclass(init=False)
class Trip:

    def __init__(self):
        self.id = ""
        self.city = ""
        self.country = ""
        self.userId = ""            # id of the user that created the trip
        self.pariticipants = ""     # list of userId separated by ' '

    def __dict__(self):
        return { 'id': self.id,
            'city': self.city,
            'country': self.country,
            'userId': self.userId,
            'pariticipants': self.pariticipants }
