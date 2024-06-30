class Car:
    '''
    Car class for all car related things

    Attributes:
    ----------

    car_code: int
        int to store a car code
    car_name: str
        a string to store car code
    car_capacity:
        s int to store car capacity
    car_weight: int
        a int to store car weight
    car_type: str
        a str to store car type

    Methods
    ---------
    probationary_licence_prohibited_vehicle(self)
        returns true if car power/mass is greater than 130 or not

    found_matching_car(self,car_code)
        return true if the car code matches

    get_car_type(self)
        return the car type
    '''
    #constructor method
    def __init__(self, car_code, car_name, car_capacity, car_horsepower, car_weight, car_type):

        #declaring classs attributes
        '''

        :param car_code:
        :param car_name:
        :param car_capacity:
        :param car_horsepower:
        :param car_weight:
        :param car_type:
        '''

        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type

    #String method, prints car information
    def __str__(self):
        return str(self.car_code) + "|" + self.car_name + "|"+ str(self.car_capacity) + "|"+ str(self.car_horsepower) +"|"+ str(self.car_weight) +"|"+ str(self.car_type)


    # Method to caclulate prohibited vehicle for probationary licence drives and return True and False
    def probationary_licence_prohibited_vehicle(self):
        '''
        method to calculte power by mass ration per tonne
        :return: True or False
        '''
        self.car_horsepower = int(self.car_horsepower)
        self.car_weight = int(self.car_weight)
        prob = round(((self.car_horsepower/self.car_weight) * 1000),3)
        if prob > 130:
            return False
        elif 0<prob <= 130:
            return True
        else:
            print("Error 404: Please check input information")

    #method to check if entered car code is in database
    def found_matching_car(self, car_code):
        '''
        Method to match the car code
        :param car_code:
        :return: True or False
        '''
        if car_code == self.car_code:
            return True
        else:
            return False


    # Method to return car type

    def get_car_type(self):
        '''
        Method to return car type
        :return: car type
        '''
        return self.car_type




