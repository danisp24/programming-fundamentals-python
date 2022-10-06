quantity_decorations = int(input())
days = int(input())
ornament = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
christmas_spirit = 0
budget = 0
for n in range (1, days+1):
    if n % 11 == 0:
        quantity_decorations += 2
    if n % 2 == 0:
        budget += ornament * quantity_decorations
        christmas_spirit += 5

    if n % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_decorations
        christmas_spirit += 3 + 10
    if n % 5 == 0:
        budget += tree_lights * quantity_decorations
        christmas_spirit += 17
        if n % 3 == 0:
            christmas_spirit += 30
    if n % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")


