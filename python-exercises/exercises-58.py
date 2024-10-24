print("Word Palindrome")
print()

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("In your word > ")
print(f"Is {word} a palindrome?")
result = palindrome(word)
print(result)