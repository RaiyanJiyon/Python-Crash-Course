'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user
'''

class User:
    def __init__(self, first_name, last_name, age, gender):
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
