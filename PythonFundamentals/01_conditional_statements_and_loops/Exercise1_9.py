budget = float(input())
flour_price_kg = float(input())

eggs_pack_price = 0.75 * flour_price_kg
milk_1l = 1.25 * flour_price_kg

cozunak_value = eggs_pack_price + flour_price_kg + 0.25 * milk_1l

count_of_cozunaks = 0
colour_eggs = 0

while budget > cozunak_value:
    count_of_cozunaks += 1
    colour_eggs += 3
    if count_of_cozunaks % 3 == 0:
        colour_eggs = colour_eggs - (count_of_cozunaks - 2)
    budget = budget - cozunak_value

print(f'You made {count_of_cozunaks} cozonacs! Now you have {colour_eggs} eggs and {budget:.2f}BGN left.')
