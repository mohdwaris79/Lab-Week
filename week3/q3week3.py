def even_characters(ch):
    
    for i in range(len(ch)):
        if i % 2 == 0:
            print(ch[i], end=" ")


str=input("Enter the string ")
even_characters(str)
