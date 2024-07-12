# Define locations and their descriptions
locations = {
    "Forest": {
        "description": "You stand in a dense forest, sunlight filtering through the leaves. A path leads north and a faint trail leads east.",
        "exits": ["north", "east"],
        "items": ["rusty sword"],
        "actions": {
            "north": "Swamp",
            "east": "Ruins"
        }
    },
    "Swamp": {
        "description": "A murky swamp lies before you. Willows weep and strange insects buzz. To the south lies the forest.",
        "exits": ["south"],
        "enemies": ["Giant Frog"],
        "actions": {
            "south": "Forest"
        }
    },
    "Ruins": {
        "description": "Crumbling ruins of an ancient building. A hidden passage leads north. The forest lies to the west.",
        "exits": ["north", "west"],
        "items": ["key"],
        "actions": {
            "north": "Hidden Room",
            "west": "Forest"
        }
    },
    "Hidden Room": {
        "description": "A dusty hidden room with a treasure chest in the corner. A locked door leads south.",
        "exits": ["south"],
        "items": ["treasure"],
        "requires": ["key"],
    }
}

# Define inventory to store collected items
inventory = []

# Define current location
current_location = "Forest"

# Game loop
while True:
  # Print location description and exits
  print(locations[current_location]["description"])
  print("Exits:", ", ".join(locations[current_location]["exits"]))

  # Check for enemies in current location
  if "enemies" in locations[current_location]:
    enemy = locations[current_location]["enemies"][0]
    print(f"You encounter a {enemy}!")
    # Implement enemy encounter logic here (fight, run, etc.)
    # ...

  # Get user input for action
  action = input("What do you do? ").lower()

  # Check if action is a valid exit
  if action in locations[current_location]["exits"]:
    current_location = locations[current_location]["actions"][action]
  # Check if action is to pick up an item
  elif action == "pick up":
    item = input("What do you want to pick up? ").lower()
    if item in locations[current_location]["items"] and item not in inventory:
      inventory.append(item)
      print(f"You pick up the {item}.")
      del locations[current_location]["items"][locations[current_location]["items"].index(item)]
    else:
      print(f"You don't see a {item} here.")
  # Check if action is to use an item
  elif action == "use":
    item = input("What do you want to use? ").lower()
    if item in inventory:
      # Implement item usage logic here (unlock doors, etc.)
      # ...
      if "requires" in locations[current_location] and item == locations[current_location]["requires"]:
        if locations[current_location]["requires"] in inventory:
          print(f"You unlock the door with the {item}.")
          del locations[current_location]["requires"]
        else:
          print(f"You don't have the right item to use here.")
      else:
        print(f"The {item} doesn't seem to be useful here.")
    else:
      print(f"You don't have a {item} in your inventory.")
  # Handle invalid input
  else:
    print("I don't understand what you mean.")

  # Check for win condition (reaching hidden room with treasure)
  if current_location == "Hidden Room" and "treasure" in inventory:
    print("Congratulations! You found the treasure and won the game!")
    break


