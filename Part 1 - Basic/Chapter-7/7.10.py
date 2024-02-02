# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

# Number of participants in the poll
num_participants = 5  # You can change this number as needed

# List to store responses
responses = []

# Polling loop
for i in range(num_participants):
    dream_vacation = input("If you could visit one place in the world, where would you go? - ")
    responses.append(dream_vacation)

# Print the results
print("\nResults of the Dream Vacation Poll:")
for index, response in enumerate(responses, start=1):
    print(f"Participant {index}: {response}")
