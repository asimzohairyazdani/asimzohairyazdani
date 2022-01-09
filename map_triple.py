ls= []
ls=[int(num) for num in input("Enter elements : ").split()]
x = list(map(lambda ls : ls*3, ls))
x

output: 
Enter elements : 1 2 3 4 5 6 7
[3, 6, 9, 12, 15, 18, 21]
