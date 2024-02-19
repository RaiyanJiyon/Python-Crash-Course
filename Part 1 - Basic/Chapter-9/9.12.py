'''
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
'''

# admin_instance.py
from user import User
from admin import Admin

# Create an instance of Admin
admin = Admin("Raiyan", "Jiyon", 30, "Male")
# Call a method to show that everything is working correctly
admin.privileges.show_privileges()
