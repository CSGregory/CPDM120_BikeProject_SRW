#-----------------------------------------------------------------------------------------------------------------
# Name: Shane Winslow, Caleb Gregory, and Maison
# Team: D
# Project Name: Bike Rental Object Oriented Project
# Project Desc: Collection of Classes their related methods for the customer and bike shop entities for business logic
#-----------------------------------------------------------------------------------------------------------------
#import datetime feature from Python library
import datetime

#Bike Rental class to initialized and instantiate a bike shop along with the necessary bike shop behaviors
class BikeRental:

    #---------------------------------------------------------------------------------------------------------------
    # Name: Bike shop constructor
    # Desc: Constructor initializes and instantiates the bikeshop object
    #---------------------------------------------------------------------------------------------------------------

    def __init__(self, mountainstock=0, BMXstock=0, streetstock=0):
        
        # set the inventory variables for bike shop upon instantiation
        self.totalstock = mountainstock + BMXstock +streetstock
        self.mountainstock = mountainstock
        self.BMXstock = BMXstock
        self.streetstock = streetstock

    #--------------------------------------------------------------------------------------------------
    # Name: Display Available Inventory
    # Desc: Displays the current total of bikes in stock as well as the specific types of bike
    #--------------------------------------------------------------------------------------------------
    def DisplayAvaialbleInventory(self):

        # print total stock in inventory
        print("We have currently {} total bikes available to rent.".format(self.totalstock))
        # print mountain bike stock in inventory
        print("There are {} mountain bikes available to rent.".format(self.mountainstock))
        # print BMX stock in inventory
        print("There are {} BMX bikes available to rent.".format(self.BMXstock))
        # print Street stock in inventory
        print("There are {} street bikes available to rent.".format(self.streetstock))

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Rent Bike by Hour 
    # Desc: Allows shop to rent bike(s) on hourly basis to a customer, verify their request is possible, set their time of rental, and updates the inventory accordingly
    #----------------------------------------------------------------------------------------------------------------------------------
    def RentBikeOnHourlyBasis(self, request):
        #Set boolean variable to validate all rental requests can be fulfilled
        blnValidate = bool(True)

        intMountain, intBMX, intStreet = request


        try:
             # if any number delivered for the three variables are negative raise Exception
            if intMountain < 0 or intBMX < 0 or intStreet < 0:
                print("Number of bikes should be positive!")
                raise Exception

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intMountain > 0:
                if intMountain > self.mountainstock:
                    print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountainstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intBMX > 0:
                if intBMX > self.BMXstock:
                    print("Sorry! We have currently {} BMX bikes available to rent.".format(self.BMXstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception 
            if intStreet > 0:
               if intStreet > self.streetstock:
                    print("Sorry! We have currently {} street bikes available to rent.".format(self.streetstock))
                    blnValidate = False

            # catch blnValidate to determine whether to raise Exception
            if blnValidate == False:
                raise Exception
            
             # if all numbers good, record time or rental request for customer record, and indicate the number of different type of bikes requested, the total #, and remove bikes from inventory
            else:
                now = datetime.datetime.now()                      
                print("You have rented {} Mountain bike(s), {} BMX bike(s), and {} Street bike(s) on an hourly basis today at {} hours.".format(intMountain, intBMX, intStreet, now.hour))
                print("You will be charged $5 for each hour per bike.")
                print("We hope that you enjoy our service.")
                self.mountainstock -= intMountain
                self.BMXstock -= intBMX
                self.streetstock -= intStreet
                self.totalstock -= (intMountain + intBMX + intStreet)
                
                return now
        
        # display message when exception is raised
        except:
            print("Please modify your request and resubmit")

    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Rent Bike by Day 
    # Desc: Allows shop to rent bike(s) on daily basis to a customer, verify their request is possible, set their time of rental, and updates the inventory accordingly
    #----------------------------------------------------------------------------------------------------------------------------------
    def RentBikeOnDailyBasis(self, intMountain=0, intBMX = 0, intStreet=0):
        #Set boolean variable to validate all rental requests can be fulfilled
        blnValidate = bool(True)

        try:
            # if any number delivered for the three variables are negative raise Exception
            if intMountain < 0 or intBMX < 0 or intStreet < 0:
                print("Number of bikes should be positive!")
                raise Exception

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intMountain > 0:
                if intMountain > self.mountainstock:
                    print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountainstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intBMX > 0:
                if intBMX > self.BMXstock:
                    print("Sorry! We have currently {} BMX bikes available to rent.".format(self.BMXstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception   
            if intStreet > 0:
               if intStreet > self.streetstock:
                    print("Sorry! We have currently {} street bikes available to rent.".format(self.streetstock))
                    blnValidate = False

            # catch blnValidate to determine whether to raise Exception
            if blnValidate == False:
                raise Exception

             # if all numbers good, record time or rental request for customer record, and indicate the number of different type of bikes requested, the total #, and remove bikes from inventory
            else:
                now = datetime.datetime.now()                      
                print("You have rented {} Mountain bike(s), {} BMX bike(s), and {} Street bike(s) on an hourly basis today at {} hours.".format(intMountain, intBMX, intStreet, now.hour))
                print("You will be charged $20 for each day per bike.")
                print("We hope that you enjoy our service.")
                self.mountainstock -= intMountain
                self.BMXstock -= intBMX
                self.streetstock -= intStreet
                self.totalstock -= (intMountain + intBMX + intStreet)
                
                return now

        # display message when exception is raised
        except:
            print("Please modify your request and resubmit")
        
    #----------------------------------------------------------------------------------------------------------------------------------
    # Name: Rent Bike by Week 
    # Desc: Allows shop to rent bike(s) on weekly basis to a customer, verify their request is possible, set their time of rental, and updates the inventory accordingly
    #----------------------------------------------------------------------------------------------------------------------------------
    def RentBikeOnWeeklyBasis(self, intMountain=0, intBMX = 0, intStreet=0):
        #Set boolean variable to validate all rental requests can be fulfilled
        blnValidate = bool(True)

        try:
            # if any number delivered for the three variables are negative raise Exception
            if intMountain < 0 or intBMX < 0 or intStreet < 0:
                print("Number of bikes should be positive!")
                raise Exception
                blnValidate = bool(False)
            
            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intMountain > 0:
                if intMountain > self.mountainstock:
                    print("Sorry! We have currently {} mountain bikes available to rent.".format(self.mountainstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intBMX > 0:
                if intBMX > self.BMXstock:
                    print("Sorry! We have currently {} BMX bikes available to rent.".format(self.BMXstock))
                    blnValidate = False

            # compare rental request to bike type avaialbility in the inventory, if not true then report and rasie exception
            if intStreet > 0:
               if intStreet > self.streetstock:
                    print("Sorry! We have currently {} street bikes available to rent.".format(self.streetstock))
                    blnValidate = False
            
            # catch blnValidate to determine whether to raise Exception
            if blnValidate == False:
                raise Exception

            # if all numbers good, record time or rental request for customer record, and indicate the number of different type of bikes requested, the total #, and remove bikes from inventory
            else:
                now = datetime.datetime.now()                      
                print("You have rented {} Mountain bike(s), {} BMX bike(s), and {} Street bike(s) on an hourly basis today at {} hours.".format(intMountain, intBMX, intStreet, now.hour))
                print("You will be charged $60 for each week per bike.")
                print("We hope that you enjoy our service.")
                self.mountainstock -= intMountain
                self.BMXstock -= intBMX
                self.streetstock -= intStreet
                self.totalstock -= (intMountain + intBMX + intStreet)
                
                return now  
        
        # display message when exception is raised
        except:
            print("Please modify your request and resubmit")
    

    #-----------------------------------------------------------------------------------------------------------------------------
    # Name: Return Bike
    # Desc: Allows the bike shop to process a customers bike return by:
    #    1. Updating the inventory by receiving the customers rented bikes
    #    2. Identifying the time the customer is making the return, and computing the total rental time for the bikes
    #    3. Calculating the bill to deliver to customer based on their total rental period
    #    3. Automatically modifying the bill based on whether the customer is eligible for the Family Rental Discount
    #    4. Indicating whether the customer provided a coupon ending with '***BBP' for 10% off the total bill
    #------------------------------------------------------------------------------------------------------------------------------
    def ReturnBike(self, request):

        #set variables according to request object
        dtmRentalTime, intMountainBikes, intBMXBikes, intStreetBikes, intTotalNumBikes = request
        #declare bill variable
        bill = 0

        if dtmRentalTime and intMountainBikes >= 0 and intBMXBikes >= 0 and intStreetBikes >=0 and intTotalNumBikes:
            # add the returned bikes to the appropriate inventory variable, record time of return, and calculate rental period
            self.mountainstock += intMountainBikes
            self.BMXstock += intBMXBikes
            self.streetstock += intStreetBikes
            self.totalstock += intTotalNumBikes
            now = datetime.datetime.now()
            dtmRentalPeriod = now - dtmRentalTime
            
            # set benchmarks for assigning correct rental basis
            dtmUnder5Hours = datetime.timedelta(0,0,0,0,0,5,0)
            dtmUnder5Days = datetime.timedelta(5,0,0,0,0,0,0)
           
            # assign rental basis (hourly, daily, weekly) according to total time period of rental - modifying hourly or daily basis according to whether customer reached certain limits
            # if customer rental period is less than 5 hours, assign to customer to rental basis hourly, otherwise shift to daily
            if dtmRentalPeriod < dtmUnder5Hours:
                rentalBasis = 1
            # if customer rental period is less than 5 days, assign customer to rental basis daily, otherwise shift to weekly
            elif dtmRentalPeriod < dtmUnder5Days:
                rentalBasis = 2
            else:
                rentalBasis = 3

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(dtmRentalPeriod.seconds/3600,2) * 5 * intTotalNumBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                # if rental basis shifted from hourly to daily, it may be less than 1 official day, add 1 day to Rental Period for correct calculation
                if dtmRentalPeriod.days < 1:
                    dtmRentalPeriod = dtmRentalPeriod + datetime.timedelta(days=1)
                bill = dtmRentalPeriod.days * 20 * intTotalNumBikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                # if rental basis shifted from daily to weekly, it may be less than 1 week can and therefore a fraction when divided by 7 - modify to rental time period to at least 7 days if so 
                if dtmRentalPeriod.days < 7:
                    dtmRentalPeriod = datetime.datetime(0,0,7,0,0,0,0)
                bill = round(dtmRentalPeriod.days / 7,2) * 60 * intTotalNumBikes
            
            # automatically apply family rental discount for 25% off if # of bikes returned is equal to or between 3 and 5
            if (3 <= intTotalNumBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.75
            
            # allow customer to provide coupon ending in '***BPP' to apply additional 10% off total bill
            strCoupon = input("Did the customer provide a coupon ending in *BPP? Enter 'Y' or 'N': ")
            blnCoupon = bool(False)
            if strCoupon == 'Y':
                blnCoupon = True

            if blnCoupon == True:
                bill = bill * 0.9
            
            # print bill for to collect from customer
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill

        # catch if error with issuing return
        else:
            print("Are you sure you rented a bike with us?")
            return None

#Customer class to initialized and instantiate a customer along with the necessary customer behaviors
class Customer():

    #---------------------------------------------------------------------------------------------------------------
    # Name: Customer Constructor
    # Desc: Constructor initializes and instantiates the customer object
    #---------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.intMountainBikes = 0
        self.intBMXBikes = 0
        self.intStreetBikes = 0 
        self.intTotalNumBikes = 0
        self.dtmRentalTime = 0
        self.dblBill = 0.0

    #---------------------------------------------------------------------------------------------------------------
    # Name: Customer request
    # Desc: Method takes in a request issued by the customer
    #---------------------------------------------------------------------------------------------------------------
    def RequestBike(self):

        # Prompts the customer with how many and of what kind of bikes the customer would like to rent from the bike shop
        intMountainBikes = input("How many Mountain bikes would you like to rent? ")
        intBMXBikes = input("How many BMX bikes would like to rent? ")
        intStreetBikes = input("How many Street bikes would you like to rent? ")

        # Checks to ensure that the number of Mountain Bikes requested by customer is an integer greater than or equal to 0
        try:
            intMountainBikes = int(intMountainBikes)
            intMountainBikes >= 0
        except ValueError:
            print("Need an integer greater than or equal to 0 for Mountain bike request")
            return -1

        # Checks to ensure that the number of Street Bikes requested by customer is an integer greater than or equal to 0
        try:
            intStreetBikes = int(intStreetBikes)
            intStreetBikes >= 0
        except ValueError:
            print("Need an integer greater than or equal to 0 for Street bike request")
            return -1

        # Checks to ensure that the number of BMX Bikes requested by customer is an integer greater than or equal to 0
        try:
            intBMXBikes = int(intBMXBikes)
            intBMXBikes >= 0
        except ValueError:
            print("Need an integer greater than or equal to 0 for BMX bike request")
            return -1

        # Calculates the total number of bikes requests made by the customer by summing the variables
        intTotalBikesRequested = intBMXBikes + intStreetBikes + intMountainBikes

        # Checks to make sure that the customer requested at least 1 bike
        if intTotalBikesRequested < 1:
            print("Invalid input. Total number of bikes should be greater than zero!")
            return -1

        # if all bikes requests made by customer are valid, it set their instance variable to the desired value
        else:
            self.intBMXBikes = intBMXBikes
            self.intStreetBikes = intStreetBikes
            self.intMountainBikes = intMountainBikes
            self.intTotalNumBikes = intTotalBikesRequested
       
        # returns the total number of bikes requested
        return self.intMountainBikes, self.intBMXBikes, self.intStreetBikes
   
    #---------------------------------------------------------------------------------------------------------------
    # Name: Return Bike
    # Desc: Method allows the customer to return their bikes based on customer object and set the information as a new object to be used for processing the return by the bike shop
    #---------------------------------------------------------------------------------------------------------------
    def ReturnBike(self):
        
        #Checks to ensure all the parameters assigned within the Customer class are variables to be used in processing the return request within the Bike Rental class
        if self.dtmRentalTime and self.intMountainBikes >= 0 and self.intBMXBikes >= 0 and self.intStreetBikes >= 0 and self.intTotalNumBikes:
            return self.dtmRentalTime, self.intMountainBikes, self. intBMXBikes, self.intStreetBikes, self.intTotalNumBikes
        #if the information provided does not meet the specifications set all variables to 0
        else:
            return 0,0,0,0,0
    
    



#test

#Create shops
shop1 = BikeRental(25,25,25)
Customer1 = Customer()
request1 = Customer1.RequestBike()
Customer1.dtmRentalTime = shop1.RentBikeOnHourlyBasis(request1)
Customer1.dtmRentalTime = datetime.datetime.now() + datetime.timedelta(hours=-4)
return1 = Customer1.ReturnBike()
shop1.ReturnBike(return1)

# Create Customers
customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer4 = Customer()

# determine number of bikes
customer1.intMountainBikes = 1
customer1.intBMXBikes = 2
customer1.intStreetBikes = 3
customer1.intTotalNumBikes = 6 #eligible for family discount

customer2.intMountainBikes = 1
customer2.intBMXBikes = 2
customer2.intStreetBikes = 1
customer2.intTotalNumBikes = 4 

customer3.intMountainBikes = 0
customer3.intBMXBikes = 2
customer3.intStreetBikes = 0
customer3.intTotalNumBikes = 2 

customer4.intMountainBikes = 2
customer4.intBMXBikes = 1
customer4.intStreetBikes = 1
customer4.intTotalNumBikes = 4 

# detrmine rental time
customer1.dtmRentalTime = datetime.datetime.now() + datetime.timedelta(hours=-4)
customer2.dtmRentalTime = datetime.datetime.now() + datetime.timedelta(hours=-23)
customer3.dtmRentalTime = datetime.datetime.now() + datetime.timedelta(days=-4)
customer4.dtmRentalTime = datetime.datetime.now() + datetime.timedelta(days=-14)

# create request to return the bike
request1 = customer1.returnBike()
request2 = customer2.returnBike()
request3 = customer3.returnBike()
request4 = customer4.returnBike()

# return the bike to shop and get a bill
shop1.ReturnBike(request1) 
shop1.ReturnBike(request2) 
shop1.ReturnBike(request3) 
shop1.ReturnBike(request4) 
