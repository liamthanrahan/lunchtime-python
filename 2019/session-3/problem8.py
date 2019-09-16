max_weight = 6


def fill_backpack(items):
    # Initialise backpack
    backpack = {
        "items": [],
        "weight": 0}

    for item in items:
        new_weight = backpack['weight'] + item['weight']
        if new_weight <= max_weight:
            backpack['items'].append(item['name'])
            backpack['weight'] += item['weight']

    # loop through the items in the order given
    # add item to backpack if backpack weight will not exceed 6kg
    backpack["weight"] = round(backpack["weight"], 2)

    return backpack

    # This is an example backpack
    # backpack = {
    #     "items": ["toothbrush", "sandwhich", "bon soy", "book on python"],
    #     "weight": 2.750
    # }


items = [
    {"name": "tooth brush", "weight": 0.050},
    {"name": "sandwhich", "weight": 0.100},
    {"name": "iPod", "weight": 0.250},
    {"name": "tomahawk", "weight": 2.000},
    {"name": "bon soy", "weight": 1.000},
    {"name": "sling shot", "weight": 0.800},
    {"name": "book on python", "weight": 1.600},
    {"name": "water", "weight": 1.800},
    {"name": "tissues",  "weight": 0.150},
    {"name": "first aid kit", "weight": 0.750},
    {"name": "flint", "weight": 1.075},
    {"name": "magnifying glass", "weight": 0.450}
]

print(fill_backpack(items))
