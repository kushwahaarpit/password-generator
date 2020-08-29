import string
import random

#main function
def gen():
    s1 = string.ascii_uppercase
    
    s2 = string.ascii_lowercase
    
    s3 = string.digits
    
    s4 = string.punctuation
    
   
    passlen = int(input("Enter the password length\n"))  #for input the lenght of password
    
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    

    random.shuffle(s)  #to shuffle the alphabets, numbers and symbols
    
    pas =("".join(s[0:passlen])) # to join the list up to the lenght inserted by the user
    print(pas) #to print the randomly generated password
    
gen()
