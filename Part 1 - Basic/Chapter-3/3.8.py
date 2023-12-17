# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

# •	Store the locations in a list. Make sure the list is not in alphabetical order.
# •	Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

# •	 Use sorted() to print your list in alphabetical order without modifying the actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed


# Original list of places
places = ["London", "Kashmir", "Berlin", "New York", "Goa"]

# Print the original list
print("Original List:", places)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Sorted list in alphabetical order:", sorted(places))

# Show that the original list is still in its original order
print("Original List:", places)

# Use sorted() to print the list in reverse alphabetical order without changing the original order
print("Sorted list in reverse alphabetical order:", sorted(places, reverse=True))

# Show that the original list is still in its original order
print("Original List:", places)

# Use reverse() to change the order of the list in place
places.reverse()

# Print the list to show that its order has changed
print("Reversed list:", places)

# Use reverse() again to revert the order back to the original
places.reverse()

# Print the list to show it's back to its original order
print("Original List:", places)

# Use sort() to change the list to alphabetical order
places.sort()

# Print the list to show that its order has been changed
print("Sorted list in alphabetical order:", places)

# Use sort() again to change the list to reverse alphabetical order
places.sort(reverse=True)

# Print the list to show that its order has changed
print("Sorted list in reverse alphabetical order:", places)
