#List = collection of items (duplicate is allowed)
s_l=["bread","milk","butter"]
my_list=[1,2,3,3]
print(my_list)
print(len(my_list))
print(my_list[0])
#print(my_list[10])--error
#Indexing
my_list[0]="Suraj"
my_list[1]="prasad"
print("element at the index 0", my_list[0])
print(my_list)

for element in my_list:
    print(element)
#Append

my_list.append(4) #append object to the end of the list.
my_list.append(10) #append object to the end of the list.
print(my_list)

#extend

my_list.extend(["c",12,11])
print(my_list)

#insert()

my_list.insert(1,"J")
print(my_list)

my_list.insert(-1,"praveen")
print(my_list)

#remove()
my_list.remove("J")
print(my_list)


#copy()

my_copy_list=my_list.copy()
print(my_copy_list)

#clear()

#sort()

#reverse()


