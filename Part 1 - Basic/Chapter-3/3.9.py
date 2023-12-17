# 3.9. Dinner Guests: Working with one of the programs from Exercises 3.4 through 3.7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner

#==============================================
# Start from exercise 3.7 
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

print("The number of people i am inviting to dinner is",len(inviting_list))