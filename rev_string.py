def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "1234abcd"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s))  

output:
  The original string  is :  1234abcd
  The reversed string using extended slice operator  is :  dcba4321
