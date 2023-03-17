import ast

with open('database.txt', 'r') as f:
    database = ast.literal_eval(f.read())

with open('weightage.txt', 'r') as f:
    weightage = ast.literal_eval(f.read())

def increment_weights(items, increment, weights):
    for item in items:
        if item in weights:
            if weights[item] < 10:
                weights[item] += increment
                if weights[item] >= 10:
                    for k in weights.keys():
                        weights[k] = 0
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
    
    if not first_category:
        if any(item in database['biodegradable'] for item in environment_items):
            first_category = 'biodegradable'
        elif any(item in database['recyclable'] for item in environment_items):
            first_category = 'recyclable'
        elif any(item in database['hazardous'] for item in environment_items):
            first_category = 'hazardous'
    
    if first_category == 'biodegradable':
        biodegradable_items = [item for item in environment_items if item in database['biodegradable']]
        increment_weights(biodegradable_items, 1, biodegradable_weights)
        
        if all(w == 0 for w in biodegradable_weights.values()):
            first_category = None
            
    elif first_category == 'recyclable':
        recyclable_items = [item for item in environment_items if item in database['recyclable']]
        increment_weights(recyclable_items, 1, recyclable_weights)
        
        if all(w == 0 for w in recyclable_weights.values()):
            first_category = None
            
    elif first_category == 'hazardous':
        hazardous_items = [item for item in environment_items if item in database['hazardous']]
        increment_weights(hazardous_items, 1, hazardous_weights)
        
        if all(w == 0 for w in hazardous_weights.values()):
            first_category = None
            
    else:
        others_items = [item for item in environment_items if item not in database['biodegradable'] and item not in database['recyclable'] and item not in database['hazardous']]
        increment_weights(others_items, 1, others_weights)

with open('weightage.txt', 'w') as f:
    f.write(f"{{'biodegradable': {biodegradable_weights}, 'recyclable': {recyclable_weights}, 'hazardous': {hazardous_weights}, 'others': {others_weights}}}")
