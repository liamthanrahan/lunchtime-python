def suggest_travel(distance):
    distance_num = float(distance)
    if (distance_num > 5):
        return 'You should take the train.'
    elif (distance_num > 2):
        return 'You should cycle.'
    else:
        return 'Stop being lazy and walk!'


# my_distance = input("Enter distance: ")
# print(suggest_travel(my_distance))
