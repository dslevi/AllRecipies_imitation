import sqlite3

DB = None
CONN = None

# def make_new_Detail(id, dish, type, prep, cook, serving):
#     query = """INSERT INTO Details VALUES (?, ?, ?, ?, ?, ?)"""
#     DB.execute(query, (id, dish, type, prep, cook, serving,))
#     CONN.commit()
#     print """\
#     Successfully added dish details: 
#     Dish: %s 
#     Type: %s 
#     Prep time: %s 
#     Cook time: %s 
#     Serving size: %s""" % (dish, type, prep, cook, serving)


# def make_new_Direction(id, dish, directions):
#     query = """INSERT INTO Directions VALUES (?, ?, ?)"""
#     DB.execute(query, (id, dish, directions,))
#     CONN.commit()
#     print """\
#     Successfully added dish directions:
#     Dish: %s
#     Directions: %s""" % (dish, directions)

# def make_new_Recipe(id, dish, ingredients, recipe):
#     ingred = ingredients.split()
#     query = """INSERT INTO Recipe VALUES (?, ?, ?, ?)"""
#     DB.execute(query, (id, dish, ingredients, recipe,))
#     CONN.commit()
#     print """\
#     Successfully added dish recipe:
#     Dish: %s
#     Main ingredient 1: %s
#     Main ingredient 2: %s
#     Main ingredient 3: %s
#     Recipe: %s""" % (dish, ingred[0], ingred[1], ingred[2], recipe)

def find_Recipies_with_ingreds(ingred):
    distinct_recipies = []
    for i in ingred:
        ingred_query = "%" + i + "%"
        query = """SELECT dish FROM Recipe WHERE main_ingred LIKE ?"""
        DB.execute(query, (ingred_query,))
        all_recipies = DB.fetchall()
        for x in all_recipies:
            if x[0] not in distinct_recipies:
                distinct_recipies.append(x[0])
    print "Recipe matches:"
    for x in distinct_recipies:
        print x

def find_Recipies_with_details(type, prep, cook, serving):
    pass

def show_all_Recipies():
    query = """SELECT * FROM Recipe JOIN Directions ON (Recipe.id = Directions.id)"""
    DB.execute(query, ())
    row = DB.fetchall()
    for x in row:
        print "Dish:", x[1]
        print "---"
        print "Ingredients:"
        ingredients = x[3].split("|")
        for y in ingredients:
            print y.strip()
        print "Directions:"
        directions = x[6].split("|")
        for y in directions:
            print y.strip()
        print ""

def find_Recipe(dish):
    pass

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("Recipies.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit" or command != "q":
        input_string = raw_input("AllRecipies Clone> ")
        tokens = input_string.split()
        command = tokens[0]

        if command == "new_detail":
            print "Please enter the below, separated by commas."
            details = raw_input("Id, dish, type, prep, cook, and serving size:")
            tokens = details.split(", ")
            make_new_Detail(*tokens)
        elif command == "new_direction":
            id, dish = raw_input("Id, Dish:").split(", ")
            direction = ""
            while True:
                x = raw_input("Directions: ")
                if x == "end":
                    break
                direction += x + "|"
            make_new_Direction(id, dish, direction)
        elif command == "new_recipe":
            make_new_Recipe(args[0], args[1], args[2], args[3], args[4:])
        elif command == "find_ingreds":
            ingredients = []
            while True:
                x = raw_input("Ingredients: ")
                if x == "":
                    break
                ingredients.append(x)
            find_Recipies_with_ingreds(ingredients)
        elif command == "find_details":
            find_Recipies_with_details(*args)
        elif command == "show_recipies":
            show_all_Recipies()
        elif command == "find_recipe":
            find_Recipe(*args)
        elif command == "H":
            print """
            Valid commands:

            new_detail
            new_direction
            new_recipe
            find_ingreds
            find_details
            show_recipies
            find_recipe
            """
        else:
            print "Invalid command. Enter 'H' for a list of commands."

    CONN.close()

if __name__=="__main__":
    main()


