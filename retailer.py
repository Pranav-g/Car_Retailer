import random
class Retailer():
    '''
    Class for retialers

    Attributes
    -----------
    retailer_id : int
        a int to store retailer id
    retailer_name: str
        a str to store retailer name

    Methods
    --------------
    generate_retailer_id(self)
        generates a random retailer id
    '''

    #Class constructor
    def __init__(self, retailer_id, retailer_name):
        '''

        :param retailer_id:
        :param retailer_name:
        '''
        self.retailer_id = retailer_id
        if self.retailer_id == -1:
            self.generate_retailer_id()
        self.retailer_name = retailer_name

    # String method for output
    def __str__(self):
        return str(self.retailer_id) + self.retailer_name


    # Method generates a random 8 digit number and set it as retailer ID
    #also store it in exisiting retailers lists.
    def generate_retailer_id(self):
        '''
        Method to generate random retailer id
        :return: generated retaielr ID
        '''

        #initialisting the list
        list_retailer = []

        # storing randomly generated unique ID in the list
        while True:
            rand = random.randint(10000000, 99999999)
            if rand not in list_retailer:
                list_retailer.append(rand)
                self.retailer_id = rand
                break
            else:
                continue




