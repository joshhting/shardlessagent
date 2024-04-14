import random

def generateProblem(mode):
    ret = "Oh no! A trolley is headed towards TRACK1. You can pull the lever to divert it to the other track, killing TRACK2 instead. What do you do?"
    people = {  "Noah Anderson Weiskircher",
                "Nathan Goldberg",
                "Wolfgang Kienzle",
                "Josh Ting",
                "Nadir Benbouchaib",
                "Ben Holt",
                "juubs"
                }
    memes = {   "the CEO of Pepsi",
                "the Dune 2 Collectible Popcorn Bucket",
                "a really cute dog",
                "The World Trade Center",
                "Grief, a black card, and Not Dead After All",
                "60 Memnites",
                "stock Murktide",
                "your peanits",
                "55 burgers"
                }

    allVictims = people.union(memes)
    track1Num = random.randint(1, 3)
    track2Num = random.randint(1, 3)
    if mode.lower() == "meme":
        track1 = random.sample(allVictims, track1Num)
        track2 = random.sample(allVictims, track2Num)
    else:
        sample = random.sample(people, track1Num + track2Num)
        track1 = sample[:track1Num]
        track2 = sample[track1Num:]

    if len(track1) == 1:
        track1Text = track1[0]
    elif len(track1) == 2:
        track1Text = track1[0] + " and " + track1[1]
    else:
        track1Text = ""
        for i in range(len(track1)):
            if i != 0:
                track1Text += ", "
            if i == len(track1) - 1:
                track1Text += "and "
            track1Text += track1[i]

    if len(track2) == 1:
        track2Text = track2[0]
    elif len(track2) == 2:
        track2Text = track2[0] + " and " + track2[1]
    else:
        track2Text = ""
        for i in range(len(track2)):
            if i != 0:
                track2Text += ", "
            if i == len(track2) - 1:
                track2Text += "and "
            track2Text += track2[i]

    ret = ret.replace("TRACK1", track1Text).replace("TRACK2", track2Text)
    return ret

print(generateProblem(""))