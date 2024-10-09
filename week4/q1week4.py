
def cal_sum_sub():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculate sum and subtraction
    total = num1 + num2
    print("Sum:", total)
    
    difference = num1 - num2
    print("Subtraction:", difference)

# Call the function once, without recursion
cal_sum_sub()
