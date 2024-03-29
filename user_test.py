import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
username_login
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Faith", "Ngotho", "faithngotho", "Fai_0796")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the user object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "Faith")
        self.assertEqual(self.new_user.last_name, "Ngotho")
        self.assertEqual(self.new_user.username, "faithngotho")
        self.assertEqual(self.new_user.password, "Fai_0796")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved to user array
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        bjects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("first_name", "last_name", "user_name", "pass")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("first_name", "last_name", "user_name", "pass")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information about
        the user
        '''

        self.new_user.save_user()
        test_user = User("first_name", "last_name", "user_name", "password")
        test_user.save_user()
        found_user = User.find_by_username("user_name")
        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("first_name", "last_name", "user_name", "pass")
        test_user.save_user()
        user_exists = User.user_exist("user_name")
        self.assertTrue(user_exists)
        
if __name__ == '__main__':
    unittest.main()