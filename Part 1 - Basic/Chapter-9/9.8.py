'''
9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.
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


class Privileges:
    """A class to represent privileges."""

    def __init__(self):
        """Initialize the privileges attribute."""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the privileges."""
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A class to represent an admin, inherits from User."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize attributes of the parent class, User, and Privileges."""
        super().__init__(first_name, last_name, age, gender)
        # Initialize a Privileges instance as an attribute
        self.privileges = Privileges()


# Create an instance of Admin
admin = Admin("John", "Doe", 30, "Male")
# Call the method to show privileges
admin.privileges.show_privileges()
