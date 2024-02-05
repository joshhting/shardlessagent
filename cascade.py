import random

def cascade(arg: str):
    f = open("lines.txt", "r")
    jokes = f.readlines()
    joke = random.choice(jokes).replace('#', arg)
    # joke = jokes[3].replace('#', arg) # uncomment for pepsi
    return joke
