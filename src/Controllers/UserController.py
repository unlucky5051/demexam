from src.Models.Users import *

class UserController:
    def log_in(self,input_login,input_password):
        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False
    def get(self):
        return Users.select().execute()

    def add(self,input_login,input_password,input_name,input_role_id):
        Users.create(login = input_login,password = input_password, name = input_name,role_id = input_role_id)

    def update_status(self,id_user):
        Users.update({Users.status : False}).where(Users.id == id_user).execute()

    @classmethod
    def show(cls,login):
        return Users.get(Users.login == login)

    @classmethod
    def show_user(cls, role_id):
        return Users.select().where(Users.role_id == role_id)

    @classmethod
    def list_user(cls,role_id):
        list= []
        for user in UserController.show_user(role_id):
            list.append(user.login)
        return list



if __name__ == "__main__":
    print(UserController.show('admin_Ekaterina').role.id)