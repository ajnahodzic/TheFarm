import random
import string

class Implement:
    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def get_implement_type(self):
        return None

class Sprayer(Implement):
    def __init__(self, filling_type):
        super().__init__()
        self.filling_type = filling_type

    def get_implement_type(self):
        return f"Sprayer filled with {self.filling_type}"

class Mower(Implement):
    def __init__(self):
        super().__init__()

    def get_implement_type(self):
        return f"Mower"

class Driller(Implement):
    def __init__(self):
        super().__init__()

    def get_implement_type(self):
        return f"Driller"