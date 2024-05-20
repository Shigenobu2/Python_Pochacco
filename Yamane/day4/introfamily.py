from introduce import Intoro
class IntroFam(Intoro):
     def __init__(self,name,age,cat):
        super().__init__(name,age)
        self.cat=cat

     def cat_out(self):
        cat_name="飼い猫の名前は"+self.cat+"です"
        return cat_name
        