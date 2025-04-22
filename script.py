#Creating an empty list
my_list = []

#Appending elements 10, 20, 30, 40 to the list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value 15 at the second position in the list
my_list.insert(1, 15)

#Extending the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

#Removing the last element from the list
my_list.pop(len(my_list)-1)

#Sorting the list in ascending order
my_list.sort()

#Finding and printing the index of the value 30 in the list
for i in range(len(my_list)):
    if (my_list[i] == 30):
        print(i)
