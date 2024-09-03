#list is mutable in nature(duplicate value allowed in tuple)

squares =[1,4,9,16,25]

squares[3]="suraj"
print(squares)

#Tuple-- collection of items--Immutable in nature (duplicate value allowed in tuple)

my_tuple=(1,4,9,16,25)

#conversion to list from tuple is possible
my_api_list=list(my_tuple)
print(my_api_list)

my_api_tuple=tuple(my_api_list)
print(my_api_tuple)

#tuples use less memory




