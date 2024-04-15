import random

class TrolleyProblem():
    template = "Oh no! A trolley is headed towards TRACK1. You can pull the lever to divert it to the other track, killing TRACK2 instead. What do you do?"
    track1 = []
    track2 = []
        
    def generateProblem(self, advanced: bool):
        f = open("trolley_base.txt", "r")
        subjects = f.readlines()
        if advanced:
            f = open("trolley_advanced.txt", "r")
            subjects += f.readlines()

        track1Num = random.randint(1, 3)
        track2Num = random.randint(1, 3)
        sample = random.sample(subjects, track1Num + track2Num)
        self.track1 = list(map(lambda n: n.replace('\n', ''), sample[:track1Num]))
        self.track2 = list(map(lambda n: n.replace('\n', ''), sample[track1Num:]))
        

        if len(self.track1) == 1:
            track1Text = self.track1[0]
        elif len(self.track1) == 2:
            track1Text = self.track1[0] + " and " + self.track1[1]
        else:
            track1Text = ""
            for i in range(len(self.track1)):
                if i != 0:
                    track1Text += ", "
                if i == len(self.track1) - 1:
                    track1Text += "and "
                track1Text += self.track1[i]

        if len(self.track2) == 1:
            track2Text = self.track2[0]
        elif len(self.track2) == 2:
            track2Text = self.track2[0] + " and " + self.track2[1]
        else:
            track2Text = ""
            for i in range(len(self.track2)):
                if i != 0:
                    track2Text += ", "
                if i == len(self.track2) - 1:
                    track2Text += "and "
                track2Text += self.track2[i]

        ret = self.template.replace("TRACK1", track1Text).replace("TRACK2", track2Text)
        return ret

