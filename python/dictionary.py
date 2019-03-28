# Now we know that Lists are indexed with integer numbers. 
# But what if we don’t want to use integer numbers as indices? 
# Some data structures that we can use are numeric, string, or other types of indices.
# Let’s learn about the Dictionary data structure. 
# Dictionary is a collection of key-value pairs. Here’s what it looks like:

dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}

# The key is the index pointing to the value. How do we access the Dictionary value? 
# You guessed it — using the key. Let’s try it:

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"]))
print("But you can call me %s" %(dictionary_tk["nickname"])) 
print("And by the way I'm %s" %(dictionary_tk["nationality"]))

# Here we have a key (age) value (24) pair using string as the key and integer as the value.

dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

dictionary_tk['age'] = 24

bookshelf = ["The Effective Engineer","The 4 hours work week","Zero to One","Lean Startup","Hooked"]

for book in bookshelf:
    print(book)