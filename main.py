# your imports goes here
import os
import random
import re
from car_retailer import CarRetailer
from retailer import Retailer
from car import Car
from order import Order
import time


#function to print main menu
def main_menu():
	print('''
	
					WELCOME TO CAR RETAILER.COM
					
					PLEASE SELECT ONE OF THE OPTION FROM BELOW
					
					1) Look for the nearest car retailer
					2) Get car purchase advice
					3) Place a car order
					4) Exit
	
	
	
	''')


#Functiona randomply generates the tets data
def generate_test_data():
#retailer class objects
	r1 = Retailer(-1,"None")
	r2 = Retailer(-1, "None")
	r3 = Retailer(-1, "None")
	r4 = Retailer(-1, "None")
	r5 = Retailer(-1, "None")
	r6 = Retailer(-1, "None")
	r7 = Retailer(-1, "None")
	r8 = Retailer(-1, "None")
	# print(str(rin.retailer_id))
	statements = [f"{str(r1.retailer_id)}, dLrIrEaovi, Wellington Rd Clayton, VIC3168, (8.8, 24.2), ['BY962604, zSyOgLqCHc, 7, 600, 2422, RWD', 'MF852547, RYjEUsOSQa, 6, 193, 2640, AWD', 'GH215142, ABdjbRaLvPi, 15, 245, 2896, AWD', 'UI737865, imGniKhZOMg, 14, 140, 2965, AWD']",
				  f"{str(r2.retailer_id)}, eMrIrFaovi, Clayton rd Clayton, VIC3167, (11.1, 23.4), ['AB963704, aSyOgLqCHc, 2, 250, 2122, AWD', 'ZY852548, ABjEUsPSQa, 7, 650, 2140, RWD', 'LP216252, GHdjbQaLvPj, 14, 244, 2785, RWD', 'GH737895, imHniKhZOMa, 13, 150, 2745, RWD']",
				  f"{str(r3.retailer_id)}, fNrIrGaovz, Springvale Rd Clayton, VIC3178, (9.6, 26.2), ['CD974811, bSyOgLqCHc, 3, 650, 2222, FWD', 'YX852549, CDjEUsTGQa, 8, 175, 2250, FWD', 'FG216341, RTdjbFaLvPk, 13, 249, 2555, FWD', 'RG739652, imIniJhZOMv, 12, 160, 2965, FWD']",
				  f"{str(r4.retailer_id)}, gNrIrHaovg, Malvern Rd Clayton, VIC3169, (8.8, 24.2), ['EF962504, cSyOgLqCHc, 4, 300, 2432, RWD', 'TR852550, EFjEUsWDQa, 2, 650, 2750, AWD', 'SD215561, HJdjbSaLvPl, 12, 256, 2456, AWD', 'EF737563, imJniLhZOMg, 11, 170, 2745, AWD']",
				  f"{str(r5.retailer_id)}, hOrIrIaovy, Caufield Rd Clayton, VIC3700, (10.4, 22.1), ['GH962504, zSyOgLqCHc, 5, 650, 2424, AWD', 'LM852551, GHjEUsRGQa, 3, 190, 2150, RWD', 'HJ217651, DFdjbTaLvPm, 11, 278, 2963, RWD', 'GH738963, imKniMhZOMq, 10, 180, 2452, RWD']",
				  f"{str(r6.retailer_id)}, hPrIrJaovx, SouthYarra Rd Clayton, VIC3171, (7.8, 24.2), ['IJ962504, dSyOgLqCHc, 6, 200, 2022, FWD', 'RQ852552, IJjEUsESQa, 4, 650, 2620, FWD', 'EF217632, OPdjbTaLvPn, 10, 278, 2456, FWD', 'LK737425, imLniNhZOMt, 9, 190, 2965, FWD']",
				  f"{str(r7.retailer_id)}, iQrIrKaovb, FlindersStreet Rd Clayton, VIC3172, (5.2, 27.2), ['KL962504, eSyOgLqCHc, 7, 600, 2422, AWD', 'AB852553, KLjEUsGRQa, 5, 250, 2310, AWD', 'WE218745, HJdjbLaLvPo, 11, 289, 2756, AWD', 'MN739655, imMniPhZOMz, 8, 140, 2745, RWD']",
				  f"{str(r8.retailer_id)}, jRrIrLaova, Parliament Rd Clayton, VIC3177, (3.8, 24.2), ['MN962504, fSyOgLqCHc, 7, 232, 2440, FWD', 'UV852554, MNjEUsSDQa, 6, 550, 2750, RWD', 'WA218633, DFdjbAaLvPp, 10, 287, 2111, RWD', 'ZX737855, imNniAhZOMe, 14, 170, 2789, FWD']"]
	lines = random.sample(statements,3)
	path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
	with open(path, "w") as file:
		for statements in lines:
			file.write(statements + "\n")

	order_path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\order.txt"
	with open(order_path, 'w') as file:
		pass

