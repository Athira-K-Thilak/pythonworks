
class SuperHero:

    def __init__(self,name,suit):

        self.name=name

        self.suit=suit

    def __str__(self):

        return self.name


class SpiderMan(SuperHero):

    def  __init__(self,name,suit):

        super().__init__(name,suit)

    def super_power(self):

        print("spider sense","web shooting","sticky hands")

class MinnalMurali(SuperHero):

    def  __init__(self,name,suit):

        super().__init__(name,suit)

    def super_power(self):

        print("running","jumping","reflex")

spiderman_instance=SpiderMan("spiderman","spider suit")

print(spiderman_instance)

spiderman_instance.super_power()
                
minnalmurali_instance=MinnalMurali("minnalmurali","minnalmurali suit")

print(minnalmurali_instance)
        
minnalmurali_instance.super_power()        
  
