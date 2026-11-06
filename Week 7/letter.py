import random
letters = "abcdefghijklmnopqrstuvwxyz"
input_letter = random.choice(letters)

# don't edit the code above
# put your code below here:

print(input_letter)

vowels = "aeiou"
idk = "y"


if input_letter in vowels:
    print("This letter is a vowel!")
elif input_letter in idk:
    print("It depends!")
else:
    print("This letter is a consonant!")
    
