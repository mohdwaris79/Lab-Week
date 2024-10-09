num= int(input("Enter the number: "))
org_num=num
new_num=0
while num>0:
    remainder=num % 10
    new_num=new_num * 10 + remainder
    num=num // 10
if (org_num == new_num):
    print("Entered number is a palindrome number!")    
else:
    print("The number entered is not a palindrome number")    
    