import ast

DATABASE_FILE = 'database.txt'
DAMAGE_FILE = 'damage.txt'

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

while True:
    environment = input("What items has Wall-E found in the environment? (comma-separated list, press q to quit)\n")
    if environment.lower() == 'q':
        break
    environment_items = [item.strip() for item in environment.split(',')]

    # Update tool and damage weights for items found in environment
    for item in environment_items:
        if item in damage_tools:
            if item in damage_weights:
                damage_weights[item] += 1
            else:
                damage_weights[item] = 0

            tools = damage_tools[item]
            for tool in tools:
                if tool in tool_weights:
                    tool_weights[tool] += 1
                else:
                    tool_weights[tool] = 0

    # Save updated tool and damage weights to database file
    with open(DATABASE_FILE, 'w') as f:
        f.write(str((tool_weights, damage_weights)))

    print('Tool weights:')
    print(tool_weights)
    print('Damage weights:')
    print(damage_weights)
