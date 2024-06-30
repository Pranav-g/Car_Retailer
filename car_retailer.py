# Importing OS library for file handling related opertaions
import os
#Importing time package
import time
#Importing RE library for reading file opertaions
import re
#Importing Random to generate a random numbrt
import random
#Calling Retailer class from retailer file
from retailer import Retailer
#Calling Order class from order file
from order import Order
#Calling Car class from car file
from car import Car



class CarRetailer(Retailer, Car):
    '''    A class used to represent operations related Car and Retailer


    Attributes
    ----------
    retailer_id : str
        a string to store retailer ID number
    retailer_name : str
        a string to store the name of the retailer
    carretailer_address : str
        a string to store the address of the retailer
    carretailer_business_hours : int
        a string to store the business hours of the retailer
    carretailer_stock : list
        a list to store the retailer and their car stock
    path : raw string
        path to the file
    cur_hour: int
        A int to store the current time
    postcode: int
         a int to store the value postcode of the user
    car_code: str
        a string to store the value of car need to be removed
    car: str
        a string to store the car object
    car_types : str
         a string to store the car type
    licence_type: str
        a string to store the licence type


    Methods
    ------

    load_current_stock(self,path)
        load the current retailer id and their cars in a list

    is_opertaing(self,cur_hour)
        return is the retailer is still working

    get_all_stock(self)
        return the carretailer_stck list

    get_postcode_distance(slef, postcode)
        return the difference between user postcode and retailer's postcode

    remove_from_stok(self, car_code)
        remoce the car object from the stock and print it on the stock.txt

    add_to_stock(self, car)
        adds the car obejct to a retialers data

    get_stck_by_car_type(self, car_types)
        returns the car object accorinf to the licence type

    car_recomendation(self)
        reandomly returns a car onject

    create order(self, car_code)
        return a order object
        '''
    retailer_dict = {}
    # COnstructor method of class
    def __init__(self, retailer_id, retailer_name, carretailer_address,
                 carretailer_business_hours,carretailer_stock = []):
        super().__init__(retailer_id, retailer_name)
        # self.generate_random_value()
        # Car.__init__(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
        self.carretailer_address = carretailer_address
        self.carreatiler_business_hours = carretailer_business_hours
        self.carretailer_stock = carretailer_stock

        '''
        Parameters
        ----------
        retailer_id : str
            Retailer ID
        retailer_name: str
            Retailer Name
        carretailer_address : str
            Address of the car retailer
        carretailer_business_hours : int
            working hurs of the retailer
        carretailer_stock: list 
            list to store the retailer and their car codes
        '''





    # METHOD TO PRINT RETAILER DETAILES
    def __str__(self):
        return self.retailer_id +"|"+ self.retailer_name +"|"+ self.carretailer_address +"|"+ self.carreatiler_business_hours +"|"+ self.carretailer_stock


    # 2.3.3 Method to Load the current stock of the car retailer according to the retailer_id
    #Will add the path in main function, not here
    try:
        def load_current_stock(self, path):
            '''
            Loads the retailer and their car stock codes in a list
            :param path:
            :return: NA
            '''

            retailer_dict = {}
            #using try and catch if file is removed
            try:
                #reading files
                with open(path, 'r') as file:
                    for l in file:
                        point = l.strip().split(', ')
                        #declaring dictionary
                        key = point[0]
                        values = point[6].replace('[','').replace("'",''), point[12].replace("'",''), point[18].replace("'",''), point[24].replace("'",'').replace(']','')
                        retailer_dict[key] = values
                        for key, values in retailer_dict.items():
                            if key == self.retailer_id:
                                values = retailer_dict[str(self.retailer_id)]
                                #storing values in list
                                self.carretailer_stock = values
                                # return self.carretailer_stock


            except FileNotFoundError:
                print(f"This file is not present at location:{path}")
                return {}








        # 2.3.4 Method to check if car retailer is still working
        def is_operating(self, cur_hour):
            '''
            Method to check if retailer is working or not
            :param cur_hour:
            :return: True or False
            '''
            pattern = r'\(([\d.]+),\s*([\d.]+)\)'
            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"

            try:
                #opening file
                with open(path,'r') as file:
                    for l in file:
                        match = re.search(pattern, l)
                        point = l.strip().split(', ')
                        if self.retailer_id == point[0]:
                            if match:
                                open_hr = float(match.group(1)[1:])
                                close_hr = float(match.group(2)[:-1])
                                biz_hr = open_hr,close_hr
                                #checking current time
                                # curr_time = time.localtime()
                                # #converting local time in decimals
                                # current_hour = current_time.tm_hour + current_time.tm_min / 60
                                #Checks if retailer is working or not
                                if biz_hr[0] < cur_hour < biz_hr[1]:
                                    return True
                                else:
                                    return False
                            # else:
                            #     match

                        else:
                            continue
            # Exceptional handling if file is missing from location
            except FileNotFoundError
                print(f"This file is not present at location:{path}")
                return {}



        #2.3.5 Method to print all the cars of the retailer
        def get_all_stock(self):
            '''
            Method to print all the cars of the retailer
            :return: car.carretailer_stock
            '''

            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
            #Calling load_current_retailer function
            self.load_current_stock(path)
            # print(self.carretailer_stock[1][1])
            print(f"Retailer is {self.retailer_id}")


            return self.carretailer_stock




        #2.3.6 difference between the car retailer PIN and user PIN
        def get_postcode_distance(self, postcode):
            '''
            Method to calculate diffference beteween retailers post code and user post code
            :param postcode:
            :return: difference between their postcodes
            '''
            pattern = r'VIC\d+'
            pin = self.carretailer_address
            #Taking last 4 digits of the retailers postcode
            code = int(pin[3:])
            dis = abs(code - postcode)
            return f"The difference between Your postcode and the Retailer with ID: {self.retailer_id} postcode is  {dis}"




        # 2.3.7 Method to remove a car from stock of a retailer


        def remove_from_stock(self, car_code):
            '''
            Method to remove car object from retailer's stock
            :param car_code:
            :return: True or False
            '''
            #declaring a dictionary
            retailer_dict = {}
            # updated_retailer_dict = {}

            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
            count = 0
            #opening file
            with open(path, 'r') as file:
                for l in file:
                    # count = 0
                    point = l.strip().split(', ')
                    key = point[0]
                    values = point[1:]
                    # point[4] == point[4].replace("'",'').replace('(','')
                    # point[5] == point[5].replace("'",'').replace(')','')
                    # print(point[4])
                    retailer_dict[key] = values

                    count+=1
                    # print(key)
                    # print(self.retailer_id)


                    for key, values in retailer_dict.items():
                        if key == self.retailer_id: #checks for the retailer id in dictionary
                            values = retailer_dict[str(self.retailer_id)]
                            # print(f"value 5 = {values[5]}")
                            #Checks if carcode is in the retailers stock
                            if car_code == values[5].replace("'",'').replace('[','').replace('"',''):
                                si = 5
                                ei = 10
                                retailer_dict[self.retailer_id] = retailer_dict[self.retailer_id][:si] + retailer_dict[self.retailer_id][ei+1:]
                                with open(path, 'r+') as file:
                                    lines = file.readlines()
                                if 1 <= count <= len(lines):
                                    del lines[count - 1]
                                    with open(path, 'w') as file:
                                        file.writelines(lines) #deletes the used line
                                # with open(path, "w") as file:
                                #         for key, values in updated_retailer_dict.items():

                                        l = retailer_dict[self.retailer_id]

                                        file.write(f"{self.retailer_id}, {l}") #Create a new line with new data

                                        return True #if deletion was successfull

                            elif car_code == values[11].replace("'", '').replace('[', ''):
                                si = 11
                                ei = 16
                                retailer_dict[self.retailer_id] = retailer_dict[self.retailer_id][:si] + retailer_dict[self.retailer_id][ei+1:]
                                with open(path, 'r+') as file:
                                    lines = file.readlines()
                                if 1 <= count <= len(lines):
                                    del lines[count - 1]
                                    with open(path, 'w') as file:
                                        file.writelines(lines)
                                        # with open(path, "w") as file:
                                        # if self.retailer_id
                                        l = retailer_dict[self.retailer_id]
                                        file.write(f"{self.retailer_id}, {l}")
                                        return True

                            elif car_code == values[17].replace("'", '').replace('[', ''):
                                si = 17
                                ei = 22
                                retailer_dict[self.retailer_id] = retailer_dict[self.retailer_id][:si] + retailer_dict[self.retailer_id][ei+1:]
                                with open(path, 'r+') as file:
                                    lines = file.readlines()
                                if 1 <= count <= len(lines):
                                    del lines[count - 1]
                                    with open(path, 'w') as file:
                                        file.writelines(lines)
                                        # with open(path, "w") as file:
                                        l = retailer_dict[self.retailer_id]
                                        file.write(f"{self.retailer_id}, {l}")
                                        return True

                            elif car_code == values[23].replace("'", '').replace('[', ''):
                                si = 23
                                ei = 28
                                retailer_dict[self.retailer_id] = retailer_dict[self.retailer_id][:si] + retailer_dict[self.retailer_id][ei+1:]
                                with open(path, 'r+') as file:
                                    lines = file.readlines()
                                if 1 <= count <= len(lines):
                                    del lines[count - 1]
                                    with open(path, 'w') as file:
                                        file.writelines(lines)
                                        # with open(path, "w") as file:
                                        l = retailer_dict[self.retailer_id]
                                        file.write(f"{self.retailer_id}, {l}")
                                        return True

                            else:
                                return False, "Formatting issue"
                                break


                            # else:
                            #     print("This Car donot exist with current retailer")
                            #     break
                            # print(car_code, values[5])


                        else:
                            continue



        #2.3.8 Method to add a car to stock.txt
        def add_to_stock(self, car):
            '''
            Method to add a car retailer to stock
            :param car:

            :return: True or False
            '''
            reatailer_dict = {}
            with open(path, 'w') as file:
                for l in file:
                    point = l.strip().split(', ')
                    key = point[0]
                    values = point[1:]
                    reatiler_dict[key] = values
                    #Checks for retailer
                    if retailid in retailer_dict:
                        car_code, car_name, car_capacity, car_horsepower, car_weight, car_type = car
                        for c in retailer_dict[retailerid]:
                            if item != car_code:
                                value4 = retailer_dict[retailerid][4]
                                value4.append(car)
                                del l
                                #delete unused line
                                for key, values in retailer_dict.items():
                                    line = key + ', ' + ', '.join(values) + '\n'
                                    #print back to stock.txt
                                    file.write(line)
                                    return True #is succesfull
                            else:
                                print(" Car already present in the system")
                                return False #If unsuccessfull
                    else:
                        print("No matching Retailer ID found in system")



        #2.3.9 Method to filter on the basis of a car_type and return car details
        def get_stock_by_car_type(self, car_types):
            '''
            Method to filter according to car type
            :param car_types:
            :return: Car object
            '''
            # retailer_dict = {}
            # updated_retailer_dict = {}
            #creating a list to store valid car objects
            car_object = []
            #inintiating a list
            retailer_dict ={}
            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
            with open(path, 'r') as file:
                #readinf the file
                for l in file:
                    point = l.strip().split(', ')
                    key = point[0]
                    values = point[1:]
                    #adding values to dictionary
                    retailer_dict[key] = values

                    #formatting the values

                    cartype1 = point[11].replace('"','').replace("'",'')
                    cartype2 = point[17].replace('"','').replace("'",'')
                    cartype3 = point[23].replace('"','').replace("'",'')
                    cartype4 = point[29].replace("'",'').replace('"','').replace(']','')
                    # print(cartype4)
                    # print(point[29])
                    # print(cartype1)
                    # print(point[11])

                    #checks for the retailer id


                    for key, values in retailer_dict.items():
                        if key == self.retailer_id:
                            values = retailer_dict[str(self.retailer_id)]
                            for i in range(len(car_types)):
                                #checks for the car type
                                if car_types[i] == cartype1:
                                    c0 = Car(values[5].replace('[','').replace("'",''),
                                             values[6], values[7], values[8], values[9],values[10].replace('"','').replace(']',''))
                                    #append the values to list
                                    car_object.append(str(c0))
                                    # return car_types[1]
                                if car_types[i] == cartype2:
                                    c5 = Car(values[11].replace('[', '').replace("'", ''),
                                             values[12], values[13], values[14], values[15],
                                             values[16].replace('"', '').replace(']', ''))
                                    car_object.append(str(c5))
                                if car_types[i] == cartype3:
                                    c6 = Car(values[17].replace('[', '').replace("'", ''),
                                             values[18], values[19], values[20], values[21],
                                             values[22].replace('"', '').replace(']', ''))
                                    car_object.append(str(c6))
                                if car_types[i] == cartype4:
                                    c7 = Car(values[23].replace('[', '').replace("'", ''),
                                             values[24], values[25], values[26], values[27],
                                             values[28].replace('"', '').replace(']', ''))
                                    car_object.append(str(c7))
                                if not car_object:
                                    print(f"Retailer donot have this car type in stock")

                            return car_object




        #2.3.10 Mthod to return a car object as per the lisence type asked by the user
        def get_stock_by_licence_type(self, licence_type):
            '''
            Method to return a car object on the basis of licence
            :param licence_type:
            :return: car object list
            '''
            #declaring dictinary
            retailer_dict = {}
            #declaring  aemplty list
            car_object_list = []
            new_list = []
            # updated_retailer_dict = {}
            # tuple_updated_retailer_dict = {}
            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"

            with open(path, 'r') as file:
                #reading file
                for l in file:
                    point = l.strip().split(', ')
                    key = point[0]
                    values = point[1:]
                    retailer_dict[key] = values


                    for key, values in retailer_dict.items():
                        #checks for retailer id
                        if key == self.retailer_id:
                            values = retailer_dict[str(self.retailer_id)]
                            c_cr1 = Car(values[5].replace('[',''), values[6], values[7], values[8].replace('"','').replace("'",''), values[9].replace('"','').replace("'",''), values[10].replace(']',''))
                            c_cr2 = Car(values[11].replace('[',''), values[12], values[13], values[14].replace('"','').replace("'",''), values[15].replace('"','').replace("'",''), values[16].replace(']',''))
                            c_cr3 = Car(values[17].replace('[',''), values[18], values[19], values[20].replace('"','').replace("'",''), values[21].replace('"','').replace("'",''), values[22].replace(']',''))
                            c_cr4 = Car(values[23].replace('[',''), values[24], values[25], values[26].replace('"','').replace("'",''), values[27].replace('"','').replace("'",''), values[28].replace(']',''))

                            if licence_type == "P":
                                #if licence type input was probationry
                                if c_cr1.probationary_licence_prohibited_vehicle() == True:
                                    car_object_list.append(str(c_cr1))
                                if c_cr2.probationary_licence_prohibited_vehicle() == True:
                                    car_object_list.append(str(c_cr2))
                                if c_cr3.probationary_licence_prohibited_vehicle() == True:
                                    car_object_list.append(str(c_cr3))
                                if c_cr4.probationary_licence_prohibited_vehicle() == True:
                                    car_object_list.append(str(c_cr4))

                                return car_object_list

                            elif licence_type == "L" or licence_type == "F":
                                #for all other cases, ar object
                                # new_list = car_object_list[(c_cr1) + (c_cr2) + (c_cr3) + (c_cr4)]
                                return str(c_cr1), str(c_cr2), str(c_cr3), str(c_cr4)




        #2.3.11 Method to randomly select a car object from the retailer stock
        def car_recommendation(self):
            '''
            Method to recommend a car according a retailer
            :return: car onbject
            '''
            # Declaring a retailer dictionary which holds all the car details
            retailer_dict = {}
            updated_retailer_dict = {}
            # tuple_updated_retailer_dict = {}
            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"

            with open(path, 'r') as file:
                #reading file
                for l in file:
                    point = l.strip().split(', ')
                    key = point[0]
                    values = point[6:]
                    retailer_dict[key] = values
                    for key, values in retailer_dict.items():
                        grp_values = values[:6], values[6:12], values[12:18], values[18:]
                        updated_retailer_dict[key] = grp_values

                    for key, values in updated_retailer_dict.items():
                        #checks for the retailer id
                        if key == self.retailer_id:
                            values = updated_retailer_dict[str(self.retailer_id)]
                            recom = random.choice(values)
                            c2 = Car(recom[0].replace('"','').replace("'",'').replace('[',''), recom[1].replace("'",''), recom[2].replace("'",''), recom[3].replace("'",''), recom[4].replace("'",''), recom[5].replace("'",'').replace('"','').replace(']',''))
                            return f"Car code: {str(c2.car_code)}\nCar name:{str(c2.car_name)}\nCar capacity:{str(c2.car_capacity)}\nCar horsepower: {str(c2.car_horsepower)}\nCar weight:{str(c2.car_weight)}\nCar type:{str(c2.car_type)}"






        #2.3.12 Method to create order
        def create_order(self, car_code):
            '''
            Method to create a order
            :param car_code:
            :return: order object
            '''
            #present time
            timestamp = int(time.time())
            path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\order.txt"
            # print(self.carretailer_stock)
            # if car_code == self.carretailer_stock[0][0] or car_code == self.carretailer_stock[1][0] or car_code == self.carretailer_stock[2][0] or car_code == self.carretailer_stock[0] or car_code == self.carretailer_stock[1] or car_code == self.carretailer_stock[2]:
            #     print("yes")
            #if return value of remove from stock is true, then only create the order
            if self.remove_from_stock(car_code) == True:
                co = Car(car_code, "none", "none", "none", "none", "none")
                ro = Retailer(self.retailer_id, "none")
                o1 = Order("none", car_code, self.retailer_id, timestamp)
                o2 = Order(o1.generate_order_id(car_code), co, ro, timestamp)
                #writing back the order object in order.txt
                with open(path, 'a+') as file:
                    file.write(str(o2) + "\n")
                return str(o2)


    #catches if file gets removed accidently or intentionally
    except FileNotFoundError:
        (print("File not found"))




# class BicycleRetailer(Retailer):
#     def __init__(self, bycycleretaileradd):
#         Retailer.__init__(retailer_id,ratiler_name)
#         self.bycycleretaileradd = bycycleretaileradd















