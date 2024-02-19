'''
9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
'''

class User:
    """A class to represent a user."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes for user's first name, last name, age, and gender."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User First Name - {self.first_name}")
        print(f"User Last Name - {self.last_name}")
        print(f"User Age - {self.age}")
        print(f"User Gender - {self.gender}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome {self.first_name} {self.last_name}")


class Admin(User):
    """A class to represent an admin, inherits from User."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes of the parent class, User."""
        super().__init__(first_name, last_name, age, gender)
        # Initialize attributes specific to Admin
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the admin's set of privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin
admin = Admin("John", "Doe", 30, "Male")
# Call the method to show privileges
admin.show_privileges()
