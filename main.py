from app.models.user import User

def index():
    users = User.select('id', 'email').where('id', '>', 2).take(10).get()
    print(users)


if __name__ == '__main__':
    index()