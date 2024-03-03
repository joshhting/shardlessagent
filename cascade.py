import random

def cascade(arg: str):
    f = open("lines.txt", "r")
    templateList = f.readlines()
    template = random.choice(templateList)
    # template = templateList[33] # uncomment for specific template
    if template[0] == '+':
        arg = arg.upper()
        template = template[1:]
    joke = template.replace('#', arg)
    return joke
