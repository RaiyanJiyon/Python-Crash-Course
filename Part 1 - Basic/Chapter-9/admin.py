# admin.py
from user import User  # Importing the User class from the user module

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
