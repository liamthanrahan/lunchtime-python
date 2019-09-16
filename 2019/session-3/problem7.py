def my_append(a_list, element):
    # add your function her
    appended_list = a_list
    if not element in a_list:
        appended_list.append(element)
    return appended_list


print(my_append([1, 2, 3], 4))
print(my_append([1, 2, 3], 3))
