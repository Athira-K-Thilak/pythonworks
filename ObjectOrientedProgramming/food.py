
class Cusine:

    cusine_name:str

    def __init__(self,cusine_name):
        
        self.cusine_name=cusine_name

class MealType:

    name=str

    def __init__(self,name):

        self.name=name

class Dish(Cusine,MealType):

    dish_name:str

    def __init__(self,cusine_name,name,dish_name,):

        Cusine.__init__(self,cusine_name)            

        MealType.__init__(self,name)

        self.dish_name=dish_name

    def display_dish_info(self):

        print(self.cusine_name,self.name,self.dish_name)   

dish_instance=Dish("Indian","breakfast","gheeroast")

dish_instance.display_dish_info()



