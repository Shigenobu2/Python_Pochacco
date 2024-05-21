class pricedown:
    def __init__(self, hm_class, price_down):
        self.hm_class = hm_class
        self.price_down = price_down

    def name_out(self):
        nametxt = "私の名前は、" + self.name + "です"
        return nametxt

    def age_out(self):
        agetxt = "年齢は、" + self.age + "歳です"
        return agetxt