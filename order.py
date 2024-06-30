import random
import time
from car import Car
from retailer import Retailer



class Order(Car, Retailer):
    '''
    Class for all the orders

    Attributes
    ----------
    order_id : int
        a int to store order id

    order_car : str
        a str to store car code

    order retailer: int
        a int to store retailer id

    order_ceration time: int
        a int to store order creation time
    car_code : str
        anothe rstr to hold car code
    '''
    def __init__(self, order_id, order_car, order_retailer, order_creation_time):
        '''

        :param order_id:
        :param order_car:
        :param order_retailer:
        :param order_creation_time:
        '''
        # Car().__init__()
        # Retailer().__init__()
        self.order_id = order_id
        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time

    def __str__(self):
        return f"{self.order_id} {(self.order_car.car_code)} {self.order_retailer.retailer_id}  {self.order_creation_time}"


    #2.4.3 Method to generate a unique order ID
    def generate_order_id(self, car_code):
        '''

        :param car_code:
        :return: unique order id
        '''
        str_1 = "~!@#$%^&*"

        #step1
        leng = 6
        my_str = ''.join(chr(random.randint(97,122)) for _ in range(leng))

        #step2
        my_str = ''.join(my_str[i].upper() if i % 2 == 1 else my_str[i] for i in range(leng))

        #step3
        asci = [ord(char) for char in my_str]

        #step4

        remain = [((acode ** 2) % len(str_1)) for acode in asci]

        #step5
        corchar = ""
        cvalue = []
        for r in remain:
            corchar +=str_1[r]
            cvalue.append(corchar)

        #step6
        final=[]
        for i in range(len(corchar)):
            my_str += corchar[i] * i

        final.append(my_str)

        #step7
        # timestamp = int(time.time())
        result = "".join([final[0],self.order_car,str(self.order_creation_time)])
        return result







