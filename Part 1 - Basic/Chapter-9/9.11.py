'''
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly
'''

# admin_import.py
from user_admin import Admin

# Create an instance of Admin
admin = Admin("Raiyan", "Jiyon", 30, "Male")
# Call a method to show that everything is working correctly
admin.privileges.show_privileges()
