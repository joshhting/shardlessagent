import random

def cascade(arg: str):
    f = open("lines.txt", "r")
    templateList = f.readlines()
    template = random.choice(templateList)
    # template = templateList[3] # uncomment for specific template

    # check to capitalize arg
    if template[0] == '+':
        arg = arg.upper()
        template = template[1:]

    # check for a/an
    article = "an" if ((0x208222 >> (ord(arg[0]) & 0x1f)) & 1) else "a"
    template = template.replace("a(n)", article)

    joke = template.replace('#', arg)
    return joke
