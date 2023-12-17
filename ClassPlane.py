from colorama import Fore, Style
from ClassPassenger import Passenger

class Plane:
    def __init__(self, name, company, seats, destination):
        self.__name = name
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passengers = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def company(self):
        return self.__company
    @company.setter
    def setCompany(self, company):
        self.__company = company

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def setSeats(self, seats):
        self.__seats = seats

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def setDestination(self, destination):
        self.__destination = destination

    @property
    def passengers(self):
        return self.__passengers
    @passengers.setter
    def setPassengers(self, passengers):
        self.__passengers = passengers

    #Add a passenger to the list of passengers
    #Input: firstName, lastName, passportNr
    #Output: -
    @passengers.setter
    def addPassenger(self, firstName, lastName, passportNr):
        try:
            if type(firstName) != str or type(lastName) != str or type(passportNr) != int:
                raise ValueError("The arguments are not of the right type")
            if len(self.__passengers) < self.__seats:
                self.__passengers.append(Passenger(firstName, lastName, passportNr))
            else:
                raise ValueError("The plane is full")
        except ValueError as ve:
            return ve
        
    #Add a list of passengers to the list of passengers
    #Input: a list of passengers
    #Output: -
    @passengers.setter
    def addPassengers(self, passengers):
        try:
            if type(passengers) != list:
                raise ValueError("The argument is not a list")
            if len(self.__passengers) + len(passengers) <= self.__seats:
                for passenger in passengers:
                    self.__passengers.append(passenger)
            else:
                raise ValueError("The plane is full")
        except ValueError as ve:
            return ve
    
    #Remove a passenger from the list of passengers
    #Input: passenger
    #Output: -
    @passengers.setter
    def removePassenger(self, passenger):
        try:
            if type(passenger) != Passenger:
                raise ValueError("The argument is not a passenger")
            if passenger not in self.__passengers:
                raise ValueError("The passenger is not in the plane")
            self.__passengers.remove(passenger)
        except ValueError as ve:
            return ve
        
    #Update a passenger from the list of passengers
    #Input: passenger, firstName, lastName, passportNr
    #Output: -
    @passengers.setter
    def updatePassenger(self, passenger, firstName, lastName, passportNr):
        try:
            if type(passenger) != Passenger or type(firstName) != str or type(lastName) != str or type(passportNr) != int:
                raise ValueError("The arguments are not of the right type")
            if passenger not in self.__passengers:
                raise ValueError("The passenger is not in the plane")
            passenger.firstName = firstName
            passenger.lastName = lastName
            passenger.passportNr = passportNr
        except ValueError as ve:
            return ve
        
    def __str__(self):
        return "Plane: " + Fore.LIGHTMAGENTA_EX + self.__name + Style.RESET_ALL + ", Company: " + Fore.LIGHTBLUE_EX + self.__company + Style.RESET_ALL + ", Seats: " + Fore.LIGHTBLUE_EX + str(self.__seats) + Style.RESET_ALL + ", Destination:" + Fore.LIGHTBLUE_EX + self.__destination + Style.RESET_ALL +"\n"+ "Passengers: " + str(self.__passengers)+"\n"
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.__name == other.__name and self.__company == other.__company and self.__seats == other.__seats and self.__destination == other.__destination and self.__passengers == other.__passengers
    
    #Concatenation of the number of passengers and the destination 
    #Output: a string
    def concatenate(self):
        return str(len(self.__passengers)) + self.destination