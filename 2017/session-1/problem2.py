def suggest_travel(distance):
    intdistance = int(distance)
    if (intdistance > 5):
        return "You should take the train."
    elif (intdistance > 2):
        return "You should cycle."
    else:
        return "Stop being lazy and walk!"

# distance = input("How far out are you man? ")
# print(suggest_travel(distance))
