from app.models.model import Model

class User(Model):

    table = 'users'

    def __init__(self):
        super().__init__()
