quantity = int(input())
days = int(input())

money_spent = 0
spirit = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        money_spent = money_spent + quantity * 2
        spirit += 5
    if current_day % 3 == 0:
        money_spent = money_spent + quantity * 5 + quantity * 3
        spirit += 13
    if current_day % 5 == 0:
        money_spent = money_spent + quantity * 15
        spirit += 17
    if current_day % 15 == 0:
        spirit += 30
    if current_day % 10 == 0:
        spirit -= 20
        money_spent = money_spent + 23


if days % 10 == 0:
    spirit -= 30
print(f'Total cost: {money_spent}')
print(f'Total spirit: {spirit}')
