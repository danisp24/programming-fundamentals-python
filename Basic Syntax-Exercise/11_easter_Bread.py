budget = float(input())
kg_flour = float(input())
kg_eggs = kg_flour * 0.75
litre_milk = kg_flour * 1.25
ml_milk = litre_milk / 4
breads_counter = 0
colored_eggs = 0
one_bread_price = ml_milk + kg_flour + kg_eggs
while budget >= one_bread_price:
    budget -= one_bread_price
    breads_counter += 1
    colored_eggs += 3
    if breads_counter % 3 == 0:
        colored_eggs -= breads_counter - 2
print(f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

