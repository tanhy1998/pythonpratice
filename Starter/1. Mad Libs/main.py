def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("noun")
noun2 = get_input("noun")
verb1 = get_input("verb")
vert2 = get_input("verb")

story = f"""
Once upon a time, there was a {noun1} who loved to {verb1}.
One day, the {noun1} met another {noun2} who also loved to {vert2}.
They became best friends and lived happily ever after!
"""

print(story)