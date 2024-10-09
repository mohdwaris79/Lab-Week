num=int(input("Enter a number here: "))
sum=0
while num>0:
    remainder=num % 10
    sum=sum + remainder
    num//=10
print("The sum of the digits of the given number is: ", sum)