n1 = int(input("Enter number of elements to be in the original list: "))
print("Enter elements to be in the list")
l1 = []
for i in range (0,n1):
    l1.append(int(input()))
n2 = int(input("Enter number of elements to be put in second list: "))
l2 = []
for i in range (0,n2):
    l2.append(int(input()))
print("Original list: ",l1)
print("Second list: ",l2)
for i in l2:
    l1.append(i)
print("Updated list after appending:",l1)