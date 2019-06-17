#!/usr/bin/env python3.6
import random
from user import User
from credential import Credential

def create_user(first_name, last_name, username, password):
    '''
    Function to create new user
    '''
    new_user = User(first_name, last_name, username, password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def check_existing_users(username):
    '''
    Function to check is a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def create_credential(username, account, acc_username, acc_password):
    '''
    Function to create new credential
    '''
    new_credential = Credential(username, account, acc_username, acc_password)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    Function to delete cred
    '''
    credential.delete_credential()

def find_credential(username, account):
    '''
    Function that finds a credential by username and returns the credential
    '''
    return Credential.find_by_account(username, account)

def check_existing_credential(username):
    '''
    Function to check is a credential exists with that username and return a Boolean
    '''
    return Credential.credential_exist(username)

def display_credential():
    '''
    Function that returns all saved credential
    '''
    return Credential.display_credential()

def main():
    print("Hello, Welcome to Password Locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use the following short codes : ca - create a new account, da - delete account, li -log into your account, ex -exit the password locker")

        short_code = input().lower()

        if short_code == 'ca':
            print("Create Account.")
            print("-"*20)
            print ("First name: ")
            first_name = input()
            print("-"*20)
            print("Last name: ")
            last_name = input()
            print("-"*20)
            print("Username: ")
            username = input()
            print("-"*20)
            print("Password: ")
            password = input()

            save_user(create_user(first_name,last_name,username,password))

            print("-"*20)
            print(f"{first_name} {last_name}'s account created successfully.")
            print ('\n')

        elif short_code == 'da':
            print('Enter the username of the account you would like to delete')
            delete_account = input()

            if check_existing_users(delete_account):
                search_user = find_user(delete_account)
                print("Enter your password")
                password = input()

                if password == search_user.password:
                    print(f"Are you sure you want to delete account {search_user.first_name} {search_user.last_name}")
                    print("y - yes, n - no")
                    choice = input().lower()

                    if choice == 'y':
                        del_user(search_user)
                        print(f"{search_user.first_name} {search_user.last_name}'s account has been deleted")

                    elif choice == 'n':
                        print("Account still exists")
            else:
                print("Account does not exist")    

        elif short_code == 'li':
            print("Enter your username: ")
            username = input()

            if check_existing_users(username):
                print("Enter your password:")
                password = input()
                search_user = find_user(username)

                if (password == search_user.password):
                    print(f"Welcome {search_user.first_name} {search_user.last_name}")
                    print('\n')

                    while True:    
                        print("What would you like to do: cc - create a new credential, dc - delete credential, vc - display credential, va - display all credentials, lo - log out")
                        short_code = input().lower()

                        if short_code == 'cc':
                            print ("Account name: ")
                            account = input()
                            print("-"*30)
                            print("Account username: ")
                            acc_username = input()
                            print("-"*30)
                            print("Account password:")
                            print("Would you like an auto generated password?")
                            print("y - Yes, n - No")
                            choice = input().lower()

                            if choice == 'y':
                                print('\n')
                                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                                acc_password = "".join(random.choice(chars) for _ in range(8))
                                print(f"\nYour password is: {acc_password}")

                            elif choice == 'n':
                                print('\n')
                                print("Please enter password")
                                acc_password = input()
                            else:
                                print('\n')
                                print("Use either y or n")  

                            print('\n')
                            save_credential(create_credential(username, account, acc_username, acc_password))  
                            print('\n')
                            print(f"New Credential for {account} created")

                        elif short_code == 'dc':
                            print('Please enter the account name of the credential you would like to delete')
                            delete_credential = input()
                            if check_existing_credential(delete_credential):
                                search_credential = find_credential(account)
                                print(f"Are you sure you want to delete {search_credential.account} credential?")
                                print('\n')
                                print("y - Yes, n - No")
                                print('\n')
                                choice = input().lower()
                                if choice == 'y':
                                    del_credential(search_credential)
                                    print('\n')
                                    print(f"{search_credential.account} credential have been deleted.")
                                    print('\n')
                                else:
                                    print('\n')
                                    print("Credential are still available")
                                    print('\n')
                            else:
                                print('\n')
                                print ("The account does not exist")
                                print('\n')

                        elif short_code == 'vc':
                            print('\n')
                            print("Enter the account you want to display.")
                            print('\n')
                            find_name = input()
                            search_credential = find_credential(account)
                            if check_existing_credential(find_name):
                                print('\n')
                                print(f"Account: {search_credential.account}")
                                print('-'*20)
                                print(f"Username: {search_credential.account_username}")
                                print(f"Password: {search_credential.account_password}")
                                print('\n')
                            else:
                                print('\n')
                                print("That account does not exist")
                                

                        elif short_code == 'va':
                            if display_credential():
                                print('\n')
                                print("Here are your credential:")
                                

                                for credential in display_credential():
                                    if credential.username == username:
                                        print('\n')
                                        print(f"{credential.account}")
                                        print("-"*30)
                                        print(f" Username: {credential.account_username}")
                                        print(f" Password: {credential.account_password}")
                                
                            else:
                                print('\n')
                                print("No credential available")
                                print('\n')

                        elif short_code == 'lo':
                            print('\n')
                            print("log out successful.")
                            print('\n')
                            break

                        else:
                            print('\n')
                            print("Please use one of the navigation shortcodes provided.")
                            print('\n')

                else:
                    print('\n')
                    print("Sorry, wrong password")
            else:
                print('\n')
                print("Account does not exist")
                print('\n') 

        elif short_code == "ex":
            print("Bye!")
            break
        else:
            print("Please use the short codes.") 

if __name__ == '__main__':
    main()       