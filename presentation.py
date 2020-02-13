shopping_list = []
ingredients = {}

ingredients = {"Bread": {"calories": 67, "total fat(g)": 0.3, "Cholesterol(mg)": 0, "Sodium(mg)": 2, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Salt": {"calories": 0, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 3021.2, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Pepper": {"calories": 5.8, "total fat(g)": 0.1, "Cholesterol(mg)": 0, "Sodium(mg)": 0.5, "Total Carbohydrate(g)": 1.5, "Protein(g)": 0}}
ingredients = {"Onion": {"calories": 41, "total fat(g)": 0.2, "Cholesterol(mg)": 0, "Sodium(mg)": 2.8, "Total Carbohydrate(g)": 10, "Protein(g)": 1.3}}
ingredients = {"Garlic": {"calories": 1.5, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 0.5, "Total Carbohydrate(g)": 1, "Protein(g)": 0.2}}
ingredients = {"Carrot": {"calories": 16, "total fat(g)": 0.1, "Cholesterol(mg)": 0, "Sodium(mg)": 27, "Total Carbohydrate(g)": 3.8, "Protein(g)": 0.3}}
ingredients = {"Celery": {"calories": 6.8, "total fat(g)": 0.1, "Cholesterol(mg)": 0, "Sodium(mg)": 34, "Total Carbohydrate(g)": 1.5, "Protein(g)": 0.3}}
ingredients = {"Sugar": {"calories": 16, "total fat(g)": 0.1, "Cholesterol(mg)": 0, "Sodium(mg)": 2, "Total Carbohydrate(g)": 4.2, "Protein(g)": 0}}
ingredients = {"Chicken": {"calories": 62.1, "total fat(g)": 3.7, "Cholesterol(mg)": 26.7, "Sodium(mg)": 20, "Total Carbohydrate(g)": 0, "Protein(g)": 6.7}}
ingredients = {"Eggs": {"calories": 35, "total fat(g)": 3, "Cholesterol(mg)": 108, "Sodium(mg)": 35, "Total Carbohydrate(g)": 0, "Protein(g)": 3}}
ingredients = {"Flour": {"calories": 455, "total fat(g)": 1.2, "Cholesterol(mg)": 0, "Sodium(mg)": 2.5, "Total Carbohydrate(g)": 95, "Protein(g)": 13}}
ingredients = {"Milk": {"calories": 125, "total fat(g)": 4.7, "Cholesterol(mg)": 20, "Sodium(mg)": 127, "Total Carbohydrate(g)": 12, "Protein(g)": 8.5}}
ingredients = {"Chicken Stock": {"calories": 86, "total fat(g)": 2.9, "Cholesterol(mg)": 7.2, "Sodium(mg)": 343, "Total Carbohydrate(g)": 8.5, "Protein(g)": 3.8}}
ingredients = {"Oil": {"calories": 124, "total fat(g)": 14, "Cholesterol(mg)": 0, "Sodium(mg)": 9, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Vinegar": {"calories": 2.7, "total fat(g)": 0.3, "Cholesterol(mg)": 0, "Sodium(mg)": 0.3, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Vanilla Extract": {"calories": 12, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 0.4, "Total Carbohydrate(g)": 0.5, "Protein(g)": 0}}
ingredients = {"Baking Powder": {"calories": 2.4, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 488, "Total Carbohydrate(g)": 1.3, "Protein(g)": 0}}
ingredients = {"Baking Soda": {"calories": 0, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 1259, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Brown Sugar": {"calories": 11, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 0.8, "Total Carbohydrate(g)": 2.9, "Protein(g)": 0}}
ingredients = {"Cornstarch": {"calories": 488, "total fat(g)": 0.1, "Cholesterol(mg)": 0, "Sodium(mg)": 12, "Total Carbohydrate(g)": 117, "Protein(g)": 0.3}}
ingredients = {"Granulated Sugar": {"calories": 11, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 2.8, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Honey": {"calories": 64, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 0.8, "Total Carbohydrate(g)": 17, "Protein(g)": 0.1}}
ingredients = {"Cheese": {"calories": 113, "total fat(g)": 9.3, "Cholesterol(mg)": 28, "Sodium(mg)": 183, "Total Carbohydrate(g)": 0.9, "Protein(g)": 6.4}}
ingredients = {"Kosher Salt": {"calories": 0, "total fat(g)": 0, "Cholesterol(mg)": 0, "Sodium(mg)": 3021.2, "Total Carbohydrate(g)": 0, "Protein(g)": 0}}
ingredients = {"Potato": {"calories": 161, "total fat(g)": 0.2, "Cholesterol(mg)": 0, "Sodium(mg)": 17, "Total Carbohydrate(g)": 37, "Protein(g)": 4.3}}
ingredients = {"Nut": {"calories": 172, "total fat(g)": 15, "Cholesterol(mg)": 0, "Sodium(mg)": 77, "Total Carbohydrate(g)": 6, "Protein(g)": 5.7}}
ingredients = {"Yeast": {"calories": 13, "total fat(g)": 0.3, "Cholesterol(mg)": 0, "Sodium(mg)": 2, "Total Carbohydrate(g)": 1.6, "Protein(g)": 1.6}}

user_choice = input("Would you like to make a list?: ")

if "Y" in user_choice.upper():
    user_num = int(input("How many items will be in your list?: "))
for i in range(user_num):
    user_ingredient = input("What is the ingredient?: ")
    shopping_list.append(user_ingredient)
    print (shopping_list)
shopping_list.sort()

for item in shopping_list:
    if item in ingredients.keys():
        print(ingredients[item])
