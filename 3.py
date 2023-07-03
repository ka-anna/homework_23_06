#Write a function called is_sorted that is given a list 
#and returns True if the list is sorted and False otherwise. Do this without using the sort method.

ls = [1,8,6]
def is_sorted(ls):
    if sorted(ls)==ls:
        print("True")
    else:
        print("False")
is_sorted(ls)
