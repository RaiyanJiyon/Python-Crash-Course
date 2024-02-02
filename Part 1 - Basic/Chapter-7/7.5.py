# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

while True:
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
