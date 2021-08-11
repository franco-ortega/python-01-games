import random

tale = "There once was a night who was young and brave."

# Concatenatation:
print("A story: " + tale)

# Option #2
print("A story: {}".format(tale))

# F-string
print(f"A story: {tale}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")

madlib = f"Computer life is so {adj}! It makes me so excited \
all the time because I love to {verb1}. Stay hydrated and {verb2} \
like you are too hot. Cos you are!"

print(madlib)


adj_2 = random.choice(["bold", "quiet", "hungry", "loud"])
verb1_2 = random.choice(["run", "sleep", "eat", "shout"])
verb2_2 = random.choice(["fly", "swim", "devour", "snore"])

madlib2 = f"Hacker life is so {adj_2}! It makes me so excited \
all the time because I love to {verb1_2}. Stay wet and {verb2_2} \
like you are in the zone!"

print(madlib2)