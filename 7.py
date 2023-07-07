#Create a global variable called x and set it to 10. Write a function called my_function that defines a local variable with the same 
#name x and assigns it a value of 20. 
#Inside the function, print the local x variable and the global x variable. Call my_function and observe the output.


x = 10
def my_function():
    x = 20
    print(x)
my_function()
print(x)
