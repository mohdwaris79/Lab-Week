lower=int(input("Enter the Lower range number here: "))
upper=int(input("Enter the Upper range number here: "))        
for num in range(lower, upper+1):
    if num>1:
        is_prime=True
        for i in range (2,num):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            print(num, end=" ")