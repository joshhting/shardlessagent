import random
from dynamo import delete_db_item, add_db_item, get_all_items

def draw_lottery(rigged = False):
    if rigged:
        return "The winner is: Yo mama!"
    people = [person['name'].strip() for person in get_all_items()]
    ret = random.choice(people)
    return "The winner is: " + ret + "!"

def view_entries():
    ret = "All contestants:\n" + "\n".join(person['name'] for person in get_all_items())
    return ret

def plus_1(entry):
    add_db_item(entry)
    return "Added " + entry + " to the list."

def minus_1(entry):
    delete_db_item(entry)
    return "Removed " + entry + " from the list."
