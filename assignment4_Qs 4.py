#number= int(input("Enter your number: "))
number=0
posetive_count=0
negative_count=0
total=0
average=0
number +=1
if (number != 0):
        while number!=0:
            number= int(input("Enter your numberrrr: "))
            if (number>0):
                posetive_count +=1
            elif (number<0):
                negative_count +=1
            total +=number
            average =float(total/(posetive_count + negative_count))
        print("The number positive is : ", posetive_count)
        print("The number negative is : ", negative_count)
        print("The total of number is : ", total)
        print("The average pf number is :", average )
else:
        print("The program ends")
