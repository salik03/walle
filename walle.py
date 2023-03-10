import ast

DATABASE_FILE = 'database.txt'
DAMAGE_FILE = 'damage(drought).txt'

# Initialize tool and damage weights
try:
    with open(DATABASE_FILE, 'r') as f:
        data = f.read()
        tool_weights, damage_weights = ast.literal_eval(data)
except FileNotFoundError:
    tool_weights = {}
    damage_weights = {}

# Load damage and tool information
try:
    with open(DAMAGE_FILE, 'r') as f:
        damage_tools = ast.literal_eval(f.read())
except FileNotFoundError:
    damage_tools = {}

def add_environment_to_tools(environment_items):
    for item in environment_items:
        if item not in damage_tools and item not in tool_weights:
            tool_weights[item] = 0

def increment_tool_weights(tools, increment):
    for tool in tools:
        if tool in tool_weights:
            tool_weights[tool] += increment
        else:
            tool_weights[tool] = increment

while True:
    environment = input("What items has Wall-E found in the environment? (comma-separated list, press q to quit)\n")
    if environment.lower() == 'q':
        break
    environment_items = [item.strip() for item in environment.split(',')]
    
    # Add environment items to tools dictionary
    add_environment_to_tools(environment_items)

    # Update tool and damage weights for items found in environment
    for item in environment_items:
        if item in damage_tools:
            if item in damage_weights:
                damage_weights[item] += 1
            else:
                damage_weights[item] = 0

            tools = damage_tools[item]
            increment_tool_weights(tools, 0.1)
    
    # Save updated tool and damage weights to database file
    with open(DATABASE_FILE, 'w') as f:
        f.write(str((tool_weights, damage_weights)))

    print('Tool weights:')
    print(tool_weights)
    print('Damage weights:')
    print(damage_weights)
