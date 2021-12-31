# list of elements
lst1 = [int(item) for item in input("Enter the list items : ").split()]
 
# creating recursive function
# to get sum
def sumof(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumof(list, size - 1)
  
# Call function     
total = sumof(lst1, len(lst1))
 
print("Sum of all elements in given list: ", total)

output:
  Enter the list items :  1 2 3 4
  Sum of all elements in given list:  10
