user_input = input("Enter any string: ")

even_index = user_input[2:len(user_input)+1:2]
odd_index = user_input[1:len(user_input)+1:2]
print(odd_index)
print(even_index)