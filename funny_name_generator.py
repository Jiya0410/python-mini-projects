import random

adjectives = ["Mighty", "Crazy", "Silent", "Flying", "Invisible", "Fearless"]
nouns = ["Tiger", "Ninja", "Warrior", "Dragon", "Panther", "Wizard"]

name = input("Enter your name: ")

nickname = random.choice(adjectives) + " " + random.choice(nouns)

print(name + ", your funny nickname is:", nickname)