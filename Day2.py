#Find Largest of Three numbers
first=int(input("Enter the number:"))
second=int(input("Enter the number:"))
Third=int(input("Enter the number:"))
if first > second:
    if first>Third:
        print(first)
    else:
        print(Third)
elif second>first:
    if second>Third:
        print(second)
    else:
        print(Third)
