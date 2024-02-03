""" 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you """

# From page 153

# Define a function called build_profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # Create an empty dictionary to store the user profile
    profile = {}
    
    # Add first and last names to the profile
    profile['first_name'] = first
    profile['last_name'] = last

    # Add any additional user information from user_info to the profile
    for key, value in user_info.items():
        profile[key] = value
    
    # Return the completed user profile
    return profile

# Call the build_profile function with specific information for the user
user_profile = build_profile('Raiyan', 'Jiyon', location='Dhaka', field='CSE')

# Print the resulting user profile dictionary
print(user_profile)
