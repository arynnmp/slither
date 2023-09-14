#Find the middle number of a list
#If the list lenght is odd, take the middle number
#If the list length is even, take the average of the middle two numbers

def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum/2
  else:
    return my_list[int(len(my_list)/2)]


#add a list to test the function
print(middle_element([5, 2, -10, -4, 4, 5]))