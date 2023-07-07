#Write a function called power_of that takes a parameter n and returns a function called power that calculates the nth power of a 
#given number. 
#Test the power_of function by calling it with different values of n and then using the returned power function to calculate powers.

def power_of(n):
    def power (x):
        return x ** n
    print(power(5))
power_of(2)
power_of(4)
