from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, petname):
        super().__init__(name, age)
        self.petname = petname

    def cat_out(self):
        pettxt = "飼い猫の名前は、" + self.petname + "です"
        return pettxt
