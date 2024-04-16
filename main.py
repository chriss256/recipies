import csv

def foringredients(file_name, ingredients):
    matching_recipe_titles = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if all(ingredient.lower() in row[1].lower() for ingredient in ingredients):
                    matching_recipe_titles.append(row[0])
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please provide the correct path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return matching_recipe_titles


def bytitle(file_name, title):
    matching_recipe_titles = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if title.lower() in row[0].lower():
                    matching_recipe_titles.append(row[0])
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please provide the correct path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return matching_recipe_titles


def get_recipe_details(file_name, title):
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if title.lower() == row[0].lower():
                    return row[1], row[2]
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please provide the correct path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None


def main():
    print("Welcome to the long list of recipes follow the instructions to find the recipes your looking for.")
    file_name = 'blank.csv'
    recipe_titles = []
    while True:
        user_choice = input(
            "Search by ingredients (1) search by title (2) or view details of a recipe (3) or type Exit to quit: ").strip().lower()
        if user_choice == '1':
            ingredients = input("Enter ingredients separated by a comma: ").split(',')
            ingredients = [ingredient.strip().lower() for ingredient in ingredients]
            recipe_titles = foringredients(file_name, ingredients)
            if recipe_titles:
                print()
                print("Recipes with your ingredient(s):")
                print()
                for idx, title in enumerate(recipe_titles, 1):
                    print(f"{idx}. {title}")
                print()
            else:
                print("No recipes with those ingredients.")
        elif user_choice == '2':
            title = input("Enter the recipe title to search for: ").strip().lower()
            recipe_titles = bytitle(file_name, title)
            if recipe_titles:
                print()
                print("Recipes with your title search:")
                print()
                for idx, title in enumerate(recipe_titles, 1):
                    print(f"{idx}. {title}")
                print()
            else:
                print(f"No recipes found with a title containing '{title}'.")
        elif user_choice == '3':
            if not recipe_titles:
                print("Please search for recipes first to view details.")
                continue
            try:
                idx = int(input("Enter the number of the recipe you want to view details for: "))
                if 1 <= idx <= len(recipe_titles):
                    title = recipe_titles[idx - 1]
                    ingredients, instructions = get_recipe_details(file_name, title)
                    if ingredients and instructions:
                        print()
                        print(f"Ingredients for {title}:")
                        print()
                        print("     "+ingredients)
                        print()
                        print(f"Instructions for {title}:")
                        print()
                        print("     "+instructions)
                        print()
                    else:
                        print(f"Details not found for {title}.")
                else:
                    print("Invalid number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif user_choice == 'exit':
            break
        else:
            print(
                f"You need to pick one! Enter '1' to search by ingredients, '2' to search by title, '3' to view recipe details, or 'exit' to quit.")


if __name__ == "__main__":
    main()
