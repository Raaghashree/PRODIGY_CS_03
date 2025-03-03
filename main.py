def evaluate_password_strength(passcode):
    length = len(passcode)
    score = 0
    special_chars = {'@', '#', '$', '&'}

    if 8 <= length <= 24:
        score += 1
    else:
        print("Password must be between 8 to 24 characters!")

    if any(char.isupper() for char in passcode):
        score += 1
    else:
        print("Password must contain at least one uppercase letter!")

    if any(char.islower() for char in passcode):
        score += 1
    else:
        print("Password must contain at least one lowercase letter!")

    if any(char.isdigit() for char in passcode):
        score += 1
    else:
        print("Password must include at least one digit!")

    if any(char in special_chars for char in passcode):
        score += 1
    else:
        print("Password must contain at least one special symbol (@, #, $, &)!")

    return score  

user_password = input("Enter your password: ")
strength = evaluate_password_strength(user_password)

if strength >= 4:
    print("Good! Strong Password!")
elif strength >= 2:
    print("No...Weak Password, consider making it stronger.")
else:
    print("Oh no! Invalid Password, does not meet security requirements.")
