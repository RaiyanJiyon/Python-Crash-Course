# 7-6. Three Exits: Write different versions of either Exercise 7.4 or Exercise 7.5 
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a 'quit' value

active = True

while active:
    # Ask the user for their age
    age = input("Please enter your age Or, enter 'quit' to exit: ")

    # Check if the user wants to quit
    if age.lower() == 'quit':
        break  # exit the loop if the user enters 'quit'

    # Convert the input to an integer
    age = int(age)

    # Determine the ticket price based on age
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    # Display the ticket price to the user
    print(f"The cost of your movie ticket is ${ticket_price}")