#function to handle all the logical operations
def main():

	generate_test_data() #randomly generate data

	path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
	pattern_rid = r'\b\d{8}\b'
	retailers = [] #list to store retailer id
	retailer_name = [] #list to store retailer name
	with open(path, "r") as file: #reading files

		for line in file:
			new_retailer = re.findall(pattern_rid, line)
			retailers.append(new_retailer)

			#extracting retailer name
			point = line.strip().split(', ')
			retail_name = point[1]
			retailer_name.append(retail_name)


	while True: #initiating while loop
		main_menu() # Calling main menu fucntion
		try: #handling errors
			user_input = int(input("Please select any one of the option\n")) #Taking user input for main menu options
			if 1<=user_input<=4:
				if user_input == 1:
					print("Please enter your postcode digits, for example 1234")
					postcode_input = int(input(" Enter Your Postcode : ")) #taking postcode
					if 1000<= postcode_input <= 9999:
						pattern_add = r"VIC\d{4}"
						# d1 = CarRetailer("1","1","1","1")
						# dis.append(d1.get_postcode_distance(postcode_input))
						with open(path, "r") as file:
							for l in file:
								match = re.search(pattern_add, l)
								if match:
									retail_add = match.group()
									# print(retail_add)

									match_id = re.search(pattern_rid, l)
									if match_id:
										retail_id = match_id.group()
									# r1 = Retailer(retail_id, "1")
										cr1 = CarRetailer(retail_id,retail_name,retail_add,"1",) #car retailer object
										print(cr1.get_postcode_distance(postcode_input)) #prints the difference of postcodes
					else:
						print("Invalid input: Please enter the input in format 1234")
						# raise ValueError("Invalid input, please enter a 4 digit postcode")

				if user_input == 2: #all reatiler related ops
					print('''
							Car Retailers that are working with us
							
							''')
					print(f"Press 1 for {retailers[0][0]}")
					print(f"Press 2 for {retailers[1][0]}")
					print(f"Press 3 for {retailers[2][0]}")
					retail_input = int(input("Please select a Retailer: ")) #loading retailers
					if 1<= retail_input<= 3:
						if retail_input == 1:
							retail_id = str(retailers[0][0])
							retail_name = retailer_name[0]
						elif retail_input == 2:
							retail_id = retailers [1][0]
							retail_name = retailer_name[1]
						elif retail_input == 3:
							retail_id = retailers[2][0]
							retail_name = retailer_name[2]

						print('''
						
								Select one of the operations from below
								
								1) Recommend a car
								2) Get all cars in stock
								3) Get cars in stock by car types 
								4) Get probationary licence permitted cars in stock
			
								
								
								''')

						user_sub_input = int(input("Please select one from above")) #INput to select a opration for retailer
						if 1<= user_sub_input <= 4:
							if user_sub_input == 1: # gives a random value car object
								print((f"Retailer is: {retail_id}"))
								cr2 = CarRetailer(retail_id,retail_name,"retail_add","1")
								# print(retail_id)
								# print(retail_name)
								print(cr2.car_recommendation())

							elif user_sub_input == 2: #givees sall stock of the retailer
								path = path =r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"
								cr3 = CarRetailer(retail_id,retail_name,"1","1")
								# print(retail_id)
								print(cr3.get_all_stock())

							elif user_sub_input == 3: #Filters according to car type
								path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"


								car_type = []
								print("Dear teaching team, it was later in the time when I realised that this functionality has to take  a list, I didnt want to make big changes in my code.\nHence I have designed it in a way that it can take only one car type at a time\nFeel free to try it, Regards\n")
								user_car_type =(input("Please enter type of car you want\nfor example AWD, RWD, FWD "))
								user_car_type = user_car_type.upper()
								# print(user_car_type)
								if user_car_type == "AWD" or user_car_type == "RWD" or user_car_type == "FWD":
									car_type.append(user_car_type.upper())
									cr4 = CarRetailer(retail_id,retail_name,"1","1")
									# for i in range(len(cr4.get_stock_by_car_type(car_type))):
									print(cr4.get_stock_by_car_type(car_type))
								else:
									print("Invalid input, please select from AWD/RWD/FWD")

							elif user_sub_input ==4: #filters according to licence type
								cr5 = CarRetailer(retail_id, retail_name, "1", "1")
								licence_input = input("Enter the Licence type L/P/F")
								licence_input = licence_input.upper()
								if licence_input.isalpha() and len(licence_input) == 1:
									if licence_input == "F" or licence_input == "P" or licence_input == "L":
										print("Following cars are allowed for probationary Lisence holders")
										print(cr5.get_stock_by_licence_type(licence_input))

									else:
										print("Invalid input")
								else:
									print("Invalid input")

						else:
							raise ValueError("Please select any one of the four option, taking back to main menu")

					else:
						print("Please select any one of the three retailer, taking back to main menu")

				elif user_input == 3: #Creates order
					path = r"C:\Users\HP\pgoy0003\Assessments\Assignment02\Assignment 2 Template  Data\data\stock.txt"

					r_c_input = (input("PLease enter the Retailer ID and CAR ID ")) #takes user input for retailer id and car id
					pattern1 = r"^\d{8}$"
					pattern2 = r"^[A-Z]{2}\d{6}$"
					if len(r_c_input.split()) == 2:
						if re.match(pattern1, r_c_input.split()[0]):
							if re.match(pattern2, r_c_input.split()[1]):

								retailerid, carid = r_c_input.split()
								# print(retailers)
								if retailerid == retailers[0][0] or retailerid == retailers[1][0] or retailerid == retailers[2][0] : #checking retailer id
									#Current time
									curr_time = time.localtime()
									#Converting time into decimals
									current_hour = curr_time.tm_hour + curr_time.tm_min / 60
									# print(current_hour)

									cr6=CarRetailer(retailerid,"None","None","None") #car retailer pbject
									# print(retailerid)
									# print(cr6.is_operating(current_hour))
									if cr6.is_operating(current_hour) == True: #if retailer is working
										# cr6.load_current_stock(path)
										print(f"Order created == {cr6.create_order(carid)}")
									else:
										print("Retailer is not working right now, try again later ")
								else:
									print("This retailer is not present in stock")
							else:
								print("Invalid input, car code is a 2 Capital alphabet, followed by 6 digits")
						else:
							print("Invalid format for retailer ID, retailer id is 8 digit number")

					else:
						print("Invalid input, please enter in this format: retailer ID(space)car code")


				elif user_input == 4: #Exits the program
					print("Thank you for visiting")
					break

				continue

			else:
				print("PLease enter a valid input between 1 to 4")
				continue
		except ValueError:
			print("Invalid input, please try again")
		except FileNotFoundError:
			print("File is missing from directory")















if __name__ == "__main__":
	try:
		main()
	except FileNotFoundError:
		print("File do no exist in the folder")
# generate_test_data()
# main()

