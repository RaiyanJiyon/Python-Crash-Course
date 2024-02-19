'''
9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.
'''

class User:
    def __init__(self, first_name, last_name, age, gender, login_attempts) -> None:
        # Initialize attributes for user's first name, last name, age, and gender
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        # Method to print a summary of the user's information
        print(f"User First Name - {self.first_name}")
        print(f"User Last Name - {self.last_name}")
        print(f"User Age - {self.age}")
        print(f"User Gender - {self.gender}")

    def greet_user(self):
        # Method to print a personalized greeting to the user
        print(f"Welcome {self.first_name} {self.last_name}")

    def increment_login_attempts():
        pass

    def reset_login_attempts():
        pass


# Creating several instances representing different users
user1 = User("Tamim", "Zia", 24, "Male")
print("User 1 Information - ")
user1.describe_user()
user1.greet_user()

user2 = User("Tammana", "Akter", 22, "Female")
print("\nUser 2 Information - ")
user2.describe_user()
user2.greet_user()

user3 = User("Sabbir", "Ahmed", 25, "Male")
print("\nUser 3 Information - ")
user3.describe_user()
user3.greet_user()

user4 = User("Ishaq", "Ahammad", 26, "Male")
print("\nUser 4 Information - ")
user4.describe_user()
user4.greet_user()
