list1 = [1, 2, 3, 4, 5]  # Example list
list2 = list1[::-1]  # Reverse the list1 and store it in list2
a = len(list1)

for i in range(a):
    print(f"Original list item: {list1[i]}")  # Using f-string formatting
    print(f"Reverse list item: {list2[i]}")   # Access the corresponding item from list2
