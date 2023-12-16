# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.

# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list

#==============================================
# Start from exercise 3.5 
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