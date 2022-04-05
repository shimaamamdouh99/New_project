
#a)find the nth occurance of a word in a string                                    #Note         #a)1:9     b)10 : 47       c) 50:69         d):
def find_nth_occurrence(substring, string, occurrence=1):                          #solution         1           2             3
    i = -1
    for i in range(occurrence):
     i = string.find(substring, i + 1)
     if i == -1:
          break
    return i
#b)simple string matching  
#solition 1
def solve(a,b):
    if a==b:
        return True
    if len(a)-1<=len(b):
        if "*" in a:
            return True 
        else: 
            return False
    else: 
        return False       
#solution 2
def solve (a,b):
    if a==b and '*' not in a:
        return True 
    elif a=='*' or a=='': 
        return True
    elif '*' in a and ((len(b))<((len(a)-1))):
        return False 
    elif '*' in a and ((len(b))>=((len(a)-1))): 
        for i in range((len(a)+1)): 
            if a[i]==b[i]: 
                return True
            elif a[i]=='*': 
                break
            else: 
                return False 
        for m in range(-1,-(len(a)+1),1):
            if a[m]==b[m]: 
                return True 
            elif a[m]=='*': 
                break 
            else: 
                return False 
    else: 
        return False
 #we can also use find,startwith,endwith method but i try not all cases handle 

#c) Is it a palindrome?
#Solution 1:
def is_palindrome(p):
    p = p.lower()
    return p == p[::-1]
#oR solurin 2:
def is_palindrome(m):
    p=p.replace("","").lower()
    if p==p[::-1]:
        return True
    return False
#OR solutin 3:
def is_palindrome(p):
    p=p.lower() 
    p=p.replace()
    f_list = list(p) 
    f_list.reverse[::-1]
    p_2=''.join(f_list)             
    if p==p_2:
        return True
    return False   




    
    






