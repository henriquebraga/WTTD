tuple_of_tuples = ((4,3), (5,1), (1,2), (3,15,4))
final_list = []

for tuple_elements in tuple_of_tuples:
    temp_list = [] #Creates a list
    temp_list.append(tuple_elements[-1])
    final_list.append(temp_list)

final_list = sorted(final_list) #Sorting the last elements from the tuple.

for tuple_element in tuple_of_tuples:
    for list_element in final_list:
        if list_element[0] == tuple_element[-1]:
            #list_element = []        
            list_element.insert(0, list(tuple_element[:-1])) 


print(final_list)