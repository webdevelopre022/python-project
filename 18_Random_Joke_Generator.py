#Python Script to Generate a Random Joke
import pyjokes
# Fetch a random joke
joke = pyjokes.get_joke()

print("Here's a random programming joke for you:")
print(joke)

"""
#🌍Customizing Language and Joke Category
import pyjokes

# Fetch a joke in Spanish from the 'chuck' category (Chuck Norris jokes)
joke = pyjokes.get_joke(language='es', category='chuck')

print("Here's a Chuck Norris joke in Spanish:")
print(joke)

"""

"""

#🔁 Continuous Joke Stream
import pyjokes

# Display jokes indefinitely
for joke in pyjokes.forever():
    print(joke)
"""
