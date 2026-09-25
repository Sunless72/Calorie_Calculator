db= [
    ("apple", 95.0),
    ("banana", 105.0),
    ("egg", 78.0),
    ("slice of bread", 70.0),
    ("chicken breast", 165.0),
    ("rice cup", 206.0),
    ("glass of milk", 122.0),
    ("roti (1 medium)", 104.0),
    ("paratha (plain)", 260.0),
    ("puri (1 piece)", 101.0),
    ("dal tadka (1 bowl)", 150.0),
    ("dal makhani (1 bowl)", 260.0),
    ("chana masala (1 bowl)", 240.0),
    ("rajma (1 bowl)", 210.0),
    ("palak paneer (1 bowl)", 230.0),
    ("paneer butter masala (1 bowl)", 340.0),
    ("butter chicken (1 cup)", 438.0),
    ("chicken tikka (6 pieces)", 220.0),
    ("mutton curry (1 cup)", 340.0),
    ("cooked basmati rice (1 cup)", 190.0),
    ("chicken biryani (1 plate)", 480.0),
    ("veg biryani (1 plate)", 330.0),
    ("khichdi (1 cup)", 180.0),
    ("idli (1 piece)", 58.0),
    ("plain dosa (1 piece)", 133.0),
    ("masala dosa (1 piece)", 250.0),
    ("sambar (1 bowl)", 90.0),
    ("medu vada (1 piece)", 145.0),
    ("upma (1 cup)", 190.0),
    ("poha (1 cup)", 180.0),
    ("samosa (1 piece)", 262.0),
    ("pakora (1 piece)", 60.0),
    ("cucumber raita (1 bowl)", 75.0),
    ("gulab jamun (1 piece)", 150.0),
    ("masala chai with milk & sugar (1 cup)", 80.0),
    ("sweet lassi (1 glass)", 210.0),
]

tc = 0.0

consumed_items = []

print("=== Calorie Calculator ===")
print("Available items in database:")
for item in db:
    print("- " + item[0] + " (" + str(item[1]) + " cal)")
print("_____x_____x_____x_____x_____x_____")
print("Enter 'done' when you finish logging food.\n")

while True:
    name = input("Enter food item: ").strip().lower()

    if name == "done":
        break
    if name == "":
        continue

    found = False
    calories_per_unit = 0.0

    for record in db:
        db_food = record[0]
        db_calories = record[1]

        if db_food == name:
            found = True
            calories_per_unit = db_calories
            break

    if found:
        qty = input("Enter quantity/servings of " + name + ": ")
        quantity = float(qty)

        item_total = calories_per_unit * quantity
        tc = tc + item_total

        consumed_items.append((name, quantity, item_total))
        print("Added: " + str(item_total) + " calories.\n")
    else:
        print("Error: '" + name + "' not found in database. Try again.\n")

print("\n _____x_____x_____ SUMMARY _____x_____x_____")
if len(consumed_items) == 0:
    print("No items were logged.")
else:
    for entry in consumed_items:
        name = entry[0]
        qty = entry[1]
        cals = entry[2]
        print(name + " x " + str(qty) + " = " + str(cals) + " calories")

    print("_____x_____x_____x_____x_____x_____")
    print("Total Calories Consumed: " + str(tc) + " kcal")
print("_____x_____x_____x_____x_____x_____")