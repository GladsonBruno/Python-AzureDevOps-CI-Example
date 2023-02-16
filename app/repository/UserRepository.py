from app.entity.User import User

class UserRepository:
    def __init__(self):
        # Não necessita de implementação
        pass

    def __generate_users(self):
        users = []
        for x in range(0, 10):
            user_id = x + 1
            username = "Usuario {id}".format(id=user_id)
            email = "usuario-{id}@gmail.com".format(id=user_id)
            user = User(user_id, username, email)
            users.append(user)
        return users

    def get_all(self):
        users = self.__generate_users()
        return users

    def get_by_id(self, id):
        users = self.__generate_users()
        result = list(filter(lambda u: u.id == id, users))

        if len(result) > 0:
            return result[0]
        else:
            return None