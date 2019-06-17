import unittest
from credential import credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the credential object is initialized properly
        '''
        self.assertEqual(self.new_credential.first_name, "Faith")
        self.assertEqual(self.new-credential.account, "Facebook")
        self.assertEqual(self.new_credential.username, "Faith Ngotho")
        self.assertEqual(self.new_credential.password, "34816809)

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credentisl object is saved to credential array
        '''
        self.new_credential.credential()
        self.assertEqual(len(Credential.credential_list),1)
        
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_user to check if we can save multiple credential
        bjects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = credential("first_name", "last_name", "user_name", "pass")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)
        
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("first_name", "last_name", "user_name", "pass")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_account(self):
        '''
        test to check if we can find a credential by username and display information about
        the credential
        '''

        self.new_credential.save_credential()
        test_credential = Credential("first_name", "last_name", "user_name", "password")
        test_credential.save_credential()
        found_credential = Credential.find_by_username("user_name")

        self.assertEqual(found_credential.username,test_user.username)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''
        self.new_crdential.save_credential()
        test_credential = Credential("first_name", "last_name", "user_name", "pass")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("user_name")
        self.assertTrue(credential_exists)
        
if __name__ == '__main__':
    unittest.main()