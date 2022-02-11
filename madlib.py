#Python Madlib Program!!!
#Prompt the user for inputs, then print madlibbed paragraph
#Its based on string concatenation. aka putting strings together

#beginning examples
youtuber= "me"  #some strings

# a few ways to print
print("subscribe to " + youtuber)
print("subscribe to {}!".format(youtuber))
#f calls it a function.
print(f"subscribe to {youtuber}")

#create input strings from user
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me happy \
because I love to {verb1}. Stay awesome and  {verb2} like you are {famous_person}"

print(madlib)
