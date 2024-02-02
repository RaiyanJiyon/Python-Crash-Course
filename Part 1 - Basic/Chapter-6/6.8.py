# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet

# Dictionary for a cat named Whiskers
whiskers = {
    "owner's name": "Raiyan Jiyon",
    "animal_type": "cat",
    
}

# Dictionary for a dog named Buddy
buddy = {
    "owner's name": "Sabbir Ahmed",
    "animal_type": "dog",
}

# Dictionary for a parrot named Coco
coco = {
    "owner's name": "Ishaq Ahammad",
    "animal_type": "parrot",
}

# Dictionary for a fish named Bubbles
bubbles = {
    "owner's name": "Mahabub alam",
    "animal_type": "fish",
}

pets = [whiskers, buddy, coco, bubbles]

for pet in pets:
    print("Pet Details - ")

    for key, value in pet.items():
        print(f"{key}: {value}")
    print()
