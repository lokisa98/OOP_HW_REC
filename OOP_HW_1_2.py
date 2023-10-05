def read_file_in_book(file_name):
    cook_book = {}
    with open(file_name, "rt", encoding = "utf-8") as file:
        for l in file:
            dishes = l.strip()
            amount = int(file.readline())
            ingridients = []
            for i in range(amount):
                row = file.readline().strip()
                name,quantity,measure = (row.split(" | "))
                ingridients.append({'ingredient_name' : name, "quantity": quantity, "measure": measure})
            file.readline()
            cook_book[dishes] = ingridients
    return(cook_book) 

my_list = ['Омлет',"Фахитос"]  
def get_shop_list_by_delishes(name_file,dishes,person_count):

    my_recipes = {}
    for d in dishes:
        y = read_file_in_book(name_file)[d]
        for i in y:
            if i['ingredient_name'] not in my_recipes:
                my_recipes[i['ingredient_name']] = {'quantity' : (int(i['quantity'])*person_count), "measure" : i['measure']}
            else:
                (my_recipes[i['ingredient_name']]['quantity']) += (int(i['quantity'])*person_count)

    return(my_recipes)

print(get_shop_list_by_delishes("recipes.txt",my_list,10))