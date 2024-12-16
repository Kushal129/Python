import re
import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate
    engine.say(message)
    engine.runAndWait()

import re
import string
import math

def check_password_strength(password):
    strength = 0
    suggestions = []

    # 1. Length Check
    if len(password) >= 12:
        strength += 1
    elif len(password) >= 8:
        suggestions.append("Consider making your password at least 12 characters for better security.")
    else:
        suggestions.append("Password is too short. Use at least 12 characters.")

    # 2. Uppercase and Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters to make your password stronger.")

    # 3. Numbers Check
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Add at least one number for better security.")

    # 4. Special Characters Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Use at least one special character (e.g., @, #, $, %).")

    # 5. Repeated Characters Check
    if not re.search(r'(.)\1\1', password):  # No three consecutive identical characters
        strength += 1
    else:
        suggestions.append("Avoid using three or more consecutive identical characters (e.g., aaa, 111).")

    # 6. Common Patterns Check
    patterns = ["123", "abc", "password", "qwerty", "letmein", "admin"]
    if any(pattern in password.lower() for pattern in patterns):
        suggestions.append("Avoid using common patterns like '1 2 3', 'abc', or 'password'.")

    # 7. Dictionary Words Check
    # Simulating a basic dictionary check (you could use a real dictionary file for better validation)
    common_words = {"password", "welcome", "dragon", "ninja", "admin", "football", "master"}
    if password.lower() in common_words:
        suggestions.append("Your password uses a common word. Avoid dictionary words.")

    # 8. Keyboard Patterns Check
    keyboard_patterns = [
        "qwerty", "asdf", "zxcv", "1234", "5678", "0987", "qazwsx", "1q2w3e"
    ]
    if any(pattern in password.lower() for pattern in keyboard_patterns):
        suggestions.append("Avoid keyboard patterns like 'qwerty' or 'asdf'. These are easily guessable.")

    # 9. Unique Characters Check
    unique_chars = len(set(password))
    if unique_chars < len(password) * 0.5:  # At least 50% of characters should be unique
        suggestions.append("Your password doesn't have enough unique characters. Add more variety.")

    # 10. Password Entropy Check (Basic Approximation)
    entropy = len(password) * math.log2(len(set(password)))
    if entropy < 50:
        suggestions.append("Your password has low entropy. Add more complexity to improve randomness.")
    else:
        strength += 1

    # Determine the strength level
    if strength >= 7:
        return "Strong", suggestions
    elif 4 <= strength < 7:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions

def main():
    print("Welcome to the Password Strength Checker!")
    speak("Welcome to the Password Strength Checker!")
    
    while True:
        print("-----------------------------------------------------------------------------------------------------------")
        password = input("Enter a password to check its strength (or type 'exit' to quit): | ")
        print("-----------------------------------------------------------------------------------------------------------")
        if password.lower() == "exit":
            print("Goodbye! Stay secure! -KHP")
            speak("Goodbye! Stay secure!")
            break

        strength, suggestions = check_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        speak(f"Password Strength is {strength}")

        if suggestions:
            print("Suggestions to improve your password:")
            speak("Here are some suggestions to improve your password.")
            for suggestion in suggestions:
                print(f"- {suggestion}")
                speak(suggestion)
        else:
            print("Your password is strong! No suggestions needed.")
            speak("Your password is strong! No suggestions needed.")

if __name__ == "__main__":
    main()
