#Write a function called outer_function that takes a parameter x. Inside outer_function, 
#define another function called inner_function that multiplies x by a given factor. 
#Call inner_function from outer_function and print the result.




def outer_function(x):
    def inner_function(y):
        return(x*y)
    res = inner_function(2)
    print (res)
outer_function(7)
