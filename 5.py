#Create a global variable called counter and initialize it with 0.
#Write a function called increment_counter that increments the value of counter by 1 and prints the updated value.
#Call the function multiple times and observe the changes in the global variable.


counter = 0
def increment_counter():
    global counter
    counter += 1
    print(counter)
increment_counter()
increment_counter()
increment_counter()
