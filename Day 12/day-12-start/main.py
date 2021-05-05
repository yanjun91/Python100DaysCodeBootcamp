################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength) # This would resulted in NameError potion_strength not defined because there is no potion_strength variable only accessible within drink_potion() function

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

# There is no block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies # Add this line in order for next line to work, but not recommend to modify global variable in function
    enemies += 1
    print(f"enemies inside function: {enemies}")

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1 # Use return instead

increase_enemies()
print(f"enemies outside function: {enemies}")

