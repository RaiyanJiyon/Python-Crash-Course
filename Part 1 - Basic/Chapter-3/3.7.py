# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

# •	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# •	Print a message to each of the two people still on your list, letting them know they’re still invited.

# •	Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program


#==============================================
# Start from exercise 3.6 
#=================================================

inviting_list = ["Mujahid", "Ishaq", "Sabbir"]

print(inviting_list[0]+", i like to inviting you to dinner.")
print(inviting_list[1]+", i like to inviting you to dinner.")
print(inviting_list[2]+", i like to inviting you to dinner.")

# for some space 
print("\n")

# printing who can't join the dinner party 
print(inviting_list[2],"are not comming in dinner.")

# for some space 
print("\n")

# modified inviting_list person name
inviting_list = ["Mujahid", "Ishaq", "Tamim"]

print(inviting_list[0]+", i like to inviting you to dinner.")
print(inviting_list[1]+", i like to inviting you to dinner.")
print(inviting_list[2]+", i like to inviting you to dinner.")

# for extra space 
print("\n")

# printing the news
print("Guys, i found a bigger dinner table, so we can invite 3 people more for this dinner.")

# adding the person at the beggining 
inviting_list.insert(0, "Sohel")
# adding the person at the middle
inviting_list.insert(3, "Soccho")
# adding the person at the end 
inviting_list.append("Emon")

# For extra space 
print("\n")

# Print a new set of invitation messages, one for each person in your list
print(inviting_list[0]+", i like to inviting you to dinner.")
print(inviting_list[1]+", i like to inviting you to dinner.")
print(inviting_list[2]+", i like to inviting you to dinner.")
print(inviting_list[3]+", i like to inviting you to dinner.")
print(inviting_list[4]+", i like to inviting you to dinner.")
print(inviting_list[5]+", i like to inviting you to dinner.")

# For extra space 
print("\n")

print("Sorry guys, i can invite only two people for dinner.")

print(inviting_list[0],"is leaving")
inviting_list.pop(0)

print(inviting_list)
print(inviting_list[0],"is leaving")
inviting_list.pop(0)

print(inviting_list)
print(inviting_list[0],"is leaving")
inviting_list.pop(0)

print(inviting_list)
print(inviting_list[0],"is leaving")
inviting_list.pop(0)

print(inviting_list)

print("\n")

print(inviting_list[0]+", you're still invited.")
print(inviting_list[1]+", you're still invited.")

print("\n")

del inviting_list[0]
del inviting_list[0]

print("Updated invitied list-", inviting_list)