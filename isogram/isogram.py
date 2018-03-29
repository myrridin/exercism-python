def is_isogram(string):
    # Use a dictionary to track which characters have been seen
    seen = {}

    # Remove hyphens and spaces, and lowercase the string
    clean_string = string.replace('-', '').replace(' ', '').lower()

    # Iterate over the characters in the cleaned string
    for char in clean_string:
        # If it's been seen, return False
        if char in seen:
            return False

        # Otherwise record that it was seen
        seen[char] = True

    # If we get to this point, we have an isogram!
    return True


