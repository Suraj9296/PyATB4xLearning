my_shopping_list =["bread","milk","butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

#To remove the duplicate from the list -->set-->data structure


def bring_more_food(my_shopping_list):
    more_item= input("enter the item\n")
    my_shopping_list.append(more_item)
    #my_shopping_list.remove(more_item)
    #my_shopping_list.insert(0,more_item)
    return my_shopping_list

l=bring_more_food(my_shopping_list)
print(l)


