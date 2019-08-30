def my_append(a_list, element):
    if element not in a_list:
        a_list.append(element)
    return a_list

animals = ["cat", "dog", "elephant", "pig"]

print(my_append(animals, "zebra")) #["cat", "dog", "elephant", "pig", "zebra"]
