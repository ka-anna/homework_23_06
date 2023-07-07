#Write a function called is_sorted that is given a list 
#and returns True if the list is sorted and False otherwise. Do this without using the sort method.

ls = [5,9,7]
def is_sorted(ls):
 for i in range (len(ls)-1):
    if ls[i+1] <= ls[i] and ls[-(i+1)] >= ls[-(i+2)]:
        return False
 return True
print(is_sorted(ls))
