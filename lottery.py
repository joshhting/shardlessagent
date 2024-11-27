import random

FILENAME = "people.txt"

def draw_lottery(rigged = False):
    if rigged:
        return "The winner is: Yo mama!"
    with open(FILENAME) as file:
        people = [line.strip() for line in file]
    ret = random.choice(people)
    return "The winner is: " + ret + "!"

def view_entries():
    ret = "All contestants:\n"
    with open(FILENAME) as file:
        people = [line for line in file]
    for p in people:
        ret += p
    return ret

def plus_1(entry):
    with open(FILENAME) as file:
        people = [line for line in file]
    people.append(entry + "\n")
    people.sort()
    txt = ""
    for p in people:
        txt += p
    with open(FILENAME, "w") as file:
        file.write(txt)
    return "Added " + entry + " to the list."

def minus_1(entry):
    with open(FILENAME) as file:
        people = [line.strip() for line in file]
    people.remove(entry)
    txt = ""
    for p in people:
        txt += p + "\n"
    with open(FILENAME, "w") as file:
        file.write(txt[:-1])
    return "Removed " + entry + " from the list."