pokemon_balls = []
pokemon_balls.append("Poke ball")
pokemon_balls.append("Great ball")
pokemon_balls.append("Ultra ball")
pokemon_balls.append("Master ball")
pokemon_balls.append("Premier ball")

# print(pokemon_balls[2])

index = 0

# print(len(pokemon_balls))

# Here is my WHILE loop
# It has a start at index,
# and finishes at the end of the list
print("-------WHILE LOOP-------")
while index < len(pokemon_balls):
    print(pokemon_balls[index])
    index = index + 1

# Here is a FOR loop
print("-------FOR LOOP-------")
for ball in pokemon_balls:
    print(ball)


# FOR every SINGLE ITEM, which i am calling "ball"
# that exists in my COLLECTION OF ITEMS, called "pokemon_balls"
# PRINT that SINGLE ITEM'S VALUE

