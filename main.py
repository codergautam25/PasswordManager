import re


class BasePasswordManger:

    def __init__(self):
        self._current_password = None
        self._old_passwords = []

    # list that holds all of the user's past

    def get_password(self):
        """this method returns the current password as a string of the current user"""
        # return self.old_password and self.old_password[-1]
        if self._old_passwords:
            self._current_password = self._old_passwords[-1]
            return self._current_password
        return None

    # def is_correct(self, password: str) -> bool:
    # return self.old_password and password == self.old_password[-1] or False
    def is_correct(self, word):
        """this method receives a string and returns a boolean True or False depending on whether the string is equal to
        the current password or not."""
        return self._current_password == word

    def get_all_passwords(self) -> list:
        """ This method returns the all password of the user as a list """
        return self._old_passwords


class PasswordManager(BasePasswordManger):
    __highest_level = 2

    def __init__(self):
        super().__init__()

    def set_password(self, word):
        """sets the user's password.Password change is successful only if:
        - Security level of the new password is greater.
        - Length of new password is minimum 6
        However, if the old password already has the highest security level,
        new password must be of the highest security level for a successful password change.
       """

        if not len(word) >= 6:
            return "Sorry! Weak Password try with another password"
        word_level = self.get_level(word)
        curr_password = self.get_password()
        if curr_password:
            current_level = self.get_level(curr_password)
        else:
            current_level = -1
        if word_level > current_level or word_level == PasswordManager.__highest_level:
            self._old_passwords.append(word)
            return "Great! Password saved Successfully!"
        return "Sorry! Weak Password try with another password"

    def get_level(self, word):
        """ This method returns the security level of the current password.
        It can also check and return the security level of a new password passed as a string.
        Security levels:
        """
        if word.isalpha() or word.isdigit():
            return 0
        elif word.isalnum():
            return 1
        else:
            return 2


print('-' * 60)
print(('-' * 13) + "'## Welcome To Gautam's Password Manager Application'" + ('-' * 13))
print('-' * 60)
user1 = PasswordManager()
while 1:
    print("You can enter the Password or you can type EXIT for stopping the process")
    user_inp = input("Enter password:: ")
    if user_inp == 'EXIT':
        break
    print(user1.set_password(user_inp))
    while 1:
        print("Please! Select your options :: ")
        print("1-> Get Current Password Level :")
        print("2-> Set new Password :")
        print("3-> Get All passwords :")
        user_inp = int(input("Please! Enter your choice (E.g-> 1)::"))
        if user_inp == 1:
            print("Your current password is : " + user1.get_password())
        elif user_inp == 2:
            user_input = input("Enter your new password::")
            print(user1.set_password(user_input))
        elif user_inp == 3:
            print("Your all passwords are :")
            print(user1.get_all_passwords())
        else:
            print("Invalid Input!!")
