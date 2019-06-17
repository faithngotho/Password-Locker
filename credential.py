class Credential:
    """
    Class that generates new instances of credential
    """
    credential_list = []

    def __init__(self, username, account, acc_username, acc_password):
        '''
        Take input to create new credential
        '''
        self.username = username
        self.account = account
        self.acc_username = acc_username
        self.acc_password = acc_password

    def save_credential(self):
        '''
        save_credential method saves user objects into credential_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_account(cls, username, account):
        '''
        Method that takes in an account name and returns credential that matches that account.
        Args:
            account:  account to search for
        Returns :
            Credential of account that matches the account name
        '''
        for credential in cls.credential_list:
            if credential.account == account and credential.username == username:
                return credential

    @classmethod
    def credential_exist(cls, account):
        '''
        Method that checks if a credential exists from the credential array.
        Args:
            account:  account to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for credential in cls.credential_list:
            if credential.account == account:
                return True

    @classmethod
    def display_credential(cls):
        '''
        method that returns the user array
        '''
        return cls.credential_list