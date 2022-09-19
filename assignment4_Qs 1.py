user_input = input("Enter items of your list - type exit to stop: ")
list = []
lenght = 0
while user_input != 'exit' :
    user_input = input("Enter items of your list")
    list.append(user_input)
    lenght +=1
print('Your list of items is : ',list)
print("Lenght of your list is: " ,lenght)


