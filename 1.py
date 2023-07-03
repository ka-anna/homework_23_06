#Write a function called merge that takes two already sorted lists of 
#possibly different lengths, and merges them into a single sorted list. Do this without using the sort method.



ls1 = [1,5,3]
ls2 = [2,118,7,4]
s_ls1 = []
s_ls2 = []
res = []
def merge (s_ls1, s_ls2):
    global res
    for i in range (0,len(ls1)):
        s_ls1.append(min(ls1))
        ls1.remove(min(ls1))
    for j in range (0,len(ls2)):
        s_ls2.append(min(ls2))
        ls2.remove(min(ls2))
    res = s_ls1 + s_ls2
    return res.sort()
merge(s_ls1, s_ls2)
print(res)
