from errors import InputError


class UserCreate:
    def __init__(self, username, password, comfpassword):
        if not username or not password:
            raise InputError('Username and password must have some value')
        if password != comfpassword:
            raise InputError("Password's didn't mach")
        self.username = username
        self.password = password
        self.comfpassword = comfpassword

    @staticmethod
    def read_user(request):
        username = request.form['username']
        password = request.form['password']
        comfpassword = request.form['confirm password']
        return UserCreate(username, password, comfpassword)
