from project_app.models import User


class UserClass:

    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.accountType = account_type

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_account(self, account_type):
        self.accountType = account_type

    def get_account(self):
        return self.accountType