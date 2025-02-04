
for letter in input("input: ").upper():
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    print(letter)

## OR

"""
for letter in input("input: ").upper():
    if letter not in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
"""
