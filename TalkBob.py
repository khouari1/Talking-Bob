import os
print os.path.basename(__file__)
import bobf #imports the functions used below
import Tkinter

top = Tkinter.Tk()
top.title("Talking Bob")
top.geometry("300x200+300+300")
# Code to add widgets will go here...
app.grid()
button1 = Button(app, text = "Please Ok to start Bob!")
button.grid()
top.mainloop()

print ("Hello, my name is Bob. What is your name?")
name = raw_input()
print ("It's very nice to meet you," + " " + name + ".")
print ("What movie franchise do you think is better, Harry Potter or Lord of the Rings?")
movie_choices = ['harry potter', 'lord of the rings']
movie = raw_input()
movie = movie.lower()
if movie == movie_choices[0]:
    print ("I'm partial to disagree with you there," + " " + name + ".")
elif movie == movie_choices[1]:
    print ("I can tell we are going to get along just fine," + " " + name + ".")
else:
    while movie not in movie_choices:
        print (name + ", " + "that's not one of the choices! Come on, Harry Potter or Lord of the Rings?")
        movie = raw_input()
        movie = movie.lower()
print ("So can I assume that is your favourite movie?")
fave_movie = []
choices = ['yes', 'no']
fave_movie2 = raw_input()
fave_movie2 = fave_movie2.lower()
if fave_movie2 == choices[0]:
    fave_movie.append(fave_movie2)
    print ("Ok, awesome! It's mine as well!")
elif fave_movie2 == choices[1]:
    print ("Ok, what is then?")
    fave_movie_choice = raw_input()
    fave_movie.append(fave_movie_choice)
    print ("Alrighty, noted.")
else:
    while fave_movie2 not in choices:
        print (name + ", " + "that is an invalid choice!")
        fave_movie2 = raw_input()
        fave_movie2 = fave_movie2.lower()
print ("Ok, now I want to test my math skills. Give me a number and in seconds I will tell you it squared:")
while True:
    squared_choice = raw_input()
    try:
        myValue = int(squared_choice)
        bobf.squared(myValue)
        strValue = str(bobf.squared(myValue))
        print ("The answer is" + " " + strValue + ".")
        break
    except ValueError:
        print ("Please enter a number," + " " + name + ".")
print ("Alright, let's try something else just in case you don't believe I'm a maths genius!")
print ("Enter any number and I will tell you if it is a prime number:")
while True:
    prime_choice = raw_input()
    try:
        myValue2 = int(prime_choice)
        bobf.is_prime(myValue2)
        primeValue = bobf.is_prime(myValue2)
        if primeValue == True:
          print ("That is a prime number!")
        else: print ("That is not a prime number!")
        break
    except ValueError:
        print ("Please enter a number," + " " + name + ".")
print ("It's been nice talking to you. I've got to go now, see ya!")
