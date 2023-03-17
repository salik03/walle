import ast

with open('database.txt', 'r') as f:
    database = ast.literal_eval(f.read())

with open('weightage.txt', 'r') as f:
    weightage = ast.literal_eval(f.read())

def increment_weights(items, increment, weights):
    for item in items:
        if item in weights:
            weights[item] += increment
            if weights[item] == 10 or sum(weights.values()) == 10:
                for key in weights:
                    weights[key] = 0
        else:
            weights[item] = increment

biodegradable_weights = {item: 0 for item in database['biodegradable']}
recyclable_weights = {item: 0 for item in database['recyclable']}
hazardous_weights = {item: 0 for item in database['hazardous']}
others_weights = {}

first_category = None

while True:
    user_input = input("What items has Wall-E found in the environment? (comma-separated list, press q to quit)\n")
    if user_input == 'q':
        break
    environment_items = [item.strip() for item in user_input.split(',')]
    biodegradable_items = [item for item in environment_items if item in database['biodegradable']]
    recyclable_items = [item for item in environment_items if item in database['recyclable']]
    hazardous_items = [item for item in environment_items if item in database['hazardous']]
    others_items = [item for item in environment_items if item not in biodegradable_items and item not in recyclable_items and item not in hazardous_items]
    
    if first_category is None:
        if biodegradable_items:
            first_category = 'biodegradable'
        elif recyclable_items:
            first_category = 'recyclable'
        elif hazardous_items:
            first_category = 'hazardous'
    
    if first_category is not None:
        if first_category == 'biodegradable':
            increment_weights(biodegradable_items, 1, biodegradable_weights)
            if sum(biodegradable_weights.values()) == 10 or sum(weightage['biodegradable'].values()) == 10:
                biodegradable_weights = {item: 0 for item in database['biodegradable']}
                first_category = None
        elif first_category == 'recyclable':
            increment_weights(recyclable_items, 1, recyclable_weights)
            if sum(recyclable_weights.values()) == 10 or sum(weightage['recyclable'].values()) == 10:
                recyclable_weights = {item: 0 for item in database['recyclable']}
                first_category = None
        elif first_category == 'hazardous':
            increment_weights(hazardous_items, 1, hazardous_weights)
            if sum(hazardous_weights.values()) == 10 or sum(weightage['hazardous'].values()) == 10:
                hazardous_weights = {item: 0 for item in database['hazardous']}
                first_category = None
            
    increment_weights(others_items, 0.1, others_weights)
    if sum(others_weights.values()) == 10 or sum(weightage['others'].values()) == 10:
        others_weights = {}
    
with open('weightage.txt', 'w') as f:
    f.write(f"{{'biodegradable': {biodegradable_weights}, 'recyclable': {recyclable_weights}, 'hazardous': {hazardous_weights}, 'others': {others_weights}}}")
