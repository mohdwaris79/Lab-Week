def same_number():
    numbers = (50,10,60,40,50,60)
    for i in numbers:
        # Check if the current number appears more than once in the list
        if numbers.count(i) > 1:
            print(f"{i} appears more than once.")
        else:
            print(f"{i} is unique.")

same_number()
