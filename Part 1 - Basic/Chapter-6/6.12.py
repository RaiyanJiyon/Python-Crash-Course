# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

# Extended version of 6-9. Favorite Places

favorite_places = {
    "Raiyan Jiyon": {
        "places": ["Beach", "Mountains", "City Park"],
        "comments": ["Love the sandy beaches!", "Enjoy the scenic views.", "Great for picnics."]
    },
    "Sabbir Ahmed": {
        "places": ["Café", "Library", "Home"],
        "comments": ["Relaxing with a cup of coffee.", "Love reading in a quiet environment.", "Nothing beats the comfort of home."]
    },
    "Ishaq Ahammad": {
        "places": ["Historical Museum", "Botanical Garden", "Lake"],
        "comments": ["Fascinating history!", "Nature at its best.", "Tranquil and serene."]
    }
}

# Improved formatting of the output
for person, details in favorite_places.items():
    print(f"{person}'s Favorite Places:")
    for i, place in enumerate(details["places"], start=1):
        print(f"{i}. {place} - {details['comments'][i - 1]}")
    print()
