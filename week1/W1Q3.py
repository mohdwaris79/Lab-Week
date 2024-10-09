list1=[]
for i in range(1,5):
    print("Enter the", i,"number")
    num=int(input())
    if num % 5 == 0 :
        list1.append(num)
    i+=1  
print("Number which are divisible by 5 are: ",list1)   
     
    