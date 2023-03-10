import json

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)