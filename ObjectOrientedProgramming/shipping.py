
class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)   

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self, weight):
    
        print(weight*20)

class SatndardShipping(Shipping):

    def calculate_shipping_cost(self, weight):
    
        print(weight*10)


express_instance=ExpressShipping()

express_instance.calculate_shipping_cost(10)

std_instance=SatndardShipping()

std_instance.calculate_shipping_cost(10)

