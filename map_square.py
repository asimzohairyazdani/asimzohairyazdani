ls= []
ls=[int(num) for num in input("Enter elements : ").split()]
x = list(map(lambda ls : ls**2, ls))
x
output:
Enter elements : 1 2 3 4 5 6 7
[1, 4, 9, 16, 25, 36, 49]
