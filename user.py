class User:
    """
    Class to generate new instances of users
    """
    user_list= [] # Empty user list

    def __init__(self, first_name, last_name, username, password):
        '''
        To take user input and to create a new user
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        Method that takes in a username and returns a user that matches that username.
        Args:
            username:  username to search for
        Returns :
            User of person that matches the username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):
        '''
        Method that checks if a user exists from the user array.
        Args:
            username:  username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        